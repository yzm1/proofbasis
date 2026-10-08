# rwl — Rewriting logic reflection, general logics, logic-translation frameworks

Agent tag: rwl. Protocol: notes/PROTOCOL.md. Date of retrieval: 2026-10-08.
Downloads: scratchpad/dl/rwl/ (PS files converted with ghostscript `txtwrite`; PDFs with `pdftotext -layout`).
Text extraction from the dvips PostScript files lost ligatures ("fi", "fl") and overlines/Greek letters; quotes below
restore "fi"/"fl" ligatures only, and mark lost symbols with [sym]. Overline in the representation function (T ⊢ φ with a bar)
is lost in extraction; I write it as `rep(T ⊢ φ)`.

---------------------------------------------------------------------------------------------------------------

## S1. Clavel & Meseguer, "Reflection and Strategies in Rewriting Logic" (ENTCS 4, 1996)

- Bib: Manuel Clavel and José Meseguer, "Reflection and Strategies in Rewriting Logic", Electronic Notes in Theoretical
  Computer Science 4 (1996) (header printed on the document: "Electronic Notes in Theoretical Computer Science 4(1996)";
  copyright line "1996 Elsevier Science B. V."). Proceedings of the first WRLA (Asilomar; dvips line says "final-asilomar.dvi").
  No DOI printed.
- URL retrieved: https://maude.cs.illinois.edu/papers/postscript/tcs4009.ps.gz (linked from
  https://maude.cs.illinois.edu/papers/abstract/tcs4009.html). Version: author PostScript of the ENTCS paper. Pages = that PS (ENTCS page numbers printed 1–21).
- Status: VERIFIED_SOURCE.
- NOTE: This is NOT the TCS 285(2) 2002 paper "Reflection in conditional rewriting logic" (Clavel & Meseguer). I could NOT
  obtain that paper (ScienceDirect returned 403). Its content is described SECONDARY_ONLY by S2 (see below): it handles
  "(2) unsorted conditional [17]; and (3) many-sorted conditional [17]". Clavel's book (CSLI 2000) also NOT_ACCESSED.

### Definitions (verbatim)
- Def 2.1 (entailment system, cited to Meseguer [20] = General Logics): E = (Sign, sen, ⊢), ⊢_Σ ⊆ P(sen(Σ)) × sen(Σ) satisfying
  (1) reflexivity, (2) monotonicity, (3) transitivity, (4) ⊢-translation: "if Γ ⊢_Σ φ, then for any H : Σ → Σ' in Sign we have
  sen(H)(Γ) ⊢_Σ' sen(H)(φ)." (p.3)
- Def 2.3 (p.4): "Given an entailment system E and a set of theories C ⊆ |Th|, a theory U is C-universal if there is a function,
  called a representation function, ( ⊢ ) : ⋃_{T∈C} {T}×sen(T) → sen(U) such that for each T ∈ C, φ ∈ sen(T),
  T ⊢ φ ⟺ U ⊢ rep(T ⊢ φ). If, in addition, U ∈ C, then the entailment system E is called C-reflective."
- Section 2 (p.2): "We focus here on the simplest case, namely entailment systems. However, reflection at the proof calculus
  level—where not only sentences, but also proofs are reflected—is also very useful; the adequate definitions for that case
  are also in [5]." ([5] = Clavel & Meseguer, Reflection in rewriting logic (Reflection'96) — NOT_ACCESSED.)

### Main theorem (verbatim, p.9)
- Class: §3.2: "C the class of unconditional and unsorted finitely presentable rewrite theories—that is, theories whose ranked
  alphabet, and set of rules are all finite." §3.3 adds: "We also assume that for any rule t → t' in T ∈ C, var(t') ⊆ var(t)."
  Equations are eliminated: by Lemma 3.1, (Σ,E,R) ⊢ [t]→[t'] iff (Σ,∅, R ∪ E→ ∪ E←) ⊢ t→t' (equations become bidirectional rules).
- "Theorem 3.2 For any theory T = (Σ, ∅, R) ∈ C, t, t' ∈ T_Σ, T ⊢ t → t' ⟺ U ⊢ rep(T ⊢ t → t')."
  Representation (p.6): rep(T ⊢ t→t') = (T̄@[• ← t̄]) → (T̄@[• ← t̄']) [symbols partially lost]; terms are encoded as
  op{f}[...] / var{v}[] over ASCII strings. Note t, t' ∈ T_Σ (ground terms) in the theorem statement.
- Proved as Theorem 3.11 (⇒) and Theorem 3.19 (⇐). Thus BOTH preservation and reflection of derivability (entailment only).
- Finiteness of U (p.7): "As we shall prove later, U itself belongs to the class C of finitely presentable rewrite theories
  and with the representation function makes the entailment system of rewriting logic reflective." U has finite ranked
  alphabet (ASCII ∪ a handful of operators), equations only for associativity/identity of `;`, and ~14 rule schemas
  (matching, substitution, replacement are reified as rewrite rules over the encoded term).
- Proof-level reflection is only CLAIMED, not proved, in this paper (p.7, verbatim): "Note that rewriting logic has also a
  proof calculus [21]. By extending the definition of U along the lines of [14], so as to make explicit and reify the proofs
  built up by the deduction process, one can similarly exhibit a finitely presentable universal theory U' making the proof
  calculus of rewriting logic C-reflective, as defined in [5]." → status: claim (no proof in S1).
- No claim that the representation is injective, recursive, or efficient in S1 (these requirements appear in S2).
- Section 4 (p.17): metacircular interpreters "may have a fixed strategy"; strategies are a separate layer: "an internal
  strategy language is a theory-transforming function S that sends each theory T to another theory S(T) whose deductions
  simulate controlled deductions of T."

