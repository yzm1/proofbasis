# pid — Proof identity, proof nets, global correctness (F04, F05; also F01/F09)

Agent tag: pid. Downloads: `scratchpad/dl/pid/` (pdftotext; scanned PDFs read as rendered page images).
Status labels follow PROTOCOL.md. All quotes below were read in the retrieved text this session unless marked otherwise.

---

## S1. The "Joyal collapse" (CCC + initial object + classical negation is a preorder)

### S1a. Lambek & Scott, *Introduction to Higher Order Categorical Logic*, CUP 1986
- Status: **NOT_ACCESSED** (no open copy retrieved). Location known only **SECONDARY_ONLY**:
  - Došen 2003 (S5 below) says: "In [32] the discovery of that fact is credited to Joyal (p. 116), and the fact is established (on p. 67, Proposition 8.3) by relying on a proposition of Freyd (see [20], p. 7, Proposition 1.12)". [32] = Lambek & Scott 1986.
  - Girard–Lafont–Taylor (S1b) cite "[LamSco] page 67".
  - Selinger 2001 (S9) cites "(Lambek and Scott 1986, p.67)" for: in a bicartesian closed category there is no arrow A → 0 unless A ≅ 0.
  - So: statement at L&S Part I, p. 67, Prop. 8.3; attribution to Joyal at p. 116 — **three independent secondary sources agree on p.67**; p.116 / Prop 8.3 from Došen only. Not verified against the book.

### S1b. Girard, Lafont, Taylor, *Proofs and Types*, CUP 1989 (web reprint 2003)
- URL: https://www.paultaylor.eu/stable/prot.pdf (web reprint "Reprinted for the Web 2003"; printed page numbers).
- Status: VERIFIED_SOURCE. Appendix B (Lafont), §B.1, printed p. 151:
  - "More generally, all the proofs of a given sequent A ⊢ B are identified. So classical logic is inconsistent, not from a logical viewpoint (⊥ is not provable), but from an algorithmic one. This is also expressed by the fact (noticed by Joyal) that any Cartesian closed category with an initial object 0 such that 0^(0^A) ≃ A is a poset (see [LamSco] page 67)."
  - Then: "Of course, our example shows that cut elimination in sequent calculus does not satisfy the Church-Rosser property ... There are two options to eliminate this pathology: • making the calculus asymmetric: this leads to intuitionistic logic; • forbidding structural rules, except the exchange which is harmless: this leads to linear logic."
