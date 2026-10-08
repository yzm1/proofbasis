<!-- Fresh-context adversarial critique of the FIRST DRAFT of report 006 (commit 16de12f). Reproduced verbatim except paths. Responses: report 006 §10. -->

# Hostile referee critique of reports/006-definition-audit-claude.md (branch research/006-definition-audit-claude, commit 16de12f)

Target text: `git show d72ab1f:docs/STAGE_0_7_COMMON_CONJECTURE.md` (H). Cross-checked: reports 002 §2, §5; 004 §5.4–5.5; 005 §3–§9.
I had no access to primary literature in this pass. Labels on my own claims: VERIFIED = checked against repo text or a self-contained argument given here; INFERENCE = my argument with a stated gap; UNVERIFIED-MEMORY = recalled, not checked.

Severity: FATAL = a headline claim as stated is unsupported or invalid; MAJOR = a substantive error, overclaim or gap that changes a conclusion; MINOR = an accuracy, attribution or presentation defect.

---

## FATAL

### F1. §1 item 2 and §5.3: the "encoding-invariant non-vacuity is impossible" argument is invalid
**Passage.** §1: "So an *isomorphism-invariant* (encoding-invariant) non-vacuity criterion cannot be consistent with H.2 + C unless it rejects structures that every H-solution must resemble. **H.6 can only be closed by a translation-relative criterion, by fullness, or by restricting C.**" §5.3 steps 1–2.

**Argument.**
(a) *Wrong logical direction (VERIFIED, from the text).* Step 1 says that a non-interpretive invariant "must not be implied by any of" decidable equality, residual finiteness, and so on. What Propositions A and B actually support is the converse: the criterion must not *imply* decidable equality or computable separability, because no H-target has those properties. "Not implied by decidable equality" is vacuous, since no H-target has decidable equality in the first place.
(b) *Third marker not established (VERIFIED).* Step 1's third bullet ("contains no universal finitely presented group") is not shown to fail for every H-target. The text itself concedes that the groups G may sit "at different types for different G". Hosting each f.p. group at *some* endomorphism monoid is not the same as containing a single f.p. group that contains them all. So that marker is not forced to fail.
(c) *Non sequitur (VERIFIED).* Step 2 says "any criterion that excludes A_U while admitting some H-solution must refer to something beyond A's isomorphism type". This does not follow from step 1. Ruling out three specific invariants says nothing about all isomorphism invariants. Worse, A_U is not an H-solution at all: it handles only C_grp, not NJ, MILL and the rest. So "excluding A_U" places no constraint on criteria for full H.
(d) *Conflation (INFERENCE).* H.6's "encoding-invariant" most plausibly means invariance under the choice of serialization or coding of source proofs. The draft silently replaces it with "isomorphism-invariant property of the algebra A". That is a reinterpretation of H, which AGENTS.md rule 10 says must not be done silently.
(e) The "trichotomy" is not exclusive either. Fullness is itself a condition on F (it is translation-relative).

**Fix.** Downgrade to: "Propositions A and B show that any non-vacuity criterion implying decidable or computably separable ≈_A is unsatisfiable together with H on C. Whether some other isomorphism-invariant criterion works is OPEN." Remove the "can only be closed by" sentence from §1, §5.3 and §8. If the claim is kept, state the meaning of "encoding-invariant" explicitly as a proposed reading, and construct an H-solution, or a schema of solutions, to which the criterion must apply.

---

## MAJOR

### M1. Source notes do not exist, yet results are labelled ESTABLISHED as "verified in a retrieved text"
**Passage.** Line 15 ("Source logs: `reports/006-source-notes/`"); the label table (ESTABLISHED = "verified in a retrieved text unless marked (secondary)"); "see source notes" for McKinsey–Mal'cev, Mazurkiewicz, Chaudhuri–Miller–Saurin, Higman and Lean; Appendix ("Each is labelled in the source notes").

