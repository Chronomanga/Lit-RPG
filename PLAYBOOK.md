# Step-by-step LitRPG writing playbook

This sequence is our original implementation of the research, not a universal formula from one source. Steps may loop: a better character choice can change a class, and a class rule can change the world. Change the authoritative records together.

In **guided mode**, complete one requested step, present its artifact and unresolved choices, and wait for the owner's review. In **execution mode**, complete the full requested chapter, episode, or batch and its necessary checks. Routine implementation choices do not require repeated permission.

## Step 1 — Define the promise and scope

**Input:** the owner's idea and constraints. Read [STYLE.md](STYLE.md).

Decide what sort of experience this story promises: dangerous discovery, clever builds, revenge, companionship, settlement growth, comedy, cozy mastery, or another mix. Choose the setup—transported outsider, native world, virtual game, regression, System apocalypse, or another original approach. Specify the protagonist, immediate problem, personal reason to care, long-term direction, tone, narration, and requested length. Decide whether the current output is a novel or an audio serial; do not assume every novel must be 200 episodes.

**Produce:** a one-page brief using [templates/PROJECT.md](templates/PROJECT.md). Mark undecided ideas as proposals.

**Ready when:** the owner can explain who the story follows, what they want, what opposes them, what growth will feel rewarding, and what this task will deliver. Avoid a lore encyclopedia at this stage.

**Prompt:** “Complete Step 1 from my idea. Give me a clear story promise and a manageable scope, with only essential unresolved choices.”

## Step 2 — Build people who cause the story

**Input:** the brief. Read [WORLD-AND-CHARACTERS.md](WORLD-AND-CHARACTERS.md).

Give the hero a goal, motive, useful competence, limitation or mistaken belief, values under pressure, and a voice. Define what the hero knows and does not know. Design companions with their own goals and a reason to stay or refuse. Make the opposing force capable of acting without waiting for the hero. Record a believable reason for any loyalty or betrayal.

**Produce:** protagonist and initial cast cards from [templates/CHARACTER.md](templates/CHARACTER.md), plus an introduction plan.

**Ready when:** you can predict different choices these people would make in the same problem, and the hero's first consequential action has a personal reason. No demographic, personality, romance, or solo-adventure formula is mandatory.

**Prompt:** “Complete Step 2. Make the characters' goals conflict or cooperate in concrete ways, and show how we will introduce them naturally.”

## Step 3 — Design a System that can support decisions

**Input:** brief and cast. Read [SYSTEM-DESIGN.md](SYSTEM-DESIGN.md) and [CONTINUITY.md](CONTINUITY.md).

Define who has access, what the System knows, its visible messages, authority, classes, resources, costs, limits, recovery, progression, rewards, failure and death. Choose the minimum statistics needed for actual decisions. Establish whether level-up restores resources or changes only maximum values. Distinguish known rules, author-known hidden rules, and unresolved design questions.

**Produce:** [templates/SYSTEM.md](templates/SYSTEM.md), a first ability record, and a short resource calculation. Use [templates/RESOURCE-EVENTS.csv](templates/RESOURCE-EVENTS.csv) when chronological costs, recovery, or overlapping effects need tracking; record rule versions and keep current resources separate from their maxima.

**Ready when:** the author can resolve three different uses of the first power consistently, identify an impossible use, explain a costly choice, and calculate the first reward without inventing a new exception. The reader-facing explanation can remain brief.

**Prompt:** “Complete Step 3. Design the rules, test an ordinary use, a clever use, and a failed use, then show the exact costs.”

## Step 4 — Build the world shaped by those rules

**Input:** System and cast. Read [WORLD-AND-CHARACTERS.md](WORLD-AND-CHARACTERS.md).

Work outward from a few causal facts: how the world came to its current state, how powers changed life, who controls access, and what people do to survive or prosper. Explore one settlement deeply enough to feel lived in. Explain why the protagonist's unusual power matters socially. Decide what is known history, disputed belief, or intended mystery.

**Produce:** [templates/WORLD.md](templates/WORLD.md), the opening location, initial factions, and a staged revelation list.

**Ready when:** ordinary people have plausible lives and interests, the first danger has a place in the world, and the author knows which basics the opening must explain. Do not draft the whole history into Chapter 1.

**Prompt:** “Complete Step 4. Show how these powers affect everyday life and conflict, then choose only the world facts the opening needs.”

## Step 5 — Plan progression that changes possibilities

**Input:** System, world, and personal goals. Read [PACING-AND-PROGRESSION.md](PACING-AND-PROGRESSION.md) and [CONTINUITY.md](CONTINUITY.md).

