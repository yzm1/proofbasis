# fam — Relational semantics, standard translations, Sahlqvist/inductive theory for NON-classical families

Agent tag: fam. Download dir: t004/dl/fam/. All quotes below are from texts retrieved in this session unless labelled
UNVERIFIED-MEMORY or SECONDARY_ONLY.

## S1. Conradie & Palmigiano, "Algorithmic correspondence and canonicity for non-distributive logics"
- Venue: Annals of Pure and Applied Logic 170 (2019) (journal data SECONDARY_ONLY: per WebSearch result
  "Annals of Pure and Applied Logic 170(9)" and per CPZ 2019 ref [17] which gives only "Annals of Pure and Applied Logic").
- Retrieved: https://arxiv.org/pdf/1603.08515 = arXiv:1603.08515v2 [math.LO], 4 Apr 2016 (PREPRINT; page numbers = preprint).
- Status: VERIFIED_SOURCE (preprint).
- Setting (Def 1.1, p.4): "a lattice expansion (abbreviated as LE) is a tuple A = (L, F^A, G^A) such that L is a bounded
  lattice ... An LE is normal if every f^A ∈ F^A (resp. g^A ∈ G^A) preserves finite (hence also empty) joins (resp. meets)
  in each coordinate with ε_f(i) = 1 (resp. ε_g(i) = 1) and reverses finite (hence also empty) meets (resp. joins) in each
  coordinate with ε_f(i) = ∂". 
- Logic (Def 1.2, p.5): basic L_LE-logic is a set of SEQUENTS φ ⊢ ψ with lattice axioms, normality axioms for each
  connective, closed under cut, uniform substitution, ∧R/∨L and monotonicity/antitonicity rules. "For any LE-language
  L_LE, by an LE-logic we understand any axiomatic extension of the basic L_LE-logic in L_LE."
  NOTE (inference): NO weakening/contraction/exchange — only non-distributive lattice + residuated-type ops; FL formulas:
  "F := {◦} with n◦ = 2, ε◦ = (1, 1) and G = {\, /} with n\ = n/ = 2, ε\ = (∂, 1) and ε/ = (1, ∂)" (p.4).
- Coverage claim (abstract, p.1): "state-of-the-art correspondence theory for many well known substructural logics, such
  as the Lambek calculus and its extensions, the Lambek-Grishin calculus, the logic of (not necessarily distributive) de
  Morgan lattices, and the multiplicative-additive fragment of linear logic." Intro p.3: also "the axiomatic extensions
  of basic orthomodular logic". Exponentials: not mentioned anywhere (grep "exponential": 0 hits). 
- Relational semantics = RS-frames (two-sorted). Def 2.1 (p.10): "A polarity is a triple (X, Y, R) where X and Y are
  non-empty sets and R ⊆ X × Y is a binary relation." Def 2.2: RS-polarity = separating + reduced. Def 2.3 (p.13):
  RS-frame for LML = RS-polarity plus additional relations (incl. ternary R◦ ⊆ Y×X×X) "satisfying additional
  compatibility conditions guaranteeing that the operations associated with the relations in R map Galois-stable sets to
  Galois-stable sets. Because the specifics of the compatibility conditions play no role in the development of the
  present paper, we will not discuss them."
- Propositions = PAIRS OF GALOIS-STABLE SETS (Def 2.4, p.14): "V maps any p ∈ PROP to a pair V(p) = (P1, P2) such that
  P1 ⊆ X, P2 ⊆ Y and moreover u(P1) = P2 and ℓ(P2) = P1." Satisfaction (x ⊩ φ) and co-satisfaction (y ≻ φ) by
  simultaneous recursion; e.g. "M, x ⊩ φ ∨ ψ iff for all y ∈ Y, if M, y ≻ φ ∨ ψ, then xRy" (non-local disjunction).
