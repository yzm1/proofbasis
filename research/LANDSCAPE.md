# Mathematical landscape registry — seed map, not a completed review

Purpose: avoid premature tunnel vision. An item is a research lead, not endorsed machinery. **Coverage states**: seed / scoped / investigated / ruled out with argument / deferred with reason. Owners and evidence links should be added as work occurs.

| Family | Questions for ProofBasis | Initial priority | Coverage |
|---|---|---|---|
| Structural proof theory: ND, sequent, focusing, deep inference, cut elimination | Primitive/derived rules, proof transformations, normalization and admissibility | Essential | Investigated unevenly |
| General proof theory / identity of proofs | When proofs are the same; normalisation vs generality | Essential | Partial |
| Categorical logic: CCC, *-autonomous, monoidal, multicategories, doctrines | Proofs as morphisms, composition and universal properties | Essential | Partial |
| Universal algebra, clone theory, Lawvere theories | Generators, term equivalence, independence, closure under substitution | Essential | Partial, strengthened PR #16 |
| Many-sorted, second-order algebra, binding signatures, contextual categories | Binding, metavariables, substitutions, resource-sensitive operations | Essential | Partial |
| Proof-theoretic semantics, harmony, inferentialism | When rules are justified rather than merely represented; tonk-like failures | Essential | Thin |
| Logical frameworks: LF/Twelf, LLF/CLF, Dedukti, MMT, FPC | Cross-system representations, trusted signatures and certificates | Essential | Extensive but heterogeneous |
| General logics, institutions, fibrations, equipment/doctrines | Foundation-independent specification and translations | High | Partial |
| Higher-dimensional algebra: polygraphs, computads, rewriting modulo, coherence | Equations and transformations between derivations; finite resolutions | High | Thin |
| HoTT, univalent foundations, cubical type theory | Higher identities, computation of paths, fibrancy and coherence | High | Thin |
| Rewriting logic, Maude, term graph rewriting, e-graphs/equality saturation | Derivation graphs, strategy, sharing and equivalence | High | Partial |
| Concurrency: event structures, Petri nets, traces, partial-order semantics | Independence, conflict, generational/causal order | High | Partial |
| Automated deduction: resolution, superposition, SMT, constraints, proof complexity | Derived operations vs search procedures, proof size/verification | High | Partial |
| Model theory, descriptive proof semantics, proof-relevant semantics | Models, completeness, inability to infer identity from truth | Medium | Uneven |
| Computability, universal machines, incompleteness, recursion theory | Limits, degenerate interpreters, undecidable congruence | High | Substantial |
| Operads, PROPs, polycategories, double categories | Multi-input operations, modes of composition and diagrams | High | Thin |
| Type theory and logical relations, parametricity, effect modalities | Genericity, representational fidelity and resource modalities | High | Partial |
| Homological/algebraic topology analogies and higher rewrite invariants | Potential invariants of proof spaces | Exploratory | Seed |
| Wolfram multiway/ruliad metamathematics | Multiway paths, branchial/causal graphs and rule spaces | Comparative | Seed |
| Langlands/functoriality analogies | Transfer-of-structure methodology, not direct proof machinery | Defer technical dive | Seed |
| Other candidates discovered during mapping | Add with cited reason; don't assume list complete | Unknown | Open |

## Required coverage pass

An agent assigned S1 must proactively look for **important missing theory families** rather than treating this list as exhaustive. For each family locate seminal sources, strongest applicable theorems, possible obstruction or negative evidence, relationship to proof operations, and whether a focused deep dive is justified. Do not infer novelty from an incomplete survey. Look explicitly for adjacent approaches that invalidate the working framing.

## Theory deep-dive protocol

One deep dive = one narrowly scoped question and a bounded paper set, with exact theorem hypotheses, strongest positive/negative relevance and a concrete comparison against the common controls. Submit report under research/deep-dives/<slug>.md, include sources and remaining gaps. A deep dive is not permission to redefine the universal conjecture.

## Proposed additions from review 011 (pending owner review)

Source: `research/reviews/011-landscape-audit.md` (§2, §3, §5). The seed table above is **not** edited. These rows and status updates are proposals for the owner to accept, amend or reject. Status vocabulary follows this file.

### Proposed organising axis (layers)

L0 computation/derivability · L1 generation of syntax with binding · L2 justification of rules · L3 proof identity · L4 higher transformations/coherence · L5 cross-foundation translation · L6 causality. Rationale: these are distinct questions. Finite bases are already known at L0/L1 and per-logic at L3, so any novelty claim must name its layer.

### Proposed new rows