### What is machine vs environment / trusted
- Machine: the single finite rewrite theory U (finite signature, finite rules) — fixed for ALL T in C.
- Environment/data: the object theory T is passed as a DATA TERM (T̄ = ⟨V; R⟩) inside the sentence. The object rules are
  NOT trusted axioms of U; U's own rules perform matching/substitution/replacement on the encoded rules.
- Trusted: U's 14 rule schemas + rewriting logic's 4 deduction rules + the encoding function.

### Relevance (INFERENCE)
- F01/F02: This is a precise, published, proved instance of "a fixed finite theory U simulates derivability of every
  finitely presentable theory in a class C, preserving AND reflecting entailment", with the object theory supplied as data.
  It is exactly the "universal interpreter" benchmark: any ProofBasis claim of a fixed finite algebra preserving and
  reflecting derivability (R1 alone) for finitely presented rule systems is matched by this theorem (at the level of
  unconditional unsorted rewrite theories; extended in S2 to conditional mel-based ones). R1 alone is therefore not novel and
  is achieved by an interpreter-style (F02) construction.
- F04/R3: The theorem is stated for entailment only; proof identity is not addressed (proof-level version only claimed).
- F09: The universal theory simulates one object rewrite by many U-steps (matching rules 3–7, substitution rules 9–12, etc.);
  no complexity bound is stated.

---------------------------------------------------------------------------------------------------------------

## S2. Clavel, Meseguer, Palomino, "Reflection in Membership Equational Logic, Many-Sorted Equational Logic, Horn Logic
##     with Equality, and Rewriting Logic" — two versions

### S2a. Extended version (preprint; presumably the text of TCS 373(1-2):70–91, 2007 — NOT confirmed)
- URL retrieved: https://maude.sip.ucm.es/~miguelpt/papers/rmel.pdf (Palomino's paper directory). No venue/DOI printed on
  the PDF. Footnote on p.1 (verbatim): "This work is an extended and revised version of a paper presented at WRLA 2002,
  including the detailed proofs of all the results." The TCS 2007 venue (373(1-2):70–91, DOI 10.1016/j.tcs.2006.12.009)
  comes only from dblp / UCM repository listings shown in a web search — SECONDARY_ONLY; page numbers below refer to rmel.pdf.
- Status: VERIFIED_SOURCE (for the preprint text).

### S2b. Workshop version
- Bib printed on PDF: "Electronic Notes in Theoretical Computer Science 71 (2003)", 17 pages, WRLA'02.
  URL retrieved: https://maude.sip.ucm.es/~miguelpt/papers/wrla02.pdf. Status: VERIFIED_SOURCE (skimmed; theorem numbering
  3.4 / 4.1 / 5.1 / 6.2 matches S2a's Theorems 1/4/5/6).

### Prior results as summarised by S2a (SECONDARY_ONLY for those papers)
- p.1: "Clavel and Meseguer have formerly given detailed proofs for increasingly general fragments of rewriting logic, namely:
  (1) unsorted and unconditional [10], (2) unsorted conditional [17]; and (3) many-sorted conditional [17]."
  Reference list of S2a (verbatim): "[10] M. Clavel. Reflection in Rewriting Logic: Metalogical Foundations and Metaprogramming
  Applications. CSLI Publications, 2000." and "[17] M. Clavel and J. Meseguer. Reflection in conditional rewriting logic.
  Theoretical Computer Science, 285(2):245–288, 2002." So the TCS 2002 paper covers unsorted conditional and many-sorted
  conditional rewrite theories (SECONDARY_ONLY via S2a; the paper itself NOT_ACCESSED).

### Definitions (verbatim, S2a p.4)
- Def 3 = same C-universal / C-reflective definition as S1, PLUS the added requirements: "To take into account computability
  considerations, we should further require that the representation function ⊢̄ is recursive. Finally, to rule out unfaithful
  representations, we should require that the function ⊢̄ is injective."
- p.4 (Shoenfield): theories T in C must be "finite objects" and C "a space, that is, a class X of finite objects such that,
  given a finite object x, we can decide whether or not x belongs to X."

### Main theorems (verbatim)
- Hypothesis throughout: finitely presentable theories with NONEMPTY KINDS (p.5: "This is a relatively minor restriction
  that avoids the well-known complications with quantification in many-sorted equational deduction"; footnote 4: the empty-kind
  case "follows very similar lines" — claimed, not proved).
