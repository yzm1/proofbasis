# Prior-art map — reading queue, not an audited bibliography

**Important:** Entries below are research leads. Their relevance and precise theorems **must be verified from primary texts**; no universality result is claimed here.

## Core logical frameworks

- Harper, Honsell, Plotkin, *A Framework for Defining Logics* (Edinburgh LF, 1993). Search for adequacy of representations and the separation between LF machinery and object-logic signatures.
- Twelf (Pfenning and collaborators): logical relations, adequacy, totality checking and metatheory.
- Rabe, *How to Identify, Translate and Combine Logics?* (Journal of Logic and Computation). Examine exact notion of translations and preservation.
- MMT / theory morphisms (Rabe, Kohlhase and collaborators): foundation-independent theories; examine whether structural translations are faithful or merely modular.
- Dedukti / lambda-Pi calculus modulo rewriting: inspect theory-specific rewrite rules, subject reduction, confluence, and kernel trust.
- Miller and collaborators, *Foundational Proof Certificates*: distinction between certificate format, focused checker and trusted inference.

## Algebra and proof identity

- Curry–Howard–Lambek correspondence and cartesian closed categories: what 'same proof' and composition mean.
- Gentzen, *Investigations into Logical Deduction* (1935): sequents, structural rules and cut elimination.
- Girard, *Linear Logic* (1987): resource-sensitive structural rules and proof nets.
- Deep inference / calculus of structures (Guglielmi and collaborators): local inference inside formulas.
- Polygraphs, higher-dimensional rewriting, and presentations by generators and relations: what these encode faithfully.
- Rewriting logic as a logical and semantic framework (Meseguer, Martí-Oliet and collaborators): general logics, reflection, conservative encodings.

## Boundaries and performance

- Gödel completeness/incompleteness and Church/Turing undecidability: don't conflate semantic completeness, derivability and effective decision procedures.
- Cyclic proof systems and global trace conditions: local graph nodes may not determine proof correctness.
- Infinitary omega-rule and full second-order semantics: boundary of finite effective certificates.
- Cut elimination proof-size blowups, proof complexity, and tree-like versus DAG-like resolution: cost is not expressive adequacy.
- Cook–Reckhow proof systems and p-optimal proof system problem: separate search, certificate size, and checking costs.

## How to turn this into a literature review

For each lead, locate primary publication, retrieve bibliographic data, extract exact theorem with all assumptions, test applicability to candidate conjecture R0–R4, find known counterexample or limitation, and assign status per RESEARCH_PROTOCOL.md. Don't write 'X solves universality' unless the theorem matches the exact preservation property.
