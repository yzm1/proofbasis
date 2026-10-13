# CMP-01 — Common comparison contract, version 0.1 (candidate)

**Date:** 2026-10-13. **Status:** research proposal / comparison protocol; not an existence theorem, new logic, or an approved foundation-independent equivalence. **Task:** [011](../../tasks/011-common-comparison-contract.md). **Starting baseline:** main at `34900ee5afaab85dc2c094d3917c9b92f9d97589`.

## Verdict

A **common comparison *vocabulary*** is possible without asserting that there is one common proof algebra. The minimum object is a **structured deductive presentation** together with a declared notion of equivalence, and a **typed, obligation-indexed comparison map**. Existing binding-aware algebraic presentations and categorical/contextual semantics supply complementary, *not automatically equivalent*, views. The contract distinguishes failed obligations from a proven impossibility across all representations.

It does **not** solve non-vacuity by verbal prohibition, assert a canonical proof identity, or require fullness. There is no established theorem that every formal system admits such maps into one finite target. We can compare what a particular construction preserves.

## 1. A source description: signature of observable mathematical structure

A comparison instance is a tuple

**D = (J, Ctx, Sub, Hyp, Der, Comp, Eq, Res, Val, Env, Prov, optional Event).**

Each field is a *specified structure*, not assumed to exist uniformly or to be algorithmically decidable.

1. **J**: sorted judgment and object-expression families. Distinguish formulas, terms, types, propositions, well-formedness judgments and equality judgments.
2. **Ctx**: admissible, scoped object-variable and proof-hypothesis contexts; weakening, contraction, exchange, linear split, ordered use and modal zones are explicitly declared, not inherited from Set.
3. **Sub**: typed context substitutions, identity/composition, capture avoidance and renaming. In dependent calculi, a substitution changes the types of subsequent variables; record dependent substitution judgment rather than mapping contexts to unstructured lists.
4. **Hyp**: open derivation metavariables/holes with a scoped boundary; filling holes is permitted only along specified context maps and modes.
5. **Der(E, Γ; J)**: raw finite derivations or finite certificates with explicit correctness predicates. Do not identify derivations with theorem truth.
6. **Comp**: identity and partial typed grafting/cut/composition of derivations; can be categorical, multicategorical, relative-monadic or a presented operational relation. Explicit coherence laws and their proof obligations.
7. **Eq**: *chosen* typed congruence on comparable proofs; name alpha, beta, eta, commuting conversions, cut reductions, net identity, observational equivalence or proof irrelevance separately. Do not assume target definitional equality equals source equality; record equality reflection and preservation independently.
8. **Res**: explicit usage observations or structural permission discipline on contexts/operations. Raw occurrence counting need not survive beta erasure; declare what survives Eq.
9. **Val**: the source's checking/justification predicate and soundness contract *relative to specified assumptions*. Distinguish locally checkable rule instances from global graph trace requirements.
10. **Env**: signatures, mathematical assumptions, definitions, previously established lemmas and extensions; distinguish their effect on judgment derivability from mere notation changes.
11. **Prov**: provenance for each trusted premise, inference rule, equality axiom and external checker. A declared rule is an additional trusted assumption unless it carries a derivation/admissibility certificate. One must not claim it was *derived* merely because it inhabits a type in LF.
12. **Event (optional)**: events, dependency/preorder, concurrency/independence, conflict and residual maps under rewriting. A finite graph of derivation steps is not automatically a causal event structure; a proof quotient may erase historical occurrences. This extension is used only when both sides have compatible observations.

A source class must be declared independently from the target. Each field can have an explicit 'not supplied' status; do not invent missing structure to make a translation succeed.

## 2. Target, interface, translation and obligations

For a pair D_S, D_T, choose a **declared comparison interface** I consisting of source/target judgment sorts, context/port modalities, equality relations and trust policies. A translation consists of typed maps

- T_expr on object syntax and judgments;
- T_ctx on scoped contexts and admissible substitutions;
- T_hyp on scoped hypothetical proof holes;
- T_env on justified assumptions and signatures;
- T_der on derivations/certificates;
- optional T_event on identified events and residual structures.