Plan several major improvements with a cause, prerequisite, choice, cost, demonstration, and new possibility. Include growth in knowledge, relationships, judgment, control, or responsibility. Keep opponents and challenges varied. Preserve earlier abilities where useful. Set a plausible high-level direction without detailing hundreds of future rewards.

**Produce:** a progression ladder and initial [templates/PROGRESSION.csv](templates/PROGRESSION.csv). Include the first meaningful reward and what it enables. Use [templates/LEVEL-EVENTS.csv](templates/LEVEL-EVENTS.csv) for exact awards, contributor eligibility, thresholds, and overflow. Keep all intended gains labeled planned until final prose establishes them.

**Ready when:** each major gain has a reason to matter beyond a larger number, and it does not erase every interesting problem. Choose a cadence; do not impose a level-up-per-chapter quota.

**Prompt:** “Complete Step 5. Pair each major power gain with an earned event, a new decision, and a continuing limitation.”

## Step 6 — Outline a complete book arc

**Input:** character, world, and progression plans.

Name the central question this book will answer. Connect the disruption, goal pursuit, changing situation, setbacks, discoveries, climax, and consequences through choices. Tie power tests to personal stakes. Plan setups for the final solution and what the opposing force does between encounters. Resolve the book's main promise before opening the next book's question.

**Produce:** [templates/ARC.md](templates/ARC.md), a flexible sequence of major events, and a setup/payoff list.

**Ready when:** the climax depends on earlier choices and established possibilities; the hero causes important turns; the ending delivers a complete local arc. Three-act structure, mirrored images, and fixed chapter maps are available tools, not obligations.

**Prompt:** “Complete Step 6. Outline the causal arc and ending, and map the power and character choices that make the final result earned.”

## Step 7 — Design the opening experience

**Input:** book arc, style, and first power rules. Read the opening discussion in [PACING-AND-PROGRESSION.md](PACING-AND-PROGRESSION.md).

Establish a person, an immediate situation, a reason to care, an understandable choice, the story's progression promise, and a reason to continue. These functions can share a scene. If the premise starts inside a dungeon, begin there; establish personal stakes through the hero's reactions and choices. Introduce only the rules needed for the first decisions. Plan a meaningful initial result.

**Produce:** an opening sequence and first chapter card. Use [EXAMPLES.md](EXAMPLES.md) to test explanation flow.

**Ready when:** a reader can follow what is happening, why the hero acts, what the initial power allows, and why the outcome matters. A whole ordinary-world chapter, combat delay until chapter four, or identical five-chapter opening is not required.

**Prompt:** “Complete Step 7. Design the opening around the story's actual premise, and show how character investment and System understanding develop together.”

## Step 8 — Make chapter cards

**Input:** outline and current approved state. Before each next chapter/episode, open and read the same persistent Excel workbook and relevant final manuscript ending. Check the latest confirmed actual resources, knowledge, injuries, positions/custody, rule versions, stopping point, review status, and unresolved issues; resolve blockers first. Follow [CONTINUITY.md](CONTINUITY.md). Before Episode 1 is confirmed, use approved opening conditions and state that no completed episode exists.

For each chapter in the next manageable group, identify viewpoint, location, immediate goal, pressure, meaningful choice, result, emotional turn, information revealed, and state changes. Include what cannot yet be revealed. Vary action, exploration, practice, relationship scenes, recovery, and consequence. Plan a suitable ending without making every chapter an interrupted fight.

**Produce:** [templates/CHAPTER.md](templates/CHAPTER.md) cards. Keep plans provisional until prose establishes the event. Give a bounded writer only the relevant scene plan, permitted knowledge, and opening state; keep the complete future ledger outside that packet.

**Ready when:** each card performs a useful job and connects causally to the next. The cards contain enough rules to write the scene without leaking future secrets.

**Prompt:** “Complete Step 8 for the next [number] chapters. Give each a meaningful change and a clear connection to the next.”

## Step 9 — Draft the requested chapter

**Input:** approved card, style, chapter-appropriate canon, and opening state.

For every next chapter/episode, Step 8's workbook read is required before drafting, including within an authorized batch. If one novel chapter contains several episodes, run the read/write/revise/update/verify loop for each episode rather than waiting for the chapter to end. For a new project without a workbook, create one from approved opening conditions before Episode 1. If an existing workbook is inaccessible, report that and resolve access before dependent drafting; do not pretend to read it or replace actual state with an outline. Use actual confirmed episode state; preplanned outlines and numbers cannot replace it. Give the writer the bounded packet built from that read.

