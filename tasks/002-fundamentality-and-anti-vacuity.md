# Task 002 — Fundamentality, environment separation, and non-vacuity

**Suggested owner:** Claude. **Stage:** 0.5. **Output:** `reports/002-fundamentality.md` in its own PR.

## Mission

Adversarially seek a precise, **non-circular** definition of fundamental proof-construction operation and a representation criterion that rules out disguised universal interpreters without simply disallowing existing meaningful frameworks by decree.

Read AGENTS.md, the charter, definitions, falsification plan, the synthesis, and both Stage-0 PRs (including PR #2's later self-review). Verify decisive claims against primary papers.

## Problems to solve

1. Formulate **at least two inequivalent** formal definitions (e.g. operations as typed generators with homomorphic/local translations; generators-and-relations with source-indexed presentations), stating admissible environment contents and their trust provenance.
2. Analyze the difference between (i) introducing an assumption, (ii) deriving an inference rule in the core, (iii) declaring an object-logic rule, and (iv) supplying a checker or reduction procedure. Apply to LF, general/rewrite logics, Dedukti, generic modal/substructural frameworks and logical-framework adequacy.
3. Give explicit *adversarial counterconstructions*: general-purpose interpreter, checker-as-proof, wrappers disguised as structural templates, and environment-supplied equivalence rules. Try to make them pass your definition. If one passes, revise transparently or mark the definition inadequate.
4. Inspect primary sources for the generic-framework route cited in PR #2's later self-review (especially Licata–Shulman–Riley 2017 and Shulman 2023). Do these already provide a meaningful fixed generative mechanism? What exactly remains unproved?
5. Analyze whether minimality/independence can be defined invariantly under chosen translation constraints. Do not equate smallest primitive count with computational efficiency.
6. Offer the strongest **falsifiable theorem-shaped** formulation you can defend. It is acceptable to conclude that no satisfactory definition has been found.

## Required tests

- A true/false test on a small nontrivial reference calculus and at least one legitimate LF/focused/rewriting representation.
- A failure or explicit loophole for a concrete universal-machine encoding.
- A resource-sensitive negative control (unrestricted duplication must not masquerade as linear inference).
- A clear environment/machinery trust ledger.

## Deliverable structure

Executive verdict; exact formal definitions/quantifiers; comparisons with existing mathematical notions; construction/counterexample attempts; source theorem table with edition/page; limitations and unresolved questions; STOP/NARROW/PROCEED recommendation; one precise next test if necessary.

**Forbidden:** universal-algebra implementation, architectural design, corpus collection, treating original agent conclusions as proven, editing charter or the other agent's task.

## Completion test

If a proposal survives, identify an explicit property that the universal interpreter violates **and demonstrate why that property is not tailored only to reject the interpreter**. If not, say so plainly.