| Area | Why it matters | Proposed priority | Proposed status |
|---|---|---|---|
| Generic substructural/modal frameworks: Licata–Shulman–Riley, adjoint logic, MTT, Shulman LNL polycategories | Closest active programme: fixed generic machinery + per-logic structural data; open proof-identity conjecture (LSR Conj 8.5), named in 001-review as the discriminating test but never executed | Essential | Partial (001-review; 011 DD0) |
| Canonical Gentzen systems (Avron–Lev), analytic-calculus hierarchy (Ciabattoni–Galatos–Terui), display logic (Belnap) | Decidable coherence/analyticity criteria inside fixed structural settings, with proved limits (CGT Cor 7.2, Ex 7.4); originals partly not accessed | High | Partial (011) |
| Polygraphic presentation of proofs (Guiraud 2006) | Direct prior art: finite 3-polygraph (rules = 3-cells) for classical propositional proofs modulo structural bureaucracy only | High | Partial (011) |
| Squier theory / finite derivation type as obstruction theory | Presentation-invariant obstructions (S₁; undecidability; dimension-3 failure). Already used for single counterexamples in 001/010; proposed here as a method | High | Partial (001, 010, 011) |
| Binding-aware 2-dimensional rewriting (Hirschowitz 2013; reduction monads; explicit substitutions) | Addresses the binding gap of polygraphs; finiteness invariants unknown | High | Partial (011) |
| Equational finite-basis problem (Tarski; McKenzie; Lyndon/Murskiĭ/Perkins) | Canonical theory of obstructions to finite equational bases | High | Unknown (memory only) |
| First-order proof identity (expansion trees, first-order combinatorial proofs, hyperdoctrines) | All surveyed identity results are propositional | High | Unknown |
| Logic-translation theory (Mossakowski–Diaconescu–Tarlecki; proof-theoretic institutions) | Whether any morphism notion preserves proof identity | Medium | Unknown |
| Finite complete PROP presentations (Lafont circuits, ZX, interacting Hopf algebras) | Method for "finite + complete for a fixed semantics"; Lafont non-generation already in 001 as an analogy | Medium | Partial (001, 011) |
| Type theories as finite presentations / initiality (Uemura, Bauer–Haselwarter–Lumsdaine, Ahrens–Hirschowitz–Lafont–Maggesi) | "Foundation = finite schema presentation with initial semantics" for structural dependent theories; linear/modal excluded (Kaposi–Xie, 001-review) | Medium | Partial (001-review, 011) |
| Tarski–Givant / relation and cylindric algebra; abstract algebraic logic | Pre-empts finite bases for derivability (ZF in a finite equational calculus) | Medium (boundary) | Partial (011) |
| Combinatory and illative combinatory logic | Historical finite basis for computation; failure as a basis for logic (Curry) | Low (lesson) | Partial (011) |
| Admissible-rule bases (Rybakov, Jeřábek, Iemhoff) | IPC admissible rules have no finite basis; derivable vs admissible | Medium | Partial (011) |
| Process-algebra finite axiomatisability (Moller; Aceto et al.) | Signature-relative negative finite-basis theorems | Medium | Partial (011) |
| Interpretability, sameness of theories, tightness | Theorem-level comparison of foundations; the levels separate | Medium | Partial (011) |
| Combination / fibring of logics | Non-modularity of combining logics | Medium | Partial (011) |
| Reverse mathematics, ordinal analysis, realizability, logicality | Boundary references (strength, computational content, invariance) | Low | Deferred (011) |
| Directed type theory | Non-invertible transformations as types | Low–medium | Seed |
| Ludics / geometry of interaction, transcendental syntax, quantitative/graded proof theory, proof mining | Not reached in 011 | Unknown | Seed |

### Proposed status updates to existing rows

| Existing row | Current | Proposed | Evidence (011) |
|---|---|---|---|
| General proof theory / identity of proofs | Partial | Partial; deep dive DD3 recommended (narrowed to controls incl. first order) | Došen §4–5; Straßburger; Selinger Cor 3.8; 001 `proof-identity.md` |
| Proof-theoretic semantics, harmony | Thin | Partial; not a safe sole criterion | §3.3 |
| Higher-dimensional algebra: polygraphs | Thin | Partial (already engaged in 001 notes S6a and 010); DD1 recommended after DD0/DD3 | Polygraphs book Thms 7.3.5, 8.1.2, 8.2.4; Guiraud 2006 |
| HoTT / cubical | Thin | Partial; narrow question only | HoTT book; Coquand–Huber–Sattler; Sterling–Angiuli |
| Operads, PROPs | Thin | Partial | Leinster; Lack; Lafont |
| Homological analogies | Seed | Partial (FDT ⇒ FP₃; S₁ is FP∞ but not FDT); absorbed into DD1 | Polygraphs book Thms 9.3.4, 9.3.15 |
| Wolfram multiway/ruliad | Seed | Investigated enough to deprioritise (subsumption by polygraphs is an inference) | review 011 §3.5, Q6 |
| Langlands analogies | Seed | Investigated enough to deprioritise: analogy only | review 011 §3.5, Q6 |
| Concurrency rows | Partial | Deferred under reconciliation D5 (H_causal), not dismissed | D5 |
| Other candidates | Open | Remains open; the map is **not** complete | review 011 §5, last row |
