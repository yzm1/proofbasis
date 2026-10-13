# Task 015 — S2-R2 independent cross-review and conjecture selection

**Status:** authorized cross-review only; S3 proof attempts are NOT yet authorized. **Frozen common baseline:** main at `b0ead595e91350486088789585273a01bb92a530`. Both Phase-A reports are incorporated as evidence: [017](../research/reviews/017-structural-contract-repair.md) and [018](../research/reviews/018-adversarial-contract-repair.md).

**Goal:** test the actual mathematics in each report, reconcile the *different* SC versus D_MLL proposals without pretending they are identical, and recommend a single frozen proposition or an explicitly justified decision not to freeze.

## Required questions for BOTH reviewers
1. Validate or refute the K_dec group-word-problem obstruction. Verify quantifiers, existence of a finitely presented group with undecidable word problem, its embedding into the exact source class, effective equality-preserving **and reflecting** translation, and whether target equality decider indeed gives a source decider. Identify the first missing hypothesis, if any.
2. Compare A's **SC** mixed LNL pure-fragment intrinsic conservativity/full faithfulness to B's **D_MLL** specific MLL-to-free-doctrine correspondence. Formalize whether D_MLL follows from SC, is necessary for a proof strategy, is a special case only after additional assumptions, or is independent. Give a diagram of the exact functors/equalities and highlight any mismatch in doctrines, target construction or source congruence.
3. Check primary literature: whether SC, D_MLL, and the needed fragment/full-faithfulness assertions are already published; distinguish a search failure from an open conjecture. Audit Shulman LNL doctrine results, MLL nets/sequentialization and known conservative embeddings, with exact hypotheses.
4. Attack both proposals with the fixed controls: NJ beta/eta; named MLL axiom links and commuting rules; all ambient target detours; hidden MIX, contraction, equality collapse, and trust-parameter smuggling. Do not infer universal impossibility from one failed realization.
5. Decide which *one* proposed target, if any, has the highest decision value. Include explicit yes/no criteria, proof route, falsifier, stop condition, and bridge to the original cross-foundation objective.
6. Identify what has already been proved, what is a new informal claim, what is unresolved, and which hypotheses must be fixed before two agents can test the **same** proposition.

## Coordination

- **Codex A** reviews **018**, emphasizing K/K_dec/D falsifiers and the D_MLL witness; submit `research/reviews/019-cross-review-by-structural-agent.md`.
- **Codex B** reviews **017**, emphasizing SC mixed-core conservativity, DI theorem-subsumption, and the common trust/equality requirements; submit `research/reviews/020-cross-review-by-adversarial-agent.md`.
- Work on independent branches from the same frozen baseline. Both are Codex; role separation is not independent mathematical certification. Do not edit the Phase-A reports or canonical plan. Do not read the other's developing S2-R2 report before submission.
- Submit separate PRs to main. Reviewers must **not** change the proposition to rescue it mid-analysis. Proposed repairs must be labeled as *new versions*, not as results about the frozen version.

## Gate

Following both submissions, coordinator integrates their critiques as evidence and writes a proposed S3 conjecture card with immutable text/commit if warranted. S3 launches only after (i) one precise target is selected, (ii) primary-theorem status is audited, (iii) the same quantifiers/equalities/morphisms are shared by both constructive and obstruction roles, and (iv) user approval or prior authorization for that *specific target*. If the evidence shows an existing theorem, close as prior art. If no target survives, pivot with recorded reasons rather than commissioning another unconstrained definitions cycle.