- Standard translation (§2.1.2, p.15): "each RS-model M for LML can be seen as a two-sorted first-order structure ...
  Let L1 be the two-sorted first-order language with equality built over ... individual variables X and Y, with binary
  relation symbols ≤, R◇, R□, ..., ternary relation symbols R◦, R⋆ and two unary predicate symbols P1, P2 for each
  propositional variable". Lemma 2.5.4: "F ⊩ φ ≤ ψ iff F |= ∀P∀j∀m∀x∀y[(STx(φ) ∧ STy(ψ)) → xRy]".
  CAVEAT stated in footnote 11 (p.15): "the interpretation of pairs (P1, P2) of predicate symbols is restricted to such
  pairs of Galois-stable sets, and hence the interpretation of universal second-order quantification is also restricted
  to range over such sets." (So frame validity is a restricted Π^1_1 statement; first-order only after ALBA succeeds.)
- Syntactic classes: Def 3.4 (Inductive inequalities, p.22-23): "An inequality s ≤ t is (Ω, ε)-inductive if the signed
  generation trees +s and −t are (Ω, ε)-inductive. An inequality s ≤ t is inductive if it is (Ω, ε)-inductive for some Ω
  and ε." Def 3.5: ε-Sahlqvist "if every ε-critical branch is excellent".
- Main theorems (verbatim):
  * Thm 6.1 (Correctness, p.34): "If ALBA succeeds in reducing an L_LE-inequality φ ≤ ψ and yields ALBA(φ ≤ ψ), then
    A |= φ ≤ ψ iff A |= ALBA(φ ≤ ψ)." (A a fixed PERFECT L_LE-algebra.)
  * Thm 7.1 (p.37): "All L_LE-inequalities on which ALBA succeeds pivotally are canonical."
  * Thm 8.8 (p.~41): "ALBA succeeds on all inductive inequalities, and pivotal executions suffice."
  * Packaging (Example 2.6, p.15): "The theory developed in the present paper (cf. Theorems 6.1 and 7.1) guarantees that
    the LE-logic obtained by adding p ≤ ◇p to the basic logic L_LML ... is sound and complete w.r.t. the elementary class
    of RS-frames for LML defined by the sentence above."
- Self-stated limitations: §7 p.36: "the logics of the present paper do not have a single, established relational
  semantics and, moreover, the available options for relational semantics are rather involved." Intro p.2: "for many
  logics, like substructural logics, this is not the case [uniquely established set-based semantics]". Example 2.7 +
  p.16: the published duality result for MALL in Coumans–Gehrke–van Rooijen [15, Theorem 15] "does not hold as stated"
  (a correspondent was computed relative to a strictly smaller frame class); amended via ALBA (m⊥⊥ ≤ m).
  Second alternative semantics: TiRS-frames (one-sorted, Ploščica-style, finite case; §2.2) needing two standard
  translations ST(+), ST(−).
- Proof identity: NOT addressed (pure consequence/validity of sequents; algebraic semantics identifies interderivable
  formulas only).
- Relevance (INFERENCE): For the whole LE-family (FL and Lambek variants w/o structural rules, Lambek–Grishin, MALL
  without exponentials, ortho/orthomodular), there IS a fixed target (two-sorted FOL over polarity-based frames) and a
  uniform canonical translation; the environment contains only first-order frame conditions for inductive axioms. But:
  (a) it reaches only inductive extensions, (b) the base frame class conditions (compatibility) are left unspecified in
  this paper, (c) derivability-level only (R1), nothing on R2–R4; (d) the "translation" quantifies over Galois-stable
  predicates, so it is not plain FOL validity until correspondents are computed. Bears on F01 (partial prior solution
  of the derivability-level question) and F04 (no proof identity).

## S2. Conradie & Palmigiano, "Constructive canonicity of inductive inequalities"
- LMCS 16(3:8) 2020, DOI:10.23638/LMCS-16(3:8)2020 (printed on retrieved doc). Retrieved https://arxiv.org/pdf/1603.08341
  (file is the LMCS-formatted version). VERIFIED_SOURCE.
