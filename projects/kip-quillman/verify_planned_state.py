"""Independently replay declared future events; validates planning, never prose."""
import json
import re
from pathlib import Path

ROOT=Path(__file__).parent
ledger=json.loads((ROOT/'planned-state.json').read_text(encoding='utf-8'))
def time(s):
    match=re.fullmatch(r'Day\s*(\d+) (\d\d):(\d\d)(?::(\d\d))?',s)
    assert match, s
    day,h,m,sec=(int(x or 0) for x in match.groups())
    return (day-1)*86400+h*3600+m*60+sec
def maximum(level):return 40+5*(level-1)
costs={'Override':10,'Claim Room':20,'Sovereign Ward':15,'Quickstep':10,
       'Trail Sight':15,'Staunch':10,'Mend':20,'Interpose':15,'Bulwark':20}
cooldowns={'Sovereign Ward':10,'Quickstep':15,'Trail Sight':45,'Staunch':15,
           'Mend':60,'Interpose':15,'Bulwark':45}
durations={'Sovereign Ward':2,'Claim Room':30,'Quickstep':1,'Trail Sight':1,
           'Staunch':5,'Mend':20,'Interpose':3,'Bulwark':8}
state={p:{'level':level,'xp_in_bar':0,'mana':maximum(level)}
       for p,level in [('Kip',1),('Tessa',5),('Owen',9),('Dane',9)]}
last={}; fixture_end={}; active={}; rooms=[]; total_awards={p:0 for p in state}
ranks={'Override':1,'Claim Room':1,'Sovereign Ward':0}
practice={s:0 for s in ranks}; timeline=[]; recovery_windows=[]; practice_windows=[]
def snapshot():
    return {p:{**s,'max_mana':maximum(s['level']),'xp_to_next':100*s['level']} for p,s in state.items()}
for h in sorted(ledger['opening_prearrival_history'],key=lambda e:-e['seconds_before_arrival']):
    p,s=h['person'],h['ability']; t=time('Day 1 08:00:00')-h['seconds_before_arrival']
    if (p,s) in last:assert t-last[p,s]>=cooldowns.get(s,0)
    assert state[p]['mana']>=costs[s]
    state[p]['mana']-=costs[s];last[p,s]=t
for c in ledger['chapters']:
    timeline.append((time(c['start']),-10,'entry',c))
    timeline.append((time(c['end']),-20,'exit',c))
    for e in c['events']:
        t=time(e['clock'])
        assert time(c['start'])<=t<time(c['end'])
        timeline.append((t,0,e['kind'],e))
        if e['kind']=='rest':
            end=t+e['completed_minutes']*60
            assert end<=time(c['end'])
            recovery_windows.append((e['person'],t,end))
            timeline.append((end,-1,'rest_end',e))
        elif e['kind']=='cast':
            skill=e['ability'];duration=e.get('channel_seconds',durations.get(skill,e.get('control_seconds') or 1))
            active.setdefault(e['person'],[]).append((t,t+duration,skill))
            if skill=='Claim Room' and e['outcome'].startswith('success'):
                timeline.append((t+30,1,'claim_success',e))
    for p in c['practice']:
        start,end=time(p['start']),time(p['end'])
        assert (end-start)/60==p['minutes']
        practice_windows.append((p['skill'],start,end))
        timeline.append((end,2,'practice_end',p))
for gain in ledger['skill_acquisition_events']:
    timeline.append((time(gain['at']),3,'rank_gain',gain))
for loss in ledger['physical_room_losses']:
    timeline.append((time(loss['at']),1,'room_loss',loss))
for p,start,end in recovery_windows:
    assert end>start
    for cs,ce,skill in active.get(p,[]):
        assert ce<=start or cs>=end,(p,'cast interrupts rest',skill)
    if p=='Kip':
        for skill,ps,pe in practice_windows:
            assert pe<=start or ps>=end,('quiet rest double-counted as focused practice',skill)
for i,(skill,start,end) in enumerate(practice_windows):
    for other,os,oe in practice_windows[i+1:]:
        assert oe<=start or os>=end,('practice skills double counted',skill,other)
for person,windows in active.items():
    windows.sort()
    for first,second in zip(windows,windows[1:]):
        assert first[1]<=second[0],(person,'overlapping setup/channel/control',first,second)

