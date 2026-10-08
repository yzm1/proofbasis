# Research charter — version 0.1

## Purpose

Investigate whether finite, compositional, mathematically interpretable proof-construction operations can serve as a common basis across diverse logical foundations **with meaningful structural fidelity**.

The intended investigation is *metatheoretical*: what proof machinery can express, which operations are necessary or derivable, which translations are possible, and what properties such translations preserve.

## Critical distinctions

- **Machine**: rules/constructors for building, transforming, and checking derivations.
- **Environment**: signatures, mathematical definitions, axioms, scoped hypotheses, previously justified lemmas and foundation parameters.
- **Trust boundary**: an environment containing unrestricted trusted inference rules could trivialize the goal. An imported rule must either be justified via the common machinery, be explicitly marked as an additional trusted primitive, or be recognized as an unproved extension.
- **Inference rule vs tactic**: a tactic may be search, orchestration or a macro; it is not necessarily primitive reasoning.
- **Provability vs proof representation**: preserving conclusions alone is not preserving proof structure.
- **Finite basis**: finite number of generators/rule *schemas*; generated expressions and proofs may be infinite in number.
- **Universality**: always relative to an explicitly quantified class of formal systems and an explicit preservation condition.

## Initial scope

Start with **finite, effectively described formal proof systems** and finite proof objects with mechanically checkable certificates. This scope is provisional and **may be rejected** if it hides important counterexamples or entails triviality.

The long-term ambition spans mathematical reasoning *across* foundational traditions, not merely the set of theorems provable within a single chosen foundation.

## Requirements to investigate, not to assume compatible

1. Fixed finite primitives, with composition.
2. Clear distinction between core operations and environmental assumptions.
3. Preservation of proof composition and substitution.
4. Preservation of binding/scoping and appropriate resource discipline.
5. Explicitly chosen notion(s) of proof equivalence/identity, not just theorem equality.
6. Causal dependencies and independently reorderable constructions when meaningful; distinguish chronological execution and semantic order.
7. Transparent, bounded trust obligations for external evidence and theory-specific extensions.

These constraints may be inconsistent together; finding that is a valid result.

## Non-goals (initial phase)

- Inventing a general-purpose mathematical language, theorem prover, or tactic engine.
- Automatically proving all truths; Gödel and undecidability impose limits.
- Asserting a unique or minimal basis without a formal notion of comparison.
- Optimizing proof-search performance before defining existence and fidelity.
- Creating a complete taxonomy or proof graph database.
- Claiming novelty before finding strongest prior work.

## Success and failure criteria

Success in the initial phase means at least one: (a) exact known theorem subsuming the target; (b) decisive obstacle/counterexample; (c) defensible, precise, nontrivial and plausibly open conjecture with clear boundary conditions; (d) rigorous restricted result. Merely producing many documents or an implementation is not evidence of progress.

A negative finding is a successful research outcome.

## Decisions deferred

Formal definition of proof systems and morphisms; whether environments may contain rule schemas and under what certification; preservation notion(s); exact treatment of infinitely branching/infinite proofs; categorical vs type-theoretic vs graph-theoretic presentations; efficiency measures; licensing and publication strategy.