- Abstract: "We prove the canonicity of inductive inequalities in a constructive meta-theory, for classes of logics
  algebraically captured by varieties of normal and regular lattice expansions. This result encompasses Ghilardi-Meloni's
  and Suzuki's constructive canonicity results for Sahlqvist formulas and inequalities".
- Theorem 7.8 (Main): "All inductive L_LE-inequalities are constructively canonical."
- Note p.2: Ghilardi–Meloni [31] (APAL 86(1):1–32, 1997) did constructive canonical extension "for certain
  bi-intuitionistic modal algebras" (SECONDARY_ONLY for G-M content).
- Relevance (INFERENCE): canonicity holds without choice, but constructive canonical extensions need not be perfect, so
  this does NOT by itself give Kripke(-RS) completeness constructively.

## S3. Gehrke, Nagahashi, Venema, "A Sahlqvist theorem for distributive modal logic"
- Retrieved https://eprints.illc.uva.nl/id/document/174 = ILLC Prepublication PP-2002-09, dated "September 9, 2002"
  (PREPRINT; journal version APAL 131 (2005) not seen: SECONDARY_ONLY/UNVERIFIED-MEMORY for journal data).
  VERIFIED_SOURCE (preprint).
- Language: DML = {∨,∧,⊤,⊥} + ◇, □, ▷, ◁ (no implication). Def 2.4: frame F = (W, ≤, R◇, R□, R▷, R◁), ≤ partial order,
  with first-order interaction conditions (KF) "≤ ◦ R◇ ◦ ≤ ⊆ R◇, ≥ ◦ R□ ◦ ≥ ⊆ R□, ...". Valuations: "Such a valuation
  is called persistent if V(x) is downward closed for each variable x" — propositions = DOWN-closed sets (convention).
  ◇, □ standard Kripke clauses; "M, w ⊩ ▷α iff for all v with wR▷v we have M, v ⊮ α".
- Def 3.4: ε-left/right Sahlqvist; "A distributive modal logic Λ is said to be Sahlqvist provided there is a set Γ of
  Sahlqvist sequents so that Λ = K.Γ."
- Thm 3.6 "(Canonicity for Sahlqvist DML) Every Sahlqvist distributive modal logic is canonical, and hence, complete."
  Thm 3.7 "(Correspondence for Sahlqvist DML) Every Sahlqvist modal sequent corresponds to a formula in the first order
  language of frames for distributive modal logic. This first order formula can be effectively computed from the modal
  sequent." Thm 3.8 "(Sahlqvist Completeness Theorem for DML) Every Sahlqvist distributive modal logic K.Γ is sound and
  complete with respect to the elementary class of frames defined by the (set of) first-order correspondents of the
  axioms Γ."
- Proof method: correspondence by REDUCTION TO CLASSICAL modal case via Gödel-style translation (§4, p.19-20).
- Self-stated limitation (p.38-39): intuitionistic implication NOT treated: "Heyting implication is a binary dual
  operator ... fewer formulas will be 'Sahlqvist' because these basic operations may be non-smooth, that is, their σ-
  and their π-extensions may not agree. In fact, one may show, cf. [20], that this is exactly what happens for the
  implication in most infinite Heyting algebras".

## S4. Conradie, Palmigiano, Zhao, "Sahlqvist via translation"
- LMCS 15(1:15) 2019, DOI:10.23638/LMCS-15(1:15)2019 (printed). Retrieved https://arxiv.org/pdf/1603.08220 (LMCS-formatted).
  VERIFIED_SOURCE.
- Abstract: the general (unified-correspondence) definition of Sahlqvist/inductive inequalities "covers in particular all
  (bi-)intuitionistic modal logics"; "we prove the transfer of the correspondence theorem for inductive inequalities of
  arbitrary signatures of normal distributive lattice expansions. We also prove the transfer of canonicity for inductive
  inequalities, but only restricted to arbitrary normal modal expansions of bi-intuitionistic logic."
