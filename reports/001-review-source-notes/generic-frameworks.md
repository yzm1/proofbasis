# Notes [gen]: generic frameworks vs. the "vacuity–identity dilemma"

Question tested: is there a third option besides (ii) per-logic environment declares equations/rewrite rules
(claimed vacuous) and (iii) framework natively contains each foundation's connectives ("union of
foundations")? I.e. a FIXED framework whose connectives are generic (universal property / mode data /
patterns), each logic given by STRUCTURAL data only, with βη proof identity derived uniformly.

Download dir: scratchpad/review/dl/gen/ (PDFs converted with pdftotext -layout). Line refs below are to
those .txt files; page refs are to printed pages of the retrieved version.

---------------------------------------------------------------------------------------------------
## S1. Licata, Shulman, Riley — "A Fibrational Framework for Substructural and Modal Logics"
- (a) FSCD 2017, LIPIcs vol. 84, Article 25, pp. 25:1–25:22, DOI 10.4230/LIPIcs.FSCD.2017.25 (printed on PDF).
  URL retrieved: https://drops.dagstuhl.de/storage/00lipics/lipics-vol084-fscd2017/LIPIcs.FSCD.2017.25/LIPIcs.FSCD.2017.25.pdf
  (publisher version). STATUS: VERIFIED_SOURCE.
