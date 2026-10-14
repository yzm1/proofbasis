# Task 018 — Reciprocal review of the atomic-endomorphism submissions

**Date:** 2026-10-14. **Status:** selected bounded review, ready for the existing external investigators. No agents have been launched by this file.

## Decision value and immutable inputs

Determine whether report 023's actual argument establishes every mixed p→p equals id_p in the frozen B, or whether there is an exact typing/coverage/induction/equality defect. Independently assess report 024's closed-name reformulation and cancelled witness. Failed counterexample search is not positive certification.

Mathematical baseline: f2d7fcb1b00c36fdc4dfc3ab2a3e9ac487f566e7; Task 017 and reports 017/020/021 fix D*, E*, source identities and maps. No scope change.

Pinned submissions:
- Constructive report 023 at **e2cd91095a39e3b63541747fd3e02390e7e92282**, PR 35; path research/reviews/023-atomic-endomorphism-constructive.md.
- Adversarial report 024 at **d9a5272f9f31694331beb68f975e73e92436b572**, PR 36; path research/reviews/024-atomic-endomorphism-adversarial.md.
- Corrected Task 016 report 022 at **024189fdc3a91479c94dbdd7a822e6b12a478b8a**; broader bridge/coherence checks remain pending.

Read AGENTS.md and its required documents, RESEARCH_PLAN.md, research/OPERATING_PROTOCOL.md, Task 017, both pinned reports, and [coordinator review 025](../research/reviews/025-atomic-submissions-coordinator-review.md). Fetch/show the pinned commits explicitly; the reports need not be present on your starting branch. Verify decisive primary passages directly rather than inheriting evidence labels.

The tested B has one linear atom p, no nonlinear atoms and no nonidentity proof generators. Arbitrarily nested nonlinear objects, F/U, raw duals and both units remain available. Full E*, no MIX, no self-trace, no FU=id, no unit/counit identification, and no changed atom map.

## Agent B — independent attack on the positive argument

Read report 023's complete proof and reconstruct its decisive steps independently. Do not merely repeat your previous witness search.

1. Audit §3.4 coverage: give explicit target-to-auxiliary templates for the chosen projections and inverse factorizations, including nullary operations and all allowed ambient contexts. Identify any missing primitive or unjustified boundary comparison.
2. Audit (S): expand nonlinear H_L and product-left source commutations with at least two substituted slots and explicit sharing/context maps. Include a linear continuation and nested U-derived subproofs. A diagram must be equality in E*, not only matching endpoints.
3. Reconstruct the mutual cut/substitution induction. Track rank, producer/consumer heights and selected occurrences. Check contractions, multiple selected slots, producer-left rules and all principal cases. If a recursive call does not decrease or a linear occurrence is copied/dropped, show its exact typed instance.
4. Verify dual rotations/snake cancellation at raw A,A*, and F/U principal reductions with their actual zone restrictions.
5. Determine whether the equality-preserving lemma plus last-rule classification covers every permitted atomic representative. This is not a demand for strong normalization, confluence or decidable equality.
6. Reconcile the result with your closed-name search: a definable separated witness would defeat the claimed lemma; arbitrary semantic nonidentity maps would not.

Output only research/reviews/027-atomic-cross-review-by-adversarial-agent.md on your own branch in one PR. Preserve both submissions. Verdict: ACCEPT AS INDEPENDENTLY REVIEWED INFORMAL ARGUMENT, SPECIFIC PROOF GAP, TYPED COUNTEREXAMPLE, or UNRESOLVED. Acceptance is still not FORMALIZED or full SC.

## Agent A — independent reconstruction of the adversarial submission

Read report 024 and independently validate or correct its constructions.

1. Reconstruct B_L(p;p)≅B_L(;p*⅋p)≅B_N(;U(p*⅋p)) from the exact universal operations, typing both directions and checking β/η under the full ambient E*.
2. Translate its copied closed-name witness into your auxiliary rule templates. Make the nonlinear sharing, modal factorizations, linear composition and final evaluation explicit.
3. Show the precise equality cancellation; identify which cases of your cut/substitution lemma apply, including any structural rebuilding and changes to the induction parameters. Do not replace the whole check with a claim that your theorem already proves it.
4. Verify the whole-doctrine FinSet/finite-vector-space interpretation sufficiently to assess its separation claims. Distinguish soundness from syntactic fullness and definability.
5. Examine the compact trace obstruction: check the actual tensor/cotensor, I/bottom and feedback boundaries. Decide whether report 024 has excluded a candidate or merely failed to construct it; do not upgrade absence of a term to impossibility.
6. Record any defect or missing obligation in your positive proof exposed by this reconstruction. Do not silently repair report 023; propose an explicit amendment with its dependency impact.

Output only research/reviews/026-atomic-cross-review-by-constructive-agent.md on your own branch in one PR. Preserve both submissions. Verdict on report 024: VALID UNRESOLVED ADVERSARIAL EVIDENCE, SPECIFIC CORRECTION REQUIRED, CERTIFIED WITNESS, or UNRESOLVED, plus the effect on report 023's positive argument.

## Coordination and stop conditions

The independent initial phase is complete. Both may now read the frozen opposite submission, but do not communicate during reciprocal review or read the other's developing cross-review. No additional agents, implementation, broad literature/definition sweep, or extension to all pure boundaries.

Give a claim-by-claim disposition with exact typed equations or counterinstances, primary-source checks and their limits, and the strongest opposing argument. Agreement and automated PR review are not mechanical certification. A precise gap does not itself refute the atomic proposition; a certified negative witness does. A valid atomic argument does not settle full SC or the broader pending pure prerequisites.

Stop at the bounded review deliverable. The coordinator will integrate the two reviews and decide whether to accept the atomic result, request a particular repair, or retain an explicit unresolved lemma.
