# Report 008: Constructive definitions — faithful interfaces and non-vacuity (Claude)

**Task:** `tasks/008-reconcile-nonvacuity-and-interfaces.md`.

**Baseline:** main at `9c8776231cf97f4da35e7c201516f9be3607a198`, including `docs/STAGE_0_7_RECONCILIATION.md` and reports 002, 005, 006 and 007.

**Role:** constructive. The aim is the strongest defensible formulation of a nontrivial universal finite proof algebra, or a precise account of why none survives.

**Independence:** written without coordinating with Codex's Task 008 report.

**Constraints observed:**
- no prover;
- no general existence attempt;
- no edits to the charter, the reconciliation, Task 008, or other reports.

**Author and date:** Claude (Claude Code session), 2026-10-09.

**Supporting material:**
- source extractions: `reports/008-source-notes/sources.md`;
- critique of the first draft: `reports/008-source-notes/fresh-critique.md`.

**Revision note.**
- A fresh-context referee **broke the first draft** with two fatal and ten major findings. The first draft's preferred criterion was defeated by a *reader wrapper*, which smuggles a rule table into the per-source judgment wrapper, and by a *Cayley state wrapper*, which smuggles a group's multiplication table the same way.
- Its "forced restriction of C" claim was invalid.
- §12 lists every withdrawal. What follows is the repaired version.
- Its conclusions are weaker than the first draft's, and they are stated with that in mind.

---

## Status labels

| Label | Meaning |
|---|---|
| **ESTABLISHED (verified)** | Statement read this session in a retrieved primary text, or in an earlier verified log. Location given |
| **ESTABLISHED (secondary)** | Read only as restated in a retrieved secondary text |
| **PROVED HERE (informal)** | Complete pen-and-paper argument. Not machine-checked, not refereed |
| **INFERENCE** | Argument with a named gap |
| **OPEN** | Unknown |
| **UNVERIFIED-MEMORY** | Not checked against a source this session |
| **OWNER CHOICE** | Definitional decision that mathematics does not settle |

---

## 1. Executive summary

### 1.1 What survived

1. **A precise faithful interface I (§3).**
   - It covers judgments, contexts, open derivations with proof holes, Kleisli-style composition and substitution, proof equality, the environment, justification of rules, preservation and reflection.
   - Fullness is not required.
   - **The key repair is a principle:** *every per-source datum is either the translation of source content, or it is absent.*
     - Judgment wrappers and atom interfaces are **fixed by A**: a finite menu that is part of A's data and independent of S.
     - The environment contains only translated source assumptions, with provenance.
     - Per-source freedom is confined to componentwise connective images and closed rule templates.
   - The first draft's per-source wrappers were the hole the referee's attacks used.