- "Theorem 1. For all terms t ∈ T_Σ(X) and sorts s in the signature Ω of a theory T, T ⊢ t : s ⟺ U_mel ⊢ rep(T ⊢ t : s).
  Similarly, for all sentences t, t' ∈ T_Σ(X) over the signature Ω of T, T ⊢ t = t' ⟺ U_mel ⊢ rep(T ⊢ t = t')." (p.12)
  Representation: rep(T ⊢ φ) is the mel equation `(T̄ |- t̄ = t̄' if none) = true` (resp. membership) — a Boolean-valued
  provability operator `_|-_` defined by conditional equations mirroring each deduction rule (Fig. 1, p.13).
- "Theorem 4. U_mel is a universal theory in msel for the class of finitely presentable theories having nonempty sorts." (p.17)
- "Theorem 5. U*_mel is a universal theory in mshorn= for the class of all finitely presentable theories with nonempty
  sorts." (p.18) Proof composes with the conservative translation J/α (Horn → mel) from [41] — i.e. reflection is obtained
  by COMPOSING a conservative logic translation with a universal theory.
- "Theorem 6. For all finitely presentable rewrite theories with nonempty kinds T = (Ω, E, R), with Ω = (K, Σ, S), and terms
  t, t' in T_Σ(X), T ⊢ t → t' ⟺ U_rl ⊢ (T̄ |- t̄ => t̄') → true." (p.23) Rules may be conditional with equations,
  memberships and rewrites in conditions (p.18).
- U_rl is given by a finite Maude-style specification extending U_mel (finite list of ops, ~4 rule schemas Fig. 2 + equations).
  I did not find an explicit sentence in S2a stating "U_rl ∈ C" for the rl case; the conclusion states rl "is reflective".

### Limitations stated in S2a (verbatim, §8 p.24)
- Open: "Horn logic without equality"; "theories where some of the operators are frozen [7] ... and to theories where some
  kinds can be empty"; "developing adequate strategies to execute the universal theories of rewriting logic and of membership
  equational logic in Maude, so that proof objects can be associated to reflective proofs when desired."
  → i.e. the universal theories are specified for entailment; executing them and producing proof objects is future work.
- §7 p.24 (design change vs S1): S1 reflected T ⊢ t→t' as U ⊢ ⟨T̄,t̄⟩ → ⟨T̄,t̄'⟩ (transitivity of T mirrored by U's own
  transitivity); S2 reflects it as a Boolean judgement `(T̄ |- t̄ => t̄') → true`, with transitivity "explicitly reflected".
  Authors: the original approach "corresponds to thinking of the universal theory from a computational point of view";
  the new one "is more logical". (INFERENCE: two different encodings with different proof-shape correspondence; the choice
  is not canonical — relevant to F08.)
- p.24: suggestion to use Smullyan's elementary formal systems as an intermediary "taking advantage of the fact that all
  recursively enumerable sets can be recognized by EFSs" (INFERENCE: authors themselves note the r.e.-universality route,
  i.e. F02-style universality).
- Lemma 1 (p.15) discusses "an infinite number of uninteresting derivations of arbitrary depth" in U_mel for the same
  equation (via transitivity on Boolean equations `... = true`), handled by normalising to minimum-depth derivations
  (INFERENCE: many U-proofs correspond to one object proof — U's proofs do NOT reflect object proof identity).
- WRLA'02 intro (S2b p.2, verbatim): "whenever proof objects are required to justify reflective proofs, it is essential to
  make an explicit use of the corresponding universal theories" and the results "provide a general method for combining
  efficient reflective computation using the built-in functionality of the META-LEVEL module with the ability to generate
  proof objects by means of the universal theories when this is required."

### Relevance (INFERENCE)
- F01: Strongest benchmark found: a fixed finitely specified theory (U_mel / U_rl) is universal (preserves+reflects
  entailment) for ALL finitely presentable mel theories (nonempty kinds), and hence (by composing with conservative maps)
  for many-sorted equational logic and Horn logic with equality; for conditional rewrite theories over mel. Combined with S3
  (any sequent calculus → rewrite theory, conservatively), this gives a two-stage "fixed finite interpreter + environment-as-data"
  that preserves and reflects derivability for any logic presentable as a finitary sequent/rule system. R1 is thus covered.
- F02/F03: The object logic's rules live in the encoded theory T̄ (data), not in U. U itself trusts only its own finite rule
  set. This is precisely the "proof-checker-in-an-axiom"/interpreter pattern the project charter calls vacuous; the charter
  must explain what R2–R4 add beyond it.
- R3/F04: No theorem in S1/S2 relates proof identity of T to proof identity of U. S2's Lemma 1 explicitly exhibits many
  U-derivations per object entailment.

---------------------------------------------------------------------------------------------------------------

## S3. Martí-Oliet & Meseguer, "Rewriting Logic as a Logical and Semantic Framework"

### S3a. ENTCS 4 (1996) short version
- Header printed: "Electronic Notes in Theoretical Computer Science 4(1996)"; footnote: "This paper is a short version of [36]".
  URL retrieved: https://maude.cs.illinois.edu/papers/postscript/tcs4012.ps.gz. Status: VERIFIED_SOURCE.
### S3b. SRI technical report 1993 (long version)
- URL retrieved: https://maude.cs.illinois.edu/papers/postscript/MMlogframework_1993.ps.gz; bibtex entry on site:
  "TechReport, SRI International, 1993". Page numbers printed in text (pp. 1–~80). Status: VERIFIED_SOURCE.
- Handbook of Philosophical Logic vol. 9 (2002) version: NOT_ACCESSED.

### General-logics notions as restated (verbatim from S3a pp.5–8; S3b §2.5–2.6) — SECONDARY for Meseguer 1989
- S3a p.5: "An entailment system axiomatizes the consequence relation of a logic. ... A logic is obtained by combining an
  entailment system and an institution. A proof calculus enriches an entailment system with an actual proof theory. A logical
  system is a logic with a choice of a proof calculus for it."
- S3b p.9–10 (proof calculus, verbatim): "a proof calculus [70] consists of an entailment system together with: A functorial
  assignment P of a structure P(T) to each theory T. An additional functorial assignment of a set proofs(T) to each structure
  P(T). A natural function π_T assigning a sentence to each proof p ∈ proofs(T) and such that, for Γ the axioms of T, a sentence
  φ is in the image of π_T if and only if Γ ⊢ φ." Also: "We need not make a choice about the particular types of algebraic
  structures that should be allowed for different proof calculi; we can abstract from such choices by simply saying that for a
  given proof calculus there is a category Str of such structures".
  (INFERENCE: proof identity is whatever equality P(T) has; the framework does not fix any proof-identity congruence.)
- Map of entailment systems, S3b Def 5 p.10 (verbatim): "a map of entailment systems (Φ, α) : E → E' consists of a natural
  transformation α : sen ⇒ Φ;sen' and an α-sensible functor Φ : Th_0 → Th'_0 satisfying the following property:
  Γ ⊢_Σ φ ⟹ Γ' ∪ α_Σ(Γ) ⊢'_Σ' α_Σ(φ), where, by convention, (Σ', Γ') = Φ(Σ, Γ). We call (Φ, α) conservative when the above
  implication is an equivalence." Signatures may map to THEORIES (S3a p.7: "For many interesting applications one needs to map
  signatures of E to theories of E'").
- S3a p.7: "There are also notions of map of proof calculi and map of logical systems, for which we refer the reader to [39]."
  (not restated further in either version).
- S3b p.10: "we can view the establishment of a map of proof calculi having nice properties, such as conservativity, as a
  proof of correctness for a compiler".

### Framework claims and caveats (verbatim)
- Minimal adequacy criterion (S3a p.7): "The minimum requirement that seems reasonable to make on a representation map
  L → F is that it should be a conservative map of entailment systems."
- Scope (S3a p.8): "the scope of a logical framework F as the class of entailment systems E having conservative maps of
  entailment systems E → F. ... without adding further assumptions it is not reasonable to expect that we can find a logical
  framework F whose scope is the class of all entailment systems."
- Representational adequacy (S3a p.8): "Although at present we lack a precise definition of this property, it is quite easy
  to observe its absence in particular examples."
- Conjecture (S3a p.8): "We conjecture that the scope of rewriting logic contains all entailment systems of 'practical
  interest' for a reasonable axiomatization of such systems." Conclusion (S3a p.31): "our tentative conclusion is that, at the
  level of entailment systems, rewriting logic should in fact be able to represent any finitely presented logic via a
  conservative map, for any reasonable notion of 'finitely presented logic.' Making this tentative conclusion definite will
  require proposing an intuitively reasonable formal version of such a notion in a way similar to previous proposals of this
  kind by Smullyan [56] and Feferman [15]." → status: CONJECTURE by the authors (not a theorem).
- Intro (S3a p.3): "linear and relevance logics do not have adequate representations in LF, in a precise technical sense of
  'adequate' [17, Corollary 5.1.8]" ([17] = Gardner's thesis per S3a refs; not checked).
- Intro (S3b p.4): "the direct correspondence between proofs in object logics and proofs in the framework logic can often be
  maintained in a conservative way by means of maps of logics" — note "often", informal.

### Theorems (verbatim)
- S3a Theorem 4.1 (= S3b Theorem 14): "Given a linear theory T, a sequent A1,...,An ⊢ B1,...,Bm is provable in linear logic
  from the axioms in T if and only if the sequent [A1]⊗...⊗[An] → [B1]⅋...⅋[Bm] is a LINLOG(T)-rewrite, i.e., it is
  provable in rewriting logic from the rewrite theory LINLOG(T)." (propositional linear logic; conservative map of
  entailment systems; extended to a conservative map of logics LinLogic → OSRWLogic.)
- S3a Theorem 6.1 (= S3b Theorem 15): "Given a linear theory T, a linear logic sequent ⊢ A1,...,An is provable in linear logic
  from the axioms in T if and only if the sequent empty → ⊢ A1,...,An is provable in rewriting logic from the rewrite theory
  LL-SEQUENT(T)." Generality claim (S3a p.21): "the technique used in this conservative map of entailment systems is very
  general ... it can be applied to any sequent calculus, be it for intuitionistic, classical or any other logic. ... The general
  idea is to map a rule in the 'sequent' system to a rewrite rule over a 'configuration' of sequents or predicates, in such a
  way that the rewriting relation corresponds to provability of such a predicate." (Only stated for linear logic; general
  case is a methodological claim, not a theorem.)