casts=0; rests=0; grants=0;last_override_end=-1;ward_impacts=[]
for t,priority,kind,e in sorted(timeline,key=lambda x:(x[0],x[1])):
    if kind=='entry':assert snapshot()==e['entry'],('entry mismatch',e['chapter'])
    elif kind=='exit':
        assert snapshot()==e['exit'],('exit mismatch',e['chapter'],snapshot(),e['exit'])
        assert rooms==e['owned_rooms_after'],('room mismatch',e['chapter'],rooms)
    elif kind=='cast':
        p,s=e['person'],e['ability'];casts+=1
        assert state[p]['mana']==e['mana_before']
        assert e['cost']==costs[s] and state[p]['mana']>=costs[s]
        if (p,s) in last:assert t-last[p,s]>=cooldowns.get(s,0),(p,s,'cooldown')
        last[p,s]=t
        state[p]['mana']-=costs[s]
        assert state[p]['mana']==e['mana_after']
        if p=='Kip':assert ranks[s]>=1,('ability not acquired',s)
        if s=='Override':
            assert t>=last_override_end,'Kip cannot control two different fixtures at once'
            last_override_end=t+e['control_seconds']
            g=e['geometry'];limit=10 if ranks[s]==1 else 15
            assert g['distance_m']<=limit and g['prior_sight_distance_m']<=10
            assert g['prior_sight_attention_seconds']>=1
            assert all(g[k] for k in ['visible_at_start','available_at_start','within_normal_mechanical_arc','ready_at_start','target_is_constructed_fixture','shield_removed_physically_if_any'])
            if 'prior_sight_at' in g:assert time(g['prior_sight_at'])+1<=t
            fixture=e['target']
            if fixture in fixture_end:assert t-fixture_end[fixture]>=15
            assert e['control_seconds']<=5
            fixture_end[fixture]=t+e['control_seconds']
        elif s=='Claim Room':
            g=e['geometry']
            assert g['enclosed_room_max_width_m']<=20 and g['living_hostiles_inside_at_start']==0
            assert not g['boss_chamber']
            assert all(g[k] for k in ['intact_anchor','guardian_defeated_or_none_assigned','protective_seal_removed_or_absent'])
            if e['outcome'].startswith('success'):assert e['channel_seconds']==30
            else:assert e['channel_seconds']<30
        elif s=='Sovereign Ward':
            ttl=10 if ranks[s]==1 else 20
            assert e['setup_seconds']==2
            assert 2<=e['physical_impact_seconds_after_start']<2+ttl
            formed=t+2
            for previous_impact in ward_impacts:
                assert previous_impact<=formed,'A replaced Ward cannot take a later impact'
            ward_impacts.append(t+e['physical_impact_seconds_after_start'])
            assert all(e['geometry'][k] for k in ['clear_ground','within_3m','upright_2m_square','stationary','physical_impact_crosses_front'])
            assert not e['geometry']['blocks_heat_or_water']
        elif s=='Quickstep':
            g=e['geometry'];assert g['path_length_m']<=12 and g['visible_traversable_physical_path']
            assert not any(g[k] for k in ['passes_through_creature_wall_or_restraint','carries_another_adult','crosses_otherwise_impossible_gap','hazard_immunity_assumed'])
        elif s=='Trail Sight':
            g=e['geometry'];assert g['physical_track_inspected'] and g['oldest_trace_minutes']<=120
            assert g['radius_m']<=25 and g['trace_visible_line_of_sight']
            assert not g['reveals_current_person_location_or_mind']
        elif s=='Interpose':
            g=e['geometry'];assert g['path_length_m']<=8
            assert all(g[k] for k in ['visible_ally','clear_physical_path','functional_weapon_in_right_hand'])
            if g['uses_enhanced_block']:
                assert g['parryable_physical_attack'] and 0<=g['block_seconds_after_activation']<3
            assert not g['all_direction_protection_assumed']
        elif s=='Bulwark':
            g=e['geometry'];assert g['effect_seconds']<=8
            assert g['weapon_raised_in_right_hand'] and g['physical_attack_crosses_front']
            assert not g['runs_or_attacks_during_effect'] and not g['blocks_heat_poison_or_suffocation']
        elif s in ('Staunch','Mend'):
            g=e['geometry'];assert g['uninterrupted_touch_seconds']>=(5 if s=='Staunch' else 20)
            assert g['external_wound'] and not g['repairs_bone_blood_organs_or_nerves']
            if s=='Mend':
                assert g['wound_length_cm']<=20 and g['wound_depth_cm']<=1
                assert g['tissue_present_and_aligned']
    elif kind=='rest':
        assert state[e['person']]['mana']==e['mana_before']
    elif kind=='rest_end':
        p=e['person'];rests+=1
        state[p]['mana']=min(maximum(state[p]['level']),state[p]['mana']+5*e['completed_minutes'])
        assert state[p]['mana']==e['mana_after']
    elif kind=='xp':
        assert e['amount'] in (50,100,300)
        for p,reason in e['contributors'].items():
            assert reason.strip()
            old=state[p]['mana'];total_awards[p]+=e['amount'];state[p]['xp_in_bar']+=e['amount']
            while state[p]['xp_in_bar']>=100*state[p]['level']:
                state[p]['xp_in_bar']-=100*state[p]['level'];state[p]['level']+=1
            assert state[p]['mana']==old,'no refill at level gain'
    elif kind=='claim_success':
        room=e['target'].split(':',1)[0]
        capacity=1 if ranks['Claim Room']==1 else 2
        if len(rooms)==capacity:rooms.pop(0)
        rooms.append(room);assert len(rooms)<=capacity
    elif kind=='room_loss':
        assert e['room'] in rooms
        rooms.remove(e['room'])
    elif kind=='practice_end':practice[e['skill']]+=e['minutes']
    elif kind=='rank_gain':
        s=e['skill'];grants+=1
        if e['rank']==1:
            assert s=='Sovereign Ward' and ranks[s]==0 and rooms and state['Kip']['level']>=2
        else:
            assert ranks[s]==e['rank']-1
            assert state['Kip']['level']>=e['minimum_level']
            assert practice[s]>=e['practice_minutes_required']
            assert e['proof'].strip()
            previous=[c for chapter in ledger['chapters'] for c in chapter['events']
                      if c['kind']=='cast' and c['person']=='Kip' and c['ability']==s and time(c['clock'])<t]
            assert previous
            proof=previous[-1]
            if s=='Override':
                assert proof['geometry']['distance_m']<=10
                assert time(proof['clock'])+proof['control_seconds']<=t
            elif s=='Claim Room':
                assert proof['outcome'].startswith('success') and time(proof['clock'])+30==t
            elif s=='Sovereign Ward':
                assert proof['physical_impact_seconds_after_start']<=12
                assert time(proof['clock'])+proof['physical_impact_seconds_after_start']==t
        ranks[s]=e['rank']
    else:raise AssertionError(kind)
    for s in state.values():assert 0<=s['mana']<=maximum(s['level'])

# Only these owner-planned boundaries are hard-coded; the replay derives all intermediate states.
assert ledger['chapters'][14]['exit']['Kip']['mana']==25
assert ledger['chapters'][17]['exit']['Kip']['mana']==75
assert ledger['chapters'][18]['exit']['Kip']['mana']==15
assert state['Kip']['level']==9 and state['Kip']['xp_in_bar']==100
assert all(v==120 for v in practice.values())
result={'result':'PASS','scope':'Arithmetic, timing, recorded prerequisites and future state only; not prose/audio approval',
    'paid_casts_replayed':casts,'rest_windows_replayed':rests,'skill_acquisitions_replayed':grants,
    'individual_xp_totals':total_awards,'focused_practice_minutes':practice,'final':snapshot(),
    'remaining_semantic_requirements':['Final chapter prose must preserve all declared prerequisites, safe recovery, contributor actions and exact spatial geometry.',
    'Jory and other injured people stay guarded with helpers while the main four fight; main group size9 remains consistent.',
    'Rest is not proven safe by numbers; actual doors, watch and absence of immediate attack must appear plausibly.',
    'Ability rank proofs need observed successful old-version use; a recorded assertion is not itself a completed scene.']}
(ROOT/'planned-state-validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