- Thm 6.1 "(Correspondence via translation). The correspondence theorem for inductive L◦-inequalities transfers to
  inductive L-inequalities." Thm 7.1 "(Canonicity via translation). The canonicity theorem for inductive
  L◦BAE-inequalities transfers to inductive LbHAE-inequalities."
- Prop 3.1 (GMT, intuitionistic Kripke frames = posets, persistent valuations): "For every intuitionistic formula φ and
  every partial order F = (W, ≤), F ⊩ φ iff F ⊩* τ(φ)."
- History §3.1 (SECONDARY_ONLY for underlying claims): Dummett–Lemmon 1959 extended faithfulness of GMT "to all
  intermediate logics"; Blok/Esakia 1976 lattice isomorphism intermediate logics ≅ normal extensions of Grz; Chagrov–
  Zakharyaschev 1989–92 preservation of "Kripke and Hallden completeness" etc.; Wolter–Zakharyaschev transfer of
  canonicity/Kripke completeness for intuitionistic modal logics.
- Relevance (INFERENCE): for intermediate logics, unified correspondence (Heyting → as normal g-connective of order type
  (∂,1)) gives inductive intermediate axioms elementary + canonical over posets; canonicity covered here via bi-Heyting
  transfer. (Heyting algebras embed in bi-Heyting? Only perfect ones are bi-Heyting; I did not verify how CPZ handle
  plain HA — see their Cor 5.3/Prop 5.4 "For every Heyting algebra A, there exists a Boolean algebra B" — I read only
  the statement header.)
  UPDATE after reading §7.2 of CPZ: "The proof strategy of this result does not generalize successfully to DLE-logics
  or, indeed, to intuitionistic or co-intuitionistic modal logics." (§7 intro, p.15:28). They then give "a more refined
  argument" (Lemma 7.3, Prop 7.4) for the left-hand side; I did not read its conclusion. Example 2.1: "The formulas of
  intuitionistic logic are obtained by instantiating F := ∅ and G := {→} with n→ = 2, and ε→ = (∂, 1)." So IPC and its
  axiomatic extensions ARE DLE-logics in the unified-correspondence sense. Direct (non-translation) canonicity of
  inductive Heyting inequalities: claimed for DLEs in Conradie–Palmigiano 2012 [10] per S1 intro ("intuitionistic and
  distributive lattice-based (normal modal) logics [10]") — SECONDARY_ONLY (I did not access CP 2012). Also, since a
  Heyting algebra is in particular a normal LE (bounded lattice + → of order type (∂,1) that is meet-preserving in 2nd /
  join-reversing in 1st coordinate), S1 Thm 7.1+8.8 apply to inductive inequalities in the signature {∧,∨,⊤,⊥,→} over
  LE-algebras — my INFERENCE, not stated in S1 for Heyting explicitly.

## S5. Litak, "A continuum of incomplete intermediate logics" (corrected version)
- Retrieved https://arxiv.org/pdf/1808.06284 (arXiv:1808.06284v1, 20 Aug 2018; corrected version of Reports on Math.
  Logic 36 (2002) 131–141 per its own note). VERIFIED_SOURCE.
- Def 3: Kripke model = poset frame + "a function B from the set of propositional variables to the set of upward closed
  subsets of W."
- Corollary 7 "(Shehtman) An intermediate logic L determined by axioms δ, κ, and bb2 is incomplete." (incomplete = not
  the logic of any class of Kripke frames; cites [Sh77] V.B. Shehtman, "On Incomplete Propositional Logics", Soviet
  Mathematics Doklady 18:985–989, 1977 — Sh77 itself NOT_ACCESSED).
- Theorem 11: "Distinct subsets of natural numbers generate distinct intermediate logics whose axioms are δ, κ, bb2 and
  the Jankov formulas of those frames from the sequence whose indices belong to a given subset of ω. All of these logics
  are incomplete." (=> continuum many Kripke-incomplete intermediate logics.)
