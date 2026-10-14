# Task 017 submissions — coordinator progress review

**Date:** 2026-10-14. **Status:** reviewed as research submissions; no new theorem accepted. This record reviews three PRs, not only the latest one.

## Pinned evidence

| PR | Commit reviewed | Contribution | Assessment |
|---|---|---|---|
| [34](https://github.com/yzm1/proofbasis/pull/34) | 024189fdc3a91479c94dbdd7a822e6b12a478b8a | Revised Task 016 report, Task 017, backlog | Corrected evidence status; the broader pure bridge and unit-extension identification remain verification obligations. |
| [35](https://github.com/yzm1/proofbasis/pull/35) | e2cd91095a39e3b63541747fd3e02390e7e92282 | [Constructive report 023](https://github.com/yzm1/proofbasis/blob/e2cd91095a39e3b63541747fd3e02390e7e92282/research/reviews/023-atomic-endomorphism-constructive.md) | INFORMAL POSITIVE ARGUMENT; the atomic result depends on its auxiliary-presentation coverage and mutual explicit-cut/simultaneous-substitution lemma. |
| [36](https://github.com/yzm1/proofbasis/pull/36) | d9a5272f9f31694331beb68f975e73e92436b572 | [Adversarial report 024](https://github.com/yzm1/proofbasis/blob/d9a5272f9f31694331beb68f975e73e92436b572/research/reviews/024-atomic-endomorphism-adversarial.md) | UNRESOLVED; typed attempted witness cancels, and compact semantic trace has no exhibited permitted term. |

Both Task 017 reports identify the original f2d7fcb1b00c36fdc4dfc3ab2a3e9ac487f566e7 baseline and state independent execution. PRs 35/36 target the Task 016 branch rather than main. Their base branch has subsequently acquired the status/coherence revision above, without altering the frozen claim. All three PRs were open when checked. Automated review completion is not independent mathematical certification.

## What changed mathematically

Report 023 gives a candidate argument covering arbitrary mixed representatives: translate them into typed auxiliary sequent rules, eliminate explicit linear cuts and nonlinear simultaneous substitutions by mutual induction, then classify the last rule at the atomic boundary. Its auxiliary logical templates may themselves use target compositions; it explicitly distinguishes that from literal cut elimination in Shulman's Figure 2 calculus.

Report 024 converts the same atomic question into classification of closed nonlinear names of U(p*⅋p) by the stipulated universal bijections. It duplicates a genuinely closed identity-function name, reconstructs two linear identities, composes them and evaluates on p. The displayed product/modal/hom equations cancel the construction. Its compact-model trace idea would separate a scalar semantically, but the necessary tensor/cotensor and unit/counit interfaces or feedback have not been supplied by a permitted syntactic term.

These conclusions are compatible. A failed independent witness search is not a proof of the positive statement and is not a cross-review of report 023.

## Coordinator checks and their limits

I read both reports, their contracts, rule tables, proof arguments, dependency ledgers and PR comments; compared the additional commit on PR 34; and checked each PR's file scope. No decisive counterexample or invalid typing step was established in this review.

Direct primary checking: Shulman 2023 §8 Proposition 8.3 and its quotient paragraph supply representations and the full specified congruence, not the new cut/substitution lemma. The paper explicitly leaves cut elimination for future study. This supports report 023's decision to label its lemma INFERENCE rather than attribute it to the paper. This review does not independently re-certify all seven source audits reported by the agents.

Concrete points supported on this pass, still informal:
- The auxiliary F/U rules preserve their empty-linear-input restrictions.
- The ordinary principal modal and tensor/cotensor steps are licensed by the specified universal β equations.
- Simultaneous substitution is a necessary response to nonlinear contraction; repeated ordinary cuts cannot silently reuse an original height bound.
- The proposed measure is lexicographic in type rank and producer/consumer height. Lower-rank recursive problems may grow in height.
- Report 024 distinguishes definable target terms from arbitrary model arrows, and rejects both illicit promotion of a live p and a self-trace.
- Report 034's revised raw-dual comparison remains a checklist, not a completed bridge proof.

## Exact acceptance bottleneck

Before accepting the atomic conclusion, independently reconstruct report 023's §§3.4–4 argument:

1. Coverage of every selected target projection/inverse factorization, at arbitrary admissible ambient contexts.
2. Source-left-rule commutation (S), with simultaneous replacement, sharing and exact named context maps, especially when the continuation is linear.
3. Exhaustiveness and strict decrease of the mutual induction, including multiple selected slots, producer eliminations, and principal F/U/dual cases.
4. The raw-dual rotations and snake equality, without extra strictness or a self-cut.
5. Equality in the original E*: auxiliary cut-free existence must yield an actual equality chain for every target representative.

The report claims a broadly quantified cut/substitution lemma to obtain a small atomic conclusion. Review the lemma at its actual breadth; do not validate it only on a few atomic examples. Acceptance of the atomic instance would not automatically establish source equality reflection, substitution naturality for full SC, the pure bridge, the finite-schema clause, or unrestricted universality.

## Next action

[Task 018](../../tasks/018-atomic-reciprocal-review.md) freezes reciprocal review of these two submissions. Agent B attacks/reconstructs report 023; Agent A reconstructs report 024 and applies the exact auxiliary templates to its closed-name construction. Both identify specific typed defects or independently checked argument steps. No new agents are launched by this document.

Decision now: **PROCEED TO BOUNDED RECIPROCAL REVIEW; atomic statement not yet accepted**. No broader theorem attempt, implementation or general definition round. The source reports remain preserved as evidence; proposed corrections belong in separate reviews.