- Hypotheses: CCC; initial object 0; A ≅ (A⇒0)⇒0 for all A (iso, not merely a map). Conclusion: poset/preorder (at most one arrow per hom-set). The sequent-calculus version (Lafont's weak-weak example) assumes: cut elimination is a congruence/confluent and weak;contr is identified with identity.

### S1c. Došen's simpler proof + variants (S5) — strongest form found
- Došen 2003, §5 (arXiv v12 pp. 17–18), VERIFIED_SOURCE:
  - "Proposition 1. In every cartesian closed category with an initial object ⊥ we have that Hom(A, ⊥) is either empty or a singleton." (proof via π¹ = π² : ⊥×⊥ → ⊥).
  - "Proposition 2. Every cartesian closed category with an initial object ⊥ in which we have a natural transformation whose components are ζ_A : ¬¬A → A is a preorder." (only a *natural* ¬¬-elimination, not an iso, is needed.)
  - "Proposition 3. Every bicartesian closed category in which we have a dinatural transformation whose components are ξ_A : ⊤ → A + ¬A is a preorder."
  - "If classical logic requires A ≅ ¬¬A for every proposition A, then the proof theory of that logic is trivial: there is at most one proof with given assumptions and a given conclusion."
  - Escape routes he notes: "All these considerations involve an initial object ⊥. In the absence of the initiality of ⊥, matters stand better." Double-negation translation into minimal logic gives nontrivial classical proof theory.
- Selinger 2001 Corollary 3.8 (VERIFIED_SOURCE, MSCS 11, p. 13 of PDF): "A control category in which ⅋ is bifunctorial is equivalent to a boolean algebra." — i.e. control categories avoid collapse precisely by keeping ⅋ only premonoidal (non-central maps).
- Lamarche & Straßburger TLCA'05 (VERIFIED_SOURCE, final version PDF p.2, p.14): "if we try to extend naively these semantics to classical logic, it is well-known that everything collapses to a poset (a Boolean algebra, naturally)"; and "it is by now clear that the reason that we do not have collapse to a poset is that the families (Δ_A)_A and (!_A)_A are not natural."
- Straßburger RR-6013 §5 p.58–59 (VERIFIED_SOURCE): "if we do this we get a collapse: all proofs of the same formula are identified ... This observation is due to André Joyal, and a detailed proof and discussion can be found in [LS86] and in the appendix of [Gir91]." [Note: survey writes Gir91 for the appendix; the appendix with Lafont's argument is GLT89 App. B, which the survey also cites in the next sentence.]

**Relevance (INFERENCE):** F04 is *established* in a strong form: no category of proofs can simultaneously be CCC-with-initial-object (i.e. keep intuitionistic βη proof identity incl. ⊥ initial) and have natural classical double-negation elimination / excluded middle, without collapse. Any "declared proof-identity congruence" for classical logic must drop some of: CCC axioms, initiality of ⊥, naturality of Δ/!/¬¬-elim, or ∧/∨ duality. Existing nontrivial classical identities (λμ/control categories; Boolean categories/proof nets; combinatorial proofs) make *different* choices, so a single universal R3 congruence that restricts to the standard intuitionistic one on intuitionistic proofs AND to a symmetric classical one is ruled out by these theorems (for the "symmetric + CCC" combination).

---

## S2. Heijltjes & Houston — MLL with units

- Retrieved: journal version **"Proof equivalence in MLL is PSPACE-complete"**, Logical Methods in Computer Science 12(1:2) 2016, pp. 1–34, DOI:10.2168/LMCS-12(1:2)2016 (printed on PDF). URL: https://arxiv.org/pdf/1510.06178. The LICS/CSL 2014 conference version "No proof nets for MLL with units: Proof equivalence in MLL is PSPACE-complete" is cited as [HH14] in it — conference version itself **NOT_ACCESSED**.
- Status: VERIFIED_SOURCE (journal version).
- Problem definition (Abstract): "MLL proof equivalence is the problem of deciding whether two proofs in multiplicative linear logic are related by a series of inference permutations. It is also known as the word problem for ∗-autonomous categories."
- "Theorem 9.1. MLL proof equivalence is PSPACE-complete." (§9, p.32)
- Consequence (Abstract): "the existence of a satisfactory notion of proof nets for MLL with units is ruled out (under current complexity assumptions). The PSPACE-hardness result extends to equivalence of normal forms in MELL without units".
- Precise form (§1, p.2): "We show that the corresponding decision procedure for MLL with units is PSPACE-complete, which is generally supposed to preclude the existence of a polynomial-time algorithm for this problem. So there can be no canonical proof nets in the usual sense: if the proof nets are syntactically equal just when their corresponding proofs are equivalent, then the translation from proofs to proof nets must be intractable." Hypothesis implicit: P ≠ PSPACE.
- Also: "equivalence of cut-free MELL proofs is PSPACE-hard. This is in sharp contrast with many intuitionistic calculi such as the simply typed lambda-calculus, where normal forms are unique."
- Contrast (§3): "For MLL without units, Girard's original proof nets [Gir87] are canonical ... the translation from proofs to proof nets and the syntactic comparison of proof nets are both effectively computable (linear-time)".

**Relevance (INFERENCE):** F09/F04/R3: even for a tiny fragment (MLL with units), deciding the standard categorical proof identity (free ∗-autonomous category) is PSPACE-complete, so a "finite algebra with a declared identity congruence" that is *canonical* (normal forms compared syntactically) and polynomially computable cannot exist for MLL+units unless P = PSPACE. R3 "reflect identity" via syntactic equality is complexity-obstructed.

---

## S3. Hughes & van Glabbeek — MALL proof nets

### S3a. "Proof Nets for Unit-free Multiplicative-Additive Linear Logic", ACM TOCL 6(4), 2005
- Retrieved: http://boole.stanford.edu/pub/mall.pdf — author-hosted version; no journal header/DOI seen on PDF; treat as preprint-equivalent; journal bibliographic data from HH16 reference list ("ACM Transactions on Computational Logic, 6(4), 2005").
- Status: VERIFIED_SOURCE (author version).
- Abstract: "A cornerstone of the theory of proof nets for unit-free multiplicative linear logic (MLL) is the abstract representation of cut-free proofs modulo inessential rule commutation. The only known extension to additives, based on monomial weights, fails to preserve this key feature ... We present a new definition of MALL proof net which remains faithful to the cornerstone of the MLL theory."
- §4: "(K) Kernel. Does the kernel exactly characterise proof equivalence modulo rule commutation? We answer both in the affirmative ... In a sibling paper we show that any two cut-free MALL proofs are equal modulo rule commutation if and only if they map to the same proof net (see Section 4.11)." — i.e. the canonicity theorem is **deferred to a sibling paper** in the 2005 article.
- Theorem 4.18 (Cut-free sequentialisation): "A set of linkings is the translation of a proof if and only if it is a proof net" (stated p.~20 of this version). Correctness = resolution + MLL + toggling conditions (global, quantified over additive resolutions / sets of linkings).

### S3b. van Glabbeek & Hughes, "MALL proof nets identify proofs modulo rule commutation", arXiv:1609.04693 (2016)
- Status: VERIFIED_SOURCE (arXiv preprint; venue not printed on PDF).
- "THEOREM 1 Two MALL− proofs translate to the same proof net if and only if they can be converted into each other by a series of rule commutations." (MALL− = cut-free MALL without units; "valid for MALL− with and without mix").
- "THEOREM 2 Two MALL proofs are proof-net equivalent if and only if they can be converted into each other by a series of rule commutations." where "proof-net equivalence be the smallest equivalence relation on MALL proofs such that proofs that have a common translation are equivalent" — with cut, it's the equivalence *generated* by common translation (not plain equality of nets).

**Relevance (INFERENCE):** positive example of a canonical identity (rule-commutation) with a geometric representation, but only unit-free; identity = rule commutation, not cut-elimination/βη; adding units breaks canonicity (S2).

---

## S4. Correctness criteria are global (F05)

### S4a. Girard, "Linear logic", TCS 50 (1987) 1–102
- URL: http://girard.perso.math.cnrs.fr/linear.pdf (scan of journal issue; no text layer — read as page images, PDF pp. 33–36, 79–83 → printed pp. 32–35, 78–82).
- Status: VERIFIED_SOURCE (visual reading of scanned pages).
- §2.4 Definition (p.33): "A proof-structure is said to be a proof-net when it admits no shorttrip." Trips defined (§2.2(iii), p.32) by setting "the switches of all par and times links on arbitrary positions (so there are 2^n possibilities if n is the number of switches)"; longtrip = trip of length 2p visiting all formulas in both directions.
- **§2.6 Remark (p.33):** "Checking that a proof-structure has no shorttrip requires looking at 2^n different cases. This number can be decreased to 2^(n−1) ... Anyway, the soundness condition is not feasible. However, it is not part of our intentions to check soundness by concrete means. The proof-nets we shall deal with in practice will all come from sequent calculus or will be obtained from other proof-nets by means of transitions preserving the soundness condition. Hence, the soundness condition is an abstract notion (just like, say, semantic soundness)".
- Thm 2.7 (proof → proof-net, MLL without cut); Remark 2.8: "The transformation π ↦ π⁻ identifies proofs which differ by the order of rules"; Thm 2.9 (p.35): "If β is a proof-net, one can find a proof π in sequent calculus such that β = π⁻." — "the converse is a very subtle result."

### S4b. Danos & Regnier, "The structure of multiplicatives", Arch. Math. Logic 28 (1989)
- Status: **NOT_ACCESSED**. SECONDARY_ONLY via Straßburger RR-6013:
  - "2.5.3 Definition ... A switching for π is a graph obtained from π by removing for every ⅋-node one of the two edges connecting it to its children." "2.5.4 Definition A pre-proof net obeys the switching criterion (or, shortly, is correct) iff all its switchings are connected and acyclic." "2.5.5 Theorem A pre-proof net is correct if and only if it is sequentializable." Attribution (p.~?, notes to §2): "The switching criterion ... is due to Danos and Regnier [DR89]."
  - Complexity (RR-6013 §2.5): "The naive implementation of checking the switching criterion needs exponential time ... checking the RB-criterion needs only quadratic runtime ... it can be done in linear time in the size of the net" (Guerrini, "Correctness of multiplicative proof nets is linear", LICS 1999 — cited, NOT_ACCESSED). "Unfortunately, MLL− is (so far) the only logic (except some variants of it), for which this ideal of proof nets is reached."
  - For simple classical proof nets (RR-6013 §5.3): "Checking their correctness takes exponential time, which is not faster than trying to prove the conclusion from scratch."
- **Nuance for F05 (INFERENCE):** correctness is a global property (quantified over all switchings; acyclicity+connectedness of whole graph) but for MLL− it is *decidable in linear time* — global ≠ infeasible. For classical "simple nets" (sets of axiom links) correctness is coNP-hard in nature (it amounts to tautology checking — my inference; the survey only says "exponential time"). No source read states a formal theorem "correctness is not locally checkable"; that phrase is NOT found. What IS found: Girard's own statement that the criterion is "not feasible" by naive checking and is "an abstract notion".

### S4c. Hughes, "Proofs Without Syntax", Annals of Math. 164 (2006)
- Retrieved: arXiv:math/0408282v3 (6-page version; header "To appear in Annals of Mathematics. Submitted 20 Aug 2004, accepted 9 Sep 2005"). Journal page numbers NOT seen.
- Status: VERIFIED_SOURCE (arXiv version).
- "It defines a combinatorial proof of a proposition φ as a graph homomorphism h : C → G(φ) ... The main theorem is soundness and completeness: φ is true iff there exists a combinatorial proof h : C → G(φ)."
- "Each condition can be checked in polynomial time, so combinatorial proofs constitute a formal proof system [CR79]." and "There is a polynomial-time computable function taking a propositional sequent calculus proof of φ with n ≥ 0 cut rules [Gen35] to a combinatorial proof of φ with n cuts".
- Proof identity: the arXiv text does **not** state a theorem characterizing which syntactic proofs map to the same combinatorial proof. (Hughes, "Towards Hilbert's 24th problem: combinatorial proof invariants", WoLLIC 2006 — UNVERIFIED-MEMORY, NOT_ACCESSED.)
- Relevance (INFERENCE): shows a non-syntactic classical proof representation that is globally defined (skew fibration, cograph) yet polytime-checkable; identity it induces is not the λμ/CPS one.

---

## S5. Došen, "Identity of proofs based on normalization and generality", BSL 9(4) 2003
- Retrieved: arXiv:math/0208094v12 (4 Feb 2004). Journal pagination NOT seen. Status: VERIFIED_SOURCE.
- Normalization Conjecture (Prawitz, credit to Martin-Löf): "Two derivations represent the same proof if and only if they are equivalent." (equivalence = generated by reductions to normal form).
- Generality Conjecture (Lambek): "two derivations represent the same proof if and only if they are equivalent in the new sense" (same generality); formalised as faithful functor G from syntactic category K to graphical category G: "(∗) f = g in K if and only if G(f) = G(g) in G."
- Abstract: "These two proposals proved to be extensionally equivalent only for limited fragments of logic." "In classical logic, however, it [normalization] did not fare well."
- Disagreements: "in the presence of ⊤ and ⊥ the two conjectures do not agree, since normalization does not deliver the assumption concerning the two injections." "The Normalization Conjecture and the Generality Conjecture do not agree for the conjunction-implication fragment of intuitionistic logic. ... Both the soundness part and the completeness part of coherence fail for cartesian closed categories." Cause: contraction (example λx⟨x,x⟩(λy y) = ⟨λy y, λz z⟩).
- Maximality: for cartesian (and products+coproducts) categories, any extra equation collapses to preorder ("Post completeness"); for CCC via typed Böhm theorem; "maximality of bicartesian closed categories ... is, as far as I know, an open problem."
- Classical collapse: Props 1–3 (see S1c).

**Relevance (INFERENCE):** F04 even *within one foundation*: two standard identity criteria differ already for intuitionistic →∧. A "declared identity congruence" is a choice, not a given; maximality results mean one cannot add identifications freely to unify.

---

## S6. Straßburger, "Proof Nets and the Identity of Proofs", INRIA RR-6013, Oct 2006 (arXiv cs/0610123v2)
- Status: VERIFIED_SOURCE (arXiv = RR version; page numbers are RR pages).
- p.~3 (§1): "For propositional intuitionistic logic on the one side, and Cartesian closed categories on the other side, the two notions coincide. Similarly, by using *-autonomous categories, one can make the two notions coincide for linear logic ... But for classical logic ... neither notion has a commonly agreed definition (see Section 5)."
- §5 pp. 59–60: two approaches. "1. The first says that the axioms of cartesian closed categories are essential ... Instead, one sacrifices the duality between ∧ and ∨ ... Parigot's λμ-calculus ... category theoretical axiomatization [Sel01] ... it is not clear how they can be used to identify proofs in various deductive systems for classical logic (sequent calculus, resolution, tableaux, ...)." "2. The second approach considers the perfect symmetry between ∧ and ∨ ... the axioms of cartesian closed categories and the close relation to the λ-calculus have to be sacrificed. It is much less clear ... what the category theoretical axiomatization [DP04, FP04, LS05a, McK05, Str05b, Lam06] should be".
- §5.3: "for classical logic the answer to the Big Question 2.7.9 ... is no longer an obvious yes. In fact, the answer might be No!" "5.3.3 Open Research Problem Make a nice theory out of this mess."
- MLL with units (§3, near line "no canonical place"): units have "no canonical place" for attachment (detail in [LS06]).
- Conservativity remark (§3.4): "This can be used to prove that IMLL− is a conservative extension of MLL−, i.e., an IMLL− formula is provable in IMLL− if and only if it is provable in MLL−." [sic — direction as printed; content is provability-level]. Footnote 19: "This is not true for full intuitionistic linear logic with respect to linear logic." — provability-level only.

## S7. Lamarche & Straßburger, "Naming Proofs in Classical Propositional Logic", TLCA'05 (LNCS 3461)
- URL: https://www.lix.polytechnique.fr/~lutz/papers/namingproofsCL.pdf ("January 31, 2005 — Final version, appearing in proceedings of TLCA'05"). Status: VERIFIED_SOURCE.
- Thm 3.1 (Soundness) / 3.2 (Sequentialization: "a simple CLi-net (i.e., W = B) is sequentializable in CLi"); Thm 5.4 "On B-nets cut elimination via → is strongly normalizing." CLB0/CLB2 categories; "It is not hard to show that we do get a *-autonomous category ... but not one that has units in general"; "it does not seem that the categories proposed in [9] [Došen–Petrić, Proof-Theoretical Coherence 2004] can be *-autonomous without being posets." ; non-naturality of Δ, ! explains non-collapse (quoted in S1c); B-nets give idempotent sum f+f=f.
- Relevance (INFERENCE): this classical identity identifies proofs differently from λμ/control categories (sacrifices naturality of contraction/weakening and CCC); it is an incompatible choice with S9.

## S8. Guglielmi; Bruscoli–Guglielmi (deep inference)
- Guglielmi, "A System of Interaction and Structure", ACM TOCL 8(1:1) 2007, pp. 1–64 (arXiv cs/9910023v4; header "27 January 2007, ACM Transactions on Computational Logic, Vol. 8 (1:1)"). VERIFIED_SOURCE. Abstract: BV "extends multiplicative linear logic by a non-commutative self-dual logical operator. This extension is particularly challenging for the sequent calculus, and so far it is not achieved therein." Intro: "Alwen Tiu will show why BV cannot be defined in any sequent system [35, 36]" — Tiu's result itself NOT_ACCESSED (SECONDARY_ONLY).
- Bruscoli & Guglielmi, "On the Proof Complexity of Deep Inference", ACM TOCL 10(2:14) 2009, pp. 1–34, doi 10.1145/1462179.1462186 (printed in arXiv:0709.1201v3). VERIFIED_SOURCE. Abstract: "1) deep-inference proof systems are as powerful as Frege ones, even when both are extended with the Tseitin extension rule or with the substitution rule; 2) there are analytic deep-inference proof systems that exhibit an exponential speedup over analytic Gentzen proof systems that they polynomially simulate."
- Relevance (INFERENCE): F08/F09 — choice of formalism (shallow vs deep) changes both expressibility (BV) and proof size exponentially; a fixed basis cannot be neutral w.r.t. size.

---

## S9. F04 cross-foundation translations and proof identity

### S9a. Selinger, "Control Categories and Duality: on the Categorical Semantics of the Lambda-Mu Calculus", MSCS 11 (2001) 207–260
- URL: https://www.mathstat.dal.ca/~selinger/papers/control.pdf (journal-formatted PDF with MSCS header). Status: VERIFIED_SOURCE.
- Abstract: "We prove, via a categorical structure theorem, that the categorical semantics is equivalent to a CPS semantics in the style of Hofmann and Streicher. We show that the call-by-name λμ-calculus forms an internal language for control categories, and that the call-by-value λμ-calculus forms an internal language for the dual co-control categories. As a corollary ... there exist syntactic translations between call-by-name and call-by-value which are mutually inverse and which preserve the operational semantics."
- "Theorem 3.18 (Structure Theorem). Any control category P is equivalent to a category of continuations R^C." (equivalence of categories; proof via functor that is "full and faithful" and essentially onto objects).
- "Proposition 6.5 (Soundness and Completeness). The theories induced on the λμ-calculus by the call-by-name categorical interpretation are precisely the theories induced by the call-by-name CPS translation."
- "Theorem 6.12 (Axiomatization of call-by-name λμ-theories). ... T is a call-by-name theory if and only if it is a congruence relation on terms that satisfies the equations in Table 6." (Theorem 7.16 = call-by-value analogue.)
- "Proposition 8.1. Both translations preserve CPS transforms, and thus the categorical semantics, up to natural isomorphism of types. It follows that the two translations are mutually inverse ... M =n μα.L⟨|M|⟩α M∗ and M =v μα.⟨|LM Mα|⟩∗, up to natural isomorphisms of types."
- Corollary 3.8 (collapse if ⅋ bifunctorial — S1c). Remark 8.2: CBV and CBN λμ have *different* equational theories (let-commutation valid in CBN, not CBV; dual for μ-lets).
- What is preserved/reflected: CPS translation reflects AND preserves equations (completeness: theories coincide), and CBN↔CBV duality is an isomorphism *between λμ calculi with disjunction*, up to type isomorphism. Not a translation between λμ and the symmetric (Boolean-category) identities.

### S9b. Hasegawa, "Girard translation and logical predicates", J. Functional Programming 10(1):77–89, 2000
- URL: https://www.kurims.kyoto-u.ac.jp/~hassei/papers/girard.pdf (preprint "Under consideration for publication in J. Functional Programming"; read as page images p.1–2). Status: VERIFIED_SOURCE (preprint).
- Abstract: "We present a short proof of a folklore result: the Girard translation from the simply typed lambda calculus to the linear lambda calculus is fully complete."
- p.1: "The soundness and conservativity of Girard translation, not just at the provability (types) level but also the proofs (terms) level, are widely known" (citing Danos et al. 1995; Benton et al. 1993a — NOT_ACCESSED). Full completeness statement: "Let Γ be a context and σ a type of the simply typed lambda calculus, and suppose that Γ°; ∅ ⊢ M : σ° is derivable in the linear lambda calculus. Then there exists Γ ⊢ N : σ derivable in the simply typed lambda calculus such that Γ°; ∅ ⊢ M = N° : σ° holds." (Theorem 5.6). Scope: →, ⊸, ! only (minimal setting; DILL target).
- p.2: "This seems to be folklore among specialists, though we are not aware of this result explicitly mentioned in the literature."

### S9c. Hasegawa, "Linearly used effects: monadic and CPS transformations into the linear lambda calculus", FLOPS 2002, LNCS 2441, 167–182
- URL: https://www.kurims.kyoto-u.ac.jp/~hassei/papers/flops02.pdf. Status: VERIFIED_SOURCE.
- "Proposition 5 (equational completeness of Sabry and Felleisen [16]). Γ ⊢ M = N : σ holds in the computational lambda calculus if and only if Γ°; ∅ ⊢ M° = N° : (σ° → o) ⊸ o holds in the linear lambda calculus."
- "Theorem 1 (full completeness of the CPS transform). Given Γ°; ∅ ⊢ N : (σ° → o) ⊸ o in the linear lambda calculus, we have Γ ⊢ M : σ in the computational lambda calculus such that Γ°; ∅ ⊢ N = M° : (σ° → o) ⊸ o."
- §1.3: the standard CBV CPS into simply typed λ "has been shown to be equationally sound and complete (Sabry and Felleisen [16]), it is not full: there are inhabitants of the interpreted types which are not in the image of the transformation."

### S9d. Girard 1987 §5.1 (VERIFIED_SOURCE, scanned pp. 78–82)
- Translation (·)⁰: A⇒B = (!A)⊸B, A∨B = (!A)⊕(!B), ¬A = (!A)⊸0, etc.; extended to proofs case by case.
- Remark p.81: "Observe that our translation is faithful in the sense that if A⁰ is provable in linear logic, A is provable in intuitionistic logic." — **"faithful" here = provability reflection only.** "The translation is sound, not only for provability, but also w.r.t. the coherent semantics." Alternative translation (A* = !A for atoms, (A⇒B)* = !(A*⊸B*), ...) p.82: "This translation is not sound w.r.t. the coherent semantics and this is enough to show that its interest is limited."

**Relevance (INFERENCE) for F04:**
- *Positive / F01-threat:* For specific pairs there ARE translations that preserve and reflect standard proof equality and are full: STLC → linear λ (Girard translation, Hasegawa 2000); computational λ (CBV) → linear λ via linear CPS (Hasegawa 2002); λμ CBN ↔ CPS/control categories, CBN ↔ CBV duality (Selinger 2001). These are "embedding a foundation's proof identity into another" results, and should be cited as prior art for R3 preservation+reflection.
- *Negative:* (i) the classical identity they transport is the **asymmetric** λμ/CPS identity; the symmetric (∧/∨-dual) classical identities (Lamarche–Straßburger, Došen–Petrić, Führmann–Pym) are of a different kind and the collapse theorems show both cannot coexist with CCC+initial ⊥; (ii) CBN and CBV λμ have different equational theories (Selinger Remark 8.2), so even "classical λμ" has ≥2 incompatible identities; translations between them exist only with type-isomorphism twists and dualization; (iii) Girard's other ("boring") translation is not sound for coherent semantics, so faithfulness on proofs depends on the chosen translation; (iv) Došen: normalization vs generality identities already disagree for intuitionistic →∧.
- No source found that gives a single translation preserving AND reflecting identity between intuitionistic CCC identity and a symmetric classical identity; collapse theorems suggest none exists with the standard hypotheses (INFERENCE).

---

## NOT_ACCESSED / unverified
- Lambek & Scott 1986 (p.67 Prop 8.3; p.116 Joyal credit — secondary only).
- Danos & Regnier 1989 (secondary via Straßburger).
- Heijltjes & Houston LICS/CSL 2014 conference version (journal LMCS 2016 read instead).
- Guerrini LICS 1999 (linear-time MLL correctness) — secondary only.
- Tiu, SIS II (BV not sequent-definable) — secondary only.
- Bellin–Hyland–Robinson–Urban TCS 2006; Führmann–Pym; Došen–Petrić "Proof-Theoretical Coherence" — not retrieved.
- Hughes "Towards Hilbert's 24th problem" — UNVERIFIED-MEMORY.
- Annals journal version of Proofs Without Syntax (page numbers) — arXiv only.
- Sabry & Felleisen equational completeness of CPS; Hofmann–Streicher — cited via Hasegawa/Selinger only.
