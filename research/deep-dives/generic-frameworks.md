# INST-01 — Generic and indexed logical frameworks

**Date:** 2026-10-13. **Status:** bounded research comparison, not a universal existence theorem. **Task:** Task 012 / INST-01. **Baseline:** CMP-01 v0.1 on branch `research/cmp-01-live` (PR #21), still under independent review.

## Executive result

A fixed *generic deductive grammar parameterized by structural data* is established mathematical prior art. The clearest relevant strands are Licata–Shulman–Riley's (LSR) fibrational/mode-theoretic framework (2017) and Shulman's linear/nonlinear (LNL) polycategories and doctrines (2023). The latter proves that free algebras for its doctrines admit sequent-calculus presentations and that doctrine maps induce adjunctions between algebra 2-categories. **This is a substantive universal-property result, but only relative to the chosen doctrines.** It does not imply that arbitrary source inference rules are derived in one fixed, unparameterized kernel, or that all original proof identities are reflected by the generic framework.

**Crucial unresolved point:** The extended LSR author version explicitly labels **Conjecture 8.5**, completeness of permutative equality: if two derivations are equal, their normal forms are related by the specified permutation equality. Its Section 9.1 describes a hoped-for full and faithful encoding of object logics. A targeted search as of this investigation found the original extended text and later generic framework developments, **but not a primary published proof or refutation of Conjecture 8.5**. It is therefore *current resolution unverified*, not confidently 'still open'. The 2023 LNL doctrine theorem concerns a related broader categorical construction and cannot be substituted for that exact conjecture without checking both proof-equality definitions.

## 1. CMP-01 comparison grid

Codes: P = derivability preservation; R = reflection from all relevant target inhabitants; EP = proof equality preservation; ER = equality reflection; F = fullness on proof classes; C = composition/substitution; U = resource fidelity; TR = trusted-premise provenance; CF = causal trace preservation. 'Established' only for the particular cited theorem's scope.

| Framework | Mathematical structure / parameters | Established relevant strengths | Gap relative to CMP-01 |
|---|---|---|---|
| Edinburgh LF / Twelf | Dependent typed judgment families; object inference rules as signature constants | Canonical-form adequacy for specified FO/HOL natural deduction; source-term and proof substitution (HHP Thms 4.1–4.2) | Object inference constants are trusted declarations, not derived from unchanged LF core; source beta/eta/net identity not automatically kernel equality; no generic all-logic adequacy theorem |
| LLF | LF with linear context discipline | Tracks specified linear resources directly and extends LF (Cervesato–Pfenning) | New trusted logical machinery; not proof-identity universality |
| CLF | Linear/logical concurrent judgments, monad and concurrent equality | Labeled Petri-net trace classes correspond to concurrent expressions under specified equivalence (CLF II Thm 5.23 plus equality inversion lemmas) | Requires labeled tokens and fixed Petri signatures; ≠ generic proof-net equality across mathematical foundations |
| Dedukti / lambda-Pi modulo | Dependent terms with user rewrite systems | Relative embeddings and conservativity for selected functional PTS (Assaf); efficient definitional reduction where assumptions hold | Environment can supply source-specific rewriting and proof/equality computations; subject reduction/confluence/compatibility obligations; imported rewrites are not free derived proof operations |
| MMT / institutions | Theory morphisms; signatures, sentences/models, satisfaction in institutions | Modular structure and preservation under suitably defined morphisms; foundation parameter explicit | Foundation-specific logical validity/proof objects and equality need additional semantics; satisfaction-level preservation ≠ proof-level EP/ER |
| LSR modes | Generic positive and negative connectives parametrized by mode theories governing contexts and structural behavior | General sequent/normal-form calculus, identity/cut for suitable mode theories, beta/eta and permutation discussion | Conjecture 8.5 and source-to-framework equational adequacy need exact resolution; no arbitrary-foundation universality |
| Shulman LNL doctrines | LNL polycategories, structural/doctrine sketches, morphisms of doctrines | Free algebras presented by sequent calculus; doctrine maps induce adjunctions between 2-categories of algebras (published LMCS 2023) | The universal property is *relative to doctrine*. Need explicit theorem showing it reflects each source's selected Eq under specified translation, and an audit of doctrine data as trusted inference machinery |
| Dependent contextual / type-theory semantics | Contexts, substitutions, comprehension/display maps and type families | Initial/bi-initial semantic results for specified structural dependent theories (e.g. Uemura) | Compatible interaction with arbitrary linear/multimodal mode structure and equality needs proof; no automatic global source-class coverage |

## 2. What a fixed generic grammar actually buys

In LSR, a **mode theory** determines how context resources are combined and transformed; the same generic proof constructors may then describe multiple modal and substructural calculi. In Shulman's 2023 LNL formalism, a **doctrine** selects permissible structural and logical operations and their universal properties; free algebras have sequent-calculus syntax.

This matters to ProofBasis because a whole family of inference disciplines can be described with stable generic *forms of composition*, rather than one unrelated primitive for each object logic. However, a parameter describing the allowed structural maps is itself mathematical inference content. Therefore:

- **Syntax-level universality**: fixed grammar + variable data is a legitimate framework theorem.
- **Proof-theoretic legitimacy**: a rule supplied via a doctrine still needs an appropriate justification relative to that doctrine or source logic.
- **Strong source fidelity**: a source-to-generic translation must separately prove P/R and EP/ER, with chosen proof equality on both sides.
- **Universal finiteness**: even if each source doctrine is finite, there is no automatic theorem that a fixed finite *unparameterized* algebra derives all doctrines or preserves all their identities.

Thus 'a generic framework exists' is not equivalent to the ProofBasis north-star theorem, but its free/doctrine universal properties offer a better baseline for the algebra comparison than a mere universal checker.

## 3. Precise positive control

Consider a resource-sensitive source whose judgments carry a linear context and a tensor constructor. Choose a corresponding mode/doctrine admitting linear splitting but no contraction. Within a matching linear target, a proof of `P ⊗ P` requires two linear resources when `P` is atomic and there are no additional axioms or modalities. The structural constraints are carried by the context/doctrine, rather than a runtime check of a serialized derivation.

This illustrates **how U can be native to a parameterized deductive grammar**. Establishing a particular source-to-LSR adequate translation still requires a theorem, and nothing about this example establishes EP/ER or full cross-foundation universality.

A second verified positive instance is CLF's labeled Petri-net trace adequacy; its concurrent equality identifies reorderings that satisfy explicit freshness/input/output independence conditions. It captures a useful part of our partial-order requirement within its declared domain, not all proof-history equalities.

## 4. Explicit negative controls

**A. Rule import masquerading as derivation.** In LF add `bad : true(P)` to the object signature for previously unprovable atom P. A term inhabits `true(P)` relative to the expanded signature. That fact is valid LF type checking, but it does not show that P is derivable from the *unchanged logical machinery and original mathematical assumptions*. In CMP-01 terms, P may hold relative to the new environment but TR/core-derivedness does not.

**B. Cartesian duplication of a linear hypothesis.** If a proposed translation maps `P ⊗ P` to ordinary Cartesian `P × P` and maps its single source linear input P to the same unrestricted P, a diagonal `P → P × P` exists in the target although the source linear sequent `P ⊢ P ⊗ P` is not derivable. The specific translation fails R and U. This does not rule out disciplined linear-to-nonlinear modal translations.

**C. Identity mismatch.** Two cut-free MLL derivations differing by commuting independent rules correspond to the same source net. A naive LF presentation with separate uninterpreted rule constants produces target terms with different normal heads. Therefore EP for the source net quotient fails even when raw-derivation adequacy holds. This is the Report 003 fixture and the van Glabbeek–Hughes correspondence; it rules out **that encoding**, not the generic-framework approach as a whole.

**D. Cyclic global correctness.** A finite cyclic pre-proof graph assembled from locally valid inference steps need not satisfy the progressing-trace condition. No generic context grammar may assume node-local derivation well-formedness suffices for global Val. The status of a cyclic source translation requires its own global acceptance/certificate argument.

## 5. Exact LSR Conjecture 8.5 status review

**Primary source located:** Licata, Shulman, Riley, *A Fibrational Framework for Substructural and Modal Logics*, FSCD 2017, DOI 10.4230/LIPIcs.FSCD.2017.25; extended author manuscript [lsr17multi-ex.pdf](https://dlicata.wescreates.wesleyan.edu/pubs/lsr17multi/lsr17multi-ex.pdf), Section 8 and Section 9.1.

**Original statement (paraphrase):** Under its typed deductive calculus and equational theory, equality of derivations implies equality of the corresponding normal forms modulo designated permutative equality. This is labeled **Conjecture 8.5** in the extended text.

**Why it is relevant:** Section 9.1 sketches a route to equational adequacy: object derivations translated into framework derivations should be full and faithful relative to chosen identity laws, not merely equivalent at the theorem level.

**2026 verification result:** a targeted October 2026 search located the extended manuscript and the 2023 Shulman LNL doctrine paper, but no directly verified publication specifically proving or refuting this Conjecture 8.5 in the stated calculus and equality. A search failure is not evidence that a conjecture remains open. The older manuscript also reportedly has a later 'Theorem 8.5' cross-reference despite its labeled conjecture; do **not** infer it was proved from that cross-reference.

**Required future check, not optional before novelty claim:** inspect author bibliographies, citing works and any corrected revisions; determine whether the equality theorem is a corollary of later generic framework results **under identical hypotheses**. Until then mark `STATUS_UNVERIFIED_2026`.

**Bounded missing lemma:** For a selected source linear calculus and specified mode theory, prove or refute that the existing translation reflects **the source's chosen proof equality** in the generic framework's fixed equality (or show a published theorem does). In particular, don't import source equality as new unverified target equations. A narrower instance can be a useful discriminating test, but it does not independently prove an arbitrary-foundation universal algebra.

## 6. Comparing the indexed/fibrational strategy with dependent binding

Dependent type theory requires context extension `Γ,x:A` and substitutions that reindex subsequent dependent types. Linear/nonlinear modes constrain structural maps on proof-resource contexts. They address distinct axes. A universal candidate would need to demonstrate their interaction, not only show each separately expressible.

At the CMP-01 level a comparison must name:

- base category of contexts and typed substitutions;
- fibers of types/judgments/proofs over each context and reindexing;
- mode-indexed resource zones and admissible structural maps;
- chosen conversion/proof-congruence and exact coherence with reindexing;
- trusted schema/doctrine parameters and justification;
- how proof composition and mode transitions interact with dependent substitutions.

The available cited results are powerful *component constructions*, not a checked single structure satisfying arbitrary dependent and linear/modal proof calculi.

## 7. S2 decision and next step

**INST-01 outcome: partially positive, bounded by proof identity and parameter trust.** A substantial part of the structural-generation ambition is represented by established generic mode/doctrine frameworks. This motivates a comparison with ALG-01's free presentations and binding-aware signatures under the same contract.

**Not established:** full and faithful embedding of every selected proof identity; a finite unparameterized proof algebra; decidable universal checking; any unique notion of fundamental operation.

**Next bounded investigation:** compare the exact doctrine/mode parameters and equality of a chosen linear example against the free proof-category model, and separately verify the current status of LSR 8.5. Use OBS-01 to challenge claims about coherence/finite presentation rather than treating complexity results as impossibility.

**Stop rule:** if a candidate fails an equality or trust obligation, report exactly that pair and assumption. Do not inflate it into a universal impossibility theorem. If a current theorem settles the specified comparison, record redundancy and move on.

## Bibliographic provenance

- **Verified publication/abstract or primary text in this pass:** LSR FSCD 2017 publication (https://doi.org/10.4230/LIPIcs.FSCD.2017.25); extended LSR author text, §§8–9 (https://dlicata.wescreates.wesleyan.edu/pubs/lsr17multi/lsr17multi-ex.pdf); Shulman, *LNL polycategories and doctrines of linear logic*, LMCS 19(2) (2023), DOI 10.46298/lmcs-19(2:1)2023 (https://lmcs.episciences.org/11160). It establishes free doctrine algebras presented by sequent calculus and doctrine-morphism adjunctions, in the scope of the paper.
- **Prior repo source extraction, not newly independently rechecked from full primary theorem proofs:** Harper–Honsell–Plotkin LF Thms 4.1–4.2; Assaf conservativity for PTS; CLF II Thm 5.23; Uemura bi-initiality. Source reports 001–014 document versions and qualifications.
- **Unknown:** current global resolution of LSR Conj 8.5; exact equational reflection for multi-foundation source families; fully combined dependent+mode semantics with the desired proof identity.
- **No newly mechanically verified theorem** in this report. Mathematical examples are informal and standard fragment-specific arguments.
