<!-- Fresh-context adversarial critique of the FIRST DRAFT of report 008 (commit 2196540). Reproduced verbatim except paths. Responses: report 008 §12. -->

# Hostile referee critique of reports/008-constructive-definitions.md

Branch `research/008-constructive-definitions`, commit 2196540 ("draft before source verification and critique"). Repository not modified.

Labels: **VERIFIED** = checked in the repository this session, or a self-contained argument given here in full. **INFERENCE** = an argument with a named gap. **UNVERIFIED-MEMORY** = a literature fact recalled, not checked against a source.

---

## FATAL

### F1. Proposition E is false as stated. Its Corollary, the §9 row "H1 over C with N\* — False", and the matrix verdict "N\* rejects typed paths" all fall with it.

**Passage (§6.2).** "No A satisfying the hypotheses of Lemma E0 admits a translation of S_edge satisfying I ∧ N_gen … Status INFERENCE for general W, PROVED for W = identity."

**Counterexample (VERIFIED; elementary).**
- Take A = STLC(→) over type variables. It is normalizing, harmonious, and has no constants, so it satisfies N_log and the hypotheses of Lemma E0.
- Set F(Q_u) = X_u and F(Q_v) = X_v. This satisfies clause 1.
- Use the per-source wrapper W[σ] = (X_u → X_v) → σ. It contains no term subexpressions and no type constants, so clause 2 holds. Clause 3 holds trivially.
- Hypothesis leaf x ↦ λk.x.
- Template t_e[ξ] = λk. k (ξ k). The template is closed, so clause 4 holds.
- The environment is empty.

Checking the interface for Γ a list of atoms:
- **I2.** Γ ⊢ (X_u→X_v)→X_v is inhabited iff X_v ∈ Γ or X_u ∈ Γ. That is exactly S_edge-derivability. The closed types W[X_u] and W[X_v] are uninhabited, as the valuation X_u = X_v = false shows.
- **I3.** The normal inhabitants of Γ, k ⊢ X_v are y_v or k y_u. These are in bijection with the S_edge proofs x or e(y).
- **I4/I5.** Grafting holds with Kleisli substitution.

The construction generalises to any finite graph: W_G[σ] = (∏_{e:a→b}(X_a→X_b)) → σ, with t_e[ξ] = λk. π_e k (ξ k). In implicational logic with atomic implications, derivability is reachability. Normal proofs are edge paths, so I2 and I3 hold.

**So typed paths (C2), re-presented with the rule table placed in the wrapper, satisfy I ∧ N_log ∧ N_gen.** This is a false positive of N\*, or else an acceptance that the draft did not report. Either way, it contradicts §1.3: "No false positive or negative on the five cases".

**A dilemma the draft cannot escape.** §3.3 says "Hypothesis leaves go to variables". With a non-identity W that is ill-typed: x : F(φ) does not have type W[F(φ)].
- **Read literally**, every source with hypotheses forces W = id. Then C5a (Hasegawa: Γ°;∅ ⊢ M° : (σ°→o)⊸o, with x ↦ λk.k x) **fails I**, and the matrix row "C5a ✔" is false.
- **Read charitably** (leaves go to a unit term), the reader-wrapper counterexample is admitted, and Proposition E is false.

**Fix.**
1. State W as a strong monad-like context with explicit unit and Kleisli substitution.
2. Add the clause **W_S and the context map mention no type variable that is the image of a source atom** (only fresh variables such as o).
3. Under that clause, Proposition E has a three-line proof (VERIFIED, given A admits type-variable substitution and has a closed inhabited type such as 1 or ∀Y.Y→Y):
   - Instantiate X_u := 1 in the closed template t_e : W[X_u] ⊢ W[X_v].
   - Apply it to unit(*) : W[1]. This gives a closed inhabitant of W[X_v] = F(⊢ Q_v).
   - That contradicts I2.

   This replaces the hand-waved step 4 ("instantiating a sufficiently rich test … by uniformity"), which is not an argument.
