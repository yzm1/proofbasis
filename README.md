# ProofBasis

**Toward a finite, structurally faithful algebra of mathematical proof construction.**

**Status:** Exploratory research. Existence, novelty, universality, and feasibility are **not established**. This is not yet a theorem prover or a new mathematical foundation.

## Question

Can a **fixed finite basis of mathematically meaningful operations** represent finite formal proofs across significantly different logical foundations, with mathematical assumptions and definitions held in a separate environment, while preserving specified aspects of proof structure?

We care about more than encoding a proof checker on a universal computer. Potential preservation requirements include composition, substitution and binding, use of assumptions/resources, proof equivalence, and causal/partial-order relationships between operations.

We do **not** assume that the answer is yes. A known theorem that already settles the question, a counterexample, an impossibility theorem, or a defensible narrower formulation is a successful early outcome.

## Start here

1. [Research charter](docs/RESEARCH_CHARTER.md) — aim, non-goals, assumptions and boundaries.
2. [Definitions and conjectures](docs/DEFINITIONS_AND_CONJECTURES.md) — candidate formal statements and unresolved choices.
3. [Falsification plan](docs/FALSIFICATION.md) — prioritized ways to defeat the premise.
4. [Prior-art map](docs/PRIOR_ART.md) — research families and primary-source starting points; **not** a completed literature review.
5. [Research protocol](docs/RESEARCH_PROTOCOL.md) — evidence standards, review gates and deliverables.
6. [Agent instructions](AGENTS.md) — required reading and operating rules for Claude, Codex and other agents.
7. [First assignment](tasks/001-existence-and-novelty-audit.md) — bounded adversarial investigation.

## Research principles

- Treat **derivability**, **proof structure**, **proof identity**, **search**, and **checking** as distinct.
- Keep **machinery versus environment** explicit; don't hide arbitrary trusted inference rules in the latter.
- Do not count a universal interpreter or a Turing-completeness argument as sufficient evidence of the sought structural universality.
- Distinguish a *finite signature of operations* from a finite set of mathematical objects or proofs.
- Treat graph/partial-order representations as hypotheses, not predetermined implementation architecture.
- Record negative results and failed conjectures as first-class findings.
- No bespoke prover, large proof corpus, or taxonomy implementation before an approved research gate.

## Project progress

**Stage 0: specification and adversarial prior-art review.** No existence theorem claimed. No candidate algebra endorsed. See [the initial assignment](tasks/001-existence-and-novelty-audit.md).

## Contributing

Critical feedback, primary-source references, decisive counterexamples, and corrections to the mathematical formulation are especially welcome. Open an issue or PR linking the exact affected claim and evidence. See [research protocol](docs/RESEARCH_PROTOCOL.md).

## Licensing

No license has been selected yet. Until one is added, standard copyright rules apply; do not assume unrestricted reuse of the contents.
