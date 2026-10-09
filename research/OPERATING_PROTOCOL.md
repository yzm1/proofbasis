# Research operations and agent coordination

## Separation of responsibilities

**Owner/coordinator:** controls north star, stage gates, source class and normative scope. Agents can propose changes but cannot silently approve them.

**Landscape agent:** breadth, omitted families, source routing, coverage status. Not authorized to declare universal existence or redefine fundamentality.

**Deep-dive agent:** exact theorems/counterexamples in one mathematical tradition; use comparison rubric and tests.

**Integration agent:** compares cross-family evidence and identifies genuine equivalences, mismatches and unexplained gaps; must cite source reports.

**Adversarial reviewer:** tries to refute both prioritization and mathematical claims; must name concrete alternatives and omissions.

## When to split vs combine

**Separate sessions** when source traditions differ greatly (e.g. cubical HoTT vs operads; harmony vs concurrency), when independence matters, or when material can be checked without modifying shared definitions.

**Combine** when the question is a direct comparison requiring common semantics, when scope/definitions must be fixed jointly, or when mutually dependent lemmas would otherwise drift.

**Never** give independent agents permission to redefine source class or conjecture mid-task. Pin common commit SHA and rubric. Prefer PRs containing reports and evidence; do not edit shared canonical plan directly from a deep dive.

## Branch and file discipline

- Root RESEARCH_PLAN.md is canonical planning spine.
- research/LANDSCAPE.md is the topical inventory.
- research/BACKLOG.md is the queue and dependency map.
- research/DECISIONS.md is the durable decision log.
- Deep dives live in research/deep-dives/, one file per topic.
- Task reports retain unique filenames and provenance; avoid collisions.
- Plans change through reviewable PRs with reasons, counterarguments and downstream task impact.

## Stage and task status

Use planned, active, submitted, reviewed, accepted-as-evidence, superseded, blocked, deferred, stopped. **Accepted-as-evidence never means theorem proven.**

## Research quality gates

An agent output must provide: exact research question, prior work with sources, conceptual map, strongest positive and negative results, scope-to-north-star bridge, uncertainties, what it changes, a suggested follow-up **only if** decision-changing.

Cross-review critical claims from different agents. Make a separate record of contradicted or withdrawn claims. Use formal proof tools only when a specific lemma warrants it.

## Budget discipline

Before starting a compute-heavy task, write one-sentence expected decision value, stop conditions, and what finding would make the work unnecessary. No benchmark or visualization infrastructure without a specific discriminating experiment.
