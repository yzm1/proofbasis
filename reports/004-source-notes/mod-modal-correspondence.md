# Notes [mod]: standard translation, correspondence, Sahlqvist, incompleteness, Fine, van Benthem, Jónsson–Tarski, translation-based ATP

Agent tag: mod. Session date 2026-10-08. All downloads in `t004/dl/mod/`. Converted with `pdftotext -layout`.
Nothing downloaded was executed. The git repo was not modified.

## Sources retrieved (with version)

| key | bibliographic data (as printed in the retrieved document) | URL retrieved | version | status |
|---|---|---|---|---|
| BvB | P. Blackburn, J. van Benthem, "Modal Logic: A Semantic Perspective", in *Handbook of Modal Logic* (Blackburn, van Benthem, Wolter eds.), header says "c 2006 Elsevier BV" | https://eprints.illc.uva.nl/id/eprint/205/1/PP-2006-30.text.pdf | ILLC preprint PP-2006-30 (chapter preprint; its page numbers are given below; the published Handbook (2007) pages may differ) | VERIFIED_SOURCE |
| GOL | R. Goldblatt, "Mathematical Modal Logic: A View of its Evolution", *Handbook of the History of Logic* Vol. 7 (Gabbay, Woods eds.), c 2006 Elsevier, 98 pp. (also *J. Applied Logic* 1(5–6):309–392, 2003, according to a PhilArchive search hit only, not checked against the document) | https://homepages.ecs.vuw.ac.nz/~rob/papers/modalhist.pdf | author's manuscript of the Handbook chapter | VERIFIED_SOURCE |
| GHV | R. Goldblatt, I. Hodkinson, Y. Venema, "Erdős graphs resolve Fine's canonicity problem". ILLC PP-2003-26; published *Bull. Symbolic Logic* 10(2):186–208, 2004 (BSL data seen in GOL's bibliography and in a search hit) | https://eprints.illc.uva.nl/id/eprint/110/1/PP-2003-26.text.pdf | preprint (23 pp.) | VERIFIED_SOURCE |
| CGV | W. Conradie, V. Goranko, D. Vakarelov, "Algorithmic correspondence and completeness in modal logic. I. The core algorithm SQEMA", *LMCS* Vol. 2 (1:5) 2006, pp. 1–26 | https://arxiv.org/pdf/cs/0602024v4 | arXiv v4 = LMCS version (header printed) | VERIFIED_SOURCE |
| KUZ | S. Kuznetsov, *Logic II Lecture Notes: Modal Logic*, Univ. of Pennsylvania, Spring 2017 | https://homepage.mi-ras.ru/~sk/lehre/penn2017/lecture_modal.pdf | lecture notes (secondary, not peer-reviewed) | VERIFIED_SOURCE (as secondary) |
| OHL93 | H. J. Ohlbach, "Translation Methods for Non-Classical Logics: An Overview", AAAI Tech. Report FS-93-01, 1993 | https://cdn.aaai.org/Symposia/Fall/1993/FS-93-01/FS93-01-016.pdf | tech report (two-column OCR is garbled; quotes below are reassembled from column fragments) | VERIFIED_SOURCE (partial legibility) |

**NOT ACCESSED:**
- Blackburn, de Rijke, Venema, *Modal Logic* (CUP 2001). No legitimate open copy was found. **All BdRV numbering below is UNVERIFIED-MEMORY.**
- Ohlbach, Nonnengart, de Rijke, Gabbay, "Encoding two-valued nonclassical logics in classical logic", *Handbook of Automated Reasoning* Vol. II, ch. 21, pp. 1403–1486. The bibliographic data comes from search-result snippets only (ACM DL record https://dl.acm.org/doi/10.5555/778522.778530, UvA DARE record). The full text was not retrieved. The MPI-I-93-230 report download failed (connection reset).
- Primary papers: Sahlqvist 1975, Fine 1974/1975, Thomason 1972/1974, van Benthem 1976/1978/1983, Jónsson–Tarski 1951/52. Their statements below are SECONDARY_ONLY (via BvB / GOL / GHV / CGV) unless marked otherwise.
- `logic.amu.edu.pl` mirror of GOL: TLS certificate expired, not used (TLS verification was not disabled).

---

## 1. Standard translation (ST) and frame correspondence

**BvB §2.2 (preprint pp. 10–11). VERIFIED_SOURCE.** This covers the polymodal case, with modalities indexed by m ∈ MOD. Verbatim:
> "ST x (p)= Px; STx (⊥) = ⊥; STx (¬ϕ) = ¬ STx (ϕ); STx (ϕ ∧ ψ) = STx (ϕ) ∧ ST x (ψ); ST x (⟨m⟩ϕ) = ∃y(Rm xy ∧ STy (ϕ)); ST x ([m]ϕ) = ∀y(Rm xy → STy (ϕ))." … "The variable y … is chosen to be any new variable" … "STx (ϕ) always contains exactly one free variable (namely x)."

The target language is the "first-order correspondence language": one binary R_m for each m ∈ MOD and one unary P for each p ∈ PROP.

**BvB Proposition 3 (p. 11), verbatim:**
> "For any basic modal formula ϕ, any model M, and any point w in M we have that M, w |= ϕ iff M |= STx (ϕ)[x ← w]."

Proof given: "immediate by induction".

**BvB p. 11.** Validity is r.e. because "a basic modal formula ϕ is valid iff STx (Σ) is a first-order validity". The text says "STx (Σ)", which looks like a typo for STx(ϕ). This is a statement about K only, i.e. the class of all frames.

**Frame level, BvB §5.3 (p. 37), verbatim:**
> "F |= ϕ(p1 , . . . , pn ) iff F |= ∀P1 · · · Pn ∀xSTx (ϕ)." "frame validity systematically treats modal formulas ϕ as the universal monadic second-order closure of their standard first-order translations".

BvB p. 38 says this second-order detour "is not eliminable". Löb's formula defines transitivity plus converse well-foundedness, "non-elementary, as an appeal to the Compactness Theorem … shows". McKinsey 23p→32p also defines a non-elementary class (by Löwenheim–Skolem).

**KEY RESULT FOR THE PROJECT. BvB Proposition 34 (§5.6, p. 42). VERIFIED_SOURCE, verbatim:**
> "Suppose that F is an elementary class of frames defined by a basic modal formula ϕ. Then the (basic modal) theory of F is recursively enumerable."
> Proof: "ϕ corresponds to some first-order formula α. Now a basic modal formula ψ is valid on frames for ϕ iff … α |= ∀P1 · · · Pn ∀xSTx (ψ) … as α is first-order, the predicates P1 · · · Pn do not occur in α and hence this is equivalent to α |= ∀xSTx (ψ). But this is a first-order entailment".

Note the hypothesis. This is about the *frame theory* of F, not about the axiomatic logic. The two coincide only if the logic is complete for F.

**Negative result, BvB p. 42:** "once we move beyond the elementary frame classes, even recursive enumerability is lost". Thomason [114] (S.K. Thomason, "Reduction of second-order logic to modal logic", ZML 21:107–114, 1975) reduces second-order consequence to global frame consequence for one modality, so "global frame consequence is not recursively enumerable". This is SECONDARY_ONLY for Thomason 1975.

**Undecidability of correspondence, BvB p. 39:** "Chagrova [19] shows that the problem of determining whether a modal formula expresses a first-order condition on frames is undecidable." SECONDARY_ONLY for Chagrova. CGV ref [3] gives: Chagrova, "An undecidable problem in correspondence theory", JSL 56:1261–1272, 1991.

**BvB Theorem 32 (p. 39):** "A modal formula defines a first-order frame property iff it is preserved under taking ultrapowers of frames." Attributed to van Benthem [119]. SECONDARY_ONLY.

**BdRV numbering (UNVERIFIED-MEMORY):** Def 2.45 (standard translation), Prop 2.47 (local equivalence), Prop 3.12 (second-order frame correspondence). These were not checked.

## 2. Sahlqvist's theorem

**Bibliographic data, VERIFIED in GOL and BvB bibliographies:** H. Sahlqvist, "Completeness and correspondence in the first and second order semantics for modal logic", in S. Kanger (ed.), *Proceedings of the Third Scandinavian Logic Symposium* (Uppsala 1973), North-Holland, 1975, pp. 110–143.
- *Discrepancy:* CGV ref [21] prints the title as "Correspondence and completeness …". GOL and BvB both print "Completeness and correspondence …".

**(a) Correspondence.**

BvB Theorem 31 (pp. 38–39), VERIFIED_SOURCE, verbatim:
> "There is an effective method for computing first-order equivalents for Sahlqvist formulas, that is, formulas of the form ϕ → ψ with antecedents ϕ constructed from atoms (possibly prefixed by boxes) using conjunctions, disjunctions and diamonds, while consequents ψ can be any modal formula with only positive occurrences of proposition symbols."

The method is the "substitution algorithm" (van Benthem). The heart of the proof: "a Sahlqvist antecedent is true under any value for its proposition symbols iff it is true under its minimal values."
- This is a simplified handbook statement. Negative formulas in antecedents and box-closure are omitted.
- Limitation stated in BvB: K4.1 = (2p→22p)∧(23p→32p) is first-order (transitive and atomic) "but this first-order equivalence cannot be computed using the substitution method".

GOL §6.3 (p. 52), VERIFIED_SOURCE. GOL's paraphrase of Sahlqvist's own class: formulas "2^n(α → β) where n ≥ 0, β is positive, and α is constructed from propositional variables and/or their negations using only ∧, ∨, 3, 2 in such a way that no positive occurrence of a variable is in a subformula that has ∧, ∨, or 3 within the scope of a 2". GOL continues:
> "He proved that the class of frames validating such a formula is definable by an explicit first-order sentence, and that this basic elementary class characterises the normal logic axiomatised by adding the formula to K."

Extensions named by GOL: polymodal and BAO equations (Sambin–Vaccaro 1989; Jónsson 1994; de Rijke–Venema 1995; Givant–Venema 1999).

CGV §5.1 (pp. 19–20), VERIFIED_SOURCE. Definitions: boxed atom; Sahlqvist antecedent "built up from ⊤, ⊥, boxed atoms, and negative formulae, using ∧, ∨ and diamonds"; Sahlqvist implication "ϕ → Pos"; Sahlqvist formula "built up from Sahlqvist implications by applying conjunctions, disjunctions, and boxes". Their statement of the theorem:
> "Sahlqvist's theorem [21] states that all Sahlqvist formulae are elementary and canonical."

**Local correspondence. CGV Theorem 4.15, VERIFIED_SOURCE:**
> "If SQEMA succeeds on a formula ϕ ∈ ML, then ϕ is locally d-persistent and hence canonical, and moreover the first-order formula returned by SQEMA is a local equivalent of ϕ."

CGV Theorem 5.4: "SQEMA succeeds on every Sahlqvist formula." Together these give the local-correspondence and canonicity version of Sahlqvist's theorem. That combination is formally checked by nobody; it is a published proof.

CGV p. 18 (Def 4.1 context):
> "(local) d-persistence implies canonicity of formulae in ML because the canonical general frame for every normal modal logic is descriptive".

**(b) Completeness and canonicity.**
- Verified statements: GOL ("characterises the normal logic axiomatised by adding the formula to K") and CGV ("elementary and canonical").
- The BdRV formulation, Theorem 4.42, "Every Sahlqvist formula is canonical; K⊕Σ is strongly complete w.r.t. the elementary class defined by the first-order correspondents of Σ", is **UNVERIFIED-MEMORY**: the number and the exact wording were not seen. The strong-completeness form follows from canonicity, since canonical logics are strongly complete with respect to their canonical frame (standard; memory).
- Likewise Thm 3.54 (correspondence) is UNVERIFIED-MEMORY.

## 3. Kripke incompleteness and general frames

**BvB Theorem 26 (p. 34), VERIFIED_SOURCE, verbatim:**
> "Let TMEQ be the normal modal logic obtained by enriching K with all instances of the following schemas: ϕ → 3ϕ (T), 23ϕ → 32ϕ (M), 3(3ϕ ∧ 2ψ) → 2(3ϕ ∨ 2ϕ) (E), and (3ϕ ∧ 2(ϕ → 2ϕ)) → ϕ (Q). There is no class of frames that validates precisely the formulas in TMEQ."

Proof: "See van Benthem [117]", i.e. "Two simple incomplete modal logics", Theoria 44:25–37, 1978. This is finitely axiomatised: 4 schemas.

**GOL §6.1 (pp. 45–46), VERIFIED_SOURCE.**
- "The first example of an incomplete logic was devised by Steven Thomason [1972b]". This is a tense logic; "Thomason's logic is not valid on any frame whatsoever! … But it is not itself inconsistent".
- "The first incomplete 2-logics were found by Thomason [1974a] and Kit Fine [1974] … Later van Benthem [1978; 1979] found some simpler ones. The simplest unearthed to date is the normal logic with axiom 2(2p ↔ p) → 2p." Every frame validating it validates W (Berk), but W is not a theorem (Magari), with proofs in Boolos–Sambin 1985.
- Blok: "'most' logics Λ are not characterised by any class of frames". Also: "every normal logic is either of degree 1 or of degree 2^ℵ0" (Blok 1978). Both SECONDARY_ONLY.

**Bibliographic data (from GOL bibliography):**
- Thomason 1974a, "An incompleteness theorem in modal logic", *Theoria* 40:30–34, 1974.
- Fine 1974, "An incomplete logic containing S4", *Theoria* 40:23–29.
- van Benthem 1978, *Theoria* 44:25–37.
- Thomason 1972b, "Semantic analysis of tense logic", *JSL* 37:150–158, 1972.
- **Discrepancy:** BvB ref [113] gives Thomason 1974 as "Theoria, 40:150–158". That page range coincides with Thomason 1972b in JSL, and Fine 1974 occupies pp. 23–29 of the same Theoria volume. GOL's 40:30–34 is more plausible. This should be checked against the journal before citing.

**General frames, GOL §6.5 (p. 56), VERIFIED_SOURCE:**
> "Thomason [1972b] … defined a 'first-order semantics' using structures S = (K, R, P), where P is a collection of subsets of K that forms a subalgebra of the full complex algebra Cm(K, R). … Validity in S is defined as truth in all models M = (S, Φ) on S satisfying the constraint that the set M(p) … belongs to P".

The descriptive frames are "dually equivalent to Malg" (Goldblatt 1974).

The exact statement "every normal modal logic is sound and complete w.r.t. a class of general frames" was **not found verbatim** in retrieved texts. It is UNVERIFIED-MEMORY (BdRV Thm 5.? on general frames). It follows from the two verified facts below together with Jónsson–Tarski (§7):
- BvB p. 68: "any axiomatic extension of K (that is, any normal modal) is complete with respect with some class of algebras", via the Lindenbaum–Tarski algebra.
- CGV p. 18: "the canonical general frame for every normal modal logic is descriptive".

**Important caveat, GOL p. 45, VERIFIED:**
> "every normal logic is complete with respect to C = {SΛ} … Whether or not Λ is sound with respect to SΛ is an important issue".

So "complete w.r.t. canonical frame" is trivial; soundness (canonicity) is the content.

## 4. Fine's theorem, its failed converse, GL and McKinsey

**Fine 1975b data (GOL bibliography):** K. Fine, "Some connections between elementary and modal logic", in S. Kanger (ed.), *Proc. Third Scandinavian Logic Symposium*, North-Holland, 1975, pp. 15–31.

**GOL §6.6 (p. 58), VERIFIED_SOURCE, verbatim:**
> "A logic Λ is called canonical if it is valid in its canonical frame SΛ … (i) If the class Fr(Λ) of all Λ-frames is closed under elementary equivalence and characterises Λ (i.e. Λ is complete), then Λ is canonical. (ii) If Λ is elementary (i.e. characterised by some elementary class), then Λ is canonical."

Fine actually proved η-canonicity for all ordinals η. Remark 3.8 of GHV notes that Fine worked monomodally but "his results can be readily extended to polymodal logics".

**GHV §1 (preprint p. 2), VERIFIED, verbatim:** "(1) if a modal logic is determined by some elementary class of frames, then it is validated by its canonical frames."

**Strengthening, GOL p. 61 (verbatim, citing Goldblatt 1993, 11.4.2):** "If a modal logic Λ is characterized by some elementary class of frames, then it is characterized by the elementary class of all models of the quasi-modal first-order theory ΨΛ (which includes all the canonical frames of Λ)."

**Converse fails.**
- GHV abstract, VERIFIED: "exhibiting a bimodal logic that is valid in its canonical frames, but is not sound and complete for any first-order definable class of Kripke frames".
- GHV Lemma 3.5: "The logic EG is canonical."
- GHV Lemma 3.6: "EG is not sound and complete for any elementary class of frames."
- GHV Lemma 3.7: EG "has the finite model property and, for a suitable choice of the Gn, is decidable".
- GHV Theorem 2.19: "There are 2^ℵ0 distinct canonical varieties of L-BAOs with the finite algebra property and not elementarily generated."
- GHV Remark 3.8: the monomodal version follows via Thomason simulation (Kracht–Wolter).
- GOL p. 61: these logics include "undecidable logics with decidable sets of axioms".

**GL (Gödel–Löb).**
- Löb's formula defines a non-elementary frame class (BvB p. 38, VERIFIED).
- KUZ §4 (p. 4), VERIFIED as secondary, verbatim: GL is "an example of a non-canonical (but yet Kripke complete) normal modal logic". The proof uses x0 = {A | N ⊨ A*} (arithmetical realisation in a sound T) as a reflexive point of the canonical frame.
- GOL p. 42: K4W "is characterised by the class of finite frames (K, R) in which R is transitive and irreflexive" (Segerberg 1971).
- *Consequence, by contraposition of Fine (ii) (an informal inference, but immediate):* GL is not characterised by any elementary class of frames. GL is Kripke-complete yet has no first-order frame environment.
- BdRV location of "GL not canonical" (Example 4.? / Exercise): UNVERIFIED-MEMORY.

**McKinsey (GOL p. 52, VERIFIED):** "no elementary class can characterise the logic K+M". The class of M-frames is not elementary (Goldblatt 1974 §17). Yet Fine 1975a: K+M "has the finite model property … and is characterised by its (finite) validating frames". GOL p. 60: "The McKinsey axiom 23p → 32p was shown not to be canonical in [Goldblatt, 1991a]".

## 5. van Benthem characterization theorem

**BvB Definition 12 and Theorem 13 (p. 21), VERIFIED_SOURCE, verbatim:**
> "A first-order formula ϕ(x) is invariant for bisimulation if for all models M and M′, and all points w in M and w′ in M′, and all bisimulations E between M and M′ such that wEw′, we have that M |= ϕ[x ← w] iff M′ |= ϕ[x ← w′]."
> "THEOREM 13 (Modal Characterisation Theorem). The following are equivalent for all first-order formulas ϕ(x) in one free variable x: 1. ϕ(x) is invariant for bisimulation. 2. ϕ(x) is equivalent to the standard translation of a basic model formula."

- Original sources: van Benthem PhD thesis 1976 and *Modal Logic and Classical Logic*, Bibliopolis 1983. SECONDARY_ONLY.
- Rosen: the theorem holds over finite models. Otto: the modal equivalent can be chosen with depth 2^k (BvB p. 21).
- This is a **model-level** result. At frame level modal logic is a fragment of monadic second-order logic (BvB p. 32).
- Related: Goldblatt–Thomason Theorem (BvB Thm 33): "A first-order frame property is modally definable iff it is preserved under taking disjoint unions, generated subframes, p-morphic images, and reflects ultrafilter extensions."

## 6. Translation-based approaches (Ohlbach et al.)

The handbook chapter is NOT ACCESSED, so its exact theorem statements are not available. What was verified in OHL93 (1993 overview; OCR garbled, fragments reassembled):
- Setting: "The logic we want to develop a translator for has to be presented by means of a possible worlds semantics." The frame properties are "given directly or … specified implicitly with Hilbert axioms".
- Relational translation: "Taking the standard 'relational' semantics for the connectives … yields a translation function which, due to the new R-literals, destroys the structure of the formulae. Moreover, the transformation into conjunctive normal form may duplicate these extra R-literals exponentially often." This is relevant to F09.
- Functional translation: an order-sorted logic with a sort W, sorts AF_n of accessibility functions, and a predicate "def" for the non-serial case. "It can be shown that this translation preserves satisfiability. A modal formula has a model if and only if the translated formula has a first-order predicate logic model. This is sufficient for doing refutational theorem proving."
- Soundness and completeness proofs are deferred: "The exact formalisms and the soundness and completeness proofs can be found in the original papers."
- SCAN (§4): "correct in the sense that its result is really equivalent to the input formula. It cannot be complete … Completeness is not possible, otherwise the theory of arithmetic would be enumerable."

From search snippet only (SECONDARY_ONLY): the chapter has sections on standard relational, functional and semi-functional translations.

The usual hypothesis is that the logic is complete for a first-order-definable frame class, with the frame axioms added as first-order background theory (my reading, UNVERIFIED-MEMORY for the chapter's wording).

## 7. Jónsson–Tarski

Data (GOL bibliography, VERIFIED):
- Part I: *Amer. J. Math.* 73:891–939, **1951**.
- Part II: *Amer. J. Math.* 74:127–162, 1952.
- *Discrepancy:* BvB ref [67] dates Part I to 1952.

**GOL §3.3 (p. 18), VERIFIED_SOURCE:**
> "The Extension Theorem of Jónsson and Tarski showed that any BAO A can be embedded isomorphically into a complete and atomic BAO Aσ which they called a perfect extension of A."
> "Combining the Extension Theorem with the representation of a complete atomic algebra (like Aσ) as one of the form Cm S, Jónsson and Tarski established that every BAO with normal operators is isomorphic to a subalgebra of the complex algebra of a relational structure."

GOL §6.5 (p. 56): "EmA = Cm CstA … is isomorphic to the perfect extension Aσ … The Jónsson–Tarski representation of A amounts to the fact that there is an injective homomorphism A ↣ EmA." Cst A has as points the ultrafilters of A.

GOL §6.6 (pp. 59–60): "if C is any class of relational structures … closed under ultraproducts, then the variety of BAO's generated by … CmC is closed under canonical embedding algebras" (Goldblatt 1989, Thm 3.6.7).

BvB §7.1 (p. 68), VERIFIED: Theorem 55, K-theorems are exactly the formulas evaluating to 1 in all modal algebras. BvB also anticipates the objection: "Isn't the whole approach really just syntax in disguise?"

---

## Status summary

| claim | status |
|---|---|
| ST definition + Prop 3 (local equivalence) | VERIFIED_SOURCE (BvB) |
| Frame validity = ∀P̄∀x ST (MSO) | VERIFIED_SOURCE (BvB) |
| Elementary-definable ⇒ frame theory is FO consequence α ⊨ ∀x ST(ψ) | VERIFIED_SOURCE (BvB Prop 34) |
| Sahlqvist correspondence (effective; local) | VERIFIED via BvB Thm 31, CGV Thm 4.15+5.4; original SECONDARY_ONLY |
| Sahlqvist completeness/canonicity | VERIFIED via GOL and CGV statements; BdRV 4.42 wording UNVERIFIED-MEMORY |
| Kripke-incomplete finitely axiomatised logics exist (TMEQ; 2(2p↔p)→2p) | VERIFIED_SOURCE (BvB Thm 26; GOL) as citations; originals SECONDARY_ONLY |
| Fine: elementary ⇒ canonical | VERIFIED via GOL and GHV; original SECONDARY_ONLY |
| Converse false (EG; 2^ℵ0 examples) | VERIFIED_SOURCE (GHV preprint) |
| GL not canonical, Kripke complete; hence not elementarily characterised | non-canonicity VERIFIED in lecture notes (KUZ, secondary); corollary is an informal inference |
| K+M not elementarily characterised; M not canonical | VERIFIED via GOL (secondary for Goldblatt 1974/1991a) |
| van Benthem characterization | VERIFIED_SOURCE (BvB Thm 13); original SECONDARY_ONLY |
| Jónsson–Tarski | VERIFIED via GOL; original SECONDARY_ONLY |
| General-frame completeness for all normal logics | UNVERIFIED-MEMORY as stated (pieces verified) |
| Ohlbach et al. 2001 handbook claims | NOT_ACCESSED; 1993 overview partially VERIFIED |

## INFERENCE: relevance to the threats (my reading)

- **F01 (already solved), positive part.** For any normal (poly)modal logic Λ characterised by an elementary class axiomatised by Γ_FO (e.g. all Sahlqvist-axiomatised logics), we get Λ ⊢ ψ iff Γ_FO ⊨ ∀x ST_x(ψ) iff Γ_FO ⊢_FOL ∀x ST_x(ψ). This combines BvB Prop 34 with completeness and FOL completeness.
  - This is a fixed FOL core with a first-order environment that preserves and reflects *theoremhood*, and it is textbook (1975–1983).
  - It gives nothing about proof identity, local consequence vs. global rules, or proof size. None of these sources address proof identity at all.
- **Boundary 1 (Kripke incompleteness).** TMEQ, Thomason/Fine logics and 2(2p↔p)→2p have no frame class at all. A frame-condition environment necessarily over-approximates them, so reflection fails.
- **Boundary 2 (complete but non-elementary).** GL and K+M are complete yet have no elementary characterising class. GL fails because it is not canonical; Fine's theorem makes that decisive. Any FOL environment of frame conditions is then unsound or incomplete.
  - Caveat: one could still encode GL into FOL in other ways, e.g. via arithmetic or via finite-frame/fmp-based methods. That is not a "canonical ST + frame conditions" translation.
- **Boundary 3 (EG).** Canonicity is *not* sufficient for an FO frame environment (GHV). The boundary of the ST+FO-env method is exactly "elementarily characterised". Fine's theorem shows this lies inside "canonical", strictly (GHV). Membership is not decidable from the axioms; Chagrova shows FO-definability of a formula is undecidable, and that bears on this.
- **F02/F03 escape hatch.** Every normal modal logic does embed faithfully into FOL via its algebraic or general-frame semantics. Examples: equational logic of BAOs with Λ's axioms as equations (BvB Thm 55 + remark), or two-sorted FO over general frames with admissible-set quantifiers.
  - In these the environment contains the axioms of Λ themselves (schemas become universally quantified statements over the algebra or admissible sets).
  - That is the "syntax in disguise" worry BvB voice (p. 69), i.e. F03.
  - So "FOL is universal for normal modal logics" is trivially true in this weak sense. It is only non-trivial if the environment is restricted to first-order conditions on the *standard* (Kripke) semantics, and then it fails (incomplete and non-elementary logics).
- **F09.** The relational ST blows up clause form ("exponentially often", OHL93). The functional translation fixes this only for certain classes (serial; otherwise "def" literals). Second-order quantifier elimination (SCAN) is necessarily incomplete.
