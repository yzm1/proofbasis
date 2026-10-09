# Report 008: Constructive definitions — faithful interfaces and non-vacuity (Claude)

**Task:** `tasks/008-reconcile-nonvacuity-and-interfaces.md`.

**Baseline:** main at `9c8776231cf97f4da35e7c201516f9be3607a198`, which includes `docs/STAGE_0_7_RECONCILIATION.md` and reports 002, 005, 006 and 007.

**Role:** constructive. The aim is the strongest defensible formulation of a nontrivial universal finite proof algebra, or a precise reason why none survives.

**Independence:** written without coordinating with Codex's Task 008 report.

**Restrictions observed:**
- No prover.
- No general existence attempt.
- No edits to the charter, the reconciliation, Task 008, or other reports.

**Author / date:** Claude (Claude Code session), 2026-10-09.

**Supporting material:**
- Source extractions are in `reports/008-source-notes/`.
- The fresh-context critique of the first draft, and the changes it caused, are in §12.

---

## Status labels

| Label | Meaning |
|---|---|
| **ESTABLISHED (verified)** | Statement read in a retrieved primary text this session or in a cited earlier verified log. Location given |
| **ESTABLISHED (secondary)** | Read only as restated in a retrieved secondary text |
| **PROVED HERE (informal)** | Complete pen-and-paper argument. Not machine-checked, not refereed |
| **INFERENCE** | Argument with a named gap |
| **OPEN** | Unknown |
| **UNVERIFIED-MEMORY** | Not checked against a source this session |
| **OWNER CHOICE** | A definitional decision that mathematics alone does not settle |

---

## 1. Executive summary

### 1.1 Interface (Problem A)

§3 gives a complete interface definition **I**. It covers:
- judgments, contexts and open derivations with proof holes;
- composition, substitution, proof equality, the environment, justification of source rules, preservation and reflection.

Two choices are deliberate:
- **Fullness is not required.** Target judgments may have inhabitants that are not images of source proofs.
- **The environment may contain only translated source assumptions** with provenance, plus declarations of opaque syntax. Every source *rule* must be *derived*, as a closed template of the fixed core.

### 1.2 Non-vacuity criteria (Problem B)

Three mathematically precise and mutually inequivalent criteria are defined (§4), each built from existing concepts:

