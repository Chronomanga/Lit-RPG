# Kip Quillman persistent continuity mirror

**Current state: Episode 1 has a recorded root final prose review; Episode 2 is next.** The same local workbook was updated and its before-Episode-2 checkpoint verified. The stopping point is **read the workbook and confirmed Episode 1 ending before writing Episode 2; resolve blocking issues first**. Refresh time and source hashes are in [metadata.json](metadata.json). Whole-book review remains pending; no real-reader approval, completed audio review, or publication is established.

Use [continuity.xlsx](continuity.xlsx) as the persistent GitHub workbook path. Refresh that same file in place. [confirmed-state.csv](confirmed-state.csv) holds four confirmed resource rows for Episode 1. [actual-episodes.json](actual-episodes.json) is a state-only projection of the canonical actual ledger, with resources, ability versions, ownership, knowledge, injuries, fatigue, relationships, threats, events, practice, and source evidence. Keep [planned-state.json](planned-state.json) and its plan exports explicitly planned. Twenty planned novel chapters do not mean twenty completed episodes: actual Episode 1 stops before the planned Chapter 1 exit. A preplanned outline or numeric PASS is never a substitute for actual episode state. Metadata records both the canonical actual-ledger hash and the projection's different byte hash; Git retains prior file versions.

## Required before and after every episode

Before writing each next episode, open and read the **same local Excel workbook**, `D:\AI\Projects\Kip Quillman - New LitRPG\outputs\continuity-20261022\Kip-Quillman-Continuity.xlsx`. Read the latest confirmed actual ending, current/max resources and XP, knowledge, injuries/fatigue, positions and object custody, rule/ability versions, unresolved issues, current stopping point, and review status. Compare the relevant final manuscript ending and resolve blocking issues. Before Episode 1 is confirmed, read the approved opening conditions and retain the zero-confirmed status.

After writing complete prose, revising it, and reading the final version, append or update confirmed actual episode facts in **that same workbook's existing sheets**. Include the final source/version or hash, all affected resource/XP and continuity checks, unresolved issues, the current stopping point, and review status. Preserve earlier history and notes. Verify the saved workbook and affected backing records against the final text and calculations before starting the next episode. Do not create a new workbook, new sheets, or a dated directory for every episode. See the [required continuity loop](../../CONTINUITY.md).

The single local authority remains `D:\AI\Projects\Kip Quillman - New LitRPG`, through its project registry, approved rules, and final revised manuscript. If scripts own backing data, refresh the existing workbook while preserving earlier rows, notes, and settings; keep one owning record for each fact. This GitHub directory is a refreshed mirror, not a second story bible. A future assistant must verify the current local manuscript, registry, workbook, and handoff before treating it as current.

## Reading boundary and authorization

This is future planning context for the owner and coordinating assistant. A bounded prose writer receives only the relevant approved rules, actual opening state, permitted knowledge, and scene plan. A simulated reader receives the actual text and audience brief only. **Do not give either worker this whole ledger, workbook, or export directory.** This repository may be public: “author-only” describes the intended reading context, not access control or spoiler protection.

The owner explicitly authorized this project ledger mirror. It includes future encounter timing, geometry, rewards, and carryover needed to audit the plan. No manuscript body or quotations, separate character-secret or world-origin documents, raw work logs, account identifiers, prompts, or research downloads are included. The actual JSON omits root editorial notes and private flags; its ending field is a factual state summary. Local file references identify provenance, not mirrored private inputs.

## Persistent files

The numerical replay and plan exports remain **planned**. The workbook separately holds confirmed Episode 1 state, and its carryover table includes explicitly labeled actual facts. Supporting rules, tools, and calculations do not establish completed scenes. The confirmed actual records cite the final reviewed source filename/version and SHA256; the private text stays local. Ability versions and unprinted companion values carry approved author rules/baselines reconciled with actual uses; they do not mean every cost or limit was narrated or disclosed. Knowledge fields separately track what Kip and the reader know.

