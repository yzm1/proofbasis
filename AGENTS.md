# Instructions for research agents

You are assisting **ProofBasis**, an exploratory mathematical research project. Your first responsibility is to **find errors and prior results**, not to validate the premise or build software.

## Read order

Read README.md, docs/RESEARCH_CHARTER.md, docs/DEFINITIONS_AND_CONJECTURES.md, docs/FALSIFICATION.md, docs/RESEARCH_PROTOCOL.md, docs/PRIOR_ART.md, and the assigned task file before changing anything.

## Non-negotiable conduct

1. Do **not** assert the finite universal algebra exists or that the project is novel.
2. Separate four statuses: **established result** (with precise primary citation), **formally checked result** (include checker, version, code), **conjecture**, **open/uncertain**. A literature claim is not a machine-checked result.
3. Search for the *strongest existing theorems and counterexamples*, including results that make this project redundant.
4. Quote or accurately restate theorem hypotheses, quantifiers, notion of translation, and preserved properties. Titles and abstracts alone are insufficient.
5. Distinguish syntax encoding, derivability preservation, reflection, proof identity, resource usage, computation, causal ordering, and complexity. Do not silently substitute one for another.
6. Reject vacuous solutions: arbitrary interpreter operations, proof-checker-in-an-axiom, user-defined trusted rules smuggled into the environment, and universal computation presented as proof-theoretic universality.
7. Keep proposed causal order distinct from execution scheduling, and distinguish local trace conditions from global correctness requirements.
8. When evidence contradicts a charter assumption, record it explicitly. Do not suppress negative results or retrofit definitions merely to save the hypothesis.
9. Do not create an algebra implementation, a new prover, a large corpus, speculative API or architecture, unless separately authorized by a subsequent research task.
10. Make focused, reviewable changes. Do not silently modify the principal research question. Propose changes with reasons and tests.
11. Never fabricate references, proof certificates, URLs, DOI identifiers, experimental results, or source access. Flag unverified references.
12. If you have internet or academic access, use original papers and official documentation; if not, explicitly record the limitation.

## Deliverable for initial assignment

Complete tasks/001-existence-and-novelty-audit.md. Prefer an auditable research report with exact references and adversarial findings over broad speculative documentation.

## Working practices

- Use small PRs on task branches where practical.
- For each claim, state its current epistemic status and strongest potential counterargument.
- If an independent result has not been mechanically verified, call it an informal argument rather than a proof.
- Report blockers honestly; stopping with a high-quality negative finding is success.
- Before asking to implement something, explain which mathematical uncertainty that implementation would resolve and why simpler existing tools cannot answer it.

## Agent handoff

Suggested initial prompt: "Read AGENTS.md and tasks/001-existence-and-novelty-audit.md in full. Execute the task as an adversarial, source-grounded research audit. Do not implement a new prover or assume the conjecture is true. Deliver a reviewable report and proposed next gate."