Write the complete prose. Put people in concrete situations; let attempts and choices produce consequences. Show powers clearly, but keep routine recordkeeping outside the scene. Introduce significant new people naturally. Use notifications when they add meaning. Preserve ordinary sentence variety and breathing room.

**Produce:** the full named chapter plus a provisional list of changes. If tools support separate workers, give the drafter a bounded brief rather than the whole future outline. Keep tentative event records separate; do not copy planned outcomes into confirmed state before Step 10.

**Ready when:** the actual prose reaches the planned useful result or an equally coherent revision of it. A synopsis, outline, or label saying “cliffhanger” is not the completed chapter. Continue directly to Step 10 for required revision.

**Prompt:** “Draft Chapter [number] in full using the approved card and current state. Then perform Step 10 within the same request.”

## Step 10 — Read, audit, and revise

**Input:** full actual chapter and its authoritative rules. Read [REVISION.md](REVISION.md) and [CONTINUITY.md](CONTINUITY.md).

Check physical action, who knows what, motive, power limits, resource arithmetic, rewards, injury, possessions, pacing, explanations, repetition, and the actual ending. Fix clear problems within scope. A major change to approved canon needs to be identified before silently propagating it. After revision, read the final text again and update continuity from what it actually says.

**Produce:** final prose, a concise changes record, [templates/STATE.md](templates/STATE.md), and updates to the progression ledger. After full prose, revision, and a final read, append or update confirmed actual episode facts in that same Excel workbook's existing sheets, including the final source/version or hash. Reconcile all affected resource, level, [knowledge](templates/KNOWLEDGE.csv), injury, custody, rule-version, and continuity checks. Record the current stopping point, review status, unresolved decisions, and recheck evidence in [templates/CONTINUITY-ISSUES.csv](templates/CONTINUITY-ISSUES.csv). Preserve earlier history and notes; do not create a new workbook or sheets per episode. Verify the saved workbook against the final text and calculations, resolving blockers before the next episode. Ask a bounded simulated reader or real beta reader focused comprehension questions when available; report which kind of review actually occurred.

**Ready when:** consequential choices and results are understandable and consistent, necessary explanations are present, and the next chapter's start matches this ending. Automated checks alone cannot establish this.

**Prompt:** “Complete Step 10. Fix the chapter, verify its final state, and tell me only the important remaining issue if there is one.”

## Step 11 — Complete and review the book

**Input:** final chapters, outline, and ledgers. Use the book-boundary pass in [CONTINUITY.md](CONTINUITY.md).

Repeat Steps 8–10 through the agreed scope, including the required workbook read before and verified update after every chapter/episode. Refresh any owner-authorized GitHub mirror at the same paths in place; use source hashes and Git history rather than new workbook names or episode sheets. Review larger runs for repeated encounter patterns, disappearing mechanics, unattended relationships, delayed promises, inflation, and false endings. Revise the outline as discoveries improve the book while keeping established facts coherent. Run a full manuscript pass at the end. Choose a sustainable writing and revision schedule.

**Produce:** complete manuscript, complete local arc, reconciled canon, and [templates/HANDOFF.md](templates/HANDOFF.md). Reconcile remaining planned rows and open issues against the complete final manuscript; a clean ledger does not replace the whole-book read before Step 12.

**Ready when:** the book pays off its central promise, the ending's solution has a basis, costs and relationships carry forward, and any sequel question grows from a real resolution. Unfinished drafts and disconnected episodes are not a finished novel.

**Prompt:** “Continue through the agreed book scope, then review the complete arc, progression, and continuity before declaring it finished.”

## Step 12 — Adapt for Pocket FM when requested

**Input:** approved underlying story and the owner's adaptation scope. Read [POCKET-FM.md](POCKET-FM.md).

Choose natural episode breaks, titles, spoken System wording, and earned continuation hooks. Preserve complete scenes, clarity, and variation in rhythm. Verify the current destination's actual requirements before submission. Track manuscript revision, audio version, listening review, and platform state separately.

**Produce:** named audio-friendly episodes, a mapping to source chapters, an episode continuity ledger, and an audio review record if audio is made.

**Ready when:** every adapted episode is coherent and correctly sequenced; actual audio, if generated, has received the required listening review; the specific publication action is authorized. Do not claim listener availability from a creator-side badge alone.

**Prompt:** “Adapt the approved story into Pocket FM episodes using Step 12. Preserve its canon and natural flow, and report exactly which production and release stages are complete.”
