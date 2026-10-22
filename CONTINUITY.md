# Keep continuity from rules to final prose

Use this alongside Steps 3, 5, and 8–11. A spreadsheet supports reading and judgment; it cannot establish that the scene followed its own numbers.

## Keep plans and events separate

Maintain one project registry with links to the System, characters, world, manuscript, and continuity. A **planned** row describes an intended event. A **confirmed** row cites the final revised text that established it, including file/version or hash. A planned reward is not earned XP. A proposed injury is not an actual injury. Do not overwrite confirmed history with a new outline.

The portable tables below supplement [STATE.md](templates/STATE.md) and [PROGRESSION.csv](templates/PROGRESSION.csv). Use one persistent Excel workbook for the project's episode continuity. Keep using that same file and its existing sheets; append or update records for each chapter/episode rather than creating a new workbook or new sheets for every episode. Preserve prior history, notes, and review evidence. If scripts own backing CSV/JSON data, refresh the existing workbook from those records while preserving earlier rows, notes, and settings. Choose a single owning record for each fact; do not hand-maintain competing bibles.

## Track enough to resolve the next choice

- **Rules and versions:** valid target, range, sight, setup, duration, cooldown, cost, recovery, interruption, and interactions. Record precisely what an upgrade changes and when it becomes available.
- **Chronological resources:** before, paid cost, eligible recovery, after, and current maximum. Walking is not resting unless this story's rules say so. Apply recovery caps and level changes at their actual times. Invalid use and interrupted valid use may have different costs.
- **Progression:** unique event, eligible contributors and their actual contributions, award, starting bar, thresholds crossed once, overflow, and final level/bar. Distinguish maximum increases from resource refills. Do not give absent allies credit automatically.
- **People and physical state:** a finite roster, injuries and their treatment, fatigue, sleep, position, equipment custody, spent supplies, room ownership, and actual travel. A healed cut does not imply repaired bone. A lost room does not automatically erase a learned skill.
- **Knowledge and trust:** who witnessed or was told a fact, when, and with what reliability. Private panels are private until shared. Record promises, bargains, refusals, and unresolved consequences.

Keep this detail behind the scenes. The reader hears the rule or number that makes the current choice understandable, rather than every spreadsheet entry.

## Required loop for every chapter or episode

If a novel chapter contains two or more episodes, run this loop for **each episode**; do not wait for the chapter or batch to end. For a new project with no workbook, create one from approved opening conditions before Episode 1. If an existing workbook is inaccessible, report that and resolve access before dependent drafting; do not pretend to read it or substitute an outline for actual state.

1. **Before writing the next episode, open and read the same persistent Excel workbook.** Read the latest confirmed actual ending, current/max resources and XP, knowledge, injuries/fatigue, positions and object custody, rule/ability versions, unresolved issues, current stopping point, and review status. Compare the relevant final manuscript ending. Resolve blocking inconsistencies before drafting. A preplanned outline or numerical replay cannot substitute for actual episode state. Before the first episode is confirmed, use the approved opening conditions and say that no completed episode exists.
2. Build the bounded writing packet from that confirmed state, current rule versions, and the permitted scene plan. Include only chapter-appropriate facts and knowledge, keeping the complete future ledger outside the packet.
3. Draft the complete chapter/episode. Keep tentative changes separate from confirmed records.
4. Read the full actual text. Trace each decisive movement, target, spell, cost, reward, injury, possession, and disclosure in time order. Fix the scene or its plan within established rules; do not introduce an exception to conceal the error.
5. Replay the numerical events. Check resource bounds, caps, cooldowns, simultaneous effects, XP overflow, eligibility, practice time, and proof before an upgrade. Use independent calculations where a mistake would change the result.
6. Check explanation and rhythm. Preserve common language and natural sentence variety; cut repeated rules and routine administration. Give a text-only simulated reader focused comprehension questions when available. Label that feedback honestly; it is not real audience approval.
7. **After full prose, revision, and a final read, update that same workbook.** Append or update confirmed actual episode facts, their final source/version or hash, all affected continuity checks, unresolved issues, current stopping point, and review status in the existing sheets. Preserve prior notes and history; close issues with evidence. Do not promote planned rows by copying their status.
8. Verify the saved workbook and affected backing records against the final text and calculations. Read back the latest confirmed ending and stopping point. Resolve blocking mismatches before starting the next episode, then repeat from step 1. A numeric PASS does not replace the prose read or establish reader, audio, or publication approval.

At book boundaries, review larger patterns as well: repeated encounters, reward inflation, forgotten relationships, missing power demonstrations, setups/payoffs, antagonist action, and the complete local ending. The book pass is additional work, not a substitute for chapter review.

## Files you can copy

- [RESOURCE-EVENTS.csv](templates/RESOURCE-EVENTS.csv): chronological costs and recovery, including effect versions and cast failure.
- [LEVEL-EVENTS.csv](templates/LEVEL-EVENTS.csv): event eligibility, resetting/cumulative XP rules, and exact results.
- [KNOWLEDGE.csv](templates/KNOWLEDGE.csv): the route by which someone learns a fact.
- [CONTINUITY-ISSUES.csv](templates/CONTINUITY-ISSUES.csv): open question, affected scenes, decision, and recheck evidence.

Use [SYSTEM.md](templates/SYSTEM.md) for the rules, [STATE.md](templates/STATE.md) for the final narrative state, and [PROGRESSION.csv](templates/PROGRESSION.csv) for growth and dependencies. Do not add empty bookkeeping categories that the story does not use.

## What a checker can establish

A checker can recompute declared events and reject inconsistent inputs. A `visible=true` flag does not prove that prose gave the character a sight line. A valid cooldown does not prove the character had time to speak a page of dialogue. A clean formula does not prove the rest was safe, the betrayal believable, or the ending satisfying. Read those things.

Include a few meaningful boundary checks when creating a project-specific tool: exact XP threshold and overflow, an interrupted paid cast, a rejected invalid target, capped recovery, an interrupted recovery minute, a range upgrade with unchanged inspection range, and overlapping effects. Test that corrupting an important value produces a failure. Do not present implementation-mirroring tests as a story audit.

## GitHub and future chats

The reusable playbook stays separate from story-specific records. Upload a story ledger only under the owner's applicable authorization. Keep manuscripts, raw research downloads, account data, and credentials out of this public repository. A project mirror must state its planned/confirmed status, source version/hash, refresh time, stopping point, review status, and refresh method. Update the same GitHub workbook and record paths in place when refreshing; Git retains the versions. Do not create a new dated workbook, directory, or set of sheets for every episode. A future assistant reads the persistent workbook and verifies the local manuscript before treating the mirror as current confirmed canon.

The owner-authorized [Kip Quillman planning tracker](projects/kip-quillman/README.md) demonstrates this separation. Its future plans are author-only context; do not pass the whole ledger to a bounded prose writer or simulated reader.