- (b) Extended version, "(extended version)", retrieved from Wayback snapshot
  http://web.archive.org/web/20200113231724/http://dlicata.web.wesleyan.edu:80/pubs/lsr17multi/lsr17multi-ex.pdf
  (author's homepage copy as archived 2020-01-13; no arXiv version found). STATUS: VERIFIED_SOURCE (that copy).
  NOTE: the arXiv id I first tried (1706.07074) is an unrelated physics paper — there is no LSR17 arXiv id known to me.

Fixed part: two-layer sequent calculus; context Γ is always cartesian; a mode-theory term α constrains use.
Two generic connectives F_α(Δ) (positive) and U_{x.α}(Δ|A) (negative); cut/identity/structurality-over-
structurality proved once. Additives are NOT instances of F/U: "additives can be defined separately by the
usual rules" (p.25:4); coproduct rules given separately (p.25:7).

Per-logic data = a mode theory Σ (Fig. 1, p.25:6): modes, function symbols (context descriptors),
**equational axioms α ≡ α′** and **directed structural-transformation axioms α ⇒ α′**, and (Sec. 4) **axioms
for equality of transformations s1 ≡ s2**. Quote (p.25:5): "the final two rules of the judgement Σ sig permit
two additional forms of signature declaration. The first of these extends a signature with an equational
axiom between two terms α and α′ ... These equational axioms will be used to encode reversible object
language structural properties, such as associativity, commutativity, and unit laws."
Quote (p.25:14): "We extend the signature Σ to allow axioms for equality of transformations s1 ≡ s2 ... and
define equality to be the least congruence closed under those axioms and some associativity, unit, and
interchange laws".
Ext. version §2.1 (lsr_ext.txt ~l.280): "we assume a metatheory with quotient sets/types, and use meta-level
equality for object-level equality" — i.e. decidability of α ≡ β is NOT addressed; and the s1≡s2 axioms
"[do] not influence provability in the sequent calculus, only identity of proofs".

Generic equations on derivations: YES. §4 (p.25:14): "The equational theory of derivations is the least
congruence containing the following equations" — unit/functoriality of cut, functoriality of
transformation action, and "the βη-laws for F and U. The β laws are the principal cut cases from our cut
admissibility proof. The η laws witness left-invertibility of F and right-invertibility of U." These are
uniform in Σ. BUT derivation identity also depends on per-logic 2-cell equations (s1 ≡ s2 axioms) via s∗(d).

Theorems (FSCD version):
- Thm 2.1 (p.25:7) "Admissibility of cut, identity, structurality-over-structurality, and respect for 2-cells"
  — for every mode theory.
- Thm 3.1 (p.25:8) "Logical Adequacy for Products and Implications ... Then Γ ⊢ A in the standard sequent
  calculus iff Γ∗ ⊢_Γ A∗." (provability only; per-example). Also Thm 3.2 (n-use variables), 3.3 (monad).
- Thm 5.6 (Completeness/Syntactic Bifibration) and 5.7 (Soundness/Interpretation in any bifibration), p.25:16:
  "Fix a bifibration π : D → M. Then there is a function ⟦−⟧ ... from ≡-classes of derivations ... to
  morphisms ... such that π(d) = α." Ext. version l.1670: "The overall conjecture is that the syntax is the
  initial bifibration over M. Together, the following soundness and completeness theorems give weak initiality".

Proof identity of the ENCODED logic (reflection) — the critical point:
- FSCD p.25:17: "One direction for future work is to continue a preliminary investigation of equational
  adequacy ... investigating whether the logical adequacy proofs are an isomorphism on βη-classes of
  derivations ... It is generally easy to show that object-language equations are true in the framework. We
  conjecture that the converse is true for the mode theories we have described here ... Proving this is
  challenging because the equational theory of Section 4 does not itself obviously have the subformula
  property. We have sketched a proof of equational adequacy for a simple case (ordered logic products),
  assuming a lemma that the equational theory from Section 4 can be characterized by permuting conversions on
  cut-free derivations."
- Ext. version: "CONJECTURE 8.5. Completeness of Permutative Equality. If d ≡ d′ then d↓ ≡p d′↓" (l.3247);
  §9.2 equational adequacy for ordered logic (product only) uses it (Remark 9.2 item 3 "By completeness of
  permutative equality (Theorem 8.5)" — labelled Theorem in the text but stated as Conjecture 8.5).
  "We do not abstract this 'template' as a lemma because the class of 'native sequent calculi' taken as input
  is not precisely defined." (l.~3302)
  => Preservation of βη: "generally easy"; REFLECTION of proof identity: conjectured, sketched only for ordered
  products, conditional on Conjecture 8.5.

Classical coverage: NO. p.25:2 "Our focus here is on propositional, single-conclusioned substructural and modal
logics, leaving extensions to quantifiers, multi-conclusioned logics, and dependent types to future work."
p.25:17: "extend our framework with first-order quantifiers, structured conclusions (as in classical or display
logic), and dependent types, which all seem possible but not obvious."

Relevance (INFERENCE): This is the best candidate for the "third option" for intuitionistic substructural/modal
logics: connectives generic, βη generic, per-logic data is a 2-multicategory. But (1) the per-logic data
INCLUDES equations and directed rewrite rules (on context descriptors and on 2-cells) — structural, not
logical, but still equations whose decidability is unaddressed (word problem for arbitrary finitely presented
equational theories is undecidable in general — standard fact, not stated in LSR); (2) reflection of proof
identity is a conjecture; (3) no classical/multi-conclusion logic; additives handled outside F/U. So it
weakens the dilemma's exhaustiveness for the intuitionistic substructural/modal family but does not settle
R3 reflection or classical coverage.

---------------------------------------------------------------------------------------------------
## S2. Licata & Shulman — "Adjoint logic with a 2-category of modes", LFCS 2016
URL retrieved: Wayback snapshot http://web.archive.org/web/20190427233624/http://dlicata.web.wesleyan.edu/pubs/ls15adjoint/ls15adjoint.pdf
(author preprint; LNCS page numbers / DOI not printed on this copy — not verified). STATUS: VERIFIED_SOURCE (preprint).
- Fixed: single-hypothesis single-conclusion sequent A [α] ⊢ B; F_α ⊣ U_α generic; cut/identity admissible;
  equational theory D ≈ D′ "the least congruence closed under" uniqueness/η rules etc. (§2.3).
- Per-logic: "The logic is parametrized by a strict 2-category of modes" (§2.1).
- Decidability, verbatim (§2.1): "we think of the mode category as being fixed at the outset, and the syntax and
  judgements of the logic as being indexed by the actual semantic objects/morphisms/2-morphisms of this category
  ... An alternative would be to give a syntax and explicit equality judgement for the mode category, which would
  be helpful if we needed a mode theory where equality of morphisms or 2-morphisms were undecidable."
  => authors explicitly contemplate undecidable mode-theory equality and sidestep it by working semantically.
- Restriction: "we consider only single-hypothesis, single-conclusion sequents, deferring an investigation of
  products and exponentials to future work."
- Theorem 1 (Syntax Determines a Pseudofunctor M → Adj); Theorem 2/3/4 soundness of calculus/equational theory.
  "the complete construction is about 500 lines of Agda" — Agda code cited at
  github.com/dlicata335/hott-agda/tree/master/metatheory/adjointlogic (NOT checked by me).
- Classical: no.

---------------------------------------------------------------------------------------------------
## S3. Shulman — "LNL polycategories and doctrines of linear logic"
LMCS 19(2):1, 2023, pp. 1:1–1:54, DOI 10.46298/LMCS-19(2:1)2023 (printed). URL: https://arxiv.org/pdf/2106.15042v5
(arXiv v5 = LMCS published layout). STATUS: VERIFIED_SOURCE. (arXiv 1712.05628 is NOT this paper.)
- Abstract: "We define and study LNL polycategories, which abstract the judgmental structure of classical linear
  logic with exponentials ... we define a notion of LNL doctrine, such that each of these classes of structures can
  be identified with the algebras for some such doctrine. We show that free algebras for LNL doctrines can be
  presented by a sequent calculus".
- Fixed part: an LNL polycategory judgmental structure (linear objects = symmetric polycategory, nonlinear = cartesian
  multicategory) + generic type-former for each "cone": generic noninvertible rule (Fig. 2d) and generic invertible
  rule (Fig. 2e) (§8, pp.1:44–1:46).
- Per-logic data: a doctrine D = "an lnl polycategory |D| equipped with a collection of distinguished 'cones'" (p.1:3)
  — purely structural/universal-property data; e.g. the cone for ⊗, &, F, U.
- Generic proof identity, verbatim (p.1:47): "The equivalence relation on derivations of ⊢ Φ whose quotient is
  Ŝ_D(Φ) can also be described syntactically. It is generated by the composition operation of S, the structural
  axioms of an lnl polycategory, the principal 'β-reduction' rule ... and the 'η-conversion' rule that two
  derivations of ⊢ ⨂_C[R1,...,Rn]^{−ε}, ... are equal if they become equal upon cutting with the noninvertible rule".
  Prop. 8.3: "There is a surjection from derivations of ⊢ Φ, in the full sequent calculus of Figure 2, to the
  hom-set Ŝ_D(Φ)."
- Limitations stated: "Unlike noninvertible rules in most common sequent calculi, ours does not build in a cut ...
  (We leave cut-elimination for future study.)" (p.1:45). Sequent calculus only "for a restricted class of doctrines"
  (|D| subterminal, finite discrete cones); infinite cones give "infinitely many rules, some with infinitely many
  premises. This is hard to implement, of course, but mathematically unproblematic" (Remark 8.4).
  Planar (non-symmetric) polycategories are excluded (Remark 2.5).
  No decidability result for the equivalence relation; the η-rule as stated is extensional (quantifies over cuts).
- Classical coverage: CLASSICAL LINEAR logic (MALL + !,?) — YES, explicitly. Classical NON-linear logic (LK with
  right weakening/contraction): NOT as a native instance — nonlinear objects form a cartesian MULTIcategory (single
  conclusion); Remark 2.7 says only the left context is split. (INFERENCE: LK would have to be reached via an encoding,
  e.g. a Girard-style translation; nothing in the paper claims a proof-identity-faithful LK instance.)
- Semantics: syntactic sequent calculus presents the FREE D-category (initiality), via small-object argument (§7–8).
Relevance (INFERENCE): strongest existing instance of a "generic framework" in the user's sense that reaches a
multiple-conclusion (classical linear) logic: connectives = universal properties (cones), per-logic data = doctrine,
β/η generated uniformly. It does not reach LK natively, has no cut-elimination or decidable equality result, and
is a semantic/free-construction result, not a translation-preserving-and-reflecting theorem for arbitrary
foundations.

---------------------------------------------------------------------------------------------------
## S4. Pruiksma, Chargin, Pfenning, Reed — "Adjoint Logic" (manuscript, 2018)
URL: http://www.cs.cmu.edu/~fp/papers/adjoint18b.pdf. STATUS: VERIFIED_SOURCE (unpublished manuscript, LIPIcs-style
draft "1:1"). Page refs per that draft.
- Per-logic data: "the schema is parameterized by a preorder of modes of truth m, along with a monotone map σ from
  this preorder into P({W, C}) assigning to each mode its set of structural properties" (§2). Exchange always
  assumed. "We use the same definition for the logical connectives at all modes." (§1)