2. **Three inequivalent criteria (§4).** Each was run unchanged on the five required cases (§5).
   - **N_sep** (computable separating semantics). It is *equivalent to decidability of ≈_A*. That conflicts with reconciliation decision D3, which explicitly does not require decidable target proof equality. N_sep is kept as a rival only.
   - **N_log** (purity: A's generators and equations are exactly the intro/elim forms and the local reductions and expansions of its type formers).
   - **N_gen** (genericity: schematic propositional variables go to fresh type variables, and fixed interfaces are used throughout).
3. **The preferred criterion N\*\* = N_log ∧ N_gen (with fixed interfaces) gives these verdicts on the five cases:**

| Case | Verdict | Status |
|---|---|---|
| C1 checker interpretation of a logic | Rejected | — |
| C2 typed-path interpretation of a logic's rule table | Rejected | — |
| C3 universal finitely presented group | Rejected | Presentation-level rejection; iso-invariant rejection OPEN |
| C4 standard LF adequacy | Rejected | Including the reader-wrapper re-presentation |
| C5 linear structural translations | Accepted | Hasegawa's CPS needs a Kleisli reading |

   - Typed paths for **graph calculi with constant atoms** are *accepted*, as a relative interpretation of a non-logical theory. §5.3 argues that this is intended, not a false positive.
   - The Gödel–Gentzen negative translation is accepted through a fixed atom interface (¬¬−).
4. **Proposition E (repaired; PROVED HERE, informal).**
   - It holds under fixed interfaces in any core with a closed inhabited type and type-variable substitution.
   - Its content: a rule between distinct *schematic propositional variables* that is not derivable cannot be derived generically. The proof is three lines (§6.2).
   - It is a *consequence* of N_gen. It is not a justification for restricting C.

### 1.2 What did not survive

| First-draft claim | Status now |
|---|---|
| "N\* has no false positives" | Withdrawn: the reader wrapper and Cayley wrapper defeated it |
| "C_harm is forced" | Withdrawn: it is an OWNER CHOICE |
| Łoś–Suszko non-structurality of S_edge | Withdrawn: Łoś–Suszko structurality concerns substitution for *variables*, and S_edge's atoms were constants |
| Lemma E0 ⇒ A_U not equivalent to any pure core | Withdrawn as an iso-invariant claim |
| First-order sources covered | Withdrawn: OPEN (O5) |

### 1.3 Candidate H1 (§7)

> ∃ A satisfying N_log, with a fixed finite interface menu, ∀ S ∈ C_harm^prop, ∃ effective F_S satisfying I and N_gen.

- **C_harm^prop** is the class of propositional calculi whose rules are intro/elim rules of declared connectives, with local soundness and local completeness, together with structural rules drawn from a **fixed finite menu** (exchange, weakening, contraction, and the standard modal context disciplines). Proof equality is generated by local reductions and expansions plus permutation conversions.
- H1 is **not vacuous**: C1–C4 are rejected for stated reasons.
- H1 is **falsifiable**.
- Its truth value is **OPEN**.

**Evidence:**
- Hasegawa's fully faithful linear CPS (ESTABLISHED, verified).
- Prawitz's second-order definitions, which preserve β but **not** η or permutative equivalence under βη (Tranchini–Pistone–Petrolo, ESTABLISHED, verified).
- The same authors propose naturality equations that restore preservation.
- Unconstrained parametricity is *inconsistent* for λμ (Hasegawa 2006, ESTABLISHED, verified). That is a warning for classical members.

### 1.4 Honest bottom line

N\*\* is the strongest criterion that survived. It survives because interfaces are fixed in A, so a source cannot relocate its rule table into wrappers or contexts. Attack A10 (state threaded through *connective images*) remains **OPEN** for C_harm^prop.

So this report delivers a **candidate H1 that is well-formed, non-vacuous on the tested cases, and falsifiable**. It does **not** deliver a proof that N\*\* excludes every interpreter. Restricting to C_harm^prop is an **owner choice**, motivated independently ("logics, not theories"). It is not forced.

---

## 2. Inputs used from the baseline

| From | Fact |
|---|---|
| Reconciliation | D2: no fullness. D3: no decidable target equality. D4: trust by provenance. D5: causality deferred. D6: non-vacuity open |
| 006 Proposition A | Faithful translation of S_G forces an undecidable ≈_A. S_G is a group calculus whose finitely presented group has unsolvable word problem |
| 006 §4.8 | D2 admits the Higman-type target A_U on group calculi |
| 007 §3.1, §4, §5 | Explicit checker calculi are in C. Typed paths preserve and reflect structure for graph calculi. A rule r and an assumption k are inter-translatable |
| 005 §4.1, §9 | Thompson's V and the free SMC (P ↦ X^{⊗n}) give faithful embeddings of S_n |

---

## 3. Problem A — the faithful interface I

### 3.1 Sources

A source S consists of:
- a finite sorted signature (report 002 §2.1), with **formula sorts**;
- **schematic propositional variables** (metavariables of formula sort);
- **constant atoms**, i.e. nullary formula symbols, which may occur in rules;
- finitely many judgment forms;
- finitely many rule schemas, with no side conditions beyond sorting and binding;
- finitely many proof-equation schemas over schematic derivations. These have formula metavariables, hypothesis variables, and proof holes ξ : (Γ ⊢ J);
- a declared **substitution discipline**: full (call-by-name or ordinary), or value-only (call-by-value).

**Environment.** A finite or r.e. set of named hypotheses u : (Γ_u ⊢ J_u), each with a provenance tag (mathematical assumption / δ-eliminable definition / imported theorem with certificate reference).

**Proof equality.** ≈_S is the congruence generated by the equation schemas, closed under metasubstitution and grafting.

### 3.2 Target

A is a single finite calculus with:
- type variables;
- finitely many type formers;
- terms typed in contexts;
- a fixed definitional congruence ≈_A generated by finitely many equation schemas.

A also comes with a **finite interface menu** 𝓜_A, a fixed finite set consisting of:
- **atom interfaces** α(X), which are type contexts in one variable built from A's formers and A's own fresh variables (e.g. α(X) = X, or α(X) = (X → o) → o);
- **judgment wrappers** W, which are type contexts with a unit η_W : σ ⊢ W[σ] and a Kleisli extension, making W a strong monad up to ≈_A;
- **context disciplines** (e.g. linear zone, intuitionistic zone).

𝓜_A is part of A, chosen **before** any source.

### 3.3 Translation data F_S

| Component | Required form |
|---|---|
| **Interface choice** | F_S selects one atom interface α_S, one wrapper W_S and one context discipline from 𝓜_A. Nothing else about the interface varies with S |
| **Formulas** | Componentwise. A schematic propositional variable p goes to α_S(X_p), where X_p is a fresh type variable. An n-ary connective c goes to a type context C_c[–₁…–ₙ] built from A's formers, the holes, and A's own fresh variables. **Constant atoms** may go to closed A-types (relative interpretation; see §5.3) |
| **Judgments** | Γ ⊢ φ goes to F(Γ) ⊢ W_S[F(φ)] |
| **Contexts** | Componentwise, x:φ ↦ x : F(φ), placed in the zone the discipline dictates. **No hypotheses are added** |
| **Leaves** | A hypothesis leaf x goes to η_W(x) |
| **Rules** | Each rule schema r goes to a closed template t_r: an A-term in the translated holes, using only the hypotheses r discharges. F(r(d⃗)) := t_r[F(d⃗)/ξ⃗], with holes of wrapped type W_S[−] |
| **Environment** | F(E) := {u : W_S[F(J_u)]}, with provenance copied. Nothing else may be added: no proof-type constants, no equations, no inductive declarations, no equality reflection |

### 3.4 Required properties

All quantifiers range over:
- every source environment E;
- every open judgment Γ ⊢ J;
- every schematic derivation with holes.

| Name | Statement |
|---|---|
| **I1 Preservation** | d : (Γ ⊢ J) under E gives F(d) : W_S[F(J)] in context F(Γ), under F(E) |
| **I2 Reflection** | If W_S[F(J)] is inhabited in context F(Γ) under F(E), then Γ ⊢ J is S-derivable under E. Target inhabitants need **not** be images |
| **I3 Faithfulness** | For d, e of the same judgment: d ≈_S e ⇔ F(d) ≈_A F(e) |
| **I4 Composition** | F(d[e/ξ]) ≈_A F(d) ⟨Kleisli⟩ F(e). F(identity) ≈_A η_W |
| **I5 Substitution** | Formula substitution: F(φ[θ/p]) is F(φ) with α_S(X_p) replaced by F(θ), and correspondingly for derivations. Hypothesis substitution: F(d[e/x]) ≈_A Kleisli-substitution of F(e) for x in F(d), **for those e the source's substitution discipline permits** (all e, or values only) |
| **I6 Effectiveness** | F_S is computable. Uniform synthesis of F_S from S is not required |

**Justification.** A source rule is justified exactly by its closed template, which is a derived operation of A.

**Why fullness is excluded.**
- Report 005 shows fullness is a separate and much stronger problem, and reconciliation decision D2 excludes it.
- The non-vacuity work is done by fixing interfaces (§3.2) and by N_gen, not by fullness.
- **Cost:** I2 controls only inhabitation, so proof-level resource integrity rests on I3 and on the templates (O8).

**Positive check: NJ(→) into STLC.** Identity interfaces (α = X, W = id). Templates λx.ξ and ξ₁ξ₂. I1–I6 hold with βη on both sides.

**Adversarial check: MILL into STLC.** I2 fails: x : X ⊢ ⟨x,x⟩ : X×X (report 007 §6.2 weight invariant).

**Why fixed interfaces close the first draft's hole.**
- **Reader wrapper.** W[σ] = (X_u→X_v) → σ mentions a source-atom image and depends on S's rule table. It is neither in a fixed 𝓜_A nor built from fresh variables only.
- **Cayley state wrapper.** W[σ] = D → D×σ, with D a sum of |G| copies of o, depends on |G|. A fixed menu cannot contain one wrapper per group.
- **Hidden hypotheses.** Context maps may add no hypotheses.
- **Is fixing interfaces ad hoc?** No. It is report 002's T2 ("wrapper independent of S"), and it follows from the principle that a per-source datum is either translated source content or absent. A per-source wrapper is precisely an unaudited per-source environment.

---

## 4. Problem B — three rival criteria

### 4.1 N_sep: computable separating semantics (a property of A)

**Definition.** There is a family of models (M_i) such that:
- denotations are computable uniformly in i;
- inequality of denotations is semi-decidable uniformly in i;
- the family separates all ≉_A pairs.

**Grounds.** Residual finiteness and McKinsey's argument (ESTABLISHED (secondary), report 006 notes); Statman's finite completeness for the simply typed λ-calculus (ESTABLISHED (secondary), report 004 notes; the originals were not accessed).

**Fact (PROVED HERE, informal; supplied by the critic).** If ≈_A is r.e., then N_sep(A) ⇔ ≈_A is decidable.
- (⇐) The term model, with denotation computed by a decision procedure, is uniformly computable and separating.
- (⇒) 006 Proposition B.

**So N_sep is decidability in disguise, and it conflicts with D3.** It is kept only as a rival for comparison.

### 4.2 N_log: purity (a property of A's presentation)

**Definition.**
1. A's only constants are the introduction and elimination forms of its type formers.
2. Each type former is locally sound (it has β-reductions). Where it is locally complete, its η-expansions are included.
3. ≈_A is generated exactly by these β and η laws, plus the commuting conversions of positive formers.
4. Base types are type variables. Closed types arise only from nullary or recursive formers, such as 1, 0, or ℕ as an inductive former.

**Clarifications prompted by the critique (M6).**
- Inductive formers without definitional η are *admitted*, with β only. Whether they are "harmonious" is contested, so this is an OWNER CHOICE.
- N_log is a property of a **presentation**. It rejects A_U's presentation. Whether some N_log presentation is *equivalent* to A_U is OPEN. Such a presentation would need an N_log core with undecidable ≈ that hosts U at some type (m1 of the critique).

**Grounds.**
- Pfenning–Davies local soundness and completeness (ESTABLISHED, verified).
- Prawitz's inversion principle (ESTABLISHED (secondary), via SEP).
- Lawvere: cartesian closed structure is "entirely given by adjointness", and Σ_f and Π_f are adjoints to substitution (ESTABLISHED, verified, TAC Reprints 16 pp. 3 and 12).

### 4.3 N_gen: genericity with fixed interfaces (a property of F_S)

**Definition.**
1. Every **schematic propositional variable** goes to α_S(X_p), with α_S from 𝓜_A and X_p fresh.
2. Connective images C_c contain no term subexpressions and no type variables other than holes and A's own fresh variables.
3. A has no type-level computation: no universes, no large elimination, no type-level β.
4. Templates are closed.

**Constant atoms are not constrained.** They may go to any closed A-type.

**Grounds.**
- Łoś–Suszko structurality: substitution-invariance for **variables** (ESTABLISHED, verified via SEP Jansana §2).
- Reynolds/Wadler parametricity: a template uniform in X_p acts the same at every instance (ESTABLISHED, verified; Reynolds 1983, Wadler 1989, Plotkin–Abadi Thm 1).
- Report 002's T1/T2.

**Why constants are free (M3 repair).**
- A constant atom whose behaviour is given by rules among constants is a **non-logical theory**. Representing it by closed A-types is a Tarskian relative interpretation. That is legitimate mathematics, not an interpreter of a *logic*.
- The first draft's clause forcing constants to be generic was ad hoc and depended on naming. It is withdrawn.

### 4.4 Inequivalence (witnesses on pairs (A, F_S))

| Witness | N_sep | N_log | N_gen |
|---|---|---|---|
| A_U with F(g) = words (group calculi) | ✘ (undecidable ≈) | ✘ | ✔ |
| A = intensional type theory with lists; C1 checker F | ✔ (decidable, INFERENCE) | ✔ (inductive, β only) | ✘ |
| A = STLC(→,0); Gödel–Gentzen F with α(X) = (X→0)→0 | ✔ | ✔ | ✔ |
| A = STLC(→) with a per-source reader wrapper (critique F1) | ✔ | ✔ | ✘ (interface not in 𝓜_A) |

The three columns disagree pairwise, so the criteria are inequivalent.

---

## 5. Test matrix: the five required cases, each criterion applied unchanged

### 5.1 The cases

| Case | Construction |
|---|---|
| **C1 Explicit checker interpretation** | F maps judgments of a *logic* S to Acc(⌜S⌝, ⌜J⌝) and derivations to certificates with checking proofs. This is the shape of report 002's B1 reflected checker, with report 007 §3.1 |
| **C2 Typed-path interpretation of source rule tables** | Two readings. **C2a:** a logic's rule table interpreted by paths indexed by formula codes. **C2b:** report 007 §4's graph calculi (constant vertex atoms Q_v, edge rules), with Q_u ⊢ Q_v ↦ Path(G,u,v). **C2c:** the critique's reader-wrapper variant, with W[σ] = ∏(X_a→X_b) → σ |
| **C3 Universal finitely presented group** | Report 006 §4.8's A_U on group calculi S_G. The Cayley state wrapper (critique M1) is included as a variant for finite G |
| **C4 Standard LF adequacy (HHP)** | Object formulas are LF terms of type o, judgments are pf(⌜φ⌝), and rules are declared Σ_FOL constants (ESTABLISHED, verified, report 007). Also C4r: the rules moved into a ∀-closed reader wrapper (critique M9.1) |
| **C5 Linear structural translations** | **C5a:** Hasegawa's linear CPS, σ ↦ (σ°→o)⊸o, from the computational (call-by-value) λ-calculus (ESTABLISHED, verified: Proposition 5 gives equality, Theorem 1 gives fullness). **C5b:** Girard's translation (I3 is UNVERIFIED-MEMORY). **C5c:** MILL ↪ ILL. **C5⁻:** MILL → STLC |

### 5.2 Matrix

✔ = accepted, ✘ = rejected.

| Case | I | N_sep | N_log | N_gen (fixed interfaces) | N\*\* = N_log ∧ N_gen |
|---|---|---|---|---|---|
| C1 checker for a logic | ✔ | ✔ (decidable) | ✔ (inductive, β) | ✘ (clause 1: variables ↦ codes) | **✘** |
| C2a typed paths for a logic | ✔ | ✔ | ✔ | ✘ (clause 1) | **✘** |
| C2b typed paths for a graph theory (constant atoms), in the componentwise form Q_v ↦ closed type T_v (e.g. the Church encoding of A3), not the literal judgment-level Path family | ✔ | ✔ | ✔ | ✔ (constants unconstrained) | **✔ intended (§5.3)** |
| C2c reader wrapper | ✔ | ✔ | ✔ | ✘ (W ∉ 𝓜_A; W mentions atom images) | **✘** |
| C3 A_U | ✔ | ✘ | ✘ (presentation) | ✔ | **✘** |
| C3 Cayley state wrapper | ✔ | ✔ | ✔ | ✘ (W depends on \|G\|) | **✘** |
| C4 HHP | ✘ (declared rule constants) | ✔ for each LF+Σ_S (not a fixed A) | ✘ (Σ_FOL constants are non-logical) | ✘ (object variables ↦ LF terms) | **✘** |
| C4r reader-wrapper LF | ✔ for free-identity sources | ✔ | ✔ | ✘ (W carries S's rules) | **✘** |
| C4′ shallow ND (atoms ↦ variables, rules ↦ λ/app) | ✔ | ✔ | ✔ | ✔ | **✔** |
| C5a Hasegawa CPS | ✔ under the Kleisli/value reading of I4–I5 (§3.4); checked only at the level of Hasegawa's Proposition 5 | ✔ (INFERENCE) | ✔ (⊸, → and ! with βη; INFERENCE for harmony of the presentation) | ✔: the wrapper (−→o)⊸o is fixed and o is read as A's fresh variable. **This reading of o is flagged** (critique m8) | **✔** |
| C5b Girard | ✔ for I1, I2, I4, I5; I3 UNVERIFIED-MEMORY | ✔ | ✔ | ✔ (α = id, W = id, →↦!−⊸−) | **✔ (subject to I3)** |
| C5c MILL ↪ ILL | ✔ | ✔ | ✔ | ✔ | **✔** |
| C5⁻ MILL → STLC | ✘ (I2) | ✔ | ✔ | ✔ | Rejected by I, not by N |

**Further rows (critique M9).** These are presentation probes that are not among the five required cases.

| Probe | N\*\* | Classification |
|---|---|---|
| Gödel–Gentzen / Kolmogorov, p ↦ ¬¬p, hypotheses unwrapped | ✔, if α(X) = (X→0)→0 ∈ 𝓜_A | Accepted via a fixed atom interface. I3 for βη is OPEN |
| Call-by-name CPS with wrapped hypotheses | Needs a context discipline "hypotheses wrapped by α" in 𝓜_A | Admissible if that discipline is in the menu |
| Report 004's ST_x(p) = P(x) | ✘ | The world variable is a term in a type (clause 2). **Intended exclusion:** ST is a derivability-level *semantic* translation, not a proof-level one |
| Free SMC embedding of S_n (P ↦ X^{⊗n}) | ✘, unless every X^{⊗n} is in 𝓜_A, which a finite menu cannot hold | **Intended exclusion** under N\*\*. S_n's equation is not a logical law (§7.4) |

### 5.3 Reasons, and the two "intended acceptances"

- **C1 and C2a.** Schematic propositional variables go to codes, i.e. data, not fresh type variables, so N_gen clause 1 rejects them. N_log cannot see this, because the core is legitimate and the problem lies in F.
- **C2b is accepted, and this is intended.**
  - A graph calculus with *constant* atoms has no schematic propositional variables. Its rules are a non-logical theory (a directed graph).
  - Its typed-path image is the free category on G, built inside A from G's data. That is a relative interpretation.
  - **Codex's question (007 §10) gets this answer:** ordinary free-category generation is admitted for *theories*. Interpreting a *logic's* schematic rule table is not admitted (C2a).
  - The dividing line is whether the interpreted rules are schematic in propositional variables.
  - **Consequence.** N\*\* says nothing about how a source's *non-logical* content is represented. That content is either honest assumptions (§3.3) or a relative interpretation in A. Neither is a vacuity concern for the question "is the core's *logic* fundamental?"
- **C3.** A_U's presentation has non-logical generators with relators, so N_log rejects it. The Cayley variant fails because its wrapper is per-source.
- **C4.** HHP is rejected three ways:
  - declared rule constants (I);
  - non-logical constants (N_log);
  - object variables as terms (N_gen).

  The reader-wrapper re-presentation C4r is rejected by fixed interfaces. That answers the critique's presentation-dependence objection: the rule table is rejected *wherever it is written*, because the per-source datum is neither translated source content nor absent.
- **C5.** Accepted, with flagged readings:
  - o is read as a fresh variable;
  - I4/I5 are read in Kleisli/value form for the call-by-value source.

---

## 6. Attempts to defeat N\*\*

### 6.1 Attack catalogue

| # | Attack | Outcome |
|---|---|---|
| A1 | Inline U's relators into a pure core | Fails at presentation level (N_log). Iso-invariant version OPEN (§4.2) |
| A2 | Interleaved coinductive data at atoms (α(X) = νY.X×Y) | Only if such an α is in 𝓜_A. **OPEN** whether a single fixed coinductive interface hosts non-logical proof identities. Irrelevant to C_harm^prop, whose equalities are logical |
| A3 | Church-encoded graph in closed types for constant atoms | **Accepted, as a relative interpretation (C2b)**. Reclassified: not an attack on the *logic* |
| A4 | Quotient types at atoms | Fails: needs a closed relation term in a type (clause 2), or an α outside the menu |
| A5 | Foreign term arguments in types | Fails (clause 2) |
| A6 | Type-level computation | Fails (clause 3). **Cost:** universe-based cores are excluded (O6) |
| A7 | Pseudo-idempotent object A⊗A ≅ A (Fiore–Leinster: Aut(A) ≅ Thompson's F in the free monoidal category on such an object; ESTABLISHED, verified, arXiv:math/0508617 Thm 1.1) | Fails under N_log: the isomorphism α is not an intro/elim pair with local reductions and expansions |
| A8 | Rule ↔ assumption laundering (007 §5) | Fails: hypotheses may enter only as translated source assumptions |
| A9 | Data inside templates | **Not harmless in general** (critique M1). Combined with a per-source state wrapper it hosts Cayley tables. With fixed interfaces, templates can thread only state that a fixed W provides |
| **A10** | **State threaded through *connective images*.** C_c[A,B] = D → D × (…), with D built from A's fresh variables, per source | **OPEN for C_harm^prop.** Clause 2 allows fresh variables in C_c, so a per-source D can be built from them. Whether this lets an interpreter pass I2 and I3 for a *logic* is unknown. Candidate repair, with its cost: require C_c to be **linear in its holes and free of auxiliary state**, i.e. to contain only type formers applied to holes. That excludes Girard's !A⊸B unless ! is applied to a hole (which it is), so it may be acceptable |
| A11 | Reader wrapper / Cayley wrapper (critique F1, M1) | Fails under fixed interfaces (C2c, C3 Cayley rows) |
| A12 | Reader context: adding hypotheses through the context map | Fails: §3.3 forbids added hypotheses |

### 6.2 Lemma E0 and Proposition E (repaired)

**Lemma E0 (PROVED HERE, informal; the critic verified it case by case).**
- *Setting.* A's normal forms are introduction forms, neutral terms, or positive eliminations of neutrals. A has no constants. Examples: STLC with ×, +, 0, 1; System F; the linear λ-calculus with !. The subformula property is **not** needed (critique M4).
- *Claim.* No normal term x : X ⊢ t : Y exists for distinct type variables X, Y. The only normal x : X ⊢ t : X is x.

**Proposition E (PROVED HERE, informal; the three-line proof is from the critique).**
- *Setting.* A has a closed inhabited type 1 and type-variable substitution. Every α ∈ 𝓜_A and every W ∈ 𝓜_A uses only A's own fresh variables.
- *Source.* S has distinct schematic propositional variables p, q and a rule e : from Γ ⊢ p infer Γ ⊢ q, and S does not derive ⊢ q.
- *Claim.* S has no translation satisfying I ∧ N_gen.

*Proof.*
1. The template t_e : W[α(X_p)] ⊢ W[α(X_q)] is closed, so it is uniform in X_p.
2. Substitute X_p := 1. This gives W[α(1)] ⊢ W[α(X_q)].
3. W[α(1)] is closed-inhabited: by η_W applied to an inhabitant of α(1), whenever α(1) is inhabited. This holds for every α built from the formers applied to 1 and fresh variables that is not uninhabited.
4. So W[α(X_q)] = F(⊢ q) is closed-inhabited, which contradicts I2. ∎

**Gap in step 3:** it needs α(1) to be inhabited, which holds for the identity interface and for (X→o)→o. Status: INFERENCE for arbitrary α.

**Reading.** A rule linking two *different* schematic variables, such as p ⊢ q for all p, q, is unsound for any logic with a non-trivial consequence relation, so such sources are degenerate. Proposition E is therefore mostly a sanity check that N_gen does not admit unsound generic templates. **It is not a reason to restrict C.** The first draft's use of it for that purpose is withdrawn.

---

## 7. Candidate H1

### 7.1 Source class C_harm^prop (OWNER CHOICE)

A source S is in C_harm^prop if:

- **(h0)** S is propositional: formula sorts only, with no term sorts. First-order extension is O5.
- **(h1)** Every rule is one of:
  - an intro/elim (right/left) rule of one of S's finitely many connectives;
  - an identity or cut rule;
  - a structural rule from the **fixed menu** {exchange, weakening, contraction, the Pfenning–Davies valid/true context discipline, the dual-zone (!) discipline}.

  There are no other "declared structural" rules (critique M7.1).
- **(h2)** Each connective is locally sound and locally complete (Pfenning–Davies; ESTABLISHED, verified).
- **(h3)** ≈_S is generated by the local reductions and expansions plus permutation/commuting conversions.
- **(h4)** All non-logical content enters through environments, with provenance.

**Members:**
- NJ with →, ∧, ∨, ⊥;
- MILL, MALL and ILL with !;
- S4 in Pfenning–Davies form.

**OPEN members:**
- classical calculi (λμ, NK). Their equations (μ-rules, Joyal collapse) do not fit (h3) without an explicit choice (critique M7.2–3).

**Non-members:**
- S_n and S_G (non-logical proof equations);
- checker calculi (their rules are not connective rules, and they have no admissible structural rules);
- first-order logic (pending O5).

**Motivation, independent of any target.** The project asks about *logical foundations*. A calculus whose rules all define connectives, with proof identity generated by their local reductions and expansions, is a standard proof-theoretic definition of a logic's proof system (Prawitz, Dummett, Pfenning–Davies).

**This is not forced by the criteria** (critique F2). The reconciliation's caution ("don't shrink C merely to make a target work") is respected by stating the choice and its consequences:
- **Under the full C,** N\*\* rejects every known universal construction for S_G-type sources. Whether *any* N\*\*-admissible A hosts S_G is OPEN.
- **Under C_harm^prop,** that question does not arise.

### 7.2 Statement

> **H1 (candidate; truth value OPEN).** There exist a finite calculus A and a finite interface menu 𝓜_A such that:
> - N_log(A) holds;
> - A has no type-level computation;
> - for every S ∈ C_harm^prop, there exists an effective F_S satisfying I1–I6 (§3.4) and N_gen(A, F_S) (§4.3).

**Quantifiers.** ∃(A, 𝓜_A) ∀S ∈ C_harm^prop ∃F_S. A and 𝓜_A are fixed before S. There is no uniform synthesis requirement.

### 7.3 Examples

| Example | Bearing on H1 |
|---|---|
| Hasegawa: computational λ-calculus → linear λ-calculus | A verified *instance* of I + N\*\* (C5a). **But** the source is call-by-value, and its membership in C_harm^prop is not established (critique M10). So it is evidence of feasibility, not an instance of (A-univ) for C_harm^prop |
| A = System F; S's connectives ∧, ∨, ⊥ by Prawitz's definitions | I1 and I2 hold (derivability). **I3 fails**: the Russell–Prawitz translation preserves β-equivalence but not η- or permutative equivalence, "not even ... =βη" (Tranchini–Pistone–Petrolo, arXiv:1607.06603v2 p. 7, ESTABLISHED, verified; also Girard–Lafont–Taylor *Proofs and Types* pp. 84–85, ESTABLISHED, verified). **The same paper proposes naturality equations under which identity is preserved** (ESTABLISHED, verified, abstract). That gives a concrete A candidate: System F plus naturality equations |
| Classical members via parametricity | Hasegawa (LMCS 2(3:3) 2006): "unconstrained relational parametricity on the λµ-calculus turns out to be inconsistent" (ESTABLISHED, verified). Parametric η cannot simply be assumed for classical sources |
| Any cartesian A, with S = MILL | Fails I2. Short argument (critique m5): instantiate the ⊗I template with both holes as the unit applied to a shared x, giving X_p ⊢ W[C_⊗(X_p,X_p)] |

### 7.4 What H1 deliberately leaves to separate questions

- **H1^theory.** Faithful representation of non-logical proof identities (S_n, S_G). By 006 Proposition A, this needs undecidable ≈_A for S_G. By §5.2 it is excluded under N\*\* with finite interface menus, unless 𝓜_A contains a coinductive α (A2, OPEN).
- **H_full and H_causal** (reconciliation). Under C_harm^prop, the permutation conversions (h3) are the natural independence relation, which offers a route to H_causal.

### 7.5 Unresolved proof obligations

| # | Obligation | Kind |
|---|---|---|
| O1 | Choose candidates (A, 𝓜_A). Leading options: System F or second-order ILL with Tranchini–Pistone–Petrolo naturality equations; an adjoint/LSR calculus with a **fixed** mode theory | Mathematical + OWNER CHOICE |
| O2 | Proposition E step 3 for arbitrary α | Mathematical (minor) |
| O3 | A formal definition of harmony for sequent and modal presentations, with the fixed structural menu | Mathematical |
| **O4** | **I3 for impredicative definitions under naturality equations.** Is Prawitz-style definability faithful for βη plus commuting conversions of ∧, ∨, ⊥, ⊗ and S4-□ in one fixed core? | **Most valuable next test (§9)** |
| O5 | First-order sources: predicate variables as type-family variables. Predicate substitution needs type-level β, which conflicts with N_gen clause 3 (critique M8) | Mathematical + OWNER CHOICE |
| O6 | Universe-based foundations (CIC, HOL) as sources, given that A has no type-level computation | Mathematical + OWNER CHOICE |
| O7 | Classical members: choose an equality; parametricity is unavailable | Mathematical + OWNER CHOICE |
| O8 | Proof-level resource integrity: should templates be linear in holes for linear rules? | OWNER CHOICE |
| O9 | A10 (state in connective images) | Mathematical |
| O10 | Is ≈_S decidable for every S ∈ C_harm^prop? If not, H1 forces undecidable ≈_A (critique m7) | Mathematical |

---

## 8. Relationship to the original objective

| Charter element | Treatment in H1 |
|---|---|
| Fixed finite primitives | A, together with a fixed finite interface menu 𝓜_A |
| Mathematically meaningful operations | N_log (operations are intro/elim forms of formers given by universal properties) together with N_gen (they act on source *structure*, through fixed interfaces) |
| Core vs environment | Only translated source assumptions; rules derived; no per-source interfaces |
| Composition, substitution, binding | I4, I5 (Kleisli; respects the source's substitution discipline) |
| Resources | Inhabitation only (I2); proof level is O8 |
| Proof identity | I3, faithful and not full |
| Causality | Deferred (D5); route via (h3) |
| **Universality class** | **Logics (C_harm^prop), by owner choice.** Non-logical theories are handled as assumptions or relative interpretations. Non-logical proof identities form a separate question H1^theory |
| Across foundations | Intuitionistic, linear and modal propositional logics: in. Classical: open (O7). First-order: open (O5). Universe-based: open (O6) |

**Assessment.**
- H1 is a precise restatement of the original ambition **for propositional logics**.
- It has a non-vacuity criterion that survives the tested attacks, except A10 which is open.
- It is falsifiable: a single member S with no admissible F_S for a given A refutes that A. A family of such S defeating every A refutes H1.
- It does **not** reach first-order, higher-order or classical foundations without settling O5–O7.
- It **gives up** the claim that a fundamental core must host arbitrary effective proof calculi. Those are exactly the calculi for which only universal-algebraic hosts are known.

---

## 9. Decision matrix and recommendation

| Option | Non-vacuity | Status | Recommendation |
|---|---|---|---|
| H0 over C (interface only) | None | Satisfiable on fragments by A_U, paths, checkers | Baseline only |
| I ∧ N_sep over C | Equals decidable ≈_A | Conflicts with D3; false on S_G | Reject |
| I ∧ N_log over C | Partial (C1, C2a are false positives) | OPEN | Reject: criterion inadequate |
| I ∧ N_gen with **per-source** interfaces (first draft) | Defeated (reader and Cayley wrappers) | — | **Withdrawn** |
| I ∧ N\*\* over C | Strong | OPEN on S_G (no admissible host known) | Keep as H1^theory question |
| **I ∧ N\*\* over C_harm^prop** | Strong; correct verdicts on the five cases | **OPEN, falsifiable** | **Recommend as candidate H1, pending O9 (A10) and the owner's choice of C** |

**Single most valuable next test (O4).**
1. Fix A = System F, or second-order ILL with !, extended by Tranchini–Pistone–Petrolo's naturality equations.
2. Decide whether the Russell–Prawitz definitions of ∧, ∨ and ⊥ (and ⊗, & and ⊕ in the linear case) are **I3-faithful**: β, η and commuting conversions preserved *and reflected*.
3. Check also whether the added equations keep ≈_A consistent and leave A within N_log.
   - The naturality equations are not obviously local reductions or expansions of ∀.
   - If they are not, N_log fails for this A, and that is itself an informative result about N_log.

**This is a literature and pen-and-paper test. No implementation is needed.**

---

## 10. Limits

- Every proposition here is informal.
- C_harm^prop and N_log depend on the formal harmony definition (O3).
- Several facts remain UNVERIFIED-MEMORY:
  - Girard-translation I3;
  - normalization of the listed cores;
  - decidability claims for N_sep rows.
- The A10 attack is unresolved.
- Lambek–Scott was not accessed.
- No novelty is claimed.

## 11. Sources

`reports/008-source-notes/sources.md`. All entries below are verified in this session unless marked otherwise.

| Source | Content used |
|---|---|
| Reynolds 1983 | Parametricity (OCR scan) |
| Wadler 1989 | Parametricity (OCR) |
| Plotkin–Abadi | Theorems 1, 2, 5 |
| Girard–Lafont–Taylor, *Proofs and Types* | pp. 84–85, 113 |
| Tranchini–Pistone–Petrolo | arXiv:1607.06603v2 |
| Hasegawa | LMCS 2(3:3) 2006 |
| Pfenning–Davies | CMU preprint, pp. 3–4 |
| SEP "Algebraic Propositional Logic" | §2 |
| Lawvere | TAC Reprints 16 |
| Fiore–Leinster | arXiv:math/0508617v2, Thm 1.1 |
| Uemura | arXiv:1904.04097v3, Defs 4.1–4.5 |
| Abel, LPAR 2008 | System F βη normalisation by evaluation (NbE) |
| Scherer | arXiv:1610.01213v3, Cor 7 |

**Reused from earlier verified logs:**
- Hasegawa 2002 (reports 005, 007);
- HHP Theorem 4.1 (report 007);
- Statman–Dowek (report 004; Statman's and Friedman's originals not accessed).

**Not accessed:**
- Lambek–Scott;
- Prawitz 1965 (secondary only);
- Łoś–Suszko 1958 original.

## 12. Changes after the fresh critique

The critique is reproduced in `reports/008-source-notes/fresh-critique.md`.

| Finding | First-draft claim | Action |
|---|---|---|
| **F1 (FATAL)** | Proposition E: S_edge has no N\*-translation. "N\* has no false positives." Typed paths rejected | **Withdrawn.** The reader wrapper W[σ] = (X_u→X_v)→σ passes the first-draft N\*. Repaired by **fixed interface menus** (§3.2–3.3). Proposition E reproved with the critic's substitution argument, under fixed interfaces, for schematic variables (§6.2) |
| **F2 (FATAL)** | "C_harm is forced" | **Withdrawn.** C_harm^prop is an OWNER CHOICE with independent motivation (§7.1) |
| M1 | A9 "data in templates harmless" | Withdrawn. The Cayley wrapper is added as a test row and rejected via fixed interfaces. A10 is added as OPEN |
| M2 | I5 ill-typed with wrappers; call-by-value | Kleisli formulation; I5 parametrised by the substitution discipline; C5a verdict flagged |
| M3 | Łoś–Suszko misapplied; constants forced generic | Constants are now unconstrained (relative interpretation). Łoś–Suszko is applied to variables only |
| M4 | Subformula property | Removed; replaced by a normal-form classification |
| M5 | N_sep presented as independent | Shown equivalent to decidable ≈_A; conflicts with D3; kept as a rival only |
| M6 | N_log ill-defined with inductive types | Redefined: inductive formers admitted with β only (owner choice); presentation-level status of A_U stated |
| M7 | C_harm loopholes; λμ; NK | Fixed structural menu; classical calculi moved to OPEN members |
| M8 | First-order "kept" | Moved to O5 (OPEN) |
| M9 | Presentation dependence; missing false negatives | Added rows: C2c, C4r, Gödel–Gentzen, CbN CPS, ST, free-SMC S_n, each classified |
| M10 | Missing source notes; label errors | Notes added; Statman/Friedman relabelled secondary; Hasegawa instance relabelled as evidence, not an (A-univ) instance |
| m1–m9 | Various | Applied: E0 iso-overclaim withdrawn; E proof replaced; C1 relabelled B1; attack count corrected; §7.3 cartesian argument added; inequivalence witnesses on pairs (A, F); m7 → O10; o-reading flagged; λμ CPS completeness noted as UNVERIFIED-MEMORY (Hofmann–Streicher, Selinger) |