**Argument (VERIFIED).** `reports/006-source-notes/` does not exist on the branch. `git status` is clean, and the commit message says "before … source verification". Every ESTABLISHED label therefore asserts source access that has not occurred, which violates AGENTS.md rules 11 and 12. Line 260 is internally contradictory: "ESTABLISHED (Mac Lane coherence; UNVERIFIED-MEMORY for the exact location)".

**Fix.** Relabel every ESTABLISHED item as UNVERIFIED-MEMORY until the notes exist with exact statements and locations. Give precise citations: Novikov 1955; Boone 1959; Higman 1961, Proc. Roy. Soc. A 262; Lyndon–Schupp IV.7 for universal f.p. groups; McKinsey 1943 JSL 8; Mal'cev 1958; Diekert–Rozenberg, *Book of Traces*. All of these are UNVERIFIED-MEMORY on my side as well.

### M2. Corollary A1 overclaims and mis-explains §4.7
**Passage.** "LF, … System F, Martin-Löf definitional equality, the free SMC and the free SMCC, and any Dedukti theory … all have decidable equality." §1 adds "simply-typed and System-F-like λ-calculi". §4.7 verdict: "Corollary A1 explains why at a structural level."

**Argument.**
- "Martin-Löf definitional equality" is true only for *intensional* MLTT. Extensional MLTT (Martin-Löf 1984, Nuprl) has equality reflection and undecidable definitional equality. Lean 4's definitional equality is also undecidable (Abel–Coquand; Carneiro 2019). Both are UNVERIFIED-MEMORY. These established frameworks pass Prop A's necessary condition, and the draft never examines them.
- Equality reflection also collapses M3's distinction between "hypotheses" and "equations". In ETT, an explicit assumption `p : Id(w, id)` in F(E_S) changes ≈_A definitionally. This is exactly the loophole H.5 and M3 are meant to close (INFERENCE).
- "System-F-like λ-calculi" is too vague. λ-calculi with η for natural numbers (extensional Gödel T) have undecidable equality (UNVERIFIED-MEMORY).
- Free SMCC: decidability is uncited. With units the coherence problem is substantially harder (Heijltjes–Houston, PSPACE-completeness for MLL with units; UNVERIFIED-MEMORY whether this transfers to IMLL).
- "LF with empty signature" has no base types at all. It fails H.1 trivially, before Prop A is even needed.

**Fix.** Restrict A1 to explicitly named calculi, each with a citation for its decidability result: intensional MLTT; Church-style System F with βη; STLC with constants and no equations; unit-free free SMC/SMCC (Kelly–Mac Lane). Add a row to §4.7 for frameworks with *undecidable* definitional equality (ETT/Nuprl, Lean 4, Dedukti with fixed non-terminating rules), and analyse their H.5/M3 status. Delete "explains why" for frameworks that A1 does not cover.

### M3. Proposition B: the "in particular" claim about finite models is not justified, and uniformity is missing
**Passage.** "(i) the family can be enumerated; (ii) in each model … computable … semi-decidably refutable … In particular, separation by finite models … is impossible."

**Argument.**
- (INFERENCE) The proof's "search for a model and a witness" needs a *uniform* effective enumeration: indices from which the denotations and the inequality semi-decisions are computed uniformly. Conditions (i) and (ii) as stated are per-model. The fix is easy, but the statement is wrong as written.
- (INFERENCE) More seriously, A has infinitely many generated sorts and types. A "finite model" assigns a finite set to *each* type, which is infinite data. Checking that a candidate satisfies A's equation *schemas*, which range over infinitely many types, is not obviously semi-decidable. So "the finite models of A" need not be an r.e. family in the sense of (i). McKinsey–Mal'cev works because a f.p. algebra with finitely many sorts has finitely describable finite quotients and only finitely many relations to check.
- Statman's finite standard models are r.e. because they are parametrised by finitely many base sizes and use full function spaces. That does not generalise to A with algebraic equations.
- "Finite-model separation is impossible" therefore holds only for r.e., uniformly computable families of finitely describable models.