- Author's caveat: the proof of Theorem 5 in the 2002 version "was incorrect"; main Theorem 11 "seems unassailable";
  proof "is fixable". Theorem 1: "A logic L lacks ac-approximability iff its modal companion above Grz τL is incomplete."
- Also stated: "the incompleteness of a modal logic does not imply the incompleteness of its intuitionistic equivalent."
- Relevance (INFERENCE): boundary result for any "canonical relational translation into FOL" approach — for these
  intermediate logics, NO class of posets (elementary or not) yields completeness; the standard translation into FOL
  over any frame class is unsound-for-reflection (R1 reflect fails). F01/F05-type boundary.

## S6. Kuznetsov, "Relational models for the Lambek calculus with intersection and constants"
- LMCS 19(4:32) 2023, DOI:10.46298/LMCS-19(4:32)2023 (printed). Retrieved https://lmcs.episciences.org/12708/pdf.
  VERIFIED_SOURCE. R-models: formulas interpreted as BINARY RELATIONS on W (sets of pairs); · = composition.
- Cites [AM94] "Hajnal Andréka and Szabolcs Mikulás. Lambek calculus and its relational semantics: completeness and
  incompleteness. Journal of Logic, Language, and Information, 3(1):1–37, 1994. doi:10.1007/BF01066355." (AM94 itself
  NOT_ACCESSED; statements below SECONDARY_ONLY via Kuznetsov):
  * "Theorem 1.8 (Andréka, Mikulás 1994). The calculus L∧ is strongly complete w.r.t. the class of all R-models."
  * "Theorem 1.9 (Andréka, Mikulás 1994). The calculus LΛ is strongly complete w.r.t. the class of square R-models."
  * "Theorem 1.10 (Mikulás 2015). If a sequent (in the language of ·, \, /, ∧) is true in all square R-models, then it is
    derivable in LΛ∧." (weak completeness only)
- Kuznetsov's own negative results (VERIFIED): Prop 2.1: "The sequent 0/(0/p), 0/(0/q) → (0/(0/q))·(0/(0/p)) is true in
  all square R-models (under the standard interpretation of 0), but not derivable in LΛ∧01." Abstract: "For the
  standard interpretation [of constants], even weak completeness fails." Thm 4.1: LΛ∧ is NOT strongly complete w.r.t.
  square R-models (explicit counterexample a\a → b·c ⊨ d → d·b·(c·b)∧(a\a)·c, not derivable).
- On proofs: "This is traditional provability semantics, which interprets theoremhood and entailment, not proofs. More
  modern semantics of proofs ... are beyond the scope of this article."
- Relevance (INFERENCE): "natural" concrete relational semantics for Lambek variants can be incomplete (even weakly)
  once constants/∧ are added — but this is incompleteness w.r.t. a FIXED concrete class (relation algebras), not w.r.t.
  all ternary/RS frames; the LE/RS-frame approach (S1) remains complete for the base logics via canonical extensions.
  Shows "relational semantics" is ambiguous: must specify frame class.

## S7. Badia, "On Sahlqvist Formulas in Relevant Logic"
- J. Philosophical Logic 47(4):673–691 (2018; online 2017), DOI 10.1007/s10992-017-9445-y. Retrieved via WebFetch of
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6060809/ (open-access author/journal version). Status: VERIFIED_SOURCE but
  ONLY THROUGH A WebFetch SUMMARIZER (quotes may be fragmentary; re-check before citing).
- RM frame ⟨W, R, ∗, O⟩, R ternary, x ≤ y iff ∃z(Oz ∧ Rzxy); valuations upward closed; standard translation
  Tx(φ→ψ) = ∀y,z(Rxyz ∧ Ty(φ) ⊃ Tz(ψ)); negation via x*.
- Theorem 18: "Every relevant Sahlqvist formula has a local first order correspondent on Routley-Meyer frames."
- Negative: a relevant formula (M) defines a class that "is not elementary. In other words, the above formula has no
  first order correspondent." (Löwenheim–Skolem argument.)
