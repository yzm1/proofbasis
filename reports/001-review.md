# Review of Report 001: mathematical validity of the "stop" verdict

| | |
|---|---|
| **Reviews** | `reports/001-existence-and-novelty.md` (PR #2, commit `cfabb9d`). That report is **not modified** by this review. |
| **Date** | 2026-10-08 |
| **Evidence log** | [`reports/001-review-source-notes/`](001-review-source-notes/) |
| **Status labels** | VERIFIED_SOURCE (passage read in the retrieved text), SECONDARY_ONLY, INFERENCE (reviewer's argument), CONJECTURE, UNKNOWN, UNVERIFIED-MEMORY. Nothing here is formally checked. |

## 0. Disclosure on independence

This review was produced in the **same session, by the same model, that wrote Report 001**. Authorship is therefore not independent. Three things were done to mitigate this:

1. A separate agent with **no access to the author's reasoning** reviewed Report 001 cold against its evidence log and two re-fetched primary sources. Its full critique is `001-review-source-notes/fresh-context-critique.md`.
2. **New primary sources** were retrieved that Report 001 did not consult: generic and modal frameworks, polarization and game semantics, canonical forms and complexity.
3. Decisive passages were re-located by the reviewer in the downloaded texts:
   - Licata–Shulman–Riley p. 25:17 and Conj. 8.5;
   - Laurent 2005 Thm 3;
   - Selinger Def. 2.11;
   - Shulman's "leave cut-elimination for future study";
   - Gratzer Cor. 8.10;
   - Zeilberger's ω-rule remark;
   - Kaposi–Xie's non-definability remark.

A reviewer from outside this session should still re-check §§3–5 before anything here is accepted.

---

## 1. Bottom line

**The negative verdict "stop" is not entailed by the evidence. It mixes four different kinds of result and promotes the weaker ones to "obstruction".**

The evidence does support three things:
- the candidate conjecture CV0 (as written in `docs/DEFINITIONS_AND_CONJECTURES.md`) is ill-posed;
- R0–R1 are known, and vacuous without an anti-vacuity condition;
- R2 is known encoding by encoding.

It does **not** support "uniform R3 is obstructed", and the vacuity–identity dilemma is **not exhaustive**. There is a third route that Report 001 did not search: *generic frameworks*. These have a fixed, small set of generic connectives; each logic is supplied as structural data; and β/η proof identity is derived uniformly. Its central open question, whether the framework *reflects* each encoded logic's proof identity, is stated as an **open conjecture by its own authors** (Licata–Shulman–Riley 2017). That is a live, precise, mathematically meaningful target bearing directly on R3.

**Recommendation:** replace "stop" with **"narrow"**, with corrections (§7). The narrowed target and a better discriminating test are in §6. Whether to *invest* remains a value judgement:
- The narrowed question lies inside an active research programme (Licata, Shulman, Riley, Pfenning, Gratzer and others), so novelty must be assessed against it.
- Report 001's stop recommendation is defensible **only** as a novelty or cost judgement. It should say so explicitly and drop the impossibility framing.

---

## 2. Classifying the evidence

Four kinds of result are in play: proven impossibility, intractability, failure of a specific translation, and absence of a known result. The table records which kind each cited item is, and whether Report 001 promoted it to a stronger kind. Sources are in Report 001's log unless marked †, which means new in this review.

| Item cited in Report 001 | What it actually shows | Kind | Promoted in Report 001? |
|---|---|---|---|
| Joyal / GLT App. B; Došen Props 1–3 | A CCC with initial ⊥ **and** a *natural* ¬¬-elimination (or dinatural excluded middle, or 0^(0^A) ≅ A) is a preorder | **Impossibility, under those hypotheses** | **Yes.** The executive summary drops the naturality hypothesis and says "uniform R3 is obstructed". † Selinger Def 2.11: a control category *is* cartesian closed, with ⅋ only premonoidal and ⊥ initial only in the focal subcategory; Cor 3.8 shows collapse occurs exactly when ⅋ is bifunctorial. Intuitionistic βη and cbn λμ (via CPS) coexist in CCCs. The collapse forbids one *combination of structure*, not a common framework |
| Gardner Cor 5.1.8 | No adequate ELF+ representation of linear or relevant logics | Impossibility, **relative to her definition** (object hypotheses must be framework hypotheses) | Partly. Report 001 does note the definition |
| Gardner Ex 5.2.6 | Prawitz ND-S4 has no natural representation (an example applying to all signatures) | Impossibility, relative to definition | No |
| Gardner Thms 5.2.11, 5.2.13 | *The particular* representation of Ex 5.1.12 is not natural; *the ND signature* is not a natural encoding of Hilbert PL | **Specific-encoding failure** († `canonical-forms-complexity.md`, verbatim OCR) | **Yes.** CX7 and the executive summary say "Hilbert S4 is not naturally representable". A Hilbert signature (K, S, MP constants) would plausibly be natural for Hilbert PL (INFERENCE) |
| Heijltjes–Houston Thm 9.1 | MLL proof equivalence (with units) is PSPACE-complete. Consequence, conditional on P ≠ PSPACE: no *tractable* canonical proof nets | **Intractability** | **Yes.** Listed among "established counterexamples", and C\* treats it as a boundary. † Hughes 2012 Thm 3/4 gives a decidable presentation of free ∗-autonomous categories by rewiring classes: a faithful representation by equivalence classes |
| Statman 1979 († now VERIFIED, scanned journal version); Nguyễn 2023 († Tower-complete for β/βη) | Deciding β(η)-conversion of simply typed terms with redexes is non-elementary | Intractability | n/a. This shows LF-style conversion is *already* far beyond PSPACE, so CX5 cannot be an obstruction to a decidable ≡_A |
| Cyclic validity: PSPACE (µMALL threads, ABSTRACT_ONLY; abstract infinite descent, citing) | No polynomial *local* certificates, unless NP = PSPACE (INFERENCE) | Intractability (conditional); for CLKIDω the lower bound is UNKNOWN | **Yes.** "Local-only R4/R5" is stated without the assumption, and "R5" is undefined in the docs |
| Baelde et al. Cor 6.6 (Σ⁰₁-complete) | Pre-proofs alone are not decidable certificates for one criterion | Undecidability of *one criterion* | **Yes.** Σ⁰₁ means r.e., so pre-proof plus a finite validity witness is a decidable certificate (INFERENCE) |
| Maraist–Odersky–Turner–Wadler §8.3 | Girard's cbv translation from λ_val is not equality-complete | **Specific-translation failure** | **Yes** (CX6). Hasegawa FLOPS 2002 (Prop 5, Thm 1): linear CPS from Moggi's λc is equationally complete and full |
| Cousineau–Dowek non-bijectivity; Felicissimo–Winterhalter Table 1 | Particular encodings lack bijections or proofs | Specific failure / absence of proof | Mostly correctly stated |
| Straßburger "no commonly agreed definition"; MDT "structurality" open; HHP "thesis" | No agreed definition or theorem | **Absence** | **Yes.** Straßburger appears in §0(c) as a "counterexample" |
| Berardi–Tatsuta Thm 8.3 | CLKIDω and LKID have different theorems in general | Impossibility of *one translation goal* (derivability equivalence) | No |
| Lafont Lemma 14 | Reversible Boolean circuits S[2] are not finitely generated | Impossibility in a specific category | Overstated as a general "resource discipline vs finite generation" result. It is an analogy only |

**Net.** Under explicit hypotheses, the category-A results rule out:
- (1) symmetric classical identity coexisting with a CCC-with-initial-⊥ and natural ¬¬-elimination in *one* category;
- (2) direct ELF+-style representation of linear and relevant logic;
- (3) natural representation of Prawitz ND-S4 in ELF+;
- (4) derivability-equivalence of cyclic and inductive systems without arithmetic.

**None of these shows that no fixed finite framework can faithfully represent the proof identities of a nontrivial cross-foundation class.**

---

## 3. The vacuity–identity dilemma (Report 001, §6.3)

### 3.1 The supporting Lemma is mis-stated

INFERENCE (elementary; found by the fresh-context reviewer and re-checked).

Under the Lemma's hypotheses (F_S injective, and ≡_A syntactic on the image), **reflection always holds**: F(d) ≡ F(d′) ⇒ d = d′ ⇒ d ~ d′. It is **preservation** that forces ~_S to be identity.

Corrected, the Lemma states that LF-style bijective adequacy cannot express a nontrivial ~_S. HHP already say this in prose (p. 3). It is a format observation, not an obstruction.

### 3.2 The case split is not exhaustive

Report 001's horns are:
- (i) quotient adequacy;
- (ii) the environment extends ≡_A, called "vacuous";
- (iii) A natively contains each foundation's identity-bearing structure, called "a union of foundations".

Horn (i) is a *format*, not a mechanism. Horn (ii) conflates different kinds of equations. Horn (iii) is described more pessimistically than the evidence allows. The alternatives below were not considered.

**(A) Generic structural frameworks.** This route is neither an interpreter nor a union of independent primitives.

- **Licata–Shulman–Riley, FSCD 2017** (LIPIcs 84, art. 25), † VERIFIED_SOURCE:
  - The framework is fixed, with two generic connectives F and U. Cut and identity are proved once for all mode theories (Thm 2.1).
  - §4 gives a single equational theory on derivations, uniform in the mode theory: "the βη-laws for F and U".
  - Each logic supplies only a **mode theory**: structural data, including equations between mode morphisms and 2-cells.
  - Coverage: single-conclusion substructural and modal logics.
- **Shulman, "LNL polycategories and doctrines of linear logic"**, LMCS 19(2) 2023, † VERIFIED:
  - This extends the generic approach to multiple-conclusion **classical linear** logic.
  - Each logic supplies a "doctrine" of universal properties, and derivation equivalence is generated by generic β and η rules.
- **Pruiksma–Chargin–Pfenning–Reed** (adjoint logic, 2018 manuscript), † VERIFIED: a logic is a preorder of modes plus a structural-property assignment (weakening, contraction). Gives cut elimination and identity expansion; no equational theory.
- **Gratzer–Kavvos–Nuyts–Birkedal**, MTT, LMCS 2021, † VERIFIED: canonicity irrespective of the mode theory (with a technical restriction).
- **Zeilberger 2008** †: connectives are defined by patterns, with generic identity and cut.

Why this escapes both horns:
- The connectives of each logic are **instances** of a fixed generic construction, not independent primitives. So horn (iii) as Report 001 describes it ("union") does not apply.
- The per-logic data does not compute on encoded proofs. So horn (ii)'s vacuity (interpreter) does not apply. INFERENCE.

What is **not** established for this route (VERIFIED_SOURCE for each limit):

- **Reflection of proof identity, i.e. faithfulness of R3, is open.** LSR p. 25:17: "We conjecture that the converse is true … We have sketched a proof of equational adequacy for a simple case (ordered logic products), assuming a lemma …". The extended version states "CONJECTURE 8.5. Completeness of Permutative Equality." **This is a precise, published, open R3 question.**
- **Classical non-linear logic (LK) is not covered natively.**
  - LSR names multi-conclusion logics as future work.
  - Shulman's non-linear objects are single-conclusion (Remark 2.7). That LK is not a native instance is INFERENCE.
  - Shulman also writes: "We leave cut-elimination for future study."
- **Decidability and vacuity move into the structural data.**
  - Licata–Shulman 2016 contemplate mode theories with undecidable equality.
  - Gratzer Cor 8.10: "If modalities and 2-cells enjoy decidable equality, typechecking MTT is decidable."
  - INFERENCE: an arbitrary finitely presented mode theory can carry an undecidable word problem, so an R1-type vacuity may re-enter through structural derivability. The anti-vacuity question becomes a restriction on admissible *structural* data. That question is **open**, not settled either way.
- **Zeilberger's pattern framework** admits infinitary negative rules: "for Nat we essentially have the ω-rule" (F02/F07 risk). Classical logic is reached only through a *choice* among "infinitely many" polarizations.
- **Meta-frameworks for presentations** (Uemura; Kaposi–Xie, FSCD 2024) †:
  - These are exactly horn (ii): β and η are declared per theory.
  - Kaposi–Xie: "substructural (e.g. linear or modal) type theories are not definable as SOGATs" by their method.
  - In their first-order-logic examples proofs are proof-irrelevant.
  - They do not answer R3 for proof-relevant logics.

**(B) Small core with faithful semantics.** Evidence that a fixed universe can be faithful for a nondegenerate classical identity:

- **Laurent, "Syntax vs. semantics: a polarized approach"** (TCS 2005, preprint), † VERIFIED:
  - Thm 3 ("Faithful completeness"): "If R1 and R2 are two cut-free sliced proof-nets such that R⋆1 = R⋆2 then R1 = R2."
  - Thm 2 gives full completeness. Thm 4 gives an equivalence of control categories.
  - Scope: propositional LLpol, which the author says encodes propositional classical logic.
- **de Carvalho–Tortora de Falco 2012 / de Carvalho 2016** †: the relational model is injective for MELL (the 2012 result excludes weakening; the 2016 one covers full MELL).
- **Abramsky–Jagadeesan** (tech report version) †: full and faithful for MLL **with MIX**, without units.

These show that the Joyal-style collapse does not prevent faithful classical semantics. **No source gives one universe proven faithful for classical, intuitionistic and linear logic together.** Melliès–Tabareau † relate the foundations by *equational axioms* over tensor logic (for example, a commutative continuation monad), at provability level only. That is evidence for "small signature + per-foundation equations", which is horn (ii) in its non-vacuous form (see C below).

**(C) Horn (ii) is not intrinsically vacuous.** Three kinds of environment equation must be separated:

| Kind | Example | Vacuous? |
|---|---|---|
| α | Equations computing on encoded data | Yes: interpreter, like I-C |
| β | Schematic laws between proof constructors | No. Preservation holds by declaration, but **reflection (conservativity) is a theorem** that can fail. Felicissimo–Winterhalter Table 1 lists four published encodings with no conservativity proof, three of them not confluent. Felicissimo Thm 46 is a hard-won reflection result |
| γ | Laws derived generically from universal properties | No. This is route A |

NCE-H's H1 forbids β and γ along with α, while H2 permits per-logic *rules* under the same kind of adequacy obligation. The asymmetry is unjustified: construction I-C already fails H2, so H1 is not needed to exclude it.

**(D) Canonical representatives on the object side.**
- Chaudhuri–Miller–Saurin 2008 (Thm 16: bijection with proof nets for unit-free cut-free MLL);
- Scherer POPL 2017 (Cor 7: βη with sums and empty type decidable, via saturation; canonical modulo ≈icc);
- Scherer–Rémy 2015.

All † VERIFIED. These exist **fragment by fragment**, for a chosen and sometimes deliberately weakened identity. For example, CMS08 "decidedly not equating all proofs that are equated in the standard categorical model … ⊤ is no longer a terminal object". Scherer states saturation "would be invalid in … a resource-aware logic". A real but local route.

**(E) Declared identity judgments plus a generic permutation congruence** (fresh-context critique §2.2): ~_S as an inhabited judgment (Pfenning §3.6), or a framework-level permutation congruence (CLF =c). Plausibly covers permutation-type identities; not β/η. INFERENCE.

### 3.3 Verdict on the dilemma

| Claim in Report 001 | Verdict |
|---|---|
| "If E may extend ≡_A, R3 is vacuous" | **Incorrect as stated.** True only for equations of kind α |
| "Otherwise A must natively contain each foundation's structure; universality by inclusion, not by a basis" | **Unsupported.** Generic frameworks (route A) are a counterexample to the *dichotomy*. They are not yet a positive solution, because faithfulness is conjectured (LSR) and LK is not covered |
| Remaining genuine content | Under rule-as-constant, rule-local, fixed-≡ encodings (literal NCE-H), only **permutation-generated** identities can plausibly be reflected; β/η-type identities cannot. This sharper statement (fresh-context critique §2.4 N3) is a **CONJECTURE** worth stating and proving or refuting |

Literal NCE-H is also internally inconsistent:
- H2 excludes HHP's syntax constants and every shallow encoding;
- so horn (iii) is itself excluded by NCE-H, and the inference "(ii) excluded ⇒ (iii)" is incoherent as written.

---

## 4. Is C\* an appropriate test of the original objective?

**No. C\* narrows the question to novelty, not existence.**

1. **C\* asks about an *existing* framework (CLF).** Its outcomes are "known" or "CLF fails". "Known" is the charter's *success* criterion (a) and positive evidence for existence. Gate 0.5 maps both outcomes to "stop", so it cannot produce evidence against existence.
2. **For any fixed finite benchmark, existence is trivial without a size or structure measure.** A disjoint union of the three calculi with their own equalities satisfies it. Report 001's amendment A1 (fix C before A) does not prevent this. **The decisive missing definition is a measure making "basis" meaningful**: for example, A fixed independently of an *infinite or parametrised* class C, as in route A, where A is fixed and C = all logics given by structural data of a stated kind. Report 001 does not name this gap.
3. **Literal NCE-H makes the NJ-βη component of C\* plausibly false by construction** (§3.3). A failure would then be an artefact of the definition.
4. **The benchmark omits the natural "small core" candidates:** generic adjoint or mode frameworks, polarized linear logic (LLP / LLpol), call-by-push-value, and multi-focusing. It also omits the dependent and set-theoretic foundations the charter cares about.

---

## 5. Does the evidence warrant stopping?

INFERENCE, weighed in both directions.

**Against continuing as chartered:**
- R0–R2 are not novel.
- CV0 is ill-posed.
- The word "universal" in the charter conflicts with known limits:
  - infinitary proofs (F07);
  - global validity conditions, costly in general (F05);
  - incompatible classical identities (cbn and cbv differ: Selinger Rem 8.2; symmetric identities are a different family).
- Any fixed A must therefore be faithful to *chosen* identities. This is correctly established by Report 001.

**Against stopping:**
- No impossibility result covers a generic-framework formulation.
- Its decisive R3 question is a stated open conjecture (LSR).
- Its extension to classical logic is partly done (Shulman 2023, classical linear) and partly open (LK with a fixed nondegenerate identity).
- These are legitimate mathematical problems. They are pen-and-paper questions requiring no software.

**Balance.** The evidence supports **"narrow"**. The narrowed problem is *not* the charter's "finite universal algebra" in its original breadth. It is:

> equational adequacy (faithfulness) of a fixed generic framework, over an infinite class of logics given by structural data, plus the question of how far that class can reach toward classical and dependent foundations.

Whether that merits ProofBasis's investment is a strategic call. It requires engaging an active literature, where the most likely contribution is a proof of, or counterexample to, an existing conjecture.

---

## 6. Recommended replacement for C\* and Gate 0.5

**C\*\* (existence-relevant, with a size measure).**
- Fix a generic framework G *before* the class: LSR's framework (single-conclusion) or Shulman's LNL polycategories (multi-conclusion linear).
- Let 𝒦 be an explicitly defined, infinite class of structural specifications: mode theories or doctrines satisfying stated decidability conditions.
- **C\*\*:** for every K ∈ 𝒦 and every pair of derivations d, d′ of an encoded sequent of the object logic L_K:

  > d ~_{L_K} d′ ⇔ ⟦d⟧ ≡_G ⟦d′⟧

  where ~_{L_K} is the standard proof identity of L_K (for example, the free structured category on its generators).

C\*\* is essentially LSR's own equational-adequacy conjecture, generalised to the chosen class. Status: **CONJECTURE (published as open by its proposers)**.

**Single discriminating next test (pen and paper).** Verify or refute Conj. 8.5 ("Completeness of Permutative Equality") of the LSR extended version, for the smallest nontrivial sub-class of 𝒦 beyond their sketched case. For example: the mode theories for intuitionistic linear logic with ⊗ and for S4, compared against the free symmetric monoidal closed category and the standard S4 calculus with its βη identity.

| Outcome | Consequence |
|---|---|
| Proved | Positive evidence that a fixed generic basis faithfully represents proof identity across a class of foundations. Novelty must then be measured against LSR and Shulman |
| Counterexample | A precise obstruction to the generic route. The first genuine category-A result against R3 |
| Stuck | Records exactly which lemma (the subformula-property gap LSR identify) is the barrier |

All three outcomes bear on existence, unlike Gate 0.5.

**Secondary questions to record, not pursue yet:**
- (a) The N3 conjecture: rule-local deep encodings reflect only permutation-generated identities.
- (b) Whether any generic framework hosts LK with Laurent's polarized identity.
- (c) The anti-vacuity restriction on admissible structural data (mode theories with decidable or convergent presentations).

---

## 7. Accept / correct / investigate

| # | Conclusion of Report 001 | Recommendation |
|---|---|---|
| 1 | CV0 is ill-posed (existential C) | **Accept**, but correct "true" to "ill-posed" (§2.2 vs T9 inconsistency) |
| 2 | R0–R1 known; vacuous without anti-vacuity (Clavel–Meseguer Thm 3.2; MDT Prop 2.25; EF+Refl) | **Accept.** † MDT Δ may be infinite and non-recursive (Def 2.22, no restriction): state this |
| 3 | R2 known per encoding; uniform version a "thesis" | **Accept.** Correct §10.1, which says "established" |
| 4 | F03 framing: primitive rules must live in the environment; the trust boundary is an adequacy obligation (CA1) | **Accept**, and extend it to equations (§3.2 C) |
| 5 | "Uniform R3 obstructed" / §0(c) list | **Correct.** Re-sort per §2. Keep only category-A items as obstructions, with hypotheses; state P ≠ PSPACE / NP ≠ PSPACE; delete "R5"; move CX5, CX6, CX7, CX10 and Straßburger out of "counterexamples" |
| 6 | Joyal/Došen as obstruction | **Correct.** Restore naturality; cite Selinger Def 2.11 and Cor 3.8 and Laurent 2005 Thm 3 as showing the collapse is avoidable |
| 7 | CX7 (Gardner) | **Correct** to "the representation of Ex 5.1.12 / the ND signature" |
| 8 | §6.3 Lemma | **Correct** "reflects" to "preserves" |
| 9 | Vacuity–identity dilemma | **Withdraw as a dichotomy.** Restate as: kind-α equations are vacuous; kind-β/γ equations and generic frameworks are live alternatives whose faithfulness is open |
| 10 | NCE-H | **Correct**: H2 should refer to proof-forming constants and address auxiliary judgments (I-S′ variant) and shallow encodings. Justify or drop the H1/H2 asymmetry. **Investigate** whether a restriction on structural data replaces H1 |
| 11 | C\*, Gate 0.5 | **Replace** with C\*\* and the Conj. 8.5 test (§6). Add the missing size/structure measure as amendment A6 |
| 12 | "Stop" | **Replace with "narrow"** and state that any stop is a novelty or cost judgement, not an impossibility result |
| 13 | Prior-art coverage | **Investigate / extend.** Add generic frameworks (LSR, Licata–Shulman, Shulman 2023, adjoint logic, MTT, Zeilberger), polarized semantics (Laurent 2005), relational injectivity (de Carvalho et al.), canonical forms (CMS08, Scherer) |
| 14 | Evidence-log gaps | **Correct**: add a log entry for Akbar Tabatabai–Jalali (confirmed by the fresh-context reviewer at arXiv:1808.06258v2); add "version read" for rows missing it |
| 15 | Not accessed in this review | **Investigate:** Girard LU (APAL 1993) and LC (MSCS 1991) (403 or closed); Fiore–Hur CSL 2010; LICS 2022 version of Gratzer; Mairson 1992; Hofmann–Streicher 2002. The pol agent's claim that free SMCCs embed fully and faithfully into free ∗-autonomous categories is UNVERIFIED-MEMORY |

---

## 8. New sources consulted in this review

Full verbatim extractions are in `001-review-source-notes/`. All entries are VERIFIED_SOURCE in the version stated unless noted.

**Generic frameworks** (`generic-frameworks.md`)
- Licata, Shulman, Riley, "A Fibrational Framework for Substructural and Modal Logics", FSCD 2017, LIPIcs 84, DOI 10.4230/LIPIcs.FSCD.2017.25 (publisher PDF), plus the extended version (author page via Wayback, 2020 copy).
- Licata & Shulman, "Adjoint logic with a 2-category of modes", LFCS 2016 (author preprint).
- Shulman, "LNL polycategories and doctrines of linear logic", LMCS 19(2) 2023 (arXiv:2106.15042v5).
- Pruiksma, Chargin, Pfenning, Reed, "Adjoint logic" (2018 manuscript).
- Gratzer, Kavvos, Nuyts, Birkedal, "Multimodal dependent type theory", LMCS 17(3) 2021; Gratzer, normalization for MTT (arXiv v1).
- Zeilberger, "On the unity of duality" (2008 preprint) and "Focusing and higher-order abstract syntax" (POPL 2008 author copy).
- Uemura, "A general framework for the semantics of type theory" (arXiv v3).
- Kaposi & Xie, "Second-order generalized algebraic theories", FSCD 2024, LIPIcs 299.
- Fiore–Hur 2010: NOT_ACCESSED.

**Polarization and semantics** (`polarization-semantics.md`)
- Selinger, MSCS 11 (2001), Def 2.11, Lemma 2.7, Cor 3.8.
- Laurent, "Syntax vs. semantics: a polarized approach" (TCS 2005 preprint), Thms 2–4.
- Laurent, "Polarized games" (APAL 2004 long version).
- Laurent & Regnier, LICS 2003.
- Melliès & Tabareau, APAL 2010 (preprint).
- Melliès, PRIMS 2016.
- de Carvalho & Tortora de Falco (arXiv:1002.3131); de Carvalho (arXiv:1502.02404).
- Abramsky & Jagadeesan (tech report DoC 92/24, arXiv:1311.6057).
- Hasegawa, "Classical linear logic of implications" (MSCS 2005 preprint).
- Girard LC and LU: NOT_ACCESSED.

**Canonical forms and complexity** (`canonical-forms-complexity.md`)
- Chaudhuri, Miller, Saurin, IFIP TCS 2008 (author copy), plus the CSL 2012 follow-up.
- Scherer, POPL 2017 (arXiv:1610.01213v3).
- Scherer & Rémy, ICFP 2015 (long version).
- Statman, TCS 9 (1979) (scan).
- Nguyễn (arXiv:2305.12601).
- Heijltjes & Houston, LMCS 2016.
- Hughes, JPAA 2012 (arXiv v4).
- Gardner thesis (OCR, re-read).
- Mairson 1992: NOT_ACCESSED.

**Fresh-context critique of Report 001** (`fresh-context-critique.md`): confirms about 15 citations against the log, and identifies errors E1–E15.

---

*This review does not modify Report 001, the charter, or the definitions. It requests that the report's author (and an outside reviewer) adjudicate the corrections in §7.*