- Fixed connectives at every mode: ⊸, ⊗, 1, ⊕_J, &_J, shifts ↑, ↓ (§2) — a fixed generic set, not user-defined.
- Theorems: Thm 3 (Admissibility of multicut), Thm 4 (Cut elimination for ADJ_E), Thm 5 (Identity Expansion).
- Proof identity: no equational theory of proofs in this paper; it cites "[24, A.3] ... by considering equivalence
  classes of proofs up to cut reductions, commuting conversions, and identity expansion" (p.~1:5) — not checked.
  Claimed design goal "(2) Preservation of proofs and proof reduction" — informal; "Due to the presence of cut,
  additional proofs may be available in the combination."
- Classical: NO. "In this paper we restrict our attention to intuitionistic logics" (§1).
Relevance (INFERENCE): per-logic data here is pure structural data (preorder + σ) — a very clean "third option" for
the W/C family of intuitionistic logics, but it covers only that family and says nothing proved about proof identity.

---------------------------------------------------------------------------------------------------
## S5. Gratzer, Kavvos, Nuyts, Birkedal — "Multimodal Dependent Type Theory"
LMCS 17(3):11, 2021, pp. 11:1–11:67, DOI 10.46298/LMCS-17(3:11)2021 (printed). URL: https://arxiv.org/pdf/2011.15021
(LMCS layout). STATUS: VERIFIED_SOURCE.
- Per-logic data: "MTT is parametrized by a mode theory which specifies a collection of modes, modalities, and
  transformations between them" (abstract); mode theory "given in the form of a small strict 2-category" (p.11:2–3).