- Binding (S3b §4.4): quantifiers/binders handled by internalising free variables and substitution as equations
  ("explicit substitutions"), i.e. binding discipline is put into the equational part E of the object rewrite theory.

### Proof identity — decisive passages
- Proof terms and equations (S3b pp.19–21, restating Meseguer 1992 [72] = "Conditional rewriting logic as a unified model of
  concurrency", TCS 96, 1992, pp.73–155 — that paper itself NOT_ACCESSED): proof terms generated by Identities [t],
  Σ-structure f(α1..αn), Replacement r(α1..αn), Composition α;β; the model T_R(X) is "the quotient of P_R(X) modulo the
  following equations": 1. Category (associativity, identities); 2. Functoriality of the Σ-structure
  ("f(α1;β1,...,αn;βn) = f(α1..αn);f(β1..βn)", "f([t1],...,[tn]) = [f(t1..tn)]"); 3. Axioms in E ("t(α1..αn) = t'(α1..αn)");
  4. Exchange ("r(ᾱ) = r([w̄]);t'(ᾱ) = t(ᾱ);r([w̄'])").
  Verbatim: "the exchange law states that rewriting at the top by means of rule r and rewriting 'below' using α are processes
  that are independent of each other and can be done either simultaneously or in any order." ... "The equations 1-4 provide in
  a sense the most abstract 'true concurrency' view of the computations of the rewrite theory R that can reasonably be given."
- NEGATIVE (S3b p.34, verbatim): in models of the linear-logic representation "for each rewrite rule in R we require just a
  natural transformation in the system, but we do not impose any coherence or uniqueness conditions on these natural
  transformations. For this reason, a LINLOG(T)-system interprets A&B as a weak product instead of a product". To obtain a
  Girard category "we do the quotient of the full subcategory of C generated by A by this set of equations" — i.e. the
  object logic's proof equations (those making it a genuine categorical model of linear logic) are NOT generated by rewriting
  logic's proof-term equations; they must be added by an extra quotient. The map is conservative at the level of
  (existence of) morphisms: "there is a morphism A → B in L if and only if there is a morphism A → B in C".

### Relevance (INFERENCE)
- R1/F01: The two-stage route "object sequent calculus → rewrite theory (conservative) → U_rl (universal)" covers derivability
  preservation+reflection for finitary rule systems; but the general sequent-calculus step is a methodology plus case
  theorems (linear logic), and "any finitely presented logic" is an explicit authors' CONJECTURE.
- R3/F04: Rewriting-logic proof identity = the fixed equations (category + functoriality + E + exchange) applied to the
  ENCODING. These equations identify encoded proofs that differ by interleaving of independent rewrites and by E (e.g.
  ACU structural axioms), but they do NOT give object-logic proof identities such as products' uniqueness (η), cut-elimination
  or commuting conversions — the authors' own linear-logic example needs an extra quotient. Hence: proof identity is
  NOT preserved/reflected by these representations in general; at best a coarse/foreign congruence is imposed.
- R4: The exchange law + functoriality are a genuine, precise, published account of "independence" of rewrite steps
  (true-concurrency equivalence of proof terms). This is relevant prior art for any R4 "causal/independence structure" claim:
  it is a local, equational independence notion (parallel/nested redexes), defined relative to the encoding's term structure.
  Whether it matches the object logic's own independence notion is not addressed.
- F03: In the sequent-calculus encodings, object rules become rewrite rules of the theory (environment) — trusted rules live
  in the environment; binding/freshness is put in equations E (also trusted).


---------------------------------------------------------------------------------------------------------------

## S4. Meseguer, "General Logics" (Logic Colloquium '87, North-Holland 1989, Studies in Logic 129, pp. 275–329)

- Bib (pages/volume from web-search listing + S2a ref [38]: "Logic Colloquium'87, pages 275–329. North-Holland, 1989").
- URL retrieved: https://courses.grainger.illinois.edu/cs522/sp2016/GeneralLogics.pdf (course-hosted copy; author affiliation
  "SRI International ... and CSLI Stanford"; no publisher pagination printed — page numbers below are the PDF's own (1–~60)).
  Version: appears to be author typescript/re-typeset copy, NOT the North-Holland typeset version. Provenance unverified.
- Status: VERIFIED_SOURCE (for this copy).

### Key passages (verbatim)
- §1.2 p.4: "The entailment relation ⊢ says nothing about the internal structure of a proof. To have a satisfactory account
  of proofs, we need the additional concept of a 'proof calculus' P for a logic L. The definition of a proof calculus is very
  general, and does not favor any particular style of proof theory. The same logic may of course have many different proof
  calculi."
- §3 p.15: "the entailment relation ⊢ is precisely what remains invariant under the many equivalent proof calculi that can
  be used for a logic. ... rather than building a particular proof calculus into the definition of a logic, it seems more
  satisfactory to axiomatize separately a proof calculus P for a logic L".
- §3 p.15–16: P(T) "will not impose any particular structure; they will postulate that P(T) has some structure, by
  declaring it an object of some category of structures." Example 11 (natural deduction): P(T) is a multicategory whose
  morphisms are sequences of natural-deduction proof trees; composition is "the proof tree obtained from the tree βi by
  glueing the tree αj at each leaf occurrence of Bj" (i.e. raw trees, no normalisation/identification).
- Functoriality caveat p.16: "given a theory morphism H ... H(φ) does not necessarily belong to Γ' ... we run into a problem of
  indeterminacy ... This difficulty has an easy solution by restricting our attention to the subcategory Th_0 ↪ Th of
  axiom-preserving theory morphisms."
- Definition 12 (p.17): "A proof calculus is a 6-tuple P = (Sign, sen, ⊢, P, Pr, π) with: 1. (Sign, sen, ⊢) an entailment
  system; 2. P : Th_0 → Struct_P a functor; ... 3. Pr : Struct_P → Set a functor; ... 4. π : proofs ⇒ sen a natural
  transformation, such that for each theory T = (Σ, Γ), the image of π_T : proofs(T) → sen(T) is the set Γ•."
- Definition 16 (effective proof subcalculus, p.20): finite axiom sets (ax ⊆ P_fin(sen_0)), sentences and proofs in
  "Space" (decidable sets of finite objects); remark: there is a partial recursive search_T enumerating proofs of φ.
- Definition 23 (map of entailment systems, p.24, verbatim): "a map of entailment systems (Φ, α) : E → E' consists of a
  natural transformation α : sen ⇒ sen' ∘ Φ and an α-sensible functor Φ : Th_0 → Th'_0 satisfying the following property:
  Γ ⊢_Σ φ ⇒ α_Σ(Γ) ⊢'_Φ(Σ,∅) α_Σ(φ). We call (Φ, α) conservative if in addition we have, Γ ⊢_Σ φ ⇔ α_Σ(Γ) ⊢'_Φ(Σ,∅) α_Σ(φ)."
  (Φ maps theories to theories: signatures may be sent to theories with extra axioms — "∅'".)
- Definition 33 (map of proof calculi, p.29, verbatim core): "a map of proof calculi (Φ, α, γ) : P → P' consists of a map
  (Φ, α) : ent(P) → ent(P') of the underlying entailment systems together with a natural transformation
  γ : proofs ⇒ proofs' ∘ Φ such that the following cells are identical" [π' ∘ γ = α ∘ π, diagram]. "An embedding of proof
  calculi is a map of proof calculi (Φ, α, γ) such that (Φ, α) ... is a subentailment system and γ is injective."
  Example 32 / text: "'systematic' means that the maps γ_T should be independent of changes in syntax, i.e., that they should
  form a natural transformation".
- Proposition 34 (p.30): "The functor ent : PCalc → Ent has a right adjoint ( )♮ : Ent → PCalc." Proof: E♮ has proofs =
  theorems (thm, with Pr = 1_Set, π = inclusion) — the proof-irrelevant calculus.

### What is / is NOT preserved (INFERENCE from the definitions above)
- A map of proof calculi maps the SET proofs(T) = Pr(P(T)) (naturally in T, over α on conclusions). It is NOT required to be
  a morphism of the proof-theoretic STRUCTURES P(T) → P'(Φ T) (no preservation of composition/identities of proofs is
  demanded by Def 33 as quoted), and nothing is required about REFLECTING proof equality, except that "embeddings" require γ
  injective. There is no notion of proof-identity congruence in the framework: proof identity is whatever equality the
  chosen P(T) carries (raw trees in Example 11).
