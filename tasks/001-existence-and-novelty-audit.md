# Task 001 — Adversarial existence and novelty audit

## Mission

Determine whether ProofBasis's desired universal finite structural proof algebra is (a) already known, (b) vacuous under current definitions, (c) defeated by established counterexamples, or (d) a defensible open research target after narrowing. Be skeptical; do not design a solver.

## Required reading

Follow AGENTS.md. Read all Stage 0 documents before making changes.

## Work packages

1. **Formalization audit** — enumerate every unresolved term in docs/DEFINITIONS_AND_CONJECTURES.md; propose at least two rigorously distinct versions of the target with clear tradeoffs.
2. **Strongest prior art** — examine original literature on general logics/rewriting logic, LF/Twelf, MMT, Dedukti, Curry–Howard–Lambek, and proof nets. Extract exact source theorems (including assumptions and proof-identity preservation).
3. **Red team** — attempt F01–F10 in docs/FALSIFICATION.md, prioritize F01–F04 and F08. Seek concrete mathematical counterexamples, not rhetorical concerns.
4. **Nontriviality benchmark** — give an explicit 'universal interpreter' construction and articulate a checkable restriction excluding it without excluding standard logical frameworks by fiat.
5. **Cross-foundation stress tests** — classical/constructive, linear/resource, dependent binding, cyclic/global validity; state precisely which preservation goals survive.
6. **Decision memo** — recommend stop, narrow, or advance, with the strongest remaining conjecture and a single discriminating next test.

## Output

Create reports/001-existence-and-novelty.md (add directory as needed), with: executive verdict; precise candidate conjectures; verified bibliography and quotations/paraphrases with locations; comparison matrix of strongest known theorems; counterexample dossier; unresolved objections; recommended next gate. Use Markdown. Do not call a theorem new without independent source verification.

May propose minimal amendments to definitions, but **do not rewrite the project mission unilaterally**. Keep disputes explicit.

## Forbidden work

No custom prover, no algebra implementation, no UI/graph database, no extensive auto-generated proof corpus, no unsupported theorem assertions, no invented citations.

## Completion standard

A useful negative verdict with traceable evidence is acceptable. A generic survey with unverified references is not. Summarize exact limits of research access. Mark every critical claim with an evidence status. Request review rather than claiming research closure.