- Fixed part: MLTT connectives at every mode (Π, Σ, Id, Bool, universes) + one generic modal type ⟨μ|−⟩.
  Definitional equality generic in M.
- Thm 6.8 (Closed Term Canonicity) "These results hold irrespective of the choice of mode theory" (abstract);
  subject to "a technical restriction" (p.11:4) — the proof assumes "·.{μ} = · ctx" (p.11:32).
- Algorithmic syntax / decidable typechecking NOT developed: "a proof of normalization ... We thus refrain from
  developing it" (§4, p.~11:15).
- Classical: NO (intuitionistic dependent type theory; classical axioms not considered).

## S5b. Gratzer — "Normalization for Multimodal Type Theory"
URL: https://arxiv.org/pdf/2106.01414 (arXiv v1, 2 Jun 2021 — NOT the LICS 2022 proceedings version; numbering may
differ). STATUS: VERIFIED_SOURCE (preprint).
- Thm 8.5 normalization functions nf, nfty. Cor 8.8 "The conversion problem in MTT is equivalent the conversion
  problem of normal forms." Cor 8.10 "If modalities and 2-cells enjoy decidable equality, typechecking MTT is decidable."
- Remark 7 (verbatim): "these normal forms do not necessarily enjoy decidable equality. Rather, the problem of
  deciding when two normal forms are convertible is precisely the problem of deciding whether certain 1- and 2-cells
  of the mode theory M are equal. Accordingly, it is possible that MTT may enjoy normalization, but not decidable
  type-checking."
Relevance (INFERENCE): confirms the general pattern: generic frameworks push the decidability burden into the
per-logic structural data; proof-identity decidability = mode-theory word problem, which can be undecidable.