The confirmed-state table and CSV use **EP** for actual episodes. The mixed carryover table/export retains its existing **Ch** column: for planned rows it means the planned novel chapter; for `ACT-*` record IDs it means the actual episode. Use the record ID, Topic, and Status together to distinguish them. The 120 ACT-001 facts concern Episode 1, not a completed planned Chapter 1. Do not combine the two timelines or interpret all Ch values as episodes.

| File | Purpose and evidence limit |
| --- | --- |
| [continuity.xlsx](continuity.xlsx) | Persistent workbook mirror, updated in place; planned chronology and separately confirmed Episode 1 state. |
| [confirmed-state.csv](confirmed-state.csv) | Four actual Episode 1 resource rows with final-text evidence; EP identifies the episode. |
| [actual-episodes.json](actual-episodes.json) | Approved factual state-only projection; canonical-source hash and projection hash are recorded separately. No manuscript body or editorial notes. |
| [planned-state.json](planned-state.json) | Owning data record for the planned replay across 20 chapters; not final-text evidence. |
| [verify_planned_state.py](verify_planned_state.py) | Replays declared costs, recovery, XP, timing, rank prerequisites, and recorded geometry. It does not read or validate prose. |
| [planned-state-validation.json](planned-state-validation.json) | Generated planning result and remaining semantic requirements. Numeric PASS is not scene, reader, audio, or release QA. |
| [progression.csv](progression.csv) | Planned gains, demonstrations, limits, and dependencies. |
| [planned-state.csv](csv/planned-state.csv) | Planned chapter entry/exit states. |
| [mana-events.csv](csv/mana-events.csv) | Planned resource replay and recorded/calculated differences. |
| [xp-events.csv](csv/xp-events.csv) | Planned contributor awards, thresholds, and overflow. |
| [event-details.csv](csv/event-details.csv) | Planned timing, prerequisites, and geometry declarations; check against each final scene. |
| [story-carryover.csv](csv/story-carryover.csv) | Planned carryover plus 120 confirmed ACT-001 facts. Ch means planned chapter for plan rows and actual episode for ACT-* rows; inspect Topic and Status. |
| [rules.csv](csv/rules.csv) | Rule inputs used by this planning export. |
| [confirmed-state-template.csv](csv/confirmed-state-template.csv) | Blank reusable EP template only. The populated actual record is the separate stable confirmed-state.csv above. |
| [metadata.json](metadata.json) | Status, source hashes, refresh time, stopping point, and provenance. |

## Recheck and refresh in place

From this project directory, run:

```console
python verify_planned_state.py
```

The script writes `planned-state-validation.json`. Run with ordinary assertions enabled; `python -O` disables its checks. PASS means declared planning inputs agree with the replay's encoded rules. It does not prove sight lines, plausible safe rest, motives, actual contribution, natural flow, or a satisfying ending. Follow the [revision passes](../../REVISION.md) on the actual prose.

For each authorized mirror refresh, reconcile the canonical local workbook and owning records first. Use the local import-update workflow to refresh the existing workbook while preserving earlier rows, notes, and settings. Copy only the authorized ledger artifacts back to **these same GitHub paths**, including `continuity.xlsx`, `confirmed-state.csv`, the state-only actual JSON projection, planned data/exports, and metadata. Preserve the projection's omission of manuscript text, quotations, and editorial notes. Verify source and projection hashes and read back the confirmed ending, stopping point, and review status. Record commit provenance, rather than creating new workbook names. The local exporter and private project inputs are not included; this repository alone can replay the plan but cannot refresh all workbook views.

This update does not adapt, submit, or publish the manuscript. Complete the book review in Step 11 before a requested Pocket FM adaptation in Step 12, and preserve separate manuscript, saved draft, submission, creator publication, listener availability, and listening-review records.