- Does NOT prove canonicity/completeness (correspondence only) — per summarizer.

## S8. Hartonas, "A General (Uniform) Relational Semantics for Sentential Logics"
- arXiv:2511.18458v1 [cs.LO], 23 Nov 2025 (PREPRINT, very recent, not peer-reviewed as far as visible). VERIFIED_SOURCE.
- Abstract: "general relational semantics framework which, by varying the axiomatization and components of the relational
  structures, provides a uniform semantics for sentential logics, classical and non-classical alike ... Completeness
  proofs rely on a choice-free construction of canonical extensions ... Correspondence results for axiomatic extensions
  of the logics of implication that we study rely on a fully abstract translation into their modal companions".
- Def 1: sorted residuated frames (two sorts 1, ∂, relation I, sorted relations R_j). Thm 3.2 "(Completeness). The
  logic Λt of implicative posets is sound and complete in the class PU of frames validating the axioms (F1), (U)".
  Thm 4.1 "The non-associative Lambek calculus is sound and complete in the frame class LK axiomatized as in Table 11."
  Thm 4.2: associative Lambek calculus "is sound in the frame class LK ..." (completeness part not read).
  Thm 3.3 (Full Abstraction) of translation φ ↦ φ● into sorted modal logic; standard translation of sorted modal logic
  into sorted FOL "exactly as in the single-sorted case, except for the relativization to two sorts".
- Self-stated: relational semantics in the literature "appears to be fragmented and ad hoc"; quotes DGP 2005 that Dunn
  "had to change his method of representation in ad hoc ways to fit the various logics."

## S9. Beall et al. (11 authors), "On the ternary relation and conditionality"
- Retrieved https://users.cecs.anu.edu.au/~jks/papers/ternary-final.pdf (author preprint dated February 10, 2011; journal
  data not printed; UNVERIFIED-MEMORY: J. Philosophical Logic 41 (2012)). VERIFIED_SOURCE for quotes.
- RM clause: "x |=M A→B iff for all y, z such that Rxyz, if y |=M A, then z |=M B."
- Footnote 14: the lemma that x;y is the intersection of worlds extending it "is a key lemma in the usual completeness
  proof for relevant logics." Footnote 21: ternary R cannot be xSy & ySz for R (collapses to classical), "also known that
  the ternary relation cannot be defined as xSz & yTz. See [7]" = Dunn, "Incompleteness of the binary semantics for R",
  Bull. Sect. Logic 16:107–110, 1987 (NOT_ACCESSED).
- No precise completeness theorem stated here.

## S10. Allwein & Dunn, "Kripke models for linear logic"
- JSL 58(2) (June 1993) 514–545, DOI 10.2307/2275217 — metadata+abstract via WebFetch of Cambridge Core page.
  Full text NOT_ACCESSED. Abstract (short verbatim fragment): "We present a Kripke model for Girard's Linear Logic
  (without exponentials) in a conservative fashion". Paraphrase of rest: base model handles noncommutative,
  nonassociative LL; coimplication added; adding contraction yields nondistributive relevance logic; builds on
  Urquhart's representation of nondistributive lattices and Dunn's gaggle theory; three-valued valuations
  (true/false/indifferent). Exact completeness theorem: NOT VERIFIED.