**Fix.** Restate (i)–(ii) uniformly and drop the unqualified "finite models" corollary. If it is kept, prove that the relevant finite models form an r.e. family under M1.

### M4. Proposition B "conflicts with report 004's proposed P₃ route" is a misattribution
**Passage.** §4.5 verdict, last line.

**Argument (VERIFIED against 004 §5.5).**
- P₃ concerns a *fixed source*: unit-free IMLL / Lambek modulo βη, whose equality is decidable (Kelly–Mac Lane, cited in 004 §5.4).
- P₃ asks whether uniform families over *all* finite promonoidal frames give a full and faithful semantics.
- P₃ is not proposed as an H-target A, and its "family" is a uniformity condition across frames, not an r.e. family of computable models of A.
- Prop B is about separating ≈_A for an A that covers all of C. There is no conflict.

**Fix.** Delete the sentence, or say only that P₃-style finite-frame semantics cannot be extended to an H-target for all of C (with the M3 caveat).

### M5. §6: P*'s (Par) blocks A_U only under an undefined semantic reading, and E8's T1⁺ compliance is reading-dependent
**Passage.** "(Par) parametricity. Every generator of A is parametric in type variables: A has no type-case and no type-indexed recursion." "P* blocks … A_U as stated, since its generators are non-identity polymorphic endomorphisms of a bare type variable. Parametricity forces ∀X.X→X to be trivial in relationally parametric models." "T1⁺ … There are no data sorts in the image of formulas."