- Prop 34 shows every entailment system trivially has a proof calculus with proofs = theorems — so "having a proof calculus"
  in this sense imposes no proof-theoretic content (F02-style triviality at the proof level).
- F07: the effective subcalculus notion requires finite axioms and decidable spaces — infinitary proofs excluded by design.

---------------------------------------------------------------------------------------------------------------

## S5. Mossakowski, Diaconescu, Tarlecki, "What is a Logic Translation?" Logica Universalis 3(1):95–124 (2009)

- URL retrieved: https://www-live.dfki.de/fileadmin/user_upload/import/4478_mor.pdf. Header: ", 1–29 c 2009 Birkhäuser Verlag
  Basel/Switzerland" (preprint pagination 1–29, not journal pagination). Journal volume/pages/DOI (10.1007/s11787-009-0005-2)
  from web search listing only (SECONDARY). Status: VERIFIED_SOURCE (preprint text).

### Definitions (verbatim)
- Def 2.1 (p.3): ER = (S, ⊢), ⊢ ⊆ P(S) × S with reflexivity, monotonicity, transitivity. Note p.3: "substructural logics can
  be encoded into Tarskian entailment relations by considering whole sequents as sentences."
- Def 2.3 (p.3): "an ER-morphism ... is a function α : S1 → S2 such that Γ ⊢1 φ implies α(Γ) ⊢2 α(φ). If also the converse
  implication holds, the ER morphism is said to be conservative." Footnote 2: Prawitz–Malmnäs use "a more permissive notion
  of conservative translation where the equivalence is only required for Γ = ∅."