**Well formedness:** each map preserves sorts, scope and the chosen context boundary. A non-native translation (such as CPS) may translate one source judgment into a *specified target judgment context*, not just the same formula.

**Compositionality:** for every defined source composition `d ∘ e`, require `T_der(d ∘ e) ≈_T T_der(d) ∘_I T_der(e)`; analogous laws for identities, variable substitution and derivation-hole grafting. If target composition requires a derived operation, construct and type it rather than declaring arbitrary decoding to be composition.

**Preservation of derivability (P):** if `Der_S(E,Γ;J)` is inhabited by a valid proof, the translated target boundary is inhabited by a valid proof.

**Reflection of derivability (R):** if the translated target boundary is inhabited by *any valid target proof* under the exact translated environment, the source boundary was derivable. Restricting the target to a source-image predicate counts as an additional condition and must be reported.

**Equality preservation (EP):** for common-boundary source derivations `d≈_S e`, their images satisfy `T_der(d)≈_T T_der(e)`.

**Equality reflection / faithfulness (ER):** equality of two translated proofs implies the source proofs were equal. EP+ER induces an injective map on proof classes.

**Fullness (F):** every target proof class at the translated boundary lies in the image. This is a distinct, stronger requirement. No default fullness assumption.

**Resource preservation (U):** the declared source usage discipline is witnessed or reflected under explicit boundary/mode maps; it is **not** inferred from theorem preservation alone.

**Trust (TR):** every assumption and new inference or equation has an explicit dependency map; a soundness theorem about an extension is separate from syntactic adequacy of its presentation.

**Causal fidelity (CF, optional):** declared events, dependencies, conflicts and independence match under specified event maps, either on raw histories or an Eq-compatible quotient. Different choices cannot be compared as though identical.

**Higher coherence (HC, optional):** transformations between proofs and transformations between those transformations are represented as typed cells rather than collapsed into Eq; a 1-categorical quotient need not preserve these cells.

A report must give a truth value/status (established under stated hypotheses / verified instance / counterexample / unknown / not applicable) for each obligation. A translation that satisfies P alone is not 'universal'.

## 3. Two established lenses and their limitations

### Lens A: binding-aware algebraic signatures, modules and relative monads