4. Separately, forbid the per-source "fixed context map" of §3.3 from adding hypotheses. As written, F(Γ) = Γ°, k : X_u→X_v is not excluded, so the same laundering works through contexts.

### F2. The claim that restricting to C_harm is "forced, not chosen for target convenience" is invalid. As written it is the move Task 008 forbids.

**Passages.** §1.7: "this restriction is **forced** for any genericity-based non-vacuity criterion". §8: "The narrowing is forced …".

**Argument (VERIFIED by reading).** The draft gives two grounds.

1. *Proposition E.* It is false (F1). Even in a repaired form it depends on N_gen clause 1, which the author introduced solely to block A3 (§6, A3 row: "Clause 1: constant atoms are generic too"). Without clause 1, S_edge is representable in pure System F. Send Q_u ↦ ∀Y.Y and Q_v ↦ ∀P Q.((P→Q)→P)→P, closed Peirce:
   - ⊥ ⊢ Peirce is inhabited, by ex falso.
   - Peirce ⊢ ⊥ is not inhabited, because Peirce is classically true.
   - Both closed types are uninhabited.

   So I2 holds for the one-edge source (INFERENCE for I3, which only needs injectivity on images). The restriction is therefore forced by the criterion the author chose, which is circular. "Any genericity-based criterion" is unproved: only this one N_gen was examined.
2. *006 Proposition A.* It excludes S_G only for **decidable-equality** cores. Reconciliation D3 explicitly says "Do not require decidable target proof equality". Shrinking C because decidable-equality targets cannot host S_G is a target-side reason. That is exactly decision item 1's warning: "don't shrink C merely to make a target work".

**Fix.**
- Present C_harm as an **OWNER CHOICE** with an independent motivation, such as "logics = structural, harmonious calculi", and state that it is *not* forced.
- Report Proposition E (repaired) as a consequence of the chosen N_gen, not as a justification of C_harm.

---

## MAJOR

### M1. N\* accepts Cayley-table interpreters for every finite-group calculus. Attack A9 ("data in templates harmless") is wrong.

**Construction (VERIFIED in outline; the decidability fact is UNVERIFIED-MEMORY).**
- Let A = STLC(→, ×, +) with strong η and commuting conversions for sums. This satisfies N_log clause 3 ("plus the commuting/permutation conversions required by positive formers").
- Let G be a finite group and D = o + … + o (|G| copies, o fresh). Only a fresh variable appears, as in Hasegawa, so even a strict reading of clause 2 passes.
- Wrapper: W[σ] = D → D × σ (state).
- Leaf: x ↦ λs.⟨s, x⟩.
- Generator g ↦ t_g[ξ] = λs. let ⟨t,y⟩ = ξ s in ⟨π_g t, y⟩, where π_g is the Cayley permutation written by case analysis.

The interface properties:
- **I3 (⇐).** Equal words give equal permutations. By η for sums (case-expanding t), the composites are βη-equal.
- **I3 (⇒).** Distinct permutations are separated in the Set model with |o| = 1.
- **I2.** D → D × X_q is closed-uninhabited and is inhabited only from X_q.
- **I4.** Grafting is Kleisli composition.

So report 005's S_n family and every finite S_G embed under I ∧ N\* into a decidable, harmonious core (decidability of STLC + sums βη: Ghani 1995 / Altenkirch–Dybjer–Hofmann–Scott 2001 / Lindley 2007, UNVERIFIED-MEMORY).

**Consequences.**
- The multiplication table is literally the template data.
- §6 A9 ("Data inside terms cannot make a translated type inhabited or uninhabited", so harmless) misses I3. Data in templates, combined with data-carrying wrappers, hosts non-logical proof identities.
- §7.1's reason for excluding S_n and §7.4's claim that S_n needs H1^shape are both wrong.

**Fix.**
- Add this attack to the catalogue.
- Either accept it explicitly as legitimate (and then explain why A_U differs other than by infinitude), or add a constraint on W. One option is to require W to be the identity, or a fixed core-level modality independent of S. Another is to require templates to be *parametric in W's auxiliary variables*: π_g inspects the injections into D, so it is not parametric in the summand structure.