- Def 2.14 (p.9): "S1 ≤ER S2 iff there is some conservative α : S1 → S2." ("Note that ≤ER is only a pre-order").
- Def 2.22 (p.10) simple theoroidal ER morphism (α, ∆): "Γ ⊢1 φ implies ∆ ∪ α(Γ) ⊢2 α(φ)".
- §4.1 (p.21): "Relationships between institutions (and entailment systems) are captured mathematically by 'institution
  morphisms', of which there are several variants, each yielding a category under a canonical composition. For the purposes
  of this paper, institution comorphisms [29] seem technically most convenient, since they capture the intuition of coding of
  one logical system into another one. (The original notion from [28] works well for 'forgetful' morphisms ...)"
  Def 4.3: entailment system comorphism (Φ, α) with α_Σ an ER morphism natural in Σ; institution comorphism (Φ, α, β) adds
  model translation β backwards and satisfaction condition. Also: Def 4.9 "weakly exact"; model-expansive corridors.

### DECISIVE NEGATIVE RESULT (verbatim)
- "Proposition 2.25. The entailment relation of PHCL has maximal expressiveness among compact countable ERs (when admitting
  simple theoroidal ER morphisms)." Proof (p.11): "Let S be any compact ER. ... For each sentence φ, we introduce a
  propositional variable which we denote by α(φ). ∆ consist of all sentences α(φ1) ∧ ... ∧ α(φn) → α(φ) such that
  {φ1,...,φn} ⊢ φ in S." ... "Thus (α, ∆) is a conservative simple theoroidal ER morphism".
- "Corollary 2.26. ... Every compact countable ER can be conservatively embedded into CPLω, using a plain ER morphism."
- Conclusion p.26: "An interesting open question is the formalisation of 'structurality' of translations between logics,
  such that translations flattening out the structure (like that in Prop. 2.25) are ruled out. However, the notions studied in
  the literature so far [48, 9] are clearly too limited here, as they focus on propositional connectives only. A proper notion
  would have to take into account also binding structures like quantification."
- Example 2.4: Kolmogorov translation CPL → IPL is a conservative ER morphism; Def 2.14 example "CPL ≤ER IPL" — expressiveness
  via conservative translation is a preorder that can invert intuitions (stronger axiomatisation = less expressive).
- No notion of proof or proof identity anywhere in the paper (entailment relations and rooms/institutions only). Ack: "We
  thank Florian Rabe for pointing out the need for non-schematic translations".

### Relevance (INFERENCE)
- F02/F03 (strong): Prop 2.25 is a published, explicit "vacuous universality" theorem: a FIXED trivial logic (propositional
  Horn clauses: 3 rules refl/weak-ctr/cut) conservatively represents EVERY compact countable entailment relation, by putting
  the entire entailment relation into the environment ∆ (generally infinite, not even r.e.-restricted in the statement).
  This is the canonical counterexample showing conservativity (preserve+reflect derivability) alone, with an unrestricted
  environment, is trivial. Any ProofBasis criterion must exclude this (e.g., finite/recursive environment, structurality,
  compositional translation of rules, proof-level correspondence).
- F04/F08: Multiple non-equivalent notions of translation (plain vs theoroidal, morphism vs comorphism, schematic vs
  non-schematic, Prawitz–Malmnäs Γ=∅ variant); the authors pick comorphisms for "technical convenience" and leave
  "structurality" open. No canonical translation notion is claimed.

---------------------------------------------------------------------------------------------------------------

## S6. Rabe, "How to Identify, Translate, and Combine Logics?" JLC 27(6):1753–1798 (2017)

- URL retrieved: https://kwarc.info/people/frabe/Research/rabe_howto_14.pdf (author preprint; no venue/DOI printed; page
  numbers refer to preprint, ~40pp). Journal data (27(6) 1753–1798, DOI 10.1093/logcom/exu079) from web search only.
  OUP PDF returned 403. Status: VERIFIED_SOURCE (preprint). Rabe & Kohlhase "A scalable module system" (I&C 2013): NOT_ACCESSED.