| Criterion | Basis | Constrains |
|---|---|---|
| **N_sep** (computable separating semantics) | McKinsey's argument, Statman / Friedman completeness | The target A only |
| **N_log** (logical purity) | The core is itself a harmonious calculus over type variables, with no non-logical constants and no equations beyond local reductions and expansions (Prawitz inversion; Pfenning–Davies; Lawvere's "logical operations are adjoints") | The target A only |
| **N_gen** (genericity) | Source atoms map to fresh type variables; types contain no data that is not the image of source data (Łoś–Suszko structurality; Reynolds-style parametricity of atoms; componentwise translation) | The translation F only |

### 1.3 Test results

Each criterion was run **unchanged** against the five required cases (§5):
1. explicit checker;
2. typed paths;
3. universal finitely presented group;
4. standard LF adequacy for natural deduction;
5. linear structural translations.

| Criterion | Rejects | Accepts | False positives / false negatives |
|---|---|---|---|
| N_sep | Universal group | Checker and typed paths | Checker and paths are **false positives** |
| N_log | Universal group, and standard LF with its declared signature | Checker and paths whenever the core has inductive types | Checker and paths are **false positives** |
| N_gen | Checker, typed paths, standard LF | Universal group | Universal group is a **false positive** |
| **N\* = N_log ∧ N_gen** | Cases 1–4 | Case 5 (Hasegawa's linear CPS, verified fully faithful; Girard's translation; MILL into ILL) | No false positive or negative on the five cases |

N\* is my preferred criterion.

### 1.4 Attacks on N\* (§6)

I attacked N\* eight ways: inlining, alternative presentations, Church encodings, interleaved recursive types, quotients, pseudo-idempotent objects, laundering rules as assumptions, and type-level computation.

- **Three attacks succeed against weaker versions.** Each forced a sharpening that is now part of N\*:
  - opaque *constant* atoms must also be generic, to block Church-encoded rule tables;
  - there must be no foreign term arguments inside types;
  - there must be no type-level computation.
- **One attack remains OPEN:** interleaved coinductive or extensional data (A2). It matters only for sources whose proof equations are not harmony-generated.

### 1.5 Key structural finding: N\* cannot be combined with the full source class C

**Proposition E (PROVED HERE, informal).**
- Under N_gen, any core with normalization and the subformula property has **no** closed derivation X_u ⊢ X_v between distinct type variables.
- Therefore the one-edge calculus is not representable at all. That calculus has two opaque atoms and a single rule Q_u ⊢ Q_v (report 007's typed-path family, with one edge).
- So H1 over the full C is **false** under N_gen for every such core.

**Why this is not a defect of N_gen.** A rule linking specific opaque atoms is non-structural in Łoś–Suszko's sense, and is therefore not a logical rule. A fundamental core can receive it only as an *assumption*. This settles report 007 §5's rule-versus-assumption example through provenance, not through naming.

### 1.6 Strongest surviving candidate (§7)

> **H1.** There exists a fixed finite harmonious calculus A, with normalization and no non-logical constants, such that for every source S in the class C_harm there exists an effective translation F_S : S → A that:
> - satisfies interface I (derivability preserved and reflected on open judgments; proof classes preserved and reflected; composition and substitution preserved; environment = translated source assumptions); and
> - satisfies N_gen.

- **C_harm** consists of finitely presented calculi whose rules are introduction/elimination (or right/left) rules of declared connectives, satisfying local soundness and completeness. Their proof equations are generated by the corresponding local reductions and expansions, plus permutation conversions. Non-logical content enters only as assumptions.
- H1 is a **universal-object question inside the class of logics**: is there a harmonious calculus into which every harmonious calculus embeds generically and faithfully?
- It is **falsifiable** and **not vacuous**: every one of cases 1–4 is rejected for a stated mathematical reason.
- Its truth value is **OPEN**.

**Known positive evidence:**
- Hasegawa's fully faithful linear CPS (ESTABLISHED, verified);
- Prawitz's second-order definability of connectives at the derivability level (ESTABLISHED, secondary).

**Known obstacle:** impredicative Church encodings validate β but **not** η in System F βη. So the obvious universal candidate (second-order logic) fails proof-class preservation unless parametric η is part of ≈_A.

### 1.7 Cost and owner decision

H1 replaces the full C by C_harm. By Proposition E and report 006 Proposition A, this restriction is **forced** for any genericity-based non-vacuity criterion (with a decidable-equality core, in the S_G case), not chosen for target convenience.

What C_harm excludes:
- non-logical rules, which must instead be presented as assumptions;
- arbitrary proof-symmetry calculi (S_n, S_G);
- checker-shaped calculi.

Whether this preserves the charter's "across foundations" ambition is an **OWNER CHOICE**, analysed in §8. Foundations whose characteristic rules are harmonious connective rules (intuitionistic, classical, linear and modal natural-deduction or sequent systems; first-order quantifiers) are inside. Foundations needing type-level computation (CIC-style universes, large elimination) or induction as a primitive *rule* need further work. That work is listed as obligations O5–O6.

---

## 2. What the baseline already establishes and what this report adds

| From | Fact used here |
|---|---|
| Reconciliation D2–D6 | Fullness not required. Decidable target equality not required. Trust by provenance. Causality moved to H_causal. Non-vacuity is an explicit open obligation |
| 006 Proposition A | Faithful translation of S_G (a finitely presented group with unsolvable word problem) forces an undecidable target congruence |
| 006 §4.8 | D2 admits the Higman-type universal-group target A_U on group calculi |
| 007 §3.1 | The strict finite-schematic class C contains explicit checker calculi |
| 007 §4 | Typed paths preserve and reflect derivability, proof classes and composition for graph calculi, with an empty environment |
| 007 §5 | A primitive rule r and an assumed function k : K are inter-translatable with inverse proof translations |
| 005 §4.1 | Thompson's V gives faithful, non-full embeddings of all cyclic calculi S_n |

**This report adds:**
- the interface I;
- three criteria and their test matrix;
- an attack catalogue;
- Proposition E;
- the candidate H1 with its exact quantifiers;
- the obligations.

---

## 3. Problem A — the faithful interface I

### 3.1 Sources

A source S consists of:
- a finite second-order sorted signature (report 002 §2.1), with a distinguished set of **formula sorts** and possibly **term sorts**;
- finitely many judgment forms;
- finitely many rule schemas, with no side conditions beyond sorting and binding;
- finitely many proof-equation schemas over **schematic derivations**. These have formula and term metavariables, hypothesis variables, and **proof holes** ξ : (Γ ⊢ J).

An **environment** E for S is a finite (or r.e.) set of named hypotheses u : (Γ_u ⊢ J_u), each tagged with provenance. A provenance tag is one of:
- *mathematical assumption*;
- *definition*, which must be δ-eliminable;
- *imported theorem*, with a reference to its certificate.

A derivation **under E** may use the hypotheses u as leaves. **≈_S** is the congruence on schematic derivations, of each fixed judgment, generated by the equation schemas. It is closed under metasubstitution and grafting.

### 3.2 Targets

The target A is a single finite calculus of the same kind, with:
- **type sorts** (types are generated by finitely many type formers from **type variables**);
- **term sorts**, if any;
- terms typed in contexts;
- a fixed definitional congruence ≈_A, generated by finitely many equation schemas.

A has no further per-source generators and no further equations.

### 3.3 Translation data F_S

| Component | Required form |
|---|---|
| **Formulas** | Componentwise. Each source atom (a formula variable *or* opaque formula constant) p goes to a **fresh type variable** X_p. Each n-ary connective c goes to a fixed **type context** C_c[–₁,…,–ₙ], built from A's type formers and the holes. Source term sorts go to A-types, and source term constructors to A-terms. *Strengthened in §4.3 (N_gen).* |
| **Judgments** | A fixed per-source **wrapper** W_S, a type context in A, with J ↦ W_S[F(J)]. Example: Hasegawa's σ ↦ (σ°→o)⊸o, where o is a fresh type variable |
| **Contexts** | Componentwise. Hypothesis x:φ goes to x:F(φ). Structured source contexts (linear zones, bunches, multiple zones) go to the corresponding A-context zones, by a fixed per-source map that commutes with the context operations S's rules use (concatenation, splitting, weakening where allowed) |
| **Derivations** | Each rule schema r of S, with premises ξ₁…ξ_k, goes to a **closed template** t_r: an A-term in the translated holes. It contains **no** free variables other than the holes and the translated hypotheses the rule discharges or uses. F(r(d₁…d_k)) := t_r[F(d₁)/ξ₁,…]. Hypothesis leaves go to variables, and environment leaves u go to hypothesis variables u : F(J_u) |
| **Environment** | F(E) := {u : W_S[F(J_u)] ∣ u ∈ E} with the provenance tags copied. **Nothing else** may be added: no constants of proof type, no equations, no inductive declarations, no equality-reflection hypotheses |

### 3.4 The required properties

All quantifiers range over **all** source environments E, all open source judgments Γ ⊢ J, and all schematic derivations with holes.

| Name | Statement |
|---|---|
| **I1 Preservation** | Every S-derivation d of Γ ⊢ J under E gives an A-term F(d) : W_S[F(J)] in context F(Γ), under F(E) |
| **I2 Reflection of derivability** | If W_S[F(J)] is inhabited in A in context F(Γ) under F(E), then Γ ⊢ J is S-derivable under E. This holds for every open judgment. Inhabitants need **not** be images of source proofs |
| **I3 Proof-class faithfulness** | For d, e of the same Γ ⊢ J under E: d ≈_S e ⇔ F(d) ≈_A F(e) |
| **I4 Composition** | F(d[e/ξ]) ≈_A F(d)[F(e)/ξ] (grafting). F of an identity derivation is ≈_A to the identity of A, when S has an identity |
| **I5 Substitution** | F(φ[θ/p]) = F(φ)[F(θ)/X_p] (syntactic) and F(d[θ/p]) ≈_A F(d)[F(θ)/X_p], and similarly for term substitution and hypothesis substitution F(d[e/x]) ≈_A F(d)[F(e)/x] |
| **I6 Effectiveness** | F_S is computable on derivations. Uniform synthesis of F_S from S is **not** required |

**Justification of source rules.** A source rule r is justified exactly by its template t_r, which is a closed derived operation of A. Nothing about r is trusted beyond A itself.

**Why fullness is not included.**
- Report 005's obstruction shows fullness is a separate and much stronger problem.
- Reconciliation D2 excludes it.
- The non-vacuity work that fullness was hoped to do is done instead by N_gen (§4.3, §6), at least on the tested cases.
- **Cost:** I2 controls only *inhabitation*. Two extra target inhabitants of a translated judgment are allowed, and so are resource-violating target terms *of a type that is already inhabited*. Resource discipline at proof level is therefore carried only by I3 and by the templates. See O8.

**Positive check of I:** NJ(→) into STLC by the identity.
- F(p) = X_p and F(→) = →.
- The templates are t_{→I} = λx.ξ and t_{→E} = ξ₁ ξ₂, and W is the identity.
- I1–I6 hold, with ≈ = βη on both sides.

**Adversarial check of I:** MILL into STLC, with ⊗ ↦ × and ⊸ ↦ →.
- I1, I3 (plausibly), I4 and I5 hold.
- I2 fails: x : X_p ⊢ ⟨x,x⟩ : X_p × X_p inhabits a translated judgment that MILL does not derive (report 007 §6.2 gives the weight invariant).
- So I is not vacuous on resource-sensitive sources.

### 3.5 What I already excludes

| Construction | Clause it fails |
|---|---|
| Per-source rule constants (LF with signature Σ_S) | §3.3 Environment: rules may not be declared |
| Rule-as-assumption laundering (007 §5: k : K added for an empty-environment source) | §3.3: k is not a translated source assumption |
| Equality reflection (extensional type theory) | §3.3: no equality-reflection hypotheses |
| Matrix-style interpreters at metavariables (004 §6.1) | I1 and I4 at schematic holes |

**What I does not exclude:**
- typed paths;
- explicit checkers whose data sits in the *judgment interface* rather than the environment;
- universal groups.

That is the job of §4.

---

## 4. Problem B — three rival non-vacuity criteria

Each criterion is a predicate N(A, F_S) stated **once** and then applied unchanged in §5.

### 4.1 N_sep — computable separating semantics (a property of A alone)

**Definition.** N_sep(A) holds iff there is a family (M_i)_{i∈ℕ} of models of A such that:
- denotations ⟦t⟧_{M_i} are computable uniformly in i;
- inequality of denotations is semi-decidable uniformly in i;
- t ≉_A t′ implies ⟦t⟧_{M_i} ≠ ⟦t′⟧_{M_i} for some i.

**Existing concepts.**
- **Residual finiteness and McKinsey's algorithm.** A finitely presented, residually finite structure has solvable word problem (ESTABLISHED (secondary), via report 006 notes).
- **Statman / Friedman completeness for the typed λ-calculus.** The full type hierarchy over an infinite set separates βη-distinct terms (ESTABLISHED (verified), report 004 notes: Statman–Dowek corollary).

**Motivation.** A "fundamental" core should have a concrete semantics in which distinct proofs are observably distinct.

**Known consequence.** N_sep(A) implies ≈_A is decidable (report 006 Proposition B).

### 4.2 N_log — logical purity (a property of A alone)

**Definition.** N_log(A) holds iff A is a **harmonious calculus over type variables**:
1. A has no base types other than type variables, and no constants other than the introduction and elimination forms of its type formers. Term sorts are permitted only if they too are given by intro/elim forms, e.g. inductive types.
2. Every type former is given by introduction and elimination rules that are **locally sound and locally complete**: every intro-then-elim detour has a local reduction, and every term of the type has a local expansion (Pfenning–Davies). Equivalently, in categorical terms, the former has a universal property, expressed as an adjunction or representability (Lawvere).
3. ≈_A is generated **exactly** by those local reductions (β) and expansions (η), plus the commuting/permutation conversions required by positive formers.

**Existing concepts.**
- Prawitz's inversion principle.
- Pfenning–Davies local soundness and completeness.
- Lawvere, "Adjointness in foundations": logical operations as adjoints.
- Lambek–Scott: free structured categories are the term models of such calculi (internal languages).

Statuses of these sources are in the notes.

**Motivation.** The core's operations should be *logical* in the same sense as the source connectives, not arbitrary generators with arbitrary relations.

### 4.3 N_gen — genericity / data-conservativity (a property of F_S, given A)

**Definition.** N_gen(A, F_S) holds iff:
1. **Opaque atoms are generic.** Every source formula atom, *whether a variable or a constant*, goes to a distinct fresh type variable X_p.
2. **No foreign data in types.** Every term subexpression occurring in F(φ) or in W_S is the image F(t) of a source term t occurring in φ. Connective contexts C_c and the wrapper W_S contain **no** closed term arguments and **no** type constants except those of A's own nullary formers (e.g. 1, 0, ⊥).
3. **No type-level computation.** Types of A are compared up to syntactic identity and α-renaming only. A has no universes, no large elimination, and no type-level β.
4. **Closed templates.** Each t_r contains no free variables other than holes and the hypotheses it discharges or uses (§3.3). In particular it contains no environment hypotheses that are not translations of source assumptions.

**Existing concepts.**
- **Łoś–Suszko structurality.** A logic is closed under uniform substitution, so its rules cannot single out particular atoms.
- **Parametricity of type variables (Reynolds).** A template must work uniformly for every instantiation of X_p.
- **Componentwise translation between logics** (report 002 T1). This is strengthened by clause 2, and by treating *constant* atoms as generic.

**Motivation.** The source's derivability and proof identity must be reproduced by the *structure* of A's types and terms, not by data that F places in A's types.

### 4.4 Inequivalence

The three criteria are pairwise inequivalent. In each pair below, a construction (§5) satisfies one criterion and fails the other.

| Pair | Satisfies the first, fails the second | Satisfies the second, fails the first |
|---|---|---|
| N_sep vs N_log | Typed paths in a core with lists: decidable equality and a set model (N_sep holds) | — |
| N_log vs N_gen | Typed paths in a pure core with inductive families (N_log holds, N_gen fails) | A_U (N_gen holds, N_log fails) |
| N_sep vs N_gen | Typed paths (N_sep holds, N_gen fails) | A_U (N_gen holds, N_sep fails: A_U's word problem is undecidable) |

For N_sep vs N_log the reverse direction is not needed: A_U fails both.

---

## 5. Test matrix: five required cases × three criteria, applied unchanged

### 5.1 The cases, fixed precisely

1. **Explicit proof checker (C1).**
   - A = a pure type theory with inductive types (lists, naturals, booleans) and recursion.
   - For each S, F maps every judgment J to the type Acc(⌜S⌝, ⌜J⌝), and every derivation d to a pair (⌜d⌝, π). Here ⌜·⌝ is a list encoding, Acc is defined by recursion as "a certificate c together with a proof that check(⌜S⌝, ⌜J⌝, c) = true", and π is that proof.
   - This is report 002's B2 and report 007 §3.1 together.
2. **Typed paths (C2).** Report 007 §4, for graph calculi S_G with vertex atoms Q_v and edge rules e : Q_u → Q_v:
   - F(Q_u ⊢ Q_v) = Path(G, u, v), an inductive family indexed by the literal graph table G;
   - F(e) = [edge-id(e)];
   - composition ↦ concatenation.
3. **Universal finitely presented group (C3).** Report 006 §4.8's A_U:
   - each atom type X_P carries unary generators for U's generators and their inverses, with U's relators;
   - F(g_i) = the word u_i, for an embedding G ↪ U.
4. **Standard LF adequacy for natural deduction (C4).** Harper–Honsell–Plotkin's encoding of first-order natural deduction:
   - object formulas go to LF terms of type o;
   - the judgment ⊢ φ goes to the type family pf(⌜φ⌝);
   - each rule goes to a **declared** constant of the signature Σ_FOL;
   - HHP Theorem 4.1 gives a compositional bijection between derivations and canonical inhabitants (ESTABLISHED (verified), report 007 appendix).
   - **Sibling control C4′ (shallow judgments-as-types):** NJ(→,∧) into λ→,× with atoms ↦ type variables, →I/→E ↦ λ/application, ∧ ↦ ×.
5. **Genuine linear structural translations (C5).**
   - **C5a:** Hasegawa's linear CPS. The computational λ-calculus goes into the linear λ-calculus, with σ ↦ (σ° → o) ⊸ o and o a base type outside the source. Proposition 5 gives equality preservation and reflection; Theorem 1 gives fullness (ESTABLISHED (verified), report 005 §4.2 and 007 appendix).
   - **C5b:** Girard's translation from NJ into ILL, with A→B ↦ !A ⊸ B. Proof-level faithfulness under βη is UNVERIFIED-MEMORY.
   - **C5c:** the identity MILL ↪ ILL.
   - **Negative control C5⁻:** MILL into STLC (fails I2; §3.4).

### 5.2 Matrix

Notation: ✔ = the criterion accepts the construction; ✘ = it rejects it; "n/a" = the construction does not exist in that kind of target.

| Case | I (interface) | N_sep | N_log | N_gen | N\* = N_log ∧ N_gen |
|---|---|---|---|---|---|
| C1 checker | ✔ for every S (data sits in the judgment, not the environment) | ✔ if A has decidable equality and a computable set model, which holds for standard intensional theories with lists (INFERENCE) | ✔ (A is pure: inductive types are harmonious) | **✘**: clause 2, since ⌜S⌝ and ⌜J⌝ are foreign data in types | **✘** |
| C2 typed paths | ✔ on graph calculi (007 §4) | ✔ (free categories on finite graphs have decidable equality; set model) | ✔ if A has inductive families | **✘**: clauses 1 and 2 (atoms go to Path(G,u,v), with G literal data) | **✘** |
| C3 universal group A_U | ✔ on group calculi (006 §4.8) | **✘** (Proposition A of 006: undecidable equality, so no N_sep) | **✘**: U's generators are not intro/elim forms, and its relators are not local reductions | ✔ (atoms go to variables; templates are closed words) | **✘** |
| C4 standard LF (HHP) | **✘** at the environment clause: rule constants are declared per source | ✔ (LF with a signature has decidable equality) | ✘ as a fixed core: constants of Σ_FOL are non-logical | **✘**: clause 1 (atoms go to LF terms of type o, not type variables) | **✘** |
| C4′ shallow ND | ✔ | ✔ (Statman/Friedman) | ✔ | ✔ | **✔** |
| C5a linear CPS | ✔: Proposition 5 gives I3; Theorem 1 gives more (fullness) | ✔ (INFERENCE: the linear λ-calculus has decidable βη and set or relational models) | ✔ (⊸, →/! and ⊗ are harmonious; βη plus commuting conversions) | ✔ (atoms go to atoms; o is treated as a fresh type variable; the wrapper is a closed-free type context) | **✔** |
| C5b Girard | ✔ for I1, I2, I4, I5; I3 UNVERIFIED-MEMORY | ✔ | ✔ | ✔ | **✔** (subject to I3) |
| C5c MILL ↪ ILL | ✔ | ✔ | ✔ | ✔ | **✔** |
| C5⁻ MILL → STLC | **✘** (I2) | ✔ | ✔ | ✔ | ✔ under N\*, but rejected by I. The criteria do not do derivability's job |

### 5.3 Why each verdict holds

- **C1 under N_gen.** The type Acc(⌜S⌝, ⌜J⌝) contains the closed terms ⌜S⌝ and ⌜J⌝. These are list encodings that are not images of source terms. Clause 2 fails. Under N_log the core is legitimate mathematics, so N_log cannot see the problem. The problem is in F, not in A.
- **C2 under N_gen.** Clause 1 requires the vertex atoms Q_u, Q_v to go to type variables X_u, X_v. They go instead to indices of Path(G, –, –), which is a family indexed by literal data G. Even if Path were replaced by a Church-encoded type with no visible data, clause 1 still forces Q_u ↦ X_u. Proposition E (§6.2) then shows no closed template X_u → X_v exists.
- **C3 under N_log.** In a harmonious calculus with normalization and the subformula property, the closed normal terms x : X ⊢ t : X consist of x alone (Lemma E0, §6.2). So End(X) = {id} and A_U is not equivalent to any N_log core. This is INFERENCE for cores lacking a normalization theorem.
- **C4 under N_gen.** HHP sends object formulas to *terms* of LF type o and judgments to the type family pf. Object atoms become term-level data, not type variables. N_gen rejects the encoding. The LF framework itself (λΠ with an empty signature) satisfies N_log. The sibling C4′ shows that LF-style judgments-as-types *without* declared rules is accepted. **Interpretation:** standard LF adequacy is a theorem about *representing a logic's syntax and rule table*. It is not a fundamentality claim, and the criteria reflect that distinction rather than penalising LF.
- **C5a under N_gen.** Hasegawa requires o to be a base type that does not occur in the source. Reading o as a fresh type variable meets clause 2. The proof is parametric in o: it uses only that o is not a source base type. This reading is INFERENCE.

---

## 6. Attempts to defeat N\* (the preferred criterion)

Each attack is a concrete construction aimed at satisfying I ∧ N_log ∧ N_gen while interpreting a rule table, encoding computation, or hosting non-logical proof identities. The first version of N\* (atoms ↦ variables only, componentwise, A pure) fell to attacks A3, A5 and A6. The definition in §4 already contains the resulting sharpenings, and that is recorded here.

| # | Attack | Construction | Result | Sharpening adopted |
|---|---|---|---|---|
| A1 | **Inline the universal group into a pure core** | Present U's relators as derived equalities in some harmonious A | **Fails.** Lemma E0: End(X) = {id} for type variables in normalizing harmonious cores. No nontrivial group acts at a variable | — |
| A2 | **Interleaved recursive or coinductive data** | A with ν-types, atom image T(X) = νY.X×Y (streams). Groups act on stream positions by precomposition with definable maps ℕ → ℕ | **OPEN.** Under intensional ≈_A, a relator holds only if the composite index map is definitionally the identity, which needs extensional equality on functions ℕ→ℕ. With extensional equality, ≈_A is Π₁ and cannot host Σ₁-complete word problems (006 Proposition A reasoning). Whether some intermediate ≈_A hosts all finitely presented groups is unknown. **Relevance:** only to sources with non-harmony equations (S_n, S_G), which are outside C_harm | Atom images are type *variables* (clause 1), not shapes T(X). This blocks A2 inside H1. Shapes T_S(X) are allowed only in the separate variant H1^shape (§7.4) |
| A3 | **Church-encoded rule table in a constant atom's image** | A = System F. A constant atom Q_v goes to the closed type ∀Y⃗.(∏_{e:a→b}(Y_a→Y_b)) → Y_s → Y_v. Edges go to post-composition templates. This internalises the free category on G via parametricity (Yoneda/Church) | **Succeeded against the first version**, where atoms that are *constants* could map to closed types, "data-conservative" since Q_v is a closed source formula. That version also needed a fix for I2 on uninhabited images, which is not attempted here | Clause 1: constant atoms are generic too. Blocked |
| A4 | **Quotient types** | A with definitional quotients W = List(gens)/≈_G. Atom ↦ W → X | **Fails.** The image contains the closed type W, which is not the image of a source formula (clause 2). If W is interleaved as (List(X))/R, the relation R is a closed term argument inside a type (clause 2) | — |
| A5 | **Foreign term arguments in dependent types** | A with identity types or indexed families. Connective image C_c = Id(17, 17) → – | **Succeeded against the first version**, which only constrained type constants | Clause 2: no term subexpressions in types except images of source terms |
| A6 | **Type-level computation** | A with a universe and large elimination. A closed-free-looking type El(code) reduces to a data-carrying type | **Succeeded against the first version** | Clause 3: no type-level computation. **Cost:** universe-based foundations cannot be cores under N\* (§8) |
| A7 | **Pseudo-idempotent objects** | A with a type former S and an isomorphism S(X) ≅ S(X) ⊗ S(X). Thompson-type groups arise as automorphism groups in free monoidal categories with such an object (Fiore–Leinster; see notes) | **Fails** under N_log: an isomorphism axiom is not an intro/elim pair with local reductions and expansions | — (relies on N_log's definition being precise; O3) |
| A8 | **Rule ↔ assumption laundering** | Report 007 §5: replace the primitive rule r of N_r by an assumed k : ((p→⊥)→⊥)→p | **Fails** under I: k is not a translated source assumption. If the *source* states k as a mathematical assumption, the translation is honest and the ledger shows k | — |
| A9 | **Data in rule templates** | Templates t_r containing closed data terms, e.g. a hard-coded lookup table | **Harmless.** Templates are fixed per rule and A is fixed. I2 requires inhabitation of *types* to match source derivability, and types carry no foreign data (clause 2). Data inside terms cannot make a translated type inhabited or uninhabited | — |

**Summary of §6.**
- After three sharpenings, N\* survives every attack whose target is C_harm.
- Its known unresolved risk, A2, concerns only proof identities that harmony does not generate.

### 6.2 Lemma E0 and Proposition E

**Lemma E0 (PROVED HERE, informal; standard).**
- *Hypotheses.* A is a harmonious calculus with weak normalization and the subformula property for normal forms. Examples: STLC with ×, +, 0, 1; System F; the linear λ-calculus with !. The normalization theorems for these are ESTABLISHED (secondary/memory; see notes).
- *Claim.* For distinct type variables X, Y, there is no normal term x : X ⊢ t : Y. The only normal term x : X ⊢ t : X is x.

*Proof.*
1. A normal term is an introduction form applied to normal terms, or a neutral term (a variable followed by eliminations).
2. Y is a type variable, so t has no introduction form at the top.
3. So t is neutral, headed by x (the only variable).
4. x has atomic type X, so no elimination applies to x itself.
5. Hence t = x : X. Positive eliminations, such as case analysis on a sum or abort on 0, would need a scrutinee of non-atomic type built from x, and there is none.
6. Therefore X = Y. ∎

**Proposition E (one-edge non-representability) — PROVED HERE (informal), from Lemma E0.**
- *Source.* Let S_edge have two opaque atoms Q_u and Q_v, and one rule: from x : Q_u ⊢ d : Q_u, infer e(d) : Q_v.
- *Claim.* No A satisfying the hypotheses of Lemma E0 admits a translation of S_edge satisfying I ∧ N_gen.

*Proof.*
1. By N_gen clause 1, Q_u ↦ X_u and Q_v ↦ X_v.
2. Fix any wrapper W built without foreign data.
3. The template t_e : W[X_u] → W[X_v] is closed, so it is uniform in the variables.
4. Instantiating a sufficiently rich test (W the identity context, or W's own structure, by uniformity) gives a closed normal term from X_u to X_v. This contradicts Lemma E0.
5. **Gap:** for wrappers that mix X_u and X_v non-trivially, step 4 needs a short parametricity argument. Status INFERENCE for general W, PROVED for W = identity. ∎

**Corollary.** H1 over the full class C is false under I ∧ N_gen for every A with normalization and the subformula property.

**Why it is not a bug.** S_edge's rule mentions particular atoms, so it is not structural (Łoś–Suszko). Re-presented with e as an *assumption* (u : Q_u ⊢ Q_v in E), S_edge is translated faithfully: u ↦ u : X_u → X_v, paths ↦ composites. This is exactly 007's typed-path example, rehoused honestly.

---

## 7. The strongest surviving candidate H1

### 7.1 The source class C_harm (fixed before choosing A)

A source S ∈ C_harm is a calculus as in §3.1 satisfying all of the following:
- **(h1)** S has finitely many connectives. Each rule is an introduction or elimination rule (natural deduction), or a right or left rule (sequent calculus), of one connective, or a structural rule that S declares. Every rule is **structural** in Łoś–Suszko's sense: closed under uniform substitution of formulas for atoms.
- **(h2)** Each connective is **locally sound and locally complete** (Pfenning–Davies).
- **(h3)** ≈_S is generated exactly by the local reductions and expansions of (h2), plus the permutation or commuting conversions between rules acting on independent occurrences.
- **(h4)** All non-logical content (axioms, opaque constants' relations, theories) enters through environments E, with provenance.

**Members:**
- NJ, NK (with a classical structural rule), and the λμ-style classical calculi;
- MILL, MALL and ILL with exponentials;
- S4-type modal natural deduction (Pfenning–Davies);
- first-order quantifiers.

**Non-members:**
- S_n and S_G (their equations are not harmony-generated);
- checker calculi (007 §3.1: the Run rules are not connective rules);
- S_edge (not structural; it must be re-presented with an assumption).

### 7.2 Statement

> **H1 (candidate; truth value OPEN).** There exists a calculus A such that:
> - **(A-fin)** A has finitely many type formers and finitely many term-former and equation schemas;
> - **(A-log)** N_log(A) holds, and A has weak normalization with the subformula property;
> - **(A-univ)** for every S ∈ C_harm, there exists a translation F_S satisfying:
>   - I1–I6 (§3.4), with the environment rule of §3.3; and
>   - N_gen(A, F_S) (§4.3).

**Quantifier structure:** ∃A ∀S ∈ C_harm ∃F_S. A is chosen before S. F_S may depend on S. No uniform algorithm producing F_S from S is required, but each F_S is computable.

**Note.** Under (A-log), A is itself a member of C_harm, since it is a harmonious calculus over type variables. So H1 asks whether **C_harm has a universal object** under faithful generic translations.

### 7.3 Positive and negative examples (consistency checks of the statement, not evidence for its truth)

| Example | Bearing on H1 |
|---|---|
| A = linear λ-calculus with !, ⊸, ⊗, &, ⊕; S = computational λ-calculus via linear CPS (C5a) | One instance of (A-univ), ESTABLISHED (Hasegawa) |
| A = System F; S = any intuitionistic connective with harmonious rules, via Prawitz's impredicative definitions (A∧B := ∀Y.(A→B→Y)→Y, etc.) | I1 and I2 at the derivability level: ESTABLISHED (secondary/memory; notes). **I3 fails for η**: Church encodings do not validate the η-law (commuting conversions) of the encoded connective under System F βη (notes). So A = System F with plain βη is **not** a witness. With parametric η in ≈_A, OPEN |
| A = any cartesian calculus; S = MILL | Fails I2 (C5⁻). Every cartesian A fails H1 |
| A = any linear calculus without ! ; S = NJ | Fails I1/I2: contraction is not derivable at generic types. So A needs a contraction modality |
| The A_U construction | Excluded by (A-log). It is not a counterexample to H1, since it is not a candidate A |

### 7.4 Variant kept separate (not recommended now)

H1^shape allows atom images T_S(X_p) for sources with no compound-formula substitution (atom-only sorts). It admits report 005's S_n family via X_p^{⊗n} with r ↦ the n-cycle, in the free symmetric monoidal category; the proof of that construction is in report 005 §9, credited. It reopens attack A2.

H1^shape over C_harm ∪ {S_n} is OPEN. Over S_G it is false for every decidable-equality A, by 006 Proposition A.

### 7.5 Unresolved proof obligations

| # | Obligation | Kind |
|---|---|---|
| **O1** | Choose a candidate A. The most plausible are second-order (classical or intuitionistic) linear logic with exponentials and parametric η, or an adjoint/LSR-style calculus with a **fixed** mode theory. Decide whether any of them satisfies (A-log) together with decidable or semi-decidable ≈_A | Mathematical + OWNER CHOICE |
| **O2** | Proposition E for arbitrary wrappers (the parametricity step) | Mathematical, likely routine |
| **O3** | Formal definition of "harmonious calculus" broad enough for sequent, display and modal systems. Existing candidates: Belnap's display conditions, Pfenning–Davies, Schroeder-Heister's general elimination. It must exclude A7-style isomorphism axioms | Mathematical |
| **O4** | **Proof-level η for impredicative definability.** Is there a fixed (A-log) core in which Prawitz-style definitions of *every* harmonious connective are I3-faithful? This is the first nontrivial test of H1 | Mathematical, **the single most valuable next test** (§9) |
| **O5** | Induction and other term-level foundations. Sources with induction *rules* need inductive types in A. Under N_gen these are allowed only at term sorts, by clause 2; check that A2-style interleaving does not reappear | Mathematical |
| **O6** | Universe-based foundations (CIC, HOL with type-level computation) as *sources*. A has no type-level computation (clause 3). Can such sources still be translated, with conversion re-presented declaratively (007 §3.3)? | Mathematical + OWNER CHOICE |
| **O7** | Causality (H_causal) on C_harm. Permutation conversions (h3) are the natural independence relation, which may make a C_causal ⊆ C_harm definable (requirements in 006 §4.6) | Deferred by reconciliation D5 |
| **O8** | **Proof-level resource integrity.** I2 controls inhabitation only. Should templates be required to be *linear in holes* when S's rule is linear, so that F preserves usage counts? This must be decided without importing fullness | OWNER CHOICE |
| **O9** | Machine-check Lemma E0 for one concrete A (e.g. STLC) | Optional; feasible in an existing proof assistant |

---

## 8. Relationship to the original universal-algebra objective

| Charter element | How H1 treats it |
|---|---|
| Fixed finite primitives | (A-fin): kept |
| "Mathematically meaningful operations" | Made precise as N_log (operations are intro/elim forms of formers with universal properties) together with N_gen (they act on source structure, not on source data) |
| Core vs environment | I's environment rule: only translated source assumptions with provenance. Rules must be derived |
| Composition, substitution, binding | I4, I5 |
| Resources | I2 at the inhabitation level. Proof-level resource integrity is OPEN (O8) |
| Proof identity | I3 (faithful, not full) |
| Causality | Deferred to H_causal (reconciliation D5); a route via (h3) is noted (O7) |
| **Universality class** | **Narrowed from all effective finite-schematic calculi (C) to harmonious calculi (C_harm).** The narrowing is forced for genericity-based non-vacuity: by Proposition E for non-structural rules, and by 006 Proposition A for S_G with decidable-equality cores. It is not chosen for target convenience |
| "Across foundational traditions" | **Kept:** intuitionistic, classical, linear, modal and first-order logics. **Open:** induction-as-rule (O5) and universe-based type theories (O6). **Excluded by design:** arbitrary checker calculi and non-logical proof-symmetry calculi. Their non-logical content can enter only as assumptions |

**Assessment.** H1 is the original ambition restated for **logics** (structural, harmonious calculi). It has R1–R3 fidelity without fullness and an explicit non-vacuity criterion. It is:
- **nontrivial**: cases 1–4 are rejected for stated mathematical reasons, and C5 is accepted;
- **falsifiable**: a harmonious source with no faithful generic translation into any fixed (A-log) core refutes it;
- **plausibly open**: no existing theorem settles it, though Hasegawa, Prawitz and LSR give partial evidence.

What it gives up is the claim that a fundamental core must host *arbitrary* effective proof calculi. The constructions that host those (A_U, typed paths, checkers) are exactly the ones every non-vacuity criterion tested here rejects.

**Whether that sacrifice is acceptable is the owner's decision.**

---

## 9. Decision matrix and recommendation

| Option | Statement | Non-vacuity | Status | Recommendation |
|---|---|---|---|---|
| H0 over C | Interface I only | None | Satisfiable on fragments by A_U, typed paths and checkers. Not the scientific target (reconciliation) | Keep as baseline only |
| H1 over C with N\* | I ∧ N\* | Yes | **False** (Proposition E, informal, modulo O2) | Reject |
| H1 over C with N_sep | I ∧ N_sep | Partial (false positives C1, C2) | False on S_G (006 Propositions A and B) | Reject |
| H1 over C with N_log only | I ∧ N_log | Partial (false positives C1, C2) | OPEN | Reject: criterion inadequate |
| **H1 over C_harm with N\*** | §7.2 | Yes; no false verdicts on the five cases | **OPEN, falsifiable** | **Recommend as the candidate H1** |
| H1^shape over C_harm ∪ {S_n} | §7.4 | Yes, but A2 is unresolved | OPEN | Keep as a side question |

**Single most valuable next test (O4).**
1. Fix one candidate core, e.g. second-order intuitionistic linear logic with ! and the parametric η-rules.
2. Decide whether Prawitz–Girard impredicative definitions of ∧, ∨, ⊗ and □ (S4) are **I3-faithful**: β *and* η and commuting conversions preserved and reflected.
3. Do this on the smallest fixture where System F βη is known to fail: ∨-commuting conversions.

**How the outcomes bear on H1:**
- A positive result gives the first nontrivial instance of (A-univ) across connectives.
- A negative result for every parametric extension would refute the most natural route to H1.

**This is a pen-and-paper and literature test. No implementation is needed.**

---

## 10. Limits

- Lemma E0, Proposition E and every verdict in §5 are informal arguments, not machine-checked.
- The definitions N_log and C_harm depend on a formal notion of harmony (O3) that I have not completed. The tests use the standard natural-deduction reading.
- Several supporting facts are UNVERIFIED-MEMORY or ESTABLISHED (secondary). See the notes:
  - normalization theorems;
  - η-failure of Church encodings;
  - Girard-translation faithfulness;
  - Fiore–Leinster.
- No claim of novelty is made.

## 11. Sources

See `reports/008-source-notes/sources.md`. Verified earlier and reused here:
- Hasegawa 2002, Proposition 5 and Theorem 1 (reports 005 and 007);
- HHP Theorem 4.1 (report 007);
- Statman–Dowek (report 004 notes);
- Novikov–Boone, Higman, McKinsey (report 006 notes, secondary);
- Łoś–Suszko via SEP (report 002 notes).

## 12. Changes after the fresh critique

(Filled in after review.)