---------------------------------------------------------------------------------------------------
## S6. Zeilberger — "On the unity of duality" (APAL 153, 2008)
URL: http://noamz.org/papers/unity-duality.pdf — author preprint dated "August 6, 2008" (journal pagination not
present). STATUS: VERIFIED_SOURCE (preprint).
- Fixed part: polarized logic in which connectives are defined by pattern-typing (∆ ⇒ p : P); the negative rule is
  higher-order: "∀(∆ ⇒ P triv) : Γ, ∆ ⊢ contra / Γ ⊢ P false" and continuations are "maps from P-patterns to
  well-typed statements" (§3, p.~19–20). Identity and reduction (cut) proven generically by subformula induction
  (Principles 3–5 etc.).
- Proof identity: no equational theory; canonical forms are η-long/β-reduced by construction: "terms that do not
  apply the identity principle are 'η-long', while terms that do not apply the reduction principle are 'β-reduced'".
- Classical: YES for provability via polarization: Thm 27 (Focusing Completeness) "If |Λ| →c |Θ| then there exists
  a pure S such that S : (Λ → Θ)." But |−| "is not injective—any formula can be given at least two polarizations ...
  in fact there are infinitely many", and "focusing proofs for different polarizations of classical theorems
  correspond to different kinds of double-negation translations" (p.~16). => the CHOICE OF POLARIZATION determines
  proof identity (CBV vs CBN); no single classical proof identity is preserved/reflected (INFERENCE grounded in quote).
- F07-type limitation, verbatim (§4): for recursive types "we can no longer rely on there being only finitely many
  patterns of any type ... it raises a question about how to interpret the higher-order rules, which we will not
  attempt to answer here."