## Items NOT accessed / UNVERIFIED-MEMORY
- Conradie & Palmigiano, APAL 163(3):338–376 (2012) (data SECONDARY via CPZ ref [15]); full text not accessed.
- GNV journal version APAL 131 (2005) 65–102 (data SECONDARY via S1 ref [24]); only 2002 preprint read.
- Dunn, Gehrke, Palmigiano, "Canonical extensions and relational completeness of some substructural logics", JSL 70(3)
  (2005) 713–740 (SECONDARY via S1 ref [19] + search abstract: "uniform treatment of completeness of relational semantics
  for various substructural logics with implication as the residual(s) of fusion").
- Gehrke, "Generalized Kripke frames", Studia Logica 84(2) (2006) 241–275 (SECONDARY via S1 ref [22]).
- Suzuki, "A Sahlqvist theorem for substructural logic", RSL 6 (2013) 229–253 (SECONDARY via S1 Ex 3.9: covers FL with
  residuation; "inequalities proven to be canonical in [43, Theorem 5.10]").
- Coumans, Gehrke, van Rooijen, "Relational semantics for full linear logic", J. Applied Logic (SECONDARY via S1 ref
  [15] & Ex 2.7; S1 says its Theorem 15 "does not hold as stated").
- Kurtonina 1995 thesis (SECONDARY via S1 Ex 3.8).
- Routley & Meyer 1973 / Routley–Meyer–Plumwood–Brady RLR 1982 completeness of R for RM frames: UNVERIFIED-MEMORY.
- Restall 2000 book; Došen 1992 ZML survey; Andréka–Mikulás 1994 (only via Kuznetsov); Shehtman 1977 (only via Litak);
  Ghilardi–Meloni 1997 (only via S2); Rodenburg 1986 intuitionistic correspondence: NOT_ACCESSED.
- Kripke 1965 completeness of IPC: SEP "Intuitionistic logic" (WebFetch summary) states "an arbitrary propositional
  formula is intuitionistically provable if and only if it is forced by the root of every Kripke model" on finite trees;
  SECONDARY_ONLY.

## Synthesis (INFERENCE, labelled)
1. Frame types: IPC/intermediate: posets, propositions = up-sets. DML/positive modal (GNV): posets+relations,
   propositions = down-sets (convention). Relevant (RM): ⟨W,R,*,O⟩, up-sets wrt ≤ defined from O,R. LE-logics (FL,
   Lambek, Lambek–Grishin, MALL w/o exponentials, ortho): two-sorted RS-polarities + relations, propositions = PAIRS of
   Galois-stable sets (not arbitrary up-sets) and disjunction is NON-LOCAL. Lambek (AM94): binary-relation algebras,
   propositions = sets of pairs.
2. Standard translation: in all the above, frame validity = universal monadic second-order statement with predicate
   quantifiers restricted to up-sets/stable sets. Restriction is itself first-order definable (heredity ∀x∀y(Px∧x≤y→Py);
   stability via u,ℓ which are first-order) — so for a logic complete w.r.t. an ELEMENTARY class K = Mod(T):
   φ ⊢_L ψ iff T ∪ Her(P̄) ⊨_FOL ∀x(ST_x(φ) → ST_x(ψ)) [local consequence; for LE: two-sorted version with ≤ on X×Y].
   (My inference from Lemma 2.5 in S1 + completeness; not a theorem I saw stated in this form.)
3. Positive theorem families giving completeness w.r.t. elementary classes for an infinite syntactically defined class
   of axiomatic extensions: GNV Thm 3.8 (Sahlqvist DML); CP-LE Thm 7.1 + 8.8 (inductive LE-inequalities, all LE
   signatures incl. FL/Lambek/MALL-no-exponentials) — with RS-frames; CPZ Thm 6.1/7.1 (correspondence for all DLE,
   canonicity transfer for bi-intuitionistic modal). Relevant logic: Badia Thm 18 gives correspondence only.
4. Boundaries: Kripke-incomplete intermediate logics (Shehtman 1977; continuum, Litak Thm 11); non-elementary relevant
   formula (Badia); concrete relational incompleteness for Lambek with constants/∧ (Kuznetsov; AM94 title). Exponentials
   of linear logic: excluded by Allwein–Dunn ("without exponentials"); not covered by LE-ALBA (S1 never mentions them).
   Undecidability of canonicity/elementarity (S1 intro: "both these properties ... are algorithmically undecidable [2]")
   means no syntactic class can be exact.
5. Proof identity: none of these sources addresses proofs; Kuznetsov explicitly excludes it. Derivability (R1) only.