**Argument.**
- (VERIFIED, from the definitions as written) A_U's generators are schematic constants a_j : X_P → X_P with U's relations. They do no type-case and no type recursion, so they satisfy Par *as defined*. Relational parametricity is a semantic property of models, and H does not require a parametric model. Under the stated syntactic Par, A_U (atom ↦ atom; the same construction as report 005 §4.1's A_V, generalised) already defeats P*, and E8 is unnecessary.
- (INFERENCE) E8 is needed only if Par means "A has a relationally parametric model". In that case E8 is plausibly parametric, since ∀X.(D→X)→(D→X) ≅ D→D by Yoneda-style parametricity, but this has to be stated as the definition.
- (VERIFIED) T1⁺ says "no data sorts in the image of formulas", yet E8 maps P ↦ D→X_P, whose image contains the data sort D. The draft's claim that E8 satisfies T1⁺ ("no formula becomes data") picks one of two readings.
- The "excluding E8 would require" list is therefore incomplete. A ban on data sorts in the images of *propositional atoms*, or 005's atom-to-atom interface, blocks E8 without forbidding arithmetic. (A_U still survives, which is the real point.)

**Fix.** Define Par precisely (syntactic or semantic). Make A_U, not E8, the primary counterexample to syntactic P*. Keep E8 only as the counterexample to semantic Par. Correct the "only F or R" conclusion of §6 accordingly.

### M6. The gate's explicit D2 check is not performed
**Passage.** H's gate: "Check whether D2 admits existing generic logical frameworks and whether any universal-checker disguise passes." The draft never tests D2 by name.

**Argument (INFERENCE, checked against 002 §2.4).** Check A_U against D2 clause by clause:
- T1: atoms ↦ atoms of the matching sort, componentwise. Passes.
- T2: fixed wrapper. Passes.
- T3: SN + HOM, with fixed group-word templates. Passes.
- T4: no logical items. Passes.
- T5: ADQ1. Passes.

So **D2 admits the Higman-type construction on C_grp.** That is the single most decision-relevant answer to the gate question, and it is left implicit. Conversely, E8 fails D2's T1, because atoms go to compound types. Route F (compound atom images) conflicts with D2's T1, and this is not stated either.

**Fix.** Add a §4.8 that runs D2 (T1–T5) on A_U, E8, B1, E6 and the free SMC on S_n, with a pass/fail per clause.

### M7. §8 "Every candidate counterexample to existence is answered by a Higman-type construction" overgeneralises
**Passage.** §8, final bullet; also the related §1 claim that H "is consistent".

**Argument (VERIFIED, from the text).**
- Proposition C and E8 cover C_grp only. No Higman-type construction is given for NJ with βη, MILL, binding, or multi-premise rules.
- §4.1's adversarial example ("a fixed finite universal equational theory that identifies codes of ≈_S-equal derivations … passes H.1–H.5 under reading (a)") is asserted without construction. "Proposition C, for groups" does not supply it. The closest established tool would be Bergstra–Tucker's finite specifications with hidden functions for (semi)computable algebras (UNVERIFIED-MEMORY), and that result is per-algebra, not universal and fixed.
- "H is consistent but not falsifiable" (§8) contradicts §1's "H is not yet a coherent nontrivial proposition". H.6 and H.7 are undefined, so consistency is not even a well-posed claim.

**Fix.** Restrict the statement to C_grp. Mark the §4.1 universal-equational-theory claim as OPEN/INFERENCE. Delete "consistent".

### M8. M4 and M6 together silently drop H.4's proof-level resource content for linear calculi
**Passage.** M4: "Merge H.4 into H.1 … move H.4's proof-level residue into H.7". M6: "H.7 restricted to C_causal (permutation-only equations)".

**Argument (VERIFIED, from the text).**
- E4 (MILL with βη and commuting conversions) is not in C_causal: β is not a permutation equation.
- After M4 and M6, nothing in H tracks "boundary occurrences" at the proof level for linear logic, which is the paradigm resource-sensitive source.
- H.1 over open judgments controls only which sequents are inhabited. It does not control whether F(d) uses a hypothesis exactly as d does. A target could map a linear proof to a term that discards and re-creates resources, as long as no new *judgments* become derivable.
- This is a weakening of H, and the §8 table records the resource row as "Preserved".

**Fix.** Keep a proof-level resource clause, for example usage-count or linearity-type preservation of F on boundary variables, independent of C_causal. Alternatively, list the loss explicitly as a change to H.

### M9. §4.6 C_causal: the definition is incoherent for trees, and the quantifiers are unspecified
**Passages and arguments.**
- (a) *(VERIFIED, from the displayed form)* "r₁(…r₂(ξ⃗)…) ~ r₂(…r₁(ξ⃗)…) where … neither consumes the other's conclusion." In the displayed nested form, r₁ *does* consume r₂'s conclusion. Sequent-calculus rule permutations are exactly adjacent rules where the lower one consumes the upper one's conclusion but acts on different formula occurrences. As written, the class is empty or ill-defined. Permutations past a binary rule (moving r into one branch) do not have this shape at all.
- (b) *(INFERENCE)* Mazurkiewicz traces need a *static* independence relation on an alphabet of letters. Independence of sequent rules depends on which occurrences are active, which makes it context-dependent. Derivations are trees, not words. "On linear derivation sequences, ≈_S is then Mazurkiewicz trace equivalence" only applies after an unspecified linearisation, and the dependence-graph theorem is then not the cited one.
- (c) *(VERIFIED, from the text)* "<_d the dependency order of d's class" is class-level, while "precedes … in F(d)" is computed on a raw target term. Two cases:
  - If "precedes" means raw tree order, reflection fails even for the *identity* translation of a sequent calculus into itself, because independent rules are tree-ordered in every representative.
  - If it means order on the ≈_A-class, A must carry a dependency order invariant under ≈_A, at least on images. Yet Propositions A and C require ≈_A to contain non-permutation equations (group relators).

  Which representatives of d and F(d) the conditions quantify over is unstated, and these are exactly the "precise quantifiers" H demands.
- (d) *(VERIFIED, from the text)* Preservation ("some target event over e precedes some over e′") is satisfied by a single pair. π⁻¹(e) may be empty (identity templates, glue), in which case preservation is unsatisfiable or vacuous. Given reflection, the independence clause is redundant.
- (e) *Positive example.*
  - "the net's link order is exactly the dependency order of the permutation class" is unsupported. The constraints on sequentialisation are given by kingdoms and empires (Bellin–van de Wiele), not by the subformula order of links.
  - I recall, UNVERIFIED-MEMORY, that sets of sequentialisations need not be the linear extensions of a single poset (there is disjunctive dependency). If so, MLL permutation classes are not trace classes.
  - Units must be excluded: for MLL with units, proof nets fail and equivalence is PSPACE-complete (Heijltjes–Houston, UNVERIFIED-MEMORY).
  - Chaudhuri–Miller–Saurin canonicity concerns *focused* MALL proofs, a different quotient.

**Fix.**
- Define independence on formula occurrences.
- Define C_causal on derivation trees, using an explicit partial order on rule instances, for example the order induced by active and principal occurrences.
- State the quantifier explicitly ("for all representatives" or "for some canonical representative").
- Define the target order on classes, and require the image classes to carry an invariant order.
- Replace the MLL example with one that has been checked, or label it OPEN.

### M10. Route R: "Propositions A and B no longer apply" does not make the route safe, and the route reverses H's "Not required" list
**Argument.**
- (INFERENCE / UNVERIFIED-MEMORY) "β, η and commuting conversions determined by universal properties" can already yield undecidable proof equality. η for an inductive type such as ℕ (extensional Gödel T) is an example. So requiring a computable separating semantics, which by Prop B's argument forces decidable ≈_A, may again be unsatisfiable.
- (VERIFIED, from H's text) Route R in effect *requires* decidable ≈_A, which H lists under "Not required". That is a change to H's principal question and must be flagged as such.
- "Falsifiable" is used ambiguously throughout (candidates can be refuted, versus H can be refuted).

**Fix.** Say that A's *proof* no longer applies. Flag that Route R overrides H's "Not required: decidable proof equivalence". Define falsifiability.

### M11. Route F may be met by universal constructions, so it is not an anti-vacuity route per se
**Argument (INFERENCE).**
- Route F needs, for each f.p. G, a type T with End(T) ≅ G exactly. Prop A still forces undecidable ≈_A.
- Algebraically universal categories realise every monoid as a full endomorphism monoid (Hedrlín–Pultr; Pultr–Trnková; UNVERIFIED-MEMORY).
- That E8 and A_U fail fullness does not show that Higman-type, computation-encoding solutions fail Route F.

**Fix.** State that Route F is OPEN with respect to non-vacuity and is not shown to exclude universal-algebraic encodings.

### M12. M3 relies on a "proof sort vs non-proof sort" distinction that is not intrinsic in type-theoretic targets
**Argument.**
- (INFERENCE) Under propositions-as-types, every type can be a proof sort. "No proof-sort constants" is ill-defined without a fixed sort discipline, which M1 does not fix.
- (VERIFIED against 002 §2.2) Report 002 withdrew item-wise environment classification as ill-defined and kept only the syntactic test "quantifies over formulas". M3 reintroduces an item-wise classification by sort without addressing that critique.
- See also M2: under equality reflection, hypotheses are equations.

**Fix.** Tie M3 to M1's Φ, with an explicit designated proof sort or judgment form. Cite 002 §2.2's withdrawn ledger and explain why the new test escapes it.

---

## MINOR

1. **Prop A, step 6 and the Σ₁ clause.** "≈_A is r.e." requires M1's reading (finitely generated congruence, r.e. typing). H's "fixed proof congruence" does not literally say this, and under some readings (e.g., observational equality) it fails. The Σ₁ condition is also unnecessary: f.p. groups with Σ₁-complete word problem exist (Clapham 1964; Boone 1966; UNVERIFIED-MEMORY). The undecidability core of Prop A is correct (VERIFIED by my check):
   - S_G ∈ C under 002 §2.1 plus finite equation schemas.
   - ≈_S at x:P ⊢ P is the Thue congruence generated by g g⁻¹ = 1 = g⁻¹ g and R_j = 1. This holds because outer rule application gives left multiplication and grafting into ξ gives right multiplication.
   - That monoid presentation presents G.
   - No other judgment is inhabited (no closed proofs; nothing between distinct atoms).
   - F is effective and the judgment is common, so the many-one reduction holds.
2. **§3, "This is report 005's Lemma … The argument is the same."** It is not the same. 005 uses normal forms rᵏ (0 ≤ k < n) and Z/n. For G there is no normal form, and the argument instead needs the standard fact Mon⟨X ∪ X⁻¹ | xx⁻¹ = x⁻¹x = 1, R⟩ ≅ Grp⟨X | R⟩. Note also that word order may reverse (G versus G^op, isomorphic via inversion).
3. **Proposition C, A_U.** A_U must include inverse generators and cancellation equations (a *monoid* presentation of U). Otherwise "U's relations" over the generators alone present a monoid, not U, and g_i⁻¹ ↦ u_i⁻¹ is not expressible. H.1 also needs "no closed terms of atom type", which holds because all generators are unary; say so. Cite report 005 §4.1 (Thompson's V, A_V) as the direct precursor: Proposition C is its generalisation from C_n to all f.p. G.
4. **E8 details.**
   - The group axioms for e, mul and inv are missing; only "U's relations" are listed.
   - With F(g_i t) = λd. F(t)(mul(c,d)), composition is reversed (an anti-homomorphism), which is harmless via inverses but should be stated.
   - The H.2 step does not need Breazu-Tannen conservativity. It follows from soundness in the set model D := U * ⟨d⟩, X := D, x := id: if mul(c_w, d) ≠ d in the theory then the interpretations differ (INFERENCE, elementary). Its UNVERIFIED-MEMORY status can be removed.
5. **§4.5 positive example 2.** It is correct (VERIFIED, by elementary reasoning about the free SMC: there are no maps between different multisets of generators and none from I; End(X^{⊗n}) ≅ S_n; an n-cycle has order n). It already appears in report 005 §9 ("End(P^⊗m) is S_m"), which should be credited. The table describes it as "non-interpreter" and "mathematically meaningful" without any criterion, since H.6 is undefined. H.4: one hypothesis becomes n wires, a change in the occurrence count that should be noted.
6. **HA-4.** Report 005 §6 already states that rⁿ = id makes event count and chain order non-invariant, and 005's freeze already restricted independence to pure permutations. Credit it; it is not a new finding of this audit.
7. **HA-6.** H explicitly lists "decidable proof equivalence" as not required, and 005 §7.3 explicitly rejects "undecidable equality ⇒ impossibility". Calling a decidability expectation "implicit" lacks textual evidence. Reword it as a conflict with *likely* non-vacuity markers.
8. **C-1.** H imports 002 §2.1, which already says "no side conditions" (002 L-d places checker-shaped sources outside the class). The "lax reading" is a stretch, and M2 largely restates H. Also, "Under the strict reading, no logic is lost (any r.e. consequence relation with a finite schematic presentation is still in)" is circular. Strict C excludes type theories with conversion or positivity side conditions unless they are re-presented (002 L-f). That undercuts §8's claim that "across foundational traditions" is "Preserved".
9. **M4 cost.** Presentation-morphism translations exclude proof-level negative translations (002 L-g, RAA at generic X). State this cost.
10. **E4.** "λx.⟨x,x⟩" proves ⊢ p ⊸ p⊗p, not p ⊢ p⊗p. The open-judgment witness is x:p ⊢ ⟨x,x⟩.
11. **Traceability.** The draft refers to "focus question 7" and "Phase A", but no task file defining the focus list is in `tasks/`. Cite it.
12. **E6.** Correct in substance (Quot.sound / EqvGen exactness give propositional faithfulness, and definitional equality is unchanged). Note also that E6 already fails D2's T1/T4 (report 002 B5).