### Definitions / theorems (verbatim)
- Def 2.35 (p.11): "A logical framework is a concrete Mmt language with distinguished constructors type and prop."
  Examples: LF (Ex 2.37), Isabelle/Pure (Ex 2.38: "one constructor for the name of each proof rule so that each proof can be
  written as an expression").
- §3.1 p.11: "We follow the Curry-Howard representation so that both logical symbols and axioms are represented as
  declarations, and both formulas and proofs are represented as expressions. In particular, axioms asserting F are just
  declarations of the form a : thm F."
- Def 3.1: logical theory = (Syn, o, thm) — syntax AND inference system are declarations in the theory Syn (p.11: "The
  syntax and inference system of L are represented as a theory Syn").
- Def 3.11 (p.14): "A Σ-proof of F is an expression p such that ⊢_{Syn,Σ} p : thm F."
- Remark 3.10 (p.13): with an equality judgment "expressions are identified up to equality" — i.e. proof identity is the
  FRAMEWORK's definitional equality (e.g. βη for LF, Ex 2.20/Rem 2.32), not an object-logic-specific congruence.
- "Theorem 2.31 (Preservation of Judgments). ... if ⊢_S J then ⊢_S' σ(J)" for well-formed morphisms; Remark 2.32: "Thm. 2.31
  can be extended to the equality judgment in a straightforward way." → morphisms translate proofs compositionally
  (homomorphic extension) and PRESERVE (framework) proof equality; reflection is not claimed.
- Def 3.35 logical morphism: "l : Syn → Syn' such that l(thm[x]) = thm'[k[x]] for some expression ... k[x] : o'".
- Def 3.39 (p.20): "We say l is proof-conservative if for all L-theories Σ and Σ-sentences F: if there is a l(Σ)-(dis)proof
  of k[l_Σ(F)], then there is a Σ-(dis)proof of F." Text: "proof-conservativity means to reflect (dis)proofs. (Like all
  well-formed morphisms, logical morphisms preserve (dis)proofs in any case.)" — reflection of EXISTENCE of proofs only.
- §4.1 p.27: "The homomorphic extension T_Σ(−) translates L-Σ-sentences and proofs to L'-T(Σ)-sentences and proofs."
- p.29 (verbatim caveat): assuming T proof-conservative "is impractically strong: It fails if we do not have any proof system
  for Syn at all, or if Syn and Syn' are too different to reflect the proofs. Essentially, showing the proof-conservativity of
  T is as hard as showing the soundness without using Thm. 4.8." Example: proof-conservativity of the modal→FOL morphism
  "is very hard to show".
- p.28: logical relations "cannot be defined generically for arbitrary expressions: For every constructor C, a separate insight
  is needed ... we currently do not know how to define it for an arbitrary one."
- §4.3 p.33: "it is straightforward to define identity/equivalence of logics as isomorphism. However, this requirement is too
  strong because intensional logical frameworks like LF make very few logical theories isomorphic." Ex 4.11: de Morgan
  translations d2(d1(∨)) = λx,y.¬¬(¬¬x ∨ ¬¬y) "equivalent but not equal to ∨". Hence identity of logics is defined only up
  to an extensional equality (Def 4.12–4.15) supplied as extra data.
- Related work p.38: "[MDT09] defines (conservative) morphisms between entailment relations to compare the strength of logics.
  These correspond to our (proof-conservative) logical morphisms."

### Relevance (INFERENCE)
- F01: Rabe/MMT is the strongest "logics-as-theories, translations-as-morphisms" account where PROOFS are first-class and are
  translated compositionally. But adequacy (bijection between object proofs and canonical framework terms) is not a general
  theorem here; it is a per-encoding obligation (LF-style). Proof identity = framework definitional equality (βη), preserved
  by morphisms but not reflected; no object-specific proof-identity congruence is part of the definition.
- F03: object inference rules are declarations in Syn (the environment/signature) — they are trusted constants, exactly the
  "trusted rules in the environment" pattern; the framework (LF typing) is the fixed machine.
- F08: Identity of logics needs a chosen extensional equality; logic-level isomorphism is too fine (Ex 4.11). Supports
  "no canonical basis".

---------------------------------------------------------------------------------------------------------------

## S7. Goguen & Burstall, "Institutions: Abstract Model Theory for Specification and Programming", JACM 39(1):95–146 (1992)

- URL retrieved: https://courses.grainger.illinois.edu/cs522/sp2016/InstitutionsAbstractModelTheory.pdf (scan of the JACM
  article; printed: "Journal of the Association for Computing Machinery, Vol 39, No 1, January 1992, pp 95-146", "© 1992 ACM
  0004-5411/92/0100-0095"; OCR quality poor). Status: VERIFIED_SOURCE (definition read).
- Definition 1 (p.101–102, OCR-repaired): "An institution I consists of (1) a category Sign, whose objects are called
  signatures, (2) a functor Sen: Sign → Set ... (3) a functor Mod: Sign → Cat^op giving for each signature Σ a category whose
  objects are called Σ-models ... and (4) a relation ⊨_Σ ⊆ |Mod(Σ)| × Sen(Σ) for each Σ ∈ |Sign|, called Σ-satisfaction,
  such that for each morphism φ: Σ → Σ' in Sign, the Satisfaction Condition m' ⊨_Σ' Sen(φ)(e) iff Mod(φ)(m') ⊨_Σ e holds".
  → purely model-theoretic; no proofs, no entailment rules.
- p.~103 (OCR): a variant "allows morphisms between sentences as well as between models; one might want to think of a
  morphism from one sentence to another as a 'proof' that the second follows from the first" (pointer only).
- Related-work paragraph (p.~98): "Meseguer [78] provides a general approach to logical systems which includes axiomatizations
  of the notions of entailment system ... and proof calculus, as well as institution. This avoids commitment to any particular
  style of proof theory".
- Proof-theoretic counterparts: Meseguer's entailment systems / proof calculi (S4); Π-institutions (Fiadeiro–Sernadas, cited by
  S5 Def 4.1 as "entailment system (or Π-institution)") — Π-institutions themselves NOT_ACCESSED.
- Relevance (INFERENCE): institutions cannot even express R1 proof-theoretically, let alone R3; useful only as the model side.

---------------------------------------------------------------------------------------------------------------

## S8. Meseguer, "Twenty years of rewriting logic", J. Logic and Algebraic Programming 81 (2012) 721–781 (survey)

