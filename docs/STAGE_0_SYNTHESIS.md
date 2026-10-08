# Stage 0 synthesis — provisional, 2026-10-08

**Status: coordination document, not a scientific verdict.** This synthesis is based on the open PR #1 and PR #2, including the *later* self-review `reports/001-review.md` present in PR #2. None has been accepted or mechanically verified. The branch intentionally leaves the original charter unchanged.

## Source branches and collision

- [PR #1](https://github.com/yzm1/proofbasis/pull/1): concise adversarial audit; recommends **narrow**, no implementation.
- [PR #2](https://github.com/yzm1/proofbasis/pull/2): expanded adversarial audit with source notes; originally recommends **stop**, then includes a subsequent review explicitly saying the stop verdict **does not follow from the evidence**. Its subsequent review discloses it is not fully independent (same model/session, with a fresh-context sub-review).
- Both PRs add `reports/001-existence-and-novelty.md` with different content. **Do not merge both unchanged**; preserve both with unique names when integrating. Do not overwrite either audit or conflate their conclusions.

## Strong points of convergence (claims still subject to checking)

1. Current CV0 is underspecified and existential quantification over the source class permits trivial satisfaction.
2. Generic interpreter universality is not the desired structural result; an anti-vacuity requirement is essential.
3. LF-like and rewriting frameworks already demonstrate powerful relative representation results and per-encoding adequacy. Do not market this as an entirely unstudied existence question.
4. Primitive inference content versus environment assumptions/definitions and proof-checker trust must be kept explicit.
5. Raw-derivation adequacy does not automatically preserve source proof equivalence.
6. Causal independence, conflict, resource discipline, and global validity are distinct; chronology is not necessarily semantics.
7. An obstacle in one encoding, or expensive equality, is not a general impossibility theorem.

## Disagreements and required corrections

- **Stop vs narrow:** PR #2's initial stop recommendation is disputed by its own later review; no global impossibility theorem has been established.
- **Vacuity–identity dilemma:** PR #2's self-review reports its original supporting lemma switched preservation and reflection. Treat original lemma as **retracted pending verification**; do not cite as a result.
- **Allegedly exhaustive horns:** The same review brings forward generic modal/substructural frameworks (Licata–Shulman–Riley, Shulman, etc.) as a potential third route. Investigate exact theorem statements and open conjectures; don't accept either dismissal or salvation without checking.
- **Complexity as obstruction:** PSPACE-complete or non-elementary equality is a computational-cost result, not a representation impossibility by itself.
- **Proposed next tests differ:** PR #1 advocates a minimal MLL proof-net-equivalence counterexample versus raw LF encoding; PR #2 suggests a larger three-foundation CLF conjecture. The former is a diagnostic example, not proof all faithful encodings fail.
- **Evidence status:** The underlying reports include partial-source, informal and independently unchecked findings. Source logs are useful research evidence, not proof certificates.

## Stage 0.5 objective

Develop (A) a meaningful, non-vacuous formal criterion for fundamental/common proof operations and trust-aware environment separation; and independently (B) a rigorous study of structural proof identity, resource behavior and causal permutations using a minimal reference example and existing frameworks.

**No joint theorem is assumed.** Do not construct a new prover, universal algebra or large corpus.

## Two independent tasks

- [Task 002 — fundamentality and anti-vacuity](../tasks/002-fundamentality-and-anti-vacuity.md), intended for Claude.
- [Task 003 — proof identity and structural fidelity](../tasks/003-structural-fidelity.md), intended for Codex.

Agents may read the Stage 0 audits but must form independent conclusions, verify primary-source claims and avoid simply endorsing whichever prior report seems more confident. Deliver separate reports and PRs without editing the other task's files.

## Decision gate

After independent task reviews, decide **stop / narrow / proceed to one restricted theorem**. Advancing requires: (i) an exact quantified conjecture with source class fixed independently; (ii) an anti-vacuity test that excludes a real interpreter counterexample without excluding legitimate structural encodings by fiat; (iii) a testable fidelity specification; (iv) explicit trust and equality boundaries; (v) a concrete unsolved lemma or independently checked counterexample, not merely lack of literature coverage.

If any condition fails, report failure and do not initiate implementation.