### M2. The interface I is ill-typed for non-identity wrappers. I5 conflicts with the C5a source's own equality.

**Passages.** §3.3: "Hypothesis leaves go to variables". §3.4 I5: "F(d[e/x]) ≈_A F(d)[F(e)/x]".

**Argument (VERIFIED).**
- x : F(φ) while F(e) : W[F(φ)], so the right-hand side of I5 is ill-typed unless W = id.
- Moreover, Hasegawa's source is Moggi's computational λ-calculus. There β holds only for **values**, and d[e/x] for non-value e is not an equation of the source. So I5 as stated is not even a source-side congruence for C5a.
- The "✔" for C5a under I was therefore not actually checked.

**Fix.**
- Define F on contexts and on leaves via a unit η_W.
- State substitution as Kleisli/let-substitution.
- Parametrise I5 by the source's substitution discipline (value substitution for call-by-value sources).

### M3. The Łoś–Suszko argument is misapplied. N_gen clause 1 is ad hoc and depends on naming.

**Passages.** §6.2: "S_edge's rule mentions particular atoms, so it is not structural (Łoś–Suszko)". §4.3 clause 1: "whether a variable or a constant".

**Argument.**
- Structurality is closure under substitutions of **propositional variables** (UNVERIFIED-MEMORY of the definition; the SEP entry is cited via 002). Constants are not substituted.
- Report 007 §4 presents the vertices as "atomic objects Q_v" (constants), and 008 calls them "opaque atoms". A rule Q_u / Q_v between constants is structural, just as ⊢ ⊤ is.
- Calling it non-structural presupposes clause 1's re-classification of constants as variables. That is circular.
- Whether a symbol is an "opaque constant atom" (forced to a variable) or a "nullary connective" (sent to a closed type context) is decided by how the source *labels* it. Minimal logic's ⊥ as an atom and intuitionistic ⊥ as a connective is the standard example.
- So clause 1 is syntactic naming, the ground Task 008 forbids using alone.

**Fix.**
- Define atom versus connective semantically, for example: "a symbol with no rules is an atom".
- Or drop clause 1's constant case and handle A3 by an I2/I3-level argument.
- Withdraw "not structural" for S_edge, or restate S_edge with atom *variables*.

### M4. (A-log) requires the subformula property, which excludes System F and second-order LL. Those are the draft's own examples and its O1 candidates.

**Passages.** Lemma E0: "Examples: … System F". §7.2 (A-log): "weak normalization with the subformula property". §7.3 and O1 propose System F and second-order ILL.

**Argument (UNVERIFIED-MEMORY, standard).** Second-order normal forms lack the subformula property, because ∀-elimination instantiates arbitrary types. H1 as stated therefore excludes every candidate the draft recommends testing.

- Lemma E0's proof never uses the subformula property. It uses only the classification of normal forms (intro / neutral / case-on-neutral) and the absence of constants.

**Fix.** Replace the hypothesis with "β(η)-normal forms are intro, neutral, or positive-elimination-of-neutral; no constants; consistency".

### M5. N_sep is equivalent to decidability of ≈_A, so it contradicts D3.