- URL retrieved: https://courses.grainger.illinois.edu/cs522/sp2016/20YearsOfRewritingLogic.pdf (journal PDF; header
  "The Journal of Logic and Algebraic Programming 81 (2012) 721–781"). Status: VERIFIED_SOURCE. Used as SECONDARY for
  Meseguer 1992 TCS 96 ("Conditional rewriting logic as a unified model of concurrency", NOT_ACCESSED).
- §3.1.1 (verbatim): the initial model T_R "is obtained as a quotient of the just-mentioned deduction-based operational
  semantics, precisely by axiomatizing algebraically when two proof terms α : t → t' and β : u → u' denote the same concurrent
  computation. ... [α] = [β] iff both proof terms denote the same concurrent computation according to the 'true concurrency'
  axioms." Axioms: associativity/identity of composition; each f a functor ("sideways parallelism"); each rule r a natural
  transformation ("parallelism under one's feet").
- §3.4 (verbatim): "rewriting logic can faithfully represent its own theories and their deductions by having a finitely
  presented rewrite theory U that is universal, in the sense that for any finitely presented rewrite theory R (including U
  itself) we have the following equivalence R ⊢ t → t' ⇔ U ⊢ ⟨R̄, t̄⟩ → ⟨R̄, t̄'⟩".
  (INFERENCE / caution: this survey statement omits the hypotheses of the proved theorems — nonempty kinds, var(t')⊆var(t)
  in S1, no frozen operators, unsorted/unconditional in S1 — so it should not be cited as the precise theorem.)
- Survey p.~(§4.x list, verbatim): the initial model semantics "specializes to: ... (ii) for Petri nets to the Best-Devillers
  commutative process model ... (iii) for the parallel lambda calculus to its traditional model, shown to be a simple quotient
  of the initial model ... and (iv) for CCS to the proved transition causal model of Degano and Priami [130], shown to be a
  simple quotient of the initial model of the corresponding rewrite theory in [84]."
  (INFERENCE: for CCS and parallel λ, rewriting-logic proof-term equivalence is FINER than the target causal/true-concurrency
  model; an extra, encoding-specific quotient is needed — the generic exchange/functoriality equations are not the object
  formalism's independence relation.)
- §1 (verbatim): "Whenever anybody is selling you a semantic or logical framework you should be wary. ... it may create a big
  gap between what is represented and its representation. I call this the representational distance imposed by the
  framework." (Turing machines example.)

---------------------------------------------------------------------------------------------------------------

## Access summary
- VERIFIED: S1 (ENTCS 4 1996 Clavel–Meseguer), S2a (rmel.pdf extended preprint), S2b (ENTCS 71 WRLA'02), S3a (ENTCS 4 M-O&M),
  S3b (SRI TR 1993 M-O&M), S4 (General Logics, course copy), S5 (MDT preprint), S6 (Rabe preprint), S7 (G&B JACM scan), S8.
- NOT_ACCESSED: Clavel & Meseguer TCS 285(2) 2002 "Reflection in conditional rewriting logic" (403); Clavel, "Reflection in
  Rewriting Logic" (CSLI 2000); Clavel & Meseguer Reflection'96 "Axiomatizing reflective logics and languages" (where
  proof-calculus-level reflection definitions live); TCS 2007 journal typeset version of S2 (preprint used instead);
  Martí-Oliet & Meseguer Handbook of Philosophical Logic vol. 9 (2002) version; Meseguer 1992 TCS 96 (secondary via S3b, S8);
  Rabe & Kohlhase I&C 2013; Fiadeiro–Sernadas Π-institutions.

---------------------------------------------------------------------------------------------------------------

## Synthesis (INFERENCE, rwl agent)
1. R1 (derivability preserve+reflect) by a FIXED FINITE machine with theories-as-data is an ESTABLISHED RESULT (S1 Thm 3.2;
   S2 Thms 1,4,5,6), within stated hypotheses (finitely presentable; nonempty kinds; S1: unconditional, unsorted,
   var(rhs)⊆var(lhs); S2: conditional mel-based rewrite theories). Any project claim restricted to R1 is subsumed (F01) and is
   of the "universal interpreter" type (F02).
2. Reaching arbitrary object logics needs a second step (object logic → rewrite theory). That step is a case-by-case
   conservative map (linear logic theorems; sequent-calculus method), and "every finitely presented logic" is an explicit
   CONJECTURE of Martí-Oliet & Meseguer, pending a formal notion of finitely presented logic.
3. Proof identity: none of S1–S6 preserves AND reflects an object-logic proof-identity congruence in general.
   - General logics: proof calculi are unconstrained structures; maps of proof calculi act on proof SETS, no reflection;
     Prop 34: proofs = theorems is always available.
   - Rewriting logic: a fixed congruence (category + functoriality + E + exchange) on proof terms of the ENCODING; for linear
     logic the authors must add an extra quotient to get genuine categorical (product/η) identities (S3b p.34); for CCS/
     parallel λ, causal models are further quotients (S8).
   - U-level reflection: proof-level universality only CLAIMED (S1 p.7); S2 Lemma 1 shows many U-derivations per object
     derivation; S2 lists proof-object generation as future work.
   - Rabe/MMT: proofs translated compositionally, framework equality preserved, existence of proofs reflected only under
     "proof-conservativity", which Rabe calls "impractically strong" and as hard as soundness.
4. Vacuity benchmark: MDT Prop 2.25 — 3-rule propositional Horn logic conservatively represents every compact countable ER via
   an environment ∆ containing the whole entailment relation. Any ProofBasis criterion must rule this out; MDT state the needed
   "structurality" notion is OPEN (esp. with binders).
5. R4: Meseguer's exchange/functoriality equations are a precise prior notion of local independence of rewrite steps
   (true concurrency) — prior art for R4, but relative to the encoding's term structure; matching an object-level causal
   model requires extra quotients.