## S6b. Zeilberger — "Focusing and Higher-Order Abstract Syntax" (POPL 2008)
URL: http://noamz.org/papers/focusing-hoas.pdf (author copy). STATUS: VERIFIED_SOURCE.
- Intuitionistic (call-by-value) only; generic identity/cut proofs ("do not even mention particular positive
  connectives"). Coq encoding: "Lam : (pat → exp) → fnc"; "Coq requires maps pat → exp to be total, so to simulate
  partial maps we add an expression Fail".
- Exotic terms, verbatim (§3.4): "Strictly speaking, plus∗ is an 'exotic term', i.e., does not represent a term of
  concrete syntax ... since it corresponds to a function defined by infinitely many pattern-branches." Footnote 6:
  "E.g., for Nat we essentially have the ω-rule". Also "for other recursive types, the identity principle Γ; P ⊢ P
  requires a derivation that is infinitely deep."
Relevance (INFERENCE): pattern-based generic frameworks achieve generic identity/cut by delegating the negative rule
to META-LEVEL functions — exactly F02/F07 risk (meta-level computation, infinitary rules) unless pattern sets are
finite (propositional case: Prop. 17 "only finitely many P-patterns").

---------------------------------------------------------------------------------------------------
## S7. Uemura — "A General Framework for the Semantics of Type Theory"
URL: https://arxiv.org/pdf/1904.04097 (arXiv v3, 26 May 2023; MSCS publication not verified by me). STATUS: VERIFIED_SOURCE.
- Fixed: representable map categories / a "semantic logical framework" with extensional equality types a = b (§5).
- Per-theory data: a signature of symbols including EQUATIONS: "An equation is encoded to a symbol of the form
  α : Γ ⇒ a = b" (§5). Π-types (Ex. 5.8) declare β ("app(A,B,abs(A,B,b),a) = ba") and η/funext as explicit symbols.
  => this is horn (ii) literally: βη declared per theory.
- Propositional logic (Ex. 5.12) includes "mono : (P : Prop, x : true(P), y : true(P)) ⇒ x = y" — proofs
  proof-irrelevant (proof identity trivial).
- Thm 6.10 bi-initial model for any type theory; Thm 7.20/7.31 theories ≃ democratic models.
- Stated limitation (§1): "non-trivial operations on contexts are not allowed. Thus, type theories with
  'dual-contexts' ... or modal type theories ... are not covered by our definition." No decidability discussion.
- Classical: not discussed (grep found nothing). INFERENCE: LEM could be added as an axiom symbol — but that is a
  per-theory trusted axiom.

## S7b. Kaposi & Xie — "Second-Order Generalised Algebraic Theories: Signatures and First-Order Semantics"
FSCD 2024, LIPIcs 299, Art. 10, pp. 10:1–10:24, DOI 10.4230/LIPIcs.FSCD.2024.10 (printed). URL:
https://drops.dagstuhl.de/storage/00lipics/lipics-vol299-fscd2024/LIPIcs.FSCD.2024.10/LIPIcs.FSCD.2024.10.pdf.
STATUS: VERIFIED_SOURCE. (arXiv 2405.09301 is NOT this paper.)
- Per-theory data: SOGAT signature; equations declared. Notation (§2.4): "we write f : A ≅ B : g for f : A ↔ B : g with
  two equations β : g (f a) = a and η : f (g b) = b" — STLC (Def. 5) is "lam : (Tm A → Tm B) ≅ Tm (A ⇒ B) : – · –".
  (INFERENCE: βη here come from declaring an isomorphism = a universal property, a halfway house, but still declared
  per connective.)
- FOL (Def. 7): "Pf : For → Prop" where Prop = Set + "irr : (a a′ : A) → a = a′" — proof identity trivialized.
- Limitation (§1): "Substructural (e.g. linear or modal) type theories are not definable as SOGATs using the method
  described in this paper". Classical propositional logic mentioned only as "the theory of Boolean algebras"
  (single-sorted algebraic theory, §2.1) — i.e. provability-level, no proof identity.

---------------------------------------------------------------------------------------------------
## S8. Fiore & Hur — "Second-order equational logic" (CSL 2010)
STATUS: NOT_ACCESSED (cl.cam.ac.uk connection reset; no Wayback copy found). UNVERIFIED-MEMORY only: presents
second-order equational logic with soundness and completeness w.r.t. second-order algebraic models; each theory's
equations (incl. β/η) are axioms of a presentation. Do not cite theorem numbers.

---------------------------------------------------------------------------------------------------
## Synthesis (INFERENCE, labelled)
1. The dilemma as stated (only (ii) or (iii)) is NOT exhaustive on its face: LSR17, LS16, PCPR18, MTT, and Shulman's
   LNL doctrines are fixed frameworks with generic connectives (F/U; cones/universal properties; generic shifts;
   generic modality) whose βη equations on derivations are given once, uniformly, and per-logic data is
   structural (mode 2-(multi)category, preorder+σ, doctrine). This is a genuine third category the report must address.
2. But the third option does not escape the dilemma cleanly:
   a. The structural data itself contains equations and directed rewrite rules (LSR mode-theory α≡β, α⇒β, s1≡s2);
      LSR/LS16 state 2-cell equations affect proof identity. Decidability is offloaded: Gratzer Remark 7 /
      Cor 8.10; LS16 explicitly mentions possibly undecidable mode equality.
   b. Reflection of the object logic's proof identity (R3 "reflect") is NOT established in general: LSR conjecture
      (equational adequacy), only sketched for ordered-logic products, conditional on Conjecture 8.5.
   c. Coverage: all intuitionistic except Shulman LNL doctrines (classical LINEAR, multiple conclusions) and
      Zeilberger (classical provability via polarization; proof identity depends on chosen polarization).
      None verified here covers LK with a fixed, faithful proof identity; LSR explicitly lists classical/
      multi-conclusion as future work.
   d. Pattern-based genericity (Zeilberger) relies on meta-level functions → ω-rule/exotic terms beyond the finite case.
   e. Meta-frameworks (Uemura, Kaposi–Xie) are horn (ii): βη declared per theory; logic proofs often made
      proof-irrelevant; substructural/modal excluded.
3. Net: the report's dilemma should be restated as at least a trilemma, with the third horn being "generic
   structural framework", whose known instances are limited to (intuitionistic substructural/modal) and
   (classical linear) families, push equational/decidability burden into mode data, and lack proved
   proof-identity reflection.