**Argument (VERIFIED).**
- Suppose ≈_A is r.e. and decidable. Take the single term model, with denotation equal to normal form or to the canonical representative. It is uniformly computable and separating, so N_sep holds.
- Conversely, 006 Proposition B gives decidability from N_sep.
- So N_sep adds no semantic content beyond "≈_A decidable". Reconciliation D3 says not to require that.
- The cited Statman/Friedman models are the wrong witnesses. Set models over infinite sets do not have computable denotations at higher types. For STLC, a family of finite models (Statman's finite completeness) would work.

**Fix.** Either state N_sep ⇔ decidable ≈_A and record the D3 conflict, or require the models to be *non-syntactic* in a defined sense.

### M6. N_log is ill-defined, and its C1/C2 "✔" verdicts and the §4.4 witnesses are unsupported.

**Passages.** §4.2 clause 1: "no base types other than type variables … Term sorts permitted … e.g. inductive types". Clause 2 requires local completeness (η) for every former.

**Argument.**
- Nat, List, Bool and Id are closed base types, which contradicts clause 1.
- Intensional theories with Nat, List and Path families do not have definitional η for these types (UNVERIFIED-MEMORY, standard). So clause 2 fails for the C1 and C2 cores as described.
- The matrix entries "N_log ✔" for C1 and C2, and the §4.4 witness "typed paths in a pure core with inductive families (N_log holds)", are therefore unestablished.
- C1's Acc also needs identity types (check(…) = true), possibly with large elimination. Its harmony status is not discussed.

**Fix.**
- Decide whether inductive types without η count as harmonious.
- Rerun the C1 and C2 rows.
- Use a clean N_log ∧ ¬N_gen witness, for example the Gödel–Gentzen p ↦ ¬¬p into STLC(→,0).

### M7. C_harm is not well-defined, and its stated members and non-members are wrong.

**Passages.** (h1): "or a structural rule that S declares. Every rule is structural in Łoś–Suszko's sense". Members: "NK (with a classical structural rule), and the λμ-style classical calculi".

**Argument.**
1. "Structural" is used in two senses: proof-theoretic (weakening, contraction) and Łoś–Suszko (substitution-invariance). "Declared structural" is an unbounded loophole:
   - A checker calculus can have **zero connectives**, all rules declared structural, and syntactic proof identity. Then (h2) is vacuous and (h3) holds with an empty generating set, so the claimed non-member is admitted.
   - Every schematic rule, the Run rules included, is closed under substitution.
2. λμ's equations (structural μ-reduction, μ-η, renaming) are neither local reductions/expansions of a connective nor "permutations between rules acting on independent occurrences". So λμ violates (h3).
3. NK's ≈_S is unspecified. With β plus η for →, ∧ and ⊥ plus ¬¬A ≅ A, Joyal's lemma collapses proofs to a preorder (UNVERIFIED-MEMORY, Lambek–Scott). Membership and the hosting obligations change with that choice.
4. For sequent calculi, "local soundness/completeness" and "permutation conversions" define different equalities from natural deduction. O3 concedes this, but §7.1 still asserts membership.

**Fix.**
- Remove "declared structural".
- Enumerate the allowed structural rules: exchange, weakening, contraction, or fixed context disciplines from a finite menu.
- Treat classical calculi as OPEN members, with an explicit proof equality.

### M8. First-order sources cannot meet N_gen and I5 together, so "first-order quantifiers … kept" is unsupported.

**Argument (INFERENCE).**
- Atoms P(t) carry term arguments. Clause 1 sends "every source formula atom" to a fresh type variable, which loses t and breaks I5 term substitution.
- Repairing this needs family variables X_P : F(ι) → ⋆.
- Predicate substitution (structurality for predicate logic) then needs type-level β, which clause 3 forbids.
- Whether such a core satisfies N_log is not discussed.

**Fix.** Restate clause 1 for predicate atoms, and decide clause 3 versus predicate substitution explicitly.

### M9. Several verdicts are presentation-dependent, and false negatives go unreported. The criteria are not robust under "alternative presentations".

1. **C4 (HHP) is rejected by N_gen only because atoms are LF terms.** The same signature can be moved into a reader wrapper as ∀-closed rule hypotheses, with atoms as type variables (F1's construction plus ∀ for schematic rules). That version passes N_gen for sources with free proof identity, and fails I3 only where the source has β/η. The C4 verdict therefore tracks where the rule table is written, not proof-theoretic structure. (INFERENCE for general rule shapes: I2 adequacy is HHP-style.)
2. **False negatives not reported in §5.** Each of the following violates clause 1 or 2, or the unwrapped-context interface, and none appears in the matrix:
   - Gödel–Gentzen/Kolmogorov negative translations (p ↦ ¬¬p, atom to compound);
   - call-by-name CPS / Kolmogorov with wrapped hypotheses (x : ¬¬A\*), which the interface cannot express;
   - the relational standard translation ST_x(p) = P(x) from report 004, whose world variable x is a foreign term in the type;
   - the free-SMC S_n embedding (P ↦ X^{⊗n}) that report 006 called natural.
3. **C4's N_sep is applied to "LF with a signature".** That is per-source, not a fixed A, so the criterion is applied to a different object than in the other rows.

**Fix.** Add these rows, and state whether each is a false negative or an intended exclusion, with a reason that does not depend on presentation.

### M10. Source discipline (AGENTS rule 11).

- **Missing notes (VERIFIED).** `reports/008-source-notes/` does not exist on the branch. Every "see notes", and each ESTABLISHED label that depends on it, is unsupported: Prawitz definability, η-failure of Church encodings, normalization theorems, Fiore–Leinster.
- **Statman/Friedman label.** It is labelled "ESTABLISHED (verified)", but 004's notes say the Friedman and Statman originals were NOT_ACCESSED (only the Statman–Dowek note was). It should be secondary.
- **C5a outside C_harm.** Hasegawa's source (the computational λ-calculus, CBV) is not shown to be in C_harm, so §7.3's "one instance of (A-univ), ESTABLISHED" is mislabelled.

---

## MINOR

- **m1. Lemma E0.** The lemma is correct for the context {x:X} in STLC(×,+,0,1), System F and linear λ with !. This was checked by case analysis:
  - η-long forms at atomic type, case and abort on neutrals, and let-! all need a neutral of compound type, and none exists;
  - System F has no ∀ at a variable head;
  - End(X) = {id} needs weak normalization plus soundness of ≈.

  But §5.3's "A_U is not equivalent to any N_log core" is an overclaim. An equivalence need not send X_P to a variable, and Aut(X^n) = S_n shows that nontrivial groups do occur. The correct route is: an effective equivalence plus a decidable ≈_B would decide U's word problem (006 Proposition A). (INFERENCE)
- **m2. Proposition E step 4.** The step is not a proof. Use the substitution argument in F1's fix.
- **m3. C1 attribution.** C1 (Acc(⌜S⌝,⌜J⌝)) is 002's **B1**-shaped reflected checker (Prf code_S code_J), not B2. B2 is atom-uniform certificates (002, line 344).
- **m4. Counting and numbering errors.**
  - §1.4 says "eight ways", but the table has A1–A9.
  - There is a §6.2 but no §6.1.
  - S_edge's rule "from x : Q_u ⊢ d : Q_u" fixes the context. Report 007's edge is Γ ⊢ Q_u ⇒ Γ ⊢ Q_v.
- **m5. Unargued §7.3 claims.** "Every cartesian A fails H1" and "linear without ! fails NJ" are stated without argument.
  - A short proof for the first: instantiate the ⊗I template with both holes as unit(x) in a shared cartesian context. This gives X_p ⊢ W[C_⊗(X_p,X_p)], contradicting I2. (VERIFIED, given closure of templates under substitution.)
  - The second is INFERENCE.
- **m6. Inequivalence of N_log and N_gen.** They predicate different things (A versus F_S), so pairwise "inequivalence" is nearly vacuous. Give witnesses on the combined pair (A, F_S).
- **m7. Possible trivial falsity of H1 is unchecked.** If some S ∈ C_harm has undecidable ≈_S (candidates: second-order sources with η for ∃/∀), then I3 forces an undecidable ≈_A. That may clash with (A-log) normalization if normalization is meant to decide ≈_A. This is UNVERIFIED-MEMORY; neither direction is checked.
- **m8. "Applied unchanged".** C5a is re-read with o as a type variable. That changes the construction, not the criterion, but it should be flagged in the matrix itself.
- **m9. λμ hosting.** CPS completeness for call-by-name λμ (Hofmann–Streicher; Selinger, control categories; UNVERIFIED-MEMORY) is the relevant positive evidence for classical sources. It is not cited, and it needs the target equality to include the response-category η.