Presentable signatures and initial semantics (Ahrens–Hirschowitz–Lafont–Maggesi, LMCS 2021, paper https://arxiv.org/abs/1805.03740) provide generative syntax with substitution and compositional signature construction. Their existence statement is for specified presentable signatures; **not every general signature automatically has initial semantics**. Earlier and related monad/module approaches cover binding and equations, including lambda abstraction/application and beta/eta for suitable effective 2-signatures (https://arxiv.org/abs/1903.00922). Theorems are not uniform logical soundness or cross-foundation proof-identity fidelity results.

This lens naturally models J, Sub, raw Der syntax, Comp via substitution, and a *declared* Eq. It must be enriched for linear/ordered contexts, global cyclic validity, resource observations and higher cell identity. An algebraic signature describing a rule is not evidence the rule is mathematically justified.

### Lens B: proof categories, contextual/fibrational models and logical frameworks

Proof categories make derivations into morphisms and composition explicit; chosen equations quotient arrows. Cartesian closed structure interprets a constructive implication/product fragment, while resource-sensitive systems require different monoidal or multicategorical structure. Uemura's framework (https://arxiv.org/abs/1904.04097, Theorem 6.10) has a **bi-initial model for a type theory under the paper's definition**, making dependent context/family semantics precise, without proving that arbitrary proof logics embed fully faithfully into one theory.

Edinburgh LF (Harper–Honsell–Plotkin 1993, Theorem 4.1 for the specified first-order encoding, https://era.ed.ac.uk/items/d9cebf2b-52bd-4532-b848-7d0402f32cf5) is an established judgments-as-types representation with canonical-forms adequacy and substitution. It puts object-system inference constants in the signature; those aren't thereby derived in an unchanged core. CLF gives a distinct resource/concurrency-sensitive view for labeled Petri-net traces (Cervesato et al., CMU-CS-02-102, Theorem 5.23; https://www.cs.cmu.edu/~fp/papers/CMU-CS-02-102.pdf), not arbitrary proof causal equivalence.

This lens naturally captures composition and context structure with typed judgments and possibly richer resource modes; its freeness/universal-property claims depend on selected doctrine/equality. A functor can be sound without being faithful or full; ordinary 1-categories collapse higher proof transformations unless enriched.

**Decision:** do not force Lens A and B into one target type. Translate between their **specified interface fragments** and require an explicit adequacy/faithfulness theorem. Initiality, freeness, and adequacy are different claims.

## 4. Worked controls — expected results and false moves

| Control | Declared source structure / equality | Positive representation or invariant | False inference / limitation |
|---|---|---|---|
| NJ with implication/conjunction | Typed hypotheses, abstraction/application, products; choose beta-eta quotient | Simply-typed lambda terms and CCC correspondence on chosen fragment; substitution/cut works | Merely encoding raw proof trees in LF does not automatically reflect beta-eta |
| Classical reasoning | Select LK with a declared equality or call-by-name lambda-mu with an explicitly chosen equational theory | Distinct control/continuation structures can model chosen fragment | Cartesian classical collapse is conditional on extra naturality/initiality assumptions, not general impossibility |
| MLL without units | Linear context split, distinct formula occurrences, sequent rule permutations | Hughes–van Glabbeek Theorem 1: cut-free MALL proof-net equality iff rule commutations, with/without mix (https://arxiv.org/abs/1609.04693) | Raw LF proof terms can distinguish two commuted rules: P holds while EP fails for the net quotient |
| Dependent lambda/type theory | Context (x:A, y:B(x)), typed substitution affects B, Pi abstraction/application | Uemura contextual models; dependent judgments encode scopes. E.g. a substitution for x changes type B(x) | Ordinary untyped graph morphism or simple clone loses dependent typing unless indexed/enriched |
| Equational rewriting | Steps, typed redex positions, closure under context, overlaps and critical pairs | Local rewrite/confluence diagrams can be presented with higher cells | a→b and a→c with irreducible b,c: branch conflict, not independently commuting steps |
| Cyclic proofs | Finite pre-proof graph PLUS global progressing-trace criterion | Brotherston–Simpson: soundness of cyclic fragment requires global condition (https://www.pure.ed.ac.uk/ws/portalfiles/portal/12304236/bs_journal.pdf) | Finite graph of individually valid nodes can be invalid overall; local validity alone inadequate |
| Checker and typed-path encoding | Arbitrary rule table embedded in data or a wrapper; source/proof interface may be isomorphic | A carefully constructed interpreter may preserve P/R/EP/ER/Comp for selected source class | Such preservation does *not* establish explanatory fundamentality. No approved universal intrinsic anti-interpreter invariant exists |
| Finitely presented group S_n or S_G | Unary proof symmetries, proof congruence via relators; sometimes undecidable word problem | Finite group-theoretic generators can faithfully embed many identity families | Faithfulness does not require fullness. Decidable *target equality* conflicts with all-source fidelity including undecidable group congruences |
| Independent steps A,B before C | Explicit dependency relation A<C, B<C; A and B unrelated | Both linearizations are valid when independent; trace-style Eq may identify them | If steps overlap, duplicate, erase, or conflict, independence needs a proven residual/diamond property, not chronology |

### Worked checks at the semantic level

**NJ:** Translate a proof of `A∧B` into a pair `(p,q)`, then projection produces `p`. Beta laws explain why the elimination following its matching introduction equals the original proof, relative to the specified equality. No new theorem is claimed.

**MLL:** In the counterexample from Report 003, two valid sequent derivations differ by interchanging an independent par step and tensor step; by the cited MALL net theorem they can map to the same net, but standard LF encodings with uninterpreted sequent rule constructors have different normal heads. This is a **failure of EP of that encoding for that quotient**, not all LF translations.

**Dependent substitution:** In context x:A, y:B(x), substituting a:A for x must also transport the second declaration to y:B(a). A port-only graph without reindexing fails the specified well-formedness obligation.

**Cyclic negative:** A finite cycle through local weakening/contraction steps proves no valid goal without a progressing trace. Global acceptance is a distinct Val field. A naive cyclic edge closure is insufficient.

**Typed path/checker equivalence:** For selected flattening-equality sources, Reports 009/010 describe an interface isomorphism between checker and path presentations. Therefore any criterion invariant under just their shared proof-class interface cannot distinguish their origin. Fundamentality needs an additional justified structure or become a relative, explicitly chosen notion. This is an existing research conclusion under stated restrictions, not a global impossibility theorem.

## 5. What a comparison result is, and is not

A comparison claim must identify a source class and target, source/target Eq, environment policy, and the exact subset of P/R/EP/ER/F/U/TR/CF/HC it proves, plus counterexamples to missing clauses. An **adequacy witness** is not just an interpreter. A **fidelity claim** is not an existence theorem for a finite core. A **finite algebra claim** separately counts typed generators, operation schemas, equation schemas, and higher coherence cells.

We require a **representation-level table** and an optional **justification-level table**: (i) which derivations exist and how they correspond; (ii) which rules/assumptions were justified in the core versus stipulated at the boundary. They must not be conflated.

**Open owner choices:** source classes, equality (raw versus beta/eta versus proof nets), whether target congruence must be decidable, what constitutes a permitted parameterization, whether events live on raw histories or proof-equivalence classes, and the eventual importance of fullness. CMP-01 does not silently settle them.

## 6. Next research gate

**ALG-01:** compare binding-aware signatures and free proof categories, including Guiraud polygraphs, with exact EP/ER/substitution conditions.

**INST-01:** compare mode-indexed generic logics and contextual/fibrational structures with same P/R/EP/ER/TR checklist; verify current status of Licata–Shulman–Riley Conjecture 8.5 before any novelty claim.

**OBS-01:** test whether Squier-style finite coherence obstruction and undecidable congruence genuinely constrain a given CMP-01 translation contract (not merely an unrelated stronger formulation).

**Failure/stop conditions:** if a candidate cannot express scoped context substitutions without external source checkers, or cannot preserve a declared proof equality without silently changing the target congruence, report the failed contract and the smallest necessary extra structure. Do not promote failure of one candidate to universal impossibility.

## References and evidence status

- **Inspected official/author source or abstract:** Ahrens et al., *Presentable signatures and initial semantics*, LMCS 2021 (https://arxiv.org/abs/1805.03740); Ahrens et al., *Modular specification of monads through higher-order presentations* (https://arxiv.org/abs/1903.00922); Harper–Honsell–Plotkin, *A Framework for Defining Logics*, LF repository edition (https://era.ed.ac.uk/items/d9cebf2b-52bd-4532-b848-7d0402f32cf5); Uemura, *A General Framework for the Semantics of Type Theory*, Thm 6.10 (https://arxiv.org/abs/1904.04097); Hughes–van Glabbeek, *MALL proof nets identify proofs modulo rule commutation*, Theorem 1 (https://arxiv.org/abs/1609.04693); Brotherston–Simpson, *Sequent calculi for induction and infinite descent* (https://www.pure.ed.ac.uk/ws/portalfiles/portal/12304236/bs_journal.pdf); Watkins et al., *A Concurrent Logical Framework II*, Thm 5.23 (https://www.cs.cmu.edu/~fp/papers/CMU-CS-02-102.pdf).
- **Prior repository evidence, not freshly independently theorem-checked:** Reports 001–010, especially 003 MLL fixture and 009/010 checker/path examples. Report 011 landscape and 012 strategy selection. Claims quoted through those reports require further primary verification before being promoted.
- **New comparisons and contract choices:** INFERENCE / proposed definitions; not certified general mathematics. No implementation, experiment, machine-checked new result, or universal impossibility result.
