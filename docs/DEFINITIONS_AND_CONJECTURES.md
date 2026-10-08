# Definitions, candidate claims, and open choices

**Epistemic status:** Working hypotheses only, not established results. This file intentionally exposes ambiguity.

## Candidate objects

- **System** S: a formal language of judgments, environments and finite derivations with verifiable inference steps. Must be defined without presupposing our target algebra.
- **Environment** E: parameters and assumptions supplied to S. Distinguish ordinary propositions/definitions from certificates for extensions of inference machinery.
- **Finite algebra** A: a fixed finite signature of typed operation schemas, with explicit composition and equations or congruence on generated terms/diagrams.
- **Representation** F_S: a mapping from derivations in S into constructions of A under a translated environment; define whether it is injective, full, faithful, or only sound and complete for conclusions.
- **Proof equivalence** ~_S: an explicitly declared equivalence relation on derivations. Merely proving the same proposition is too coarse.
- **Causal relation** <=_S: dependencies between proof events; optional independence and conflict relations. Do not assume that an observed chronological execution is causal ordering.

## Candidate conjecture, not yet a formal theorem

There exist a fixed finite algebra A and a nontrivial class C of effectively presented proof systems such that, for every S in C, a compositional translation F_S maps finite derivations into constructions of A, with:

- preservation and suitable reflection of derivability;
- compatibility with proof composition, binding, and substitution;
- a specified relation between source proof equivalence and target equivalence;
- explicit accounting of assumptions and trusted extensions;
- preservation of an agreed subset of causal/resource properties.

**WARNING:** This is deliberately under-specified. The quantification over C, the meaning of 'meaningful operations', translation effectiveness, and faithfulness conditions can change its truth value drastically. Do not cite it as an existence theorem.

## Nested research targets

**R0 — representation:** every finite derivation can be encoded and checked. Likely too weak/trivial for our ambition.

**R1 — derivability:** preserve and reflect well-formed judgments and conclusions relative to explicit environments.

**R2 — compositional structure:** preserve substitution, composition, assumption discharge, variable binding and resource conditions.

**R3 — proof identity:** preserve/reflect a specified source congruence on proofs; compare with equality of diagrams/terms in target.

**R4 — causal fidelity:** preserve dependency, independence, branch conflict, and semantically relevant order when well-defined.

Higher levels are not assumed attainable simultaneously or uniformly.

## Necessary falsification questions

1. What does 'all known mathematical proof forms' mean as a **class**, rather than an informal list?
2. Does allowing S-specific signatures or rewrite rules in E just move the primitives into the environment?
3. Can any faithful mapping exist between proof identity notions in different foundations?
4. Is a *single fixed finite signature* plausible if we demand particular local/global graph correctness properties?
5. Does importing external facts preserve trust provenance rather than turn assumptions into certified theorems?
6. If arbitrary encodings are allowed, what mathematical invariant rules out vacuity?
7. Does a fixed algebra constrain proof complexity or proof-search complexity in any interesting way?

## Examples to stress

Classical first-order vs intuitionistic; intuitionistic vs classical continuations/negative translations; linear/resource-sensitive calculi; dependent types with binding; equational and higher-dimensional rewriting; proof nets and permutations of independent inferences; cyclic proof global trace conditions; infinitary omega-rule as an explicit boundary case.

## Relationship to optimization

Do not infer that the smallest basis is fastest. Keep proof length, construction/search cost, and checking/normalization cost separate. Stronger systems may have shorter proofs but harder search. Establish fidelity before benchmark selection.
