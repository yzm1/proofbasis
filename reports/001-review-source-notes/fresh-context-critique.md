# Independent review of reports/001-existence-and-novelty.md

Reviewer stance: adversarial in both directions. Labels:
- **CONFIRMED**: checked in source text, either the evidence log in `reports/001-source-notes/` or a primary source I fetched myself (noted where so).
- **INFERENCE**: my own argument.
- **UNVERIFIED**: from memory, or not checked.

No repository files were modified.

Primary sources I downloaded myself (in `scratchpad/review/dl/fresh/`):
- Selinger, "Control categories and duality" (MSCS PDF from the author's site).
- Akbar Tabatabai–Jalali, arXiv:1808.06258v2.

---

## 0. Bottom line

The source extraction is generally careful. The quoted theorems I checked match the evidence log. The comparison matrix is valuable.

The **inference from that evidence to "stop"** is not valid as stated:

- The executive summary and the decision memo repeatedly upgrade weaker kinds of evidence into "defeated" or "obstructed":
  - a specific failed translation;
  - a complexity result;
  - a hypothesis-laden categorical collapse;
  - the absence of an agreed definition.
- The central §6.3 dilemma has three problems:
  - its lemma is mis-stated (it swaps preserve and reflect);
  - its horn (ii) conflates equations that compute on codes with schematic object-level laws;
  - under a literal reading of NCE-H, its horn (iii) is itself excluded by H2/H4.
- C\* asks whether an *existing* framework works. That is a bibliographic question, not an existence question. For a fixed finite benchmark, the existence question is trivially "yes" (a disjoint union), unless a size or structure measure on A is defined. The report never defines one.

The strongest defensible verdict is narrower: **"CV0 is ill-posed; R1/R2 (per encoding) are known; the decisive missing definition is a measure of the size or structure of A relative to C."** That is a *narrow* outcome, not an evidence-based *stop*.

---

## 1. Validity of the inference to "stop": evidence categories

### 1.1 Classification of the cited evidence

#### (A) Impossibility relative to explicit hypotheses (genuine theorems)

| Item | What it proves | Status |
|---|---|---|
| Došen Props 1–3; GLT App. B | A CCC with initial ⊥ **and** a *natural* ¬¬-elimination (Prop 2) is a preorder. So is a bicartesian closed category with a *dinatural* ⊤→A+¬A (Prop 3). GLT's form needs 0^(0^A) ≅ A. | CONFIRMED (log, proof-identity S1) |
| Selinger Cor 3.8 | A control category with bifunctorial ⅋ is a Boolean algebra. | CONFIRMED (log; I re-checked the PDF, line "Corollary 3.8") |
| Gardner Thm 5.1.7 / Cor 5.1.8 | No adequate ELF+ representation of linear or relevant logic, relative to her definition (object hypotheses = framework hypotheses). | CONFIRMED (log, OCR) |
| Gardner Ex 5.2.6 | Prawitz ND-S4 has no natural ELF+ representation. | CONFIRMED (log) |
| Berardi–Tatsuta Thm 8.3, Thm 8.4 | Derivability non-equivalence of cyclic and inductive systems; non-conservativity. | CONFIRMED (log) |
| Oda–Kimura Cor 31 | Cut is not eliminable in the stated system. | CONFIRMED (log) |
| Lafont Lemma 14 | S[2] is not finitely generated. | CONFIRMED (log) |
| MDT Prop 2.25 | A vacuity *construction*. It is a positive theorem used negatively. | CONFIRMED (log) |

#### (B) Computational intractability (requires complexity assumptions)

- **Heijltjes–Houston Thm 9.1** (PSPACE-complete). CONFIRMED.
  - The consequence "no canonical nets with a tractable translation" needs **P ≠ PSPACE**. This is implicit in their §1 and is not stated in the report's executive summary.
- **NST 2019** (ABSTRACT_ONLY) and **Cohen et al.** (citing) give PSPACE-hardness of thread/infinite-descent checking.
  - The relevant assumption for "no polynomial *local* certificate" is **NP ≠ PSPACE**. If validity had poly-size, locally checkable annotations, validity would be in NP. INFERENCE.
  - The report states no assumption at all.
  - For CLKIDω itself, the lower bound is UNKNOWN (Das 2020). CONFIRMED in the log.
- **BDKS Cor 6.6** (Σ⁰₁-complete). CONFIRMED. This is undecidability, not intractability. It concerns *one* criterion (bouncing threads, µMLLω).
  - BDKS themselves note that bounding a parameter restores decidability (log, §3c).
  - Σ⁰₁ means r.e. So pairing each pre-proof with a finite witness of validity gives a *decidable* certificate system. INFERENCE.
  - The result therefore shows that a *pre-proof alone* is not an effective certificate. It does not show that cyclic reasoning lacks finite effective certificates.
  - CA4 / A4 ("effective must mean decidable validity of finite certificates") is a fine amendment. CX10 is not an obstruction to it.
- **F09 items** (Buss; BIW, abstract only; Das Thm 6.10) are size or blow-up results, not impossibility results.

#### (C) Failure of a specific translation or encoding

- **MOTW §8.3**: Girard cbv is not complete for equality. CONFIRMED.
  - Hasegawa FLOPS 2002 Thm 1 / Prop 5 (in the log) gives a *different* translation, linear CPS, that is equationally complete and full for the computational λ-calculus.
  - So CX6 refutes one translation, not the cross-foundation goal.
- **Gardner Thm 5.2.11 and 5.2.13**: these concern *specific* representations ("the representation … given in example 5.1.12"; "the signature Σ_HPL"). CONFIRMED (log, verbatim).
  - **The report overstates them.** CX7 says Hilbert S4 "is adequately but not naturally representable". The executive summary says natural encodings "fail for Hilbert S4".
  - Thm 5.2.13 shows only that the *ND* signature does not naturally encode *Hilbert* PL. A Hilbert signature (constants K, S, MP) would trivially be natural. INFERENCE.
- **LLF sequentialisation** (CLF p. 13). CONFIRMED. This is a failure of one framework, which CLF then fixes.
- **Felicissimo–Winterhalter Table 1**: missing or flawed proofs for four encodings. This is the absence of a proof, not an impossibility.

#### (D) Absence of a known result or definition

- Straßburger: "neither notion has a commonly agreed definition".
- MDT: structurality is open.
- HHP: uniform adequacy is a "thesis".
- The CLF Petri-net adequacy proof was not seen.

### 1.2 Places where the report upgrades a category

| # | Location | Upgrade | Label |
|---|---|---|---|
| U-a | §0(c) "Defeated by established counterexamples: yes, for the uniform version of R3" | Lists CX4 (A), Straßburger (D), Selinger Rem 8.2 (different theories, not an impossibility), CX5 (B), CX6 (C) and Gardner (C, overstated) under "defeated". Only CX4 is an impossibility, and only under its hypotheses. | INFERENCE, based on CONFIRMED sources |
| U-b | §0(c), §7.6 "R3 (uniform) Obstructed (CX4–CX7)" | "Uniform R3" is never defined. F04 defines it as one congruence that is *both* CCC-with-initial-⊥ *and* symmetric classical. CV0 asks for per-S F_S into one A. Under that reading CX4 does not bite: NJ can use an initial ⊥, while cbn λμ is CPS-encoded with a non-initial response object R. Selinger's control categories explicitly do "not require that the families of maps i_A : ⊥ → A … are natural" (I checked this in the PDF). Both live in one CCC (STLC with base types) without collapse. **The report's own C\* asserts exactly this coexistence**, so §0(c) and §10.2 are in tension. | CONFIRMED (Selinger PDF) + INFERENCE |
| U-c | §0(c) "Proof identity in MLL with units is PSPACE-complete" filed as a counterexample | This is complexity, and it needs P ≠ PSPACE to imply anything. It obstructs only *polynomial canonical forms*. LF-style ≡_A with β is already non-elementary to decide by normalisation (Statman, which the report's U7 notes as UNVERIFIED-MEMORY). So CX5 does not obstruct representing MLL-with-units identity by a fixed decidable ≡_A. Boundary condition 1 of C\* ("forces ≡_A to decide a PSPACE-complete problem") is therefore not a boundary at all, unless ≡_A is required to be polynomial. | INFERENCE; Statman UNVERIFIED |
| U-d | §0(c) and §10.1 "local-only R4/R5 on cyclic proofs" | **"R5" is undefined.** The docs define only R0–R4 (I grepped: R5 occurs only in these two lines). "Local" is also undefined. Evidence: Brotherston's "global condition … (in general, anyway)" is a remark, not a theorem; PSPACE-hardness is for µMALL threads (abstract only) and abstract infinite descent; for CLKIDω the lower bound is unknown. | CONFIRMED (grep, log) |
| U-e | §10.1 "already established (R0–R2 …)" | §0(a) says "largely for R2" and F01 says R2 "Requires scope change" (uniformity is a "thesis"). The memo flattens this into "established". For resource-sensitive R2, the machine had to change (LF → LLF → CLF); per §7.2 there is no fixed-machine result. | CONFIRMED (internal) |
| U-f | §0 "If the environment may add equations …, R3 … [is] vacuous" | See §2.3: this is false for *reflection*, and the report's own evidence (FW2024 Table 1; Felicissimo Thm 46) shows it. | INFERENCE + CONFIRMED |
| U-g | §0 "Universality is then achieved by inclusion of each foundation's structure, not by a small basis" | No measure of "small" is ever defined (A5 asks for one but never supplies it). The report's own counter-consideration (CPS, Hasegawa) concedes the union may be small. The conclusion is rhetorical, not inferred. | INFERENCE |
| U-h | §2.2 "CV0 as written is true and uninformative" vs T9 "The conjecture has no fixed truth value" | Internal inconsistency. With "nontrivial" undefined, C = {A} may or may not count. The correct verdict is "ill-posed". | CONFIRMED (internal) |
| U-i | §0(a) theory U "covering about 13 systems" | It covers them as a fragment theorem only. U is *not* provability-conservative (CX13; Blanqui et al. §4). The executive summary omits this caveat, so it should not appear under the R1 "already known" heading. | CONFIRMED (log) |

**Net assessment of "stop":**
- Category (A) evidence defeats only:
  - a particular categorical combination (CX4);
  - ELF+-style direct encodings of substructural logics;
  - a few specific encodings.
- No item proves that no fixed finite A with nontrivial R3 exists for a nontrivial benchmark. As §3 below shows, for finite benchmarks such an A trivially exists.
- The evidence supports "CV0 is ill-posed; R0–R1 are vacuous without anti-vacuity; R2 is known per encoding". It does **not** support "R3 is obstructed".

"Stop" is a reasonable *value judgement* about novelty and cost. It is not entailed by the evidence. The memo should say which kind of judgement it is.

---

## 2. NCE-H (§6.2) and the vacuity–identity dilemma (§6.3)

### 2.1 The Lemma is mis-stated, and once corrected it is a near-tautology

The Lemma says "F_S reflects ~_S only if ~_S is syntactic identity". Under the hypotheses (F injective, ≡_A trivial on the image):
- **Reflection** (F(d) ≡_A F(d′) ⇒ d ~ d′) *always* holds: F(d) ≡ F(d′) ⇒ d = d′ ⇒ d ~ d′ by reflexivity.
- It is **preservation** (d ~ d′ ⇒ F(d) ≡_A F(d′)) that forces ~ ⊆ identity.

The displayed one-line argument proves the kernel statement, which is about preservation. The word "reflects" is wrong. INFERENCE (elementary).

Once corrected, the Lemma says: an injective map into a set where ≡ is equality cannot identify anything. It is not a straw man, because it does describe the standard LF adequacy format. But it is not substantive, and HHP p. 3 already says this in prose ("not to be confused with any equality … in a represented logic"; CONFIRMED in the log).

### 2.2 The case split (i)/(ii)/(iii) is not exhaustive and not independent

**(i) is not independent of (ii)/(iii).**
- Quotient adequacy needs ≡_A to be non-trivial on the image.
- That non-triviality comes either from E_S extending ≡_A (ii) or from A's native congruence (iii).
- So (i) is a *format* of the R3 requirement, not a third mechanism.

**A missing option, (iv): ~_S as a declared judgment rather than definitional equality.**
- Example: a family `eq : Prf φ → Prf φ → type` with constants for the generators of ~_S, as in Pfenning §3.6 (object reductions as signature judgments; CONFIRMED in the matrix).
- R3 then becomes "d ~_S d′ iff eq F(d) F(d′) is inhabited". That is an adequacy theorem of exactly the R1 kind.
- The report mentions this only in A3, outside the dilemma.
- H1 permits it, since it uses only constants. Whether H2 permits it depends on whether ~_S's generators count as "rule schemas" of a second judgment of S.

**A missing sub-case of (iii): a *generic* congruence.**
- Examples: CLF =c; the rewriting-logic exchange law; Mazurkiewicz-style permutation of independent rule instances.
- Such a congruence can identify constant-headed deep encodings for *any* logic whose ~_S is generated by rule permutations, without A containing each foundation's connectives.
- This is precisely the "small basis" possibility, and §6.3 does not consider it.
- It plausibly covers permutation-type identities (for example MLL⁻ rule commutation, the vGH Thm 1 setting). It does not cover normalisation-type identities (β/η). INFERENCE.

### 2.3 Horn (ii), "E_S may extend ≡_A ⇒ vacuity", conflates three kinds of equation

| Kind | Example | Vacuous? |
|---|---|---|
| (α) Equations or rewrite rules that compute on encoded data (codes, booleans, certificates) | I-C's `valid` | Yes. Interpreter-like. |
| (β) Schematic object-level laws over rule constants: per-S equations whose two sides are built from S's rule constants and pattern variables, one per generator of ~_S (e.g. `impe (impi f) a = f a`) | Felicissimo's object β via environment rules (Thm 46) | No: see below. |
| (γ) Equations from universal properties native to A | η for A's own Π | Not per-S at all. This is horn (iii). |

Kind (β) is not vacuous:
- Adding (β) equations makes *preservation* hold by declaration.
- *Reflection* (conservativity of A + E_S over ~_S) remains a substantive theorem. Rewrite rules can identify far more than intended (non-confluence, interaction with A's βη, or collapse).
- The report's own evidence shows this:
  - FW2024 Table 1: no conservativity proof for any of four real encodings; three are not confluent. CONFIRMED (log).
  - Felicissimo Thm 46: "M ↪* N iff ⟦M⟧ ↪* ⟦N⟧" is a hard-won reflection theorem. CONFIRMED (log).
- If (ii) made R3 vacuous, these results would be trivial. They are not.
- So the claim "R3 holds by declaration" is wrong for the reflection half. It is exactly parallel to R1 in LF: rules are declared, and adequacy is a theorem. The report does *not* call that vacuous. INFERENCE.

**The H1/H2 asymmetry is not justified by the report's own exclusion table.**
- H2 allows per-S *rules* (constants) under an adequacy obligation. H1 forbids per-S *equations* even under the same obligation.
- The stated motivation is I-C. But **I-C already fails H2**:
  - `acc : Πc φ. IsTrue(valid c φ) → Prf φ` is not in bijection with S's rule schemas;
  - its premise is discharged by computation.
- So H1 is *sufficient* but not *necessary* to exclude I-C.
- A symmetric criterion would close the gap: **H1-schematic**, under which E_S may contain only equations of kind (β), left-linear, between proof terms headed by rule constants, never at type level or on syntax codes, with conservativity as the H3 obligation.
- H1-schematic would plausibly admit Felicissimo-style object-β (if restricted to proof terms) and still exclude I-C. The report does not consider it. U1's H1′ is a different variant (a fixed rewrite set inside A).

### 2.4 NCE-H internal consistency

**N1. Literal H2 excludes the report's own inclusions.**
- H2 says "There is a bijection r ↦ c_r between S's rule schemas and constants of E_S".
- The HHP FOL signature also contains syntax constants (ι, o, ⊃, ∀, `true`). So literal H2 fails for HHP, contradicting the inclusion "LF encodings of FOL/HOL satisfy H1–H4".
- The intended reading is presumably "proof-forming constants". The report should state that reading. CONFIRMED (text of §6.2) + INFERENCE.

**N2. Literal H2/H4 exclude horn (iii).**
- A shallow NJ(→) encoding uses A's own λ and application for ⊃I/⊃E. It has *no* constants c_r, and F(⊃I(d)) = λx.F(d) is not of the H4 form c_r t̄ (…).
- So "Under NCE-H, (ii) is excluded, so R3 needs (iii)" is incoherent: (iii) is also excluded.
- The same applies to C\*: the counter-argument's "shallow NJ in a CLF-like framework" is not an NCE-H encoding.

**N3. What literal NCE-H actually implies.**
- With deep, rule-local encodings (H2 + H4) and fixed ≡_A (H1), images are constant-headed canonical terms.
- The only way ≡_A can identify two of them is through a generic native congruence such as CLF's =c (let-permutation).
- Normalisation-type identities such as NJ βη are therefore unreachable. F cannot normalise without violating H4 and the substitution clause of H3.
- So literal NCE-H plausibly makes the NJ-βη component of C\* *false by construction*. Gate 0.5 would then return outcome (b) as an artefact of the definition. INFERENCE (fairly robust, but informal).
- This is arguably the precise, interesting statement hiding in §6.3. It is worth stating as a conjecture in its own right: *under rule-as-constant, rule-local encodings, faithful R3 is possible exactly for ~_S generated by permutations of independent rule instances.*

**N4. H2's key phrase "no side premises discharged by computation" is informal, and I-S exploits that.**
- Consider variant I-S′: E_S declares, per S, a finite copy of the UTM's transition constants (an auxiliary judgment `Trace`) and c_r : Πψ̄ φ. Trace_r(ψ̄,φ) → Prf ψ̄ → Prf φ.
- The trace premise is discharged by an explicit *derivation* built from declared constants, not by conversion.
- Genuine LF encodings likewise use auxiliary judgments for side conditions (eigenvariable conditions, "closed theorem" for necessitation, explicit conversion judgments for type theories).
- So H2 either forbids auxiliary judgments, which excludes legitimate encodings of systems with side conditions, or admits I-S′.
- The exclusion row "I-S fails H2" holds for I-S as written, where `step` is a generic constant in A. It is fragile against I-S′. **The claim that NCE-H is checkable and excludes interpreters is not established.** INFERENCE.

**N5. H3's "S's hypotheses … realised by A's own variables" is already strong.**
- Together with Gardner Cor 5.1.8 (CONFIRMED), it forces an intuitionistic-context A to exclude linear and relevant logics at R2.
- That forces A to natively contain each S's context discipline *before R3 enters*.
- So the "union" conclusion of §6.3 is partly generated by H3 itself, not by the identity requirement. The dilemma is partly circular. INFERENCE.

**N6. Dependent type theories with judgmental computation.**
- Examples are Coq, Lean and Agda, which are central "foundational traditions".
- Under H1 + H2 they need an explicit conversion judgment.
- H3's bijection then concerns derivations that include conversion derivations, which are not the object system's notion of derivation.
- NCE-H thus quietly excludes the main dependent foundations from C. Cost item 1 ("forbids computational reflection") understates this. INFERENCE.

### 2.5 Constructions I-S and I-C

**I-S.** The construction is plausible as an informal argument. I-S is constructed for Hilbert-style S. INFERENCE. Points to tighten:
- The uniqueness of traces needs `Trace` to be indexed by configurations, so that canonical inhabitants are unique.
- Bijection also needs the syntax of formulas (strings vs well-formed formulas) to be adequate. Ill-formed strings are harmless only because the c_i reject them.
- "Rule locality (modulo trace size)": trace size is unbounded in the checker's running time. Under a size-sensitive locality notion, I-S therefore fails H4-like locality. The report notes this.

**I-C.** The construction is correct in outline. INFERENCE.
- A poly-time checker written by structural recursion over constructor data gives an orthogonal, hence confluent, and terminating rule set.
- `IsTrue true ↪ Unit` is type-level rewriting. Subject reduction then needs confluence of β together with R, which holds here, consistent with Dedukti Thm 8 (CONFIRMED in the log as stated).

**Exclusion claims.**
- I-H and I-U are correctly excluded.
- I-R is correctly excluded.
- I-C is excluded by H2 as well as H1. This undermines the motivation for H1 (§2.3).
- The I-S exclusion is fragile (N4).

---

## 3. Is C\* / Gate 0.5 an appropriate test of the original objective?

**R-1. C\* is not an existence statement.**
- It reads "There exists an *existing*, fixed framework A". Existence is about mathematics; "existing" is about the literature.
- A negative Gate 0.5 result says nothing about whether such an A exists. INFERENCE.

**R-2. For any fixed finite benchmark, existence is trivially true without a size measure.**
- Take A = the disjoint union of STLC-βη, the cbn λμ theory (Selinger Table 6) and an MLL⁻ proof-net calculus, each with its own ≡, and encode shallowly.
- This is horn (iii) taken literally.
- It is excluded only by literal H2/H4 (N2), which the report itself intends to relax for (iii), or by "existing".
- Amendment A1 (fix C before A) therefore does **not** remove triviality for finite C. The A1 test, "single-system C must fail", passes, but the union trick defeats the point.
- What is missing is a measure that makes "basis" meaningful, for example:
  - |sig(A)| must be independent of C, with C infinite or parametrised;
  - A must be fixed before an *infinite* class C is given;
  - a description-length or generic-ness criterion.
- This is the true F08/T10 gap. **It is the single decisive missing definition, and the report does not name it.** INFERENCE.

**R-3. The decision rule maps both informative outcomes to "stop".**
- (a) "known": this is charter success criterion (a) ("exact known theorem subsuming the target"). It is also *positive* evidence for existence on B. Stopping there conflates novelty with existence.
- (b) "a specific step fails in CLF/LLF": this is a failure of one framework, and the gate only tests CLF/LLF. Stopping on it upgrades a specific encoding failure (category C) to a program verdict. It could also be an artefact of literal NCE-H (N3).
- Only (c) continues, and only to a tool experiment.
- So the gate cannot yield evidence *against* existence. It can yield only "known", "CLF fails" or "open lemma".

**R-4. B is chosen near known results and is narrow.**
- It omits the traditions that make the charter interesting:
  - set-theoretic (Metamath/Mizar-style first-order ZFC);
  - HOL;
  - dependent type theory with conversion;
  - any cbv or symmetric classical identity.
- Each omission is justified by a boundary condition, but those boundaries partly rest on the overstated U-b and U-c.

**R-5. The test omits candidate unifying calculi** that are the natural "small basis" hypotheses for exactly this B. UNVERIFIED-MEMORY on the precise faithfulness theorems:
- polarised / focused linear logic (Laurent's LLP; Girard's LU);
- call-by-push-value (Levy);
- multi-focusing (Chaudhuri–Miller–Saurin, flagged in U7).

The report does list multi-focusing and Hasegawa CSL 2002 as leads. A discriminating test should ask whether **one** of these generic calculi, with *its* fixed equational theory, faithfully hosts all of B. That would be a "small basis" test. CLF's =c is a poor fit for β/η identities (N3).

**Verdict on question 3.** C\* is a narrowing that, as framed, can return only "already known" or "fails for CLF". It bears on novelty, not existence.

A better Gate 0.5:
1. Define the size or structure measure (R-2) first.
2. Then ask: is there a generic calculus G with fixed ≡_G (a candidate list fixed in advance) such that each S in B embeds faithfully with rule-local, deep-or-shallow encodings?
3. Or prove the N3-type obstruction: rule-local, rule-as-constant encodings reflect only permutation-generated identities.

Either outcome would bear on existence.

---

## 4. Errors, overstatements, internal contradictions, mis-citations

| # | Issue | Label |
|---|---|---|
| E1 | "R5" is undefined (§0(c), §10.1). | CONFIRMED (grep) |
| E2 | The Lemma says "reflects" where it should say "preserves" (§2.1). | INFERENCE (elementary) |
| E3 | CX7 / executive summary: "Hilbert-style S4 is adequately but not naturally representable" overstates Gardner Thm 5.2.11, which concerns "the representation … given in example 5.1.12". Thm 5.2.13 concerns the ND signature for Hilbert PL. | CONFIRMED (log verbatim) |
| E4 | Executive summary on Joyal/Došen drops the naturality hypothesis ("under the CCC-with-initial-object hypotheses"). Naturality (or dinaturality, or the isomorphism 0^(0^A) ≅ A) is required, and it is exactly what control categories drop (Selinger: i_A "not … natural"). | CONFIRMED (log; Selinger PDF) |
| E5 | §2.2 ("true") vs T9 ("no fixed truth value"). | CONFIRMED (internal) |
| E6 | H2 literally excludes HHP's syntax constants and shallow encodings (N1, N2). The inclusion claim for HHP and horn (iii) / C\* are inconsistent with H2 as written. | INFERENCE from the report's text |
| E7 | "Under NCE-H, (ii) is excluded, so R3 needs (iii)" overlooks options (iv) and generic congruences, and overlooks that (iii) violates H2/H4. | INFERENCE |
| E8 | CX5 is presented as an obstruction, but it is complexity-conditional (P ≠ PSPACE), and the report's own U7 undercuts it. C\* boundary condition 1 is therefore unjustified. | CONFIRMED (log) + INFERENCE |
| E9 | CX10 (Σ⁰₁) is presented as an obstruction to decidable finite certificates, but r.e. validity admits decidable certificates once witnesses are attached. | INFERENCE |
| E10 | CX12 (Lafont S[2]) "defeats finite generation under resource discipline". It concerns reversible Boolean circuits under cartesian product. Its relevance to proof algebras is analogical; Lafont's Cor 1 (A[2] finitely generated) and Cor 2 are not mentioned. | CONFIRMED (log) |
| E11 | Akbar Tabatabai–Jalali (F08, U8, bibliography) has **no entry in the evidence log**, contrary to the log README's traceability claim. I independently confirmed arXiv:1808.06258v2, Cor 4.5 ("K4 and S4 lack a terminating single-conclusion or multi-conclusion semi-analytic sequent calculus") and the "except for at most seven" phrasing. The citation is correct but not logged. Chaudhuri–Miller–Saurin and Hasegawa CSL 2002 are also absent from the log; they are correctly flagged UNVERIFIED-MEMORY. | CONFIRMED (my fetch) |
| E12 | Selinger Def 6.2 *defines* cbn equality via CPS images, so CPS faithfulness is definitional. The matrix notes this, but §6.3's counter-consideration and §10.2 cite "Def 6.2 / Prop 6.5 / Thm 6.12" as if faithfulness were the content. The content is the finite axiomatisation (Thm 6.12). This is minor, but it affects whether C\*'s cbn-λμ component is "known" or "true by definition of ~_S". | CONFIRMED (log) |
| E13 | Executive summary (a) lists theory U under "already known" without the non-conservativity caveat (CX13). | CONFIRMED |
| E14 | Executive summary (c) lists "Classical proof identity has no agreed definition" among "established counterexamples". That is absence of a definition, not a counterexample. | CONFIRMED (internal) |
| E15 | Several "VERIFIED_SOURCE" bibliography rows give no "Version read" (for example Selinger, Heijltjes–Houston, Brotherston). The log has the URLs, so this is a presentation gap, not fabrication. | CONFIRMED |

Spot checks that **passed** (CONFIRMED against the log):
- MDT Prop 2.25 and the p. 26 "structurality" open question, including the binder remark.
- Clavel–Meseguer Thm 3.2, with its ground-term and var(t′) ⊆ var(t) hypotheses.
- HHP "thesis" (p. 17) and "not to be confused" (p. 3).
- CLF "catastrophic" and "forces a sequentialization".
- Gardner Cor 5.1.8.
- Heijltjes–Houston Thm 9.1.
- MOTW §8.3 counterexample.
- Selinger Rem 8.2 and Prop 8.1.
- Došen Props 1–3 and the →∧ normalisation/generality disagreement.
- Felicissimo Thm 46.
- Blanqui et al. §4 disclaimer and the 38/28 counts.
- BDKS Cor 6.6.
- Berardi–Tatsuta Thms 8.3 and 8.4.
- The secondary status of Krajíček Thm 8.4.3.

---

## 5. Recommended changes (for the report author; not applied)

1. Rewrite §0(c) and §10.1 using the four-category split in §1.1:
   - keep "impossible" only for (A), with hypotheses stated;
   - state complexity assumptions (P ≠ PSPACE, NP ≠ PSPACE);
   - move CX6, CX7 and Straßburger to "specific failure" or "absence";
   - remove "R5".
2. Change the recommendation from "stop" to "narrow: CV0 ill-posed". Name the missing size or structure measure on A (R-2) as the decisive open definition.
3. Fix the Lemma (preserve, not reflect). Add options (iv) (judgmental identity) and generic congruence to the case split. Split horn (ii) into kinds (α), (β) and (γ).
4. Repair H2 (proof-forming constants; status of auxiliary judgments; whether shallow encodings count). Then either:
   - consider H1-schematic, or
   - justify the H1/H2 asymmetry, noting that I-C already fails H2.
5. Reformulate C\* without "existing". Either:
   - fix a measure and an infinite or parametrised class, or
   - test generic calculi (CBPV, LLP/LU, multi-focused LL) chosen in advance.
   Also consider stating the N3 obstruction conjecture, which is a crisp, plausibly provable statement bearing on existence.
6. Correct CX7 (Gardner) and the CX4 hypothesis wording. Add an evidence-log entry for Akbar Tabatabai–Jalali.
