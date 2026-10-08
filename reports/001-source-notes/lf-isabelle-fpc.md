# Source notes — tag `lf` (logical frameworks: LF, LLF/CLF, Isabelle/Pure, FPC)

Protocol: notes/PROTOCOL.md. Downloads in scratchpad/dl/lf/ (pdftotext -layout). Page numbers refer to the
retrieved version named per source. Retrieval date: 2026-10-08.

---------------------------------------------------------------------------------------------------
## 1. Harper, Honsell, Plotkin — "A Framework for Defining Logics"

- Bibliographic: R. Harper, F. Honsell, G. Plotkin. "A Framework for Defining Logics". Journal of the ACM 40(1),
  1993, 143–184 (journal data UNVERIFIED-MEMORY: the retrieved PDF carries no journal header/DOI). Conference
  version LICS 1987 (Ithaca) — the retrieved text says the work "was first reported in July, 1987 at the Symposium
  on Logic in Computer Science in Ithaca, New York" (p.3). LICS 1987 version itself: NOT_ACCESSED.
- URL retrieved: https://homepages.inf.ed.ac.uk/gdp/publications/Framework_Def_Log.pdf
  VERSION: author-prepared TeX typescript of the journal paper (PDF metadata: "TeX output 2000.11.27"), 37 pp.,
  no journal pagination. Page numbers below = printed page numbers of this typescript.
- Status: VERIFIED_SOURCE (all quotes below read in retrieved text).

### Fixed machine vs signature (what is fixed, what varies)
- Fixed machine = the LF type theory: three-level dependently typed λ-calculus (kinds K ::= Type | Πx:A.K;
  families A ::= a | Πx:A.B | λx:A.B | AM; objects M ::= c | x | λx:A.M | MN), the formation rules of Tables 1–2,
  and definitional equality (β only in the main text; βη discussed in the appendix) (§2.1, pp.3–5).
- Varies per logic = signature Σ: "A logical system is presented by a signature which assigns kinds and types to a
  finite set of constants that represent its syntax, its judgements (or assertions), and its rule schemes." (p.2)
  Signatures: "Σ ::= ⟨⟩ | Σ, a:K | Σ, c:A" (p.4). Each primitive inference rule is a constant: "To each primitive
  rule is associated a constant of higher type, with arguments the values of the parameters and the proofs of the
  premises." (p.17). E.g. "raa : Πp:o.true(¬¬p) → true(p)" and
  "imp-i : Πp:o.Πq:o.(true(p) → true(q)) → true(⊃ p q)" (p.19).
- Strength of the machine: "Its proof-theoretic strength is quite low (equivalent to that of the simply typed
  λ-calculus). In fact, the LF type system is chosen to be as weak as possible ..." (p.2).
  Theorem 2.6 (Decidability): "All assertions of the LF type system are recursively decidable." (p.9)
- TRUST (inference): the object logic's inference rules are TRUSTED declarations in Σ; the machine only checks
  well-typedness against Σ. Nothing in LF checks that Σ is a correct presentation — that is the job of an informal
  (meta-level, pen-and-paper) adequacy theorem proved separately for each signature.
- Rules vs proofs collapse: "rules are simply proofs of higher-order judgement type ... In LF there is no
  distinction between rules and proofs." (p.17)

### Definition of adequacy (verbatim, p.2)
"A signature is said to be an adequate presentation of a logical system iff there an encoding which is a
compositional bijection between the syntactic entities (terms, formulas, proofs) of the logical system and certain
valid LF terms (the so-called “canonical forms”) in that signature. By “compositional” we mean that substitution
commutes with encoding; in particular substitution in the logical system is encoded as substitution in LF ...
By “adequate” we mean “full” (does not introduce any additional entities) and “faithful” (encodes all entities
uniquely)."
Continuation (p.2): "There is some flexibility in the statement of adequacy for specific logical systems. ... we
achieve an adequate presentation of proofs of consequence, not just of pure theorems. This may not, in general, be
achievable, or even of interest. ... The adequacy theorem ensures, however, that this additional structure is a
conservative extension of the underlying logic."
NOTE: adequacy is a per-signature META-theorem, stated informally and proved by hand — it is NOT a single general
theorem of the framework; the paper proves it only for its examples.

### Canonical forms (p.9)
Definition 2.9: "A valid term U is canonical with respect to the valid signature Σ and valid context Γ iff U is in
normal form and every constant and variable occurrence in U is fully applied with respect to Σ and Γ."
(Canonical = long βη-normal forms, intention stated on p.9.) p.9 also: "Not all terms are convertible to canonical
form — consider, for example, a variable of functional type." (in the β-only system).

### Adequacy theorems (exact statements)
- Theorem 3.1 (Adequacy for Syntax, I) (p.12): "The encoding εX is a bijection between the terms of first-order
  arithmetic with free variables in X and the canonical forms of type ι in ΣFOL and ΓX. Moreover, the encoding is
  compositional in the sense that for t[x1,...,xn] a term with free variables in X = {x1,...,xn} and t1,...,tn
  terms with free variables in Y, εY(t[t1,...,tn]) = [εY(t1),...,εY(tn)/x1,...,xn]εX(t)."
  Proof method: injectivity evident; surjectivity via left-inverse δX defined on canonical forms using Lemma 2.10
  (the head of a canonical form of base type must be a variable/constant of ΓX/Σ).
- Theorem 3.2 (Adequacy for Syntax, II) (p.12): same shape for formulas (type o).
- Theorem 3.3 (p.15): same for HOL simple types / typed expressions.
- Theorem 4.1 (Adequacy for Proofs, I) (p.21): "For every first-order formula ϕ, the encoding εX,∆ is a bijection
  between valid proofs of ϕ with respect to (X, ∆) to canonical terms of type true(εX(ϕ)) in ΣFOL and ΓX,∆.
  Furthermore, εX,∆ is compositional in the sense that for any proof contexts (X,∆) and (X′,∆′) with
  X = {x1,...,xm} and ∆ = (ξ1:ϕ1,...,ξn:ϕn), if t1,...,tm are first-order terms whose variables are all in X′ and
  if Π1,...,Πn are valid proofs of ϕ1,...,ϕn with respect to (X′,∆′), then for any proof expression
  Π[x1,...,xm,ξ1,...,ξn] valid with respect to (X,∆),
  εX′,∆′(Π[t1,...,tm,Π1,...,Πn]) = [εX′(t1),...,εX′(tm),εX′,∆(Π1),...,εX′,∆′(Πn)/x1,...,xm,ξ1,...,ξn]εX,∆(Π)."
  [sic: one subscript prints as "εX′,∆(Π1)" in the typescript — likely a typo for εX′,∆′.]
  Context: ΓX,∆ = x1:ι,...,xm:ι, ξ1:true(εX(ϕ1)),...,ξn:true(εX(ϕn)) (p.21).
- Theorem 4.2 (Adequacy for HOL) (p.24): "There is a compositional bijection εA,∆ mapping valid proofs of a formula
  ϕ with respect to (A,∆) to canonical LF terms of type εA,o(ϕ) in ΣHOL and ΓA,∆." (proof omitted: "2" directly.)

### What the bijection is ON — DERIVATIONS, not just derivability
- The domain of Thm 4.1 is "valid proofs" = proof EXPRESSIONS Π of an explicit grammar
  "Π ::= hypϕ(ξ) | raaϕ(Π) | imp-iϕ,ψ(ξ:Π) | all-ix,ϕ(Π) | all-ex,ϕ,t(Π) | some-ex,ϕ,ψ(Π′, ξ:Π)" (p.18), taken
  modulo α-renaming of bound variables and bound occurrence markers ("We do not distinguish proof expressions that
  differ only in the choice of bound variables and bound occurrence markers", p.18). Discharge is by occurrence
  markers ξ ("it is hypothesis occurrences, and not hypotheses, that are discharged", p.18).
- So adequacy is a bijection on derivations up to α-equivalence (syntactic identity of natural-deduction trees with
  explicit discharge labelling) ↔ canonical LF terms. It therefore preserves AND reflects derivability (R1) and
  *syntactic* proof identity (identity of ND proof objects modulo α) — INFERENCE.
- It does NOT address any coarser proof-identity congruence (β/η normalisation of object proofs, permutative
  conversions, cut-elimination equivalence). The authors explicitly disclaim proof normalisation (p.25): "we are
  concerned with encoding formal proofs in arbitrary logical systems, and are not concerned with specifically
  intuitionistic problems such as proof normalization." LF definitional equality "is not to be confused with any
  equality that may be present in a represented logic" (p.3).
- Also: the encoding is of PROOFS OF CONSEQUENCE (open derivations, hypotheses = LF context variables).
- Subtlety recorded by authors (p.22): free-variable bookkeeping is "crucial to the correctness of the adequacy
  theorem" (proof of (∀x.ϕ)⊃(∃x.ϕ) mentions variable y not in end formula; usual presentations "appear to
  “build-in” the assumption that the domain of quantification is non-empty").

### Limitations stated in the source itself
1. Structural rules forced (p.16–17): "the consequence relation must satisfy weakening and contraction due to the
   properties of the LF function type ... Weakening and contraction are not satisfied by relevance and linear
   logics; in these cases either the encoding, the treatment of consequence, or, perhaps, LF itself must be
   changed."
2. Scope is a THESIS, not a theorem (p.17): "It is a thesis of the LF approach that pure Hilbert systems or systems
   of natural deduction can be adequately represented in LF. By “pure” we mean that there are no non-local
   applicability conditions on rules such as are associated with rules of proof which may only be applied to
   premises that do not depend on assumptions. (See Avron [2] for much further discussion of this point.)"
3. Only examples proved (p.22): "It would be interesting to etablish an adequacy theorem for a general notion of
   extension of first-order logic by additional axiom schemes and rules of inference." and "The adequacy theorem
   is a minimal correctness criterion, and does not delineate the extent to which the type structure of LF may be
   exploited in representing forms of inference that are not characteristic of the logical system being
   represented."
4. Admissibility / induction over proofs not expressible (p.23): "in view of the fact that weakening is an
   admissible rule of the LF type theory, judgements are “open” concepts. This precludes the encoding of a proof
   of admissibility of an inference rule that makes use of a principle of induction over a type of proofs. For
   example, the proof of the deduction theorem for a Hilbert-style formalization of first-order logic cannot be
   encoded as an LF term ..."
5. Rules of proof (e.g. necessitation in Hilbert S4) (p.23): "In many cases it is possible to exploit multiple
   judgements to achieve a faithful representation of such a system. (See [4] for further details.)" — i.e.
   requires changing the encoding (multiple judgements), not a uniform treatment.
6. Decidability presupposed (p.3): "(We take it for granted that proof checking in logical systems of interest is
   decidable.)"
7. Derived rules = LF terms of higher type (Schröder-Heister ∀E example, p.23) — derived rules are internal, but
   admissible rules are not.

### Relevance (INFERENCE)
- F01: LF is the canonical prior "fixed finite machine + per-logic signature" design. Its machine is finite and
  fixed (λΠ with β(η)), and Thm 4.1 is a bijection on DERIVATIONS (preserve + reflect derivability, syntactic proof
  identity up to α), compositional w.r.t. substitution of terms AND of proofs for hypotheses (R1, R2 partly). This
  is strong prior art against novelty of R1/R2 for ND-style intuitionistic-structural logics. But adequacy is
  per-signature and hand-proved; there is no general theorem "every logic of class C has an adequate signature".
- F03: In LF ALL object inference rules live in Σ (the environment) as trusted constants. If the project's
  "environment" holds assumptions/definitions only, LF is not a counterexample to the separation; if the project
  allows rule-schemata in the environment, it IS LF (and F03 bites: trust moves to Σ + an informal adequacy proof).
- F04/R3: LF says nothing about non-syntactic proof identity; definitional equality is explicitly NOT the object
  logic's equality. Any declared congruence (e.g. βη on ND proofs, permutations) is outside the adequacy notion.
- R2 resource discipline: LF forces weakening+contraction — the source's own stated reason linear/relevant logics
  need changed encodings or a changed framework (→ LLF/CLF, item 4).
- F05: "non-local applicability conditions" are explicitly excluded from the LF thesis (p.17).

---------------------------------------------------------------------------------------------------
## 2. Harper & Licata — "Mechanizing Metatheory in a Logical Framework"

- Bibliographic: R. Harper, D. R. Licata. J. Functional Programming 17(4–5), 2007, 613–673 (journal volume/pages
  UNVERIFIED-MEMORY; not printed on the retrieved PDF).
- URL retrieved: https://www.cs.cmu.edu/~rwh/papers/mech/jfp07.pdf (used). A different file (426,578 vs 448,962
  bytes) also exists at http://www.cs.cmu.edu/~drl/pubs/hl07mechanizing/hl07mechanizing.pdf with the same header;
  not compared in detail. VERSION: preprint "Under consideration for publication in J. Functional Programming", PDF created
  2007-04-19, 62 pp. Page numbers = PDF page index (matches printed page numbers).
- Status: VERIFIED_SOURCE.

### Definition of adequacy
- Abstract (p.1): "the syntactic and deductive apparatus of a system is encoded as the canonical forms of
  associated LF types; an encoding is correct (adequate) if and only if it defines a compositional bijection between
  the apparatus of the deductive system and the associated canonical forms."
- p.2: "an LF representation of a language is adequate iff it is isomorphic to the informal definition of the
  language." ... "These canonical forms are specified by an LF signature, which declares type and term constants,
  and by a world, which specifies the LF contexts under consideration." ... "we say that a higher-order LF
  representation is adequate iff there is a compositional bijection between the informal presentation of the
  language and the associated canonical forms, where a bijection is compositional iff it commutes with
  substitution."
- p.2: adequacy is proved EXTERNALLY: "The representation of an object language is not an inductive definition
  inside the LF type theory; indeed, higher-order encodings rely on negative occurrences of types. However,
  externally, the representation ... is an inductive definition because the canonical forms of LF are inductively
  defined."
- For DERIVATIONS (p.27): "Such a representation is adequate iff there is an isomorphism between the informal
  derivations of the judgement and the canonical forms of the associated type family."
- Theorem 3.11 (Adequacy for Typing Derivations) (p.33), parts 2–3 verbatim: "2. If γ ctx ⇝ Γ ctx and D derives
  γ ⊢ e : τ then there exist unique Me, Mt and M such that D :: γ ⊢ e : τ ⇝ Γ ⊢ M ⇐ of Me Mt.
  3. If γ ctx ⇝ Γ ctx and Γ ⊢ M ⇐ of Me Mt then there exist unique τ, e, and D such that
  D :: γ ⊢ e : τ ⇝ Γ ⊢ M ⇐ of Me Mt." (⇝ = the encoding relation symbol; rendered approximately from PDF.)
  => bijection on DERIVATIONS D (not just derivability).
- Compositionality for derivations is NOT proved here (p.33): "it is possible to define such an operation and then
  prove a compositionality theorem, analogous to Theorem 3.7, for the judgement ... However, because this
  compositionality result is not necessary for the remainder of this article, we elide the details."
- Theorem 3.7 (Compositionality for Terms) (p.26) is the substitution-commutation statement for syntax.
- Machine vs environment: Canonical LF (only canonical forms; hereditary substitution), parameterized by a
  subordination relation; per-language data = signature + world (allowed context shapes). Adequacy is relative to
  BOTH signature and world (p.2–3: "subordination-based transport of adequacy").
- Proof-relevance subtlety (p.27): Lemma 3.8 "(Uniqueness of Substitution Derivations) If D and D′ both derive
  [e2/x]e = e′ then D = D′." — needed for adequacy proofs, i.e. bijection-on-derivations is sensitive to whether
  side-judgements have unique derivations (INFERENCE: proof identity of auxiliary judgements leaks into adequacy).

### Limitations stated
- p.24 (exotic terms): "If, hypothetically, LF had an unrestricted case-analysis construct for analyzing terms of
  type tm, this lemma would not be true: a case-analysis of a variable would be an “exotic” canonical form of type
  tm, violating adequacy. Extensions of LF with other types must take care to preserve this property; in Concurrent
  LF, certain connectives are confined to a monad so that they do not interfere with this style of higher-order
  representation (Watkins et al., 2002)."  => the machine must be WEAK for adequacy; strengthening the fixed
  machine can break adequacy of existing signatures.
- p.55: LLF/CLF "ease the representation of language features for which LF provides no native support—e.g., a
  language with state can conveniently be represented using the linear connectives in LLF."
- p.57: "Research on Linear LF and Concurrent LF has shown how these frameworks permit facile representations of
  systems that are cumbersome to represent in LF ... The LF methodology for adequate representations scales to these
  richer frameworks; the programmer simply has a richer collection of types available for generating canonical
  forms." (note "cumbersome", not "impossible").

### Relevance (INFERENCE)
- F01: confirms the standard modern notion: adequacy = compositional bijection on canonical forms, for syntax AND
  derivations, proved per-encoding externally; this is exactly an R1+R2(substitution) preservation/reflection
  property, but only syntactic proof identity (R3 at the level of equality of derivation trees).
- F03: adequacy depends on signature + world + subordination — the "environment" carries far more than assumptions.
- Design lesson against a "strong" fixed algebra: adding operations (case analysis) creates exotic terms that break
  reflection (R1 reflect / R3 reflect). A universal algebra must be weak enough to avoid exotic inhabitants.

---------------------------------------------------------------------------------------------------
## 3. Pfenning — "Logical Frameworks" (Handbook of Automated Reasoning, ch. 17)

- Bibliographic: F. Pfenning. "Logical Frameworks". In A. Robinson, A. Voronkov (eds.), Handbook of Automated
  Reasoning, vol. II, ch. 17, pp. 1063–1147, Elsevier / MIT Press, 2001 (chapter number, volume, pages
  UNVERIFIED-MEMORY). The retrieved copy says "HANDBOOK OF AUTOMATED REASONING / Edited by Alan Robinson and Andrei
  Voronkov / © Elsevier Science Publishers B.V., 1999", "Chapter 1", "Second readers: Robert Harper, Don Sannella,
  and Jan Smith."
- URL retrieved: https://www.cs.cmu.edu/~fp/papers/handbook00.pdf. VERSION: author preprint of the chapter, 87 pp.,
  paginated 1–87 locally (NOT the published Handbook pagination). Page numbers = this preprint.
- Status: VERIFIED_SOURCE.

### What a framework is / what adequacy is
- p.3: "A logical framework is a meta-language for the specification of deductive systems." ... "Secondly, it
  should be feasible to prove (informally) that the representations of deductive systems in the framework are
  adequate so that we can trust formal derivations."  (Adequacy proofs: INFORMAL, by design.)
- p.7: "Adequacy theorems play a critical role in logical frameworks. They guarantee that we can translate
  expressions from the object language to objects in the meta-language, compute with them, and then interpret the
  results back in the object language. ... Generally, we would like the representation function to be a bijection,
  but this is not always necessary as long as we can translate safely in both directions."
  (NOTE: Pfenning here explicitly weakens adequacy below bijection — preserve+reflect suffices for some uses.)
- Theorem 3.2 (Adequacy) for first-order ND in LF (p.29), verbatim part 3: "The representation function is a
  bijection, and is compositional in the sense that the following equalities hold.
  ⌜[t/a]D⌝ = [⌜t⌝/a]⌜D⌝   ⌜[C/p]D⌝ = [⌜C⌝/p]⌜D⌝   ⌜[E/u]D⌝ = [⌜E⌝/u]⌜D⌝"
  Parts 1–2: if D derives A from labelled hypotheses then a1:i,...,p1:o,...,u1:nd⌜A1⌝,... ⊢ND ⌜D⌝ ⇑ nd⌜A⌝; and
  every canonical M of that type in that context is ⌜D⌝ for some such D. p.29: "The restriction to canonical objects
  is once again crucial, as are the restrictions on the form of the context."
  => bijection on DERIVATIONS; compositional for term-, proposition- and DERIVATION-substitution ([E/u]D, i.e.
  hypothesis discharge/cut-as-substitution).

### Proof identity (R3) — how LF handles it: as an EXPLICIT JUDGMENT IN THE SIGNATURE
- p.15: "We express local reductions and expansions via judgments which relate derivations of the same judgment."
- p.32–33 (§3.6 Higher-level judgments): "=⇒R : ΠA:o. nd A → nd A → type." (p.32) — local reduction is a
  type family declared in the signature, e.g. "redl imp : impe (impi (λu:nd A. D u)) E =⇒R D E." and
  "The adequacy theorem states that canonical LF objects of type ⌜D⌝ =⇒R ⌜D′⌝ constructed over the appropriate
  signature and in an appropriate parameter context are in bijective correspondence with derivations of
  D =⇒R D′. (p.33) We leave the precise formulation and simple proof to the diligent reader."
  => INFERENCE: in LF, any object-level proof-identity congruence is NOT part of the machine's definitional
  equality; it is a further user-declared (trusted) judgment in the signature, and its "adequacy" is again a
  per-signature informal theorem. Note LF's own βη happens to "model" object-level substitution, so the β-redex
  of the meta-level corresponds to the RHS "D E" — but the object-level reduction relation itself must be declared.

### Limitations stated
- p.65: "Parametric and hypothetical judgments can be implemented as functions in λΠ because these properties
  [exchange, weakening, substitution] match the properties of hypotheses. Logics such as linear logic in which
  assumptions do not satisfy these properties must be represented with different techniques. This has led, for
  example, to the development of the linear logical framework [Cervesato and Pfenning 1996]".
- p.70 (Substructural extensions): "Frameworks such as hereditary Harrop formulas or LF can encode linear and other
  substructural logics [Girard 1987], but their encodings are not as direct as one might hope. The reason is that
  linear assumptions (each of which must be used exactly once) can not be modeled as hypotheses in the meta-language
  (which satisfy weakening and contraction). For similar reasons, the store in the encoding of an imperative
  programming language cannot be modeled via hypotheses on the values of the cells in the store."
  Also: "Linear LF [Cervesato and Pfenning 1997] is a conservative extension of LF with linear hypotheses."
- p.47 (induction/open-endedness): "If the framework permitted an induction principle over the representation type
  i, we would no longer have an adequate encoding of first-order logic with two uninterpreted function constants.
  The encoding of the universal introduction rule ... now represents an ω-rule, since objects of type
  Πa:i. nd (A a) allow case analysis on a and are therefore no longer necessarily parametric in a. ... the adequacy
  of the representation is destroyed."
- p.47: "the type nd would not be inductively defined in the usual sense, because of the negative occurrence of nd
  in the type of impi. Straightforward attempts to formulate a valid induction principle for the type nd fail."
- p.50 (§5.2 Hilbert→ND translation): the relation "implements a total function ΠA:o. hil A → nd A which is not directly
  expressible in the framework." (meta-theorems are relations + external totality checks, not LF functions.)
- p.69 (de Bruijn's principle): "logical frameworks should be foundationally uncommitted and as weak as possible.
  This allows simple proofs of adequacy for encodings, efficient checking ... the simpler the logical framework, the
  more trusted its implementation is likely to be."
- p.71 (Polymorphism): "Adequacy of encodings using higher-order abstract syntax is also more difficult to prove,
  since the notion of η-long form is more complex ... and not preserved under substitution for type variables."
- Pfenning does NOT state a general "every logic in class C is adequately representable" theorem (searched: none
  found; INFERENCE from reading intro/conclusion and grep for "adequa").

### Relevance (INFERENCE)
- F01: the chapter is a survey confirming LF / hereditary Harrop (λProlog, Isabelle) as the established "fixed weak
  meta-calculus + per-logic signature" paradigm with per-encoding adequacy.
- F03/R3: proof-identity congruences live in the signature as trusted judgments — exactly the F03 risk if the
  project puts a declared congruence in the environment.
- F02 / strength: strengthening the fixed machine (induction, case analysis) destroys adequacy (exotic terms /
  ω-rule). This is a genuine NEGATIVE constraint on any "universal algebra": it must be parametric/weak.
- R2 resource discipline: LF cannot directly encode linear hypotheses -> motivates LLF (item 4).

---------------------------------------------------------------------------------------------------
## 4a. Cervesato & Pfenning — "A Linear Logical Framework" (LLF)

- Bibliographic: I. Cervesato, F. Pfenning. "A Linear Logical Framework". Information and Computation 179(1),
  2002, 19–75 (journal data UNVERIFIED-MEMORY: the retrieved file has a blank journal template header
  ", 1–72 ()" and "Received ; revised ; accepted", Academic Press copyright stub). Conference version LICS 1996
  (NOT_ACCESSED; cited in Pfenning's handbook chapter as [Cervesato and Pfenning 1996]).
- URL retrieved: https://www.cs.cmu.edu/~iliano/papers/ic02.pdf. VERSION: author manuscript in journal template,
  72 pp. Page numbers = PDF page index (= printed).
- Status: VERIFIED_SOURCE.

### Fixed machine
- λΠ⊸&⊤: LF's λΠ + linear implication ⊸, additive conjunction &, additive truth ⊤ (p.2). "we restrict the indices
  of type families to be linearly closed so that a type can depend only on intuitionistic assumptions, but not on
  linear variables" (p.2). Theorem 2.9 (Conservativity over LF) (p.35): for LF signature Σ, context Γ, terms U,V,
  LLF derivability of Γ ⊢Σ U ⇑↓ V (resp. context/signature validity) implies the LF one. p.35: "all the
  representation techniques, adequacy theorems, and examples developed for LF remain valid for LLF."

### Stated motivation: why LF is inadequate/indirect for linear/stateful systems (verbatim)
- p.2: "many constructs and concepts needed in common programming practice cannot be represented in a satisfactory
  way in meta-languages based on intuitionistic logic and intuitionistic type theory, such as LF. ... logical systems
  that, by definition (e.g. substructural logics) or by presentation (e.g. Dyckhoff’s contraction-free intuitionistic
  sequent calculus [17]), rely on destructive context operations require awkward encodings in an intuitionistic
  framework. Consequently the adequacy of the representation is difficult to prove and the formal meta-theory
  quickly becomes intractable."
- p.37: "Object formalisms admitting arbitrary operations on their context cannot be effectively encoded in LF: the
  standard technique, representing object context items as LF assumptions, is not sound in this case since LF
  assumptions are permanent. The alternative is to represent the object context as a term in LF and implement
  explicitly the operations required to access and manipulate it. This is undesirable since it makes the adequacy
  results difficult to prove ..."
- p.40: "the judgments-as-types methodology in λΠ cannot capture object languages that perform deletion on their
  context."
- p.53: LLF adequacy proofs "retain their simplicity ... This contrasts with other proposals, e.g., the treatment of
  linearity in LF itself [42], where adequacy theorems have complex proofs even for simple object languages."
  (=> linear logic IS encodable in plain LF, just indirectly; the claim is about directness/ease, not impossibility.)

### Proof identity / canonical forms limitation (KEY for R3/F04)
- p.64 (Conclusion), verbatim: "This choice of constructors is complete in the sense that they suffice to represent
  full intuitionistic or classical linear logic. Further, adding any other linear connective as a free type
  constructor destroys the property that usable canonical forms exist by introducing commuting conversions. This
  property is necessary in the proofs of adequacy theorems for encodings and also for the interpretation of LLF as
  an abstract logic programming language."
  => INFERENCE: the framework designers restrict the FIXED machine precisely so that its own term equality has
  canonical forms (no commuting conversions); positive connectives (⊗, 1, !, ⊕) are excluded from the machine
  because they would induce a non-trivial proof-identity congruence inside the framework.
- p.6: LF adequacy needs canonical (βη-long) forms although original LF used β only: "This discrepancy was known to
  Harper, Honsell and Plotkin when they first presented LF in 1987 [27]. A full treatment of the meta-theory of LF
  with βη-equivalence was successively devised by various authors [14, 20, 49] and resulted in non-trivial
  complications."

### Relevance (INFERENCE)
- R2/F01: resource discipline is not representable "directly" in LF; it requires changing the FIXED machine (LLF).
  So the LF family's answer to "one fixed machine for many foundations" was to keep EXTENDING the machine (LF →
  LLF → CLF), i.e. evidence against a single fixed finite machine being *natural* for all, but not a proof of
  impossibility (linear logic encodable in LF indirectly).
- F04: machine-level commuting conversions are deliberately avoided; this foreshadows CLF's monad.

---------------------------------------------------------------------------------------------------
## 4b. Watkins, Cervesato, Pfenning, Walker — "A concurrent logical framework I: Judgments and properties" (CLF)

- Bibliographic: K. Watkins, I. Cervesato, F. Pfenning, D. Walker. "A concurrent logical framework I: Judgments
  and properties". Technical Report CMU-CS-02-101, School of Computer Science, Carnegie Mellon University,
  "March 2002, revised May 2003" (printed on title page). Companion: Cervesato, Pfenning, Walker, Watkins,
  "... II: Examples" (CMU-CS-02-102) — NOT_ACCESSED. (TYPES 2003 post-proceedings paper — NOT_ACCESSED.)
- URL retrieved: https://www.cs.cmu.edu/~fp/papers/CMU-CS-02-101.pdf. VERSION: tech report, revised May 2003,
  42 PDF pp. Citations below give PRINTED page (PDF page = printed + 2).
- Status: VERIFIED_SOURCE.

### Fixed machine
- CLF = LLF (λΠ⊸&⊤) + a monad {S} whose synchronous types S ::= S1 ⊗ S2 | 1 | ∃x:A.S | A (App. A.1, printed p.32);
  abstract: "a conservative extension of the linear logical framework LLF with the synchronous connectives ⊗, 1,
  !, and ∃ of intuitionistic linear logic, encapsulated in a monad." Objects split into normal N, atomic R,
  expressions E ::= let {p} = R in E | M.
- Intro (printed p.3): LLF "corresponds to the largest freely generated fragment of intuitionistic linear logic
  [HM94, Bar96] whose proofs admit long normal forms without any commuting conversions."

### Proof identity built into the machine: concurrent equality (R3/R4 — central)
- Abstract: "A novel, algorithmic formulation of the underlying type theory concentrating on canonical forms leads
  to a simple notion of definitional equality for concurrent computations in which the order of independent steps
  cannot be distinguished."
- printed p.5: "For the LF and LLF fragments of CLF, this is the only notion of equality: two terms are equal if
  and only if they are α-equivalent. But expressions differ from the other categories of object in that they are
  subject to permutative conversions by which the monadic bindings can be reordered:
  (let {p1} = R1 in let {p2} = R2 in E) = (let {p2} = R2 in let {p1} = R1 in E)
  Of course, this rule is subject to the proviso that the bindings be independent: p1 and p2 must bind disjoint
  sets of variables, no variable bound by p1 can appear free in R2, and vice versa. ... We think of each let binding
  as a single computation step. Computation steps appearing in a single expression that are independent in the above
  sense can be thought of as occurring concurrently."
- printed p.5: "The notion of equality on CLF objects could be characterized as the least congruence relation
  including the above equation schema. The reason is that having separate syntactic classes of objects and
  expressions eliminates any need for commuting conversions. (We do not think of the permutative conversions as
  being commuting conversions.)"
- Definition 5 (Equality) (printed p.6): E1 =c E2 defined via concurrent contexts; "The judgment E1 =c E2 holds
  when E1 and E2 represent the same underlying concurrent computation even though their syntactic representations
  may differ."
- Theorem 6 (Decidability of equality) (printed p.21–22): items 1–6 incl. "4. Given E1 and E2, it is decidable
  whether E1 =c E2."
- INFERENCE: independence is purely SYNTACTIC/LOCAL — variable-disjointness of let-bindings (data-flow
  dependence), i.e. a Mazurkiewicz-trace-like quotient of the step sequence. It is a FIXED, framework-level
  proof-identity congruence (not declared per logic), and it is decidable. This is the closest prior art I found to
  "R3 + R4 inside a fixed machine": causal order = variable dependence between monadic steps.

### Adequacy: LLF fails, CLF's improved adequacy is modulo =
- LLF failure (printed p.13): "We might have hoped for an adequacy theorem relating LLF objects to concurrent
  computations of the Petri net, that is, equivalence classes of computations under rearragement of independent
  steps. But this strengthened adequacy theorem does not hold. ... the two LLF terms above correspond to
  computations differing only in the order of independent R and A steps ... But the structure of the LLF
  representation nonetheless requires that the two orderings be represented by different terms. In essence, the
  continuation-passing style of the representation forces a sequentialization of the computation."
  LLF adequacy that DOES hold (printed p.12): "Final state q1,...,qn can be reached from initial state p1,...,pm iff
  there is an object N such that ·;· ⊢ N ⇐ (q1 ⊸ ... ⊸ qn ⊸ G) ⊸ (p1 ⊸ ... ⊸ pm ⊸ G). Moreover, there is a
  bijection between sequences of firings of the transition rules of the Petri net and such canonical objects."
- Why not just add ⊗,1,! freely (printed p.13): "such an extension would not be conservative over the LF and LLF
  fragments of the type language. In fact, it would have a catastrophic effect on adequacy results for even very
  simple LF encodings. ... terms such as (let 1 = c in z : nat) destroy the bijective correspondence of the type nat
  with the set of natural numbers. Similar examples would arise in the presence of a constant of type A ⊗ B, !A,
  A ⊕ B, or 0. So the adequacy of the LF encoding is destroyed by the presence of even a single object constant
  having a type given by one of the new type constructors."
- Monad as the fix (printed p.14): "This encapsulation protects the pure LF and LLF fragments of CLF from the new
  constructs. All encodings already devised for LF or LLF remain adequate, and their adequacy proofs can remain
  exactly the same."
- Improved adequacy (printed p.14), verbatim: "Final state q1,...,qn can be reached from initial state p1,...,pm
  iff there is a object N such that ·;· ⊢ N ⇐ p1 ⊸ ... ⊸ pm ⊸ {q1 ⊗ ... ⊗ qn}. Moreover, there is a bijection
  between concurrent executions of the transition rules of the Petri net and equivalence classes of such objects
  modulo =."  NOTE: stated in prose for the example; no proof is given in this report (I saw none) —
  status: claimed, proof NOT seen (possibly in companion TR II, NOT_ACCESSED).
- Restriction (footnote 2, printed p.11–12): "One requirement of the LLF representation methodology, when applied to
  systems involving discrete sets of resources, is that the resources be distinguishable. Hence the tokens of the
  Petri net must carry unique labels. It is possible that proof irrelevance [Pfe01a] could offer a way of modeling
  indistinguishability."  => uncoloured/indistinguishable tokens (multiset identity) are NOT adequately captured.
- Limits of what concurrent equality gives (printed p.16): "Of course, even in CLF, abstract relations like the
  strong late bisimularity treated in their development would need to be treated explicitly. CLF’s concurrent
  equality simplifies such reasoning; it does not obviate the need for it."
- On other formalisms (printed p.16): Forum: "in Forum proofs cannot be manipulated as first-class objects—not
  even cut elimination is treated, let alone an equational theory on proofs." Proof nets (Perrier): "proof nets are
  treated only meta-theoretically—they are not first-class terms".

### Relevance (INFERENCE)
- R4/F01: CLF is strong prior art for building a causal-independence quotient (trace equivalence on steps) INTO a
  fixed framework's definitional equality, with decidable equality and adequacy "modulo =". Any novelty claim for
  R4 must engage CLF.
- F04: CLF shows a *single* fixed congruence (permutation of independent monadic steps) — it does NOT give
  per-logic proof identities (e.g. βη for ND, cut-elimination equivalence for LK, proof-net identity for MLL).
  Those would still be declared judgments in the signature (cf. Pfenning §3.6). So R3 "declared congruence,
  preserved and reflected" is NOT provided by CLF beyond its built-in one.
- F05/local vs global: CLF independence is local (variable occurrence). Labelled-token requirement shows identity
  of indistinguishable resources is a known gap.
- Machine design lesson: every extension of the machine risks exotic terms ("catastrophic effect on adequacy");
  encapsulation (monad) was needed to keep reflection.

---------------------------------------------------------------------------------------------------
## 5. Paulson — "The Foundation of a Generic Theorem Prover"

- Bibliographic: L. C. Paulson. "The Foundation of a Generic Theorem Prover". J. Automated Reasoning 5(3), 1989,
  363–397 (journal data UNVERIFIED-MEMORY). Retrieved version: University of Cambridge Computer Laboratory Technical
  Report UCAM-CL-TR-130 (HHP's bibliography cites "[39] Paulson, L. The foundations of a generic theorem prover.
  Tech. Rep. 130, Computer Laboratory, University of Cambridge, 1987."); the same text is on arXiv as cs/9301105
  (byte-different PDF, identical first pages).
- URLs retrieved: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-130.pdf (used) and
  https://arxiv.org/pdf/cs/9301105. VERSION: tech report / arXiv preprint, 37 pp.; page numbers = PDF page index.
  JAR published version NOT_ACCESSED; its theorem numbering may differ.
- Status: VERIFIED_SOURCE (for the TR/arXiv version).

### Fixed machine vs object-logic axioms
- Meta-logic M = fragment of intuitionistic higher-order logic (typed λ-calculus) with constants ⇒ (meta-
  implication), ⋀σ (meta-universal), ≡σ (meta-equality), and the fixed rules §2.4 (p.6): ⇒-I/⇒-E, ⋀-I/⋀-E (with
  eigenvariable condition), reflexivity/symmetry/transitivity of ≡, α, β, extensionality (≡ η), abstraction &
  combination rules.
- p.5: "The basic types and constants depend on the logic being represented. But they always include the type of
  propositions, prop, and the logical constants of M."
- p.4: "Implication expresses entailment; universal quantification expresses schematic rules and general premises;
  equality expresses definitions."
- Object logic L is presented as M_L = "a meta-logic obtained from M by adding types, constants, and axioms"
  (Definition 1, p.9). I.e. object inference rules are trusted AXIOMS (environment), the machine M is fixed.
- p.9: "The resemblance between the meta-level axioms and the rules should be regarded as a happy coincidence. An
  axiom formalizes not the syntax of a rule but its semantic justification."

### Faithfulness definition (verbatim, Definition 1, p.9)
"Let L be a logic and A1,...,Am, B be formulae of L. Let ML be a meta-logic obtained from M by adding types,
constants, and axioms. Suppose that [[−]] is a function mapping each formula A of L to a meta-formula [[A]] of ML.
Then say
 • ML is sound for L if, for every ML-proof of [[B]] from [[A1]],...,[[Am]], there is an L-proof of B from
   A1,...,Am.
 • ML is complete for L if, for every L-proof of B from A1,...,Am, there is an ML-proof of [[B]] from
   [[A1]],...,[[Am]].
 • ML is faithful for L if ML is sound and complete for L."
Preceding sentence (p.9): "The definition below is oriented towards natural deduction: it concerns entailments
rather than theorems."
- Theorems: "Theorem 2 Mipl is sound for ipl." (p.11); "Theorem 3 Mipl is complete for ipl." (p.12);
  "Theorem 4 Mifol is sound for ifol." (p.19); "Theorem 5 Mifol is complete for ifol." (p.21). Proofs by induction
  on (expanded) normal proofs in M (Prawitz normalisation of the meta-logic).
- ===> Faithfulness here is ONLY about DERIVABILITY of entailments (preserve + reflect), NOT a bijection on proofs.
  The soundness proof maps each meta-proof to some object proof, but no injectivity/identity statement is made.

### Proof identity / proof objects
- p.33: "Following the lcf tradition, Isabelle has never stored the steps of proofs. Milner’s representation of logic
  makes stored proofs unnecessary, a vital space savings. Now some people regard this as a mistake."
  => In this foundation there are no first-class proof objects; proof identity is not addressed at all.
  (Later Isabelle proof terms, Berghofer–Nipkow 2000 — UNVERIFIED-MEMORY, NOT_ACCESSED.)

### Limitations stated
- p.5: "the point is not to handle every esoteric logic." Examples cover only propositional and first-order
  (intuitionistic) logic.
- p.35: "Higher-order logic makes an adequate meta-logic from the theoretical perspective. We can draw on
  established proof theory to demonstrate soundness and completeness of the formalization of first-order logic:
  compare with the argument in Harper et al. [15]."  (again per-logic proofs, no general theorem)
- p.33 (on typed object logics): "The formalization of a typed logic in M involves a type of all object-terms,
  including those of no legal object-type; object-level type checking requires additional rules for type
  inference."

### Relevance (INFERENCE)
- F01: Isabelle/Pure is the second canonical "fixed finite meta-logic + object logic as axioms" design. Its
  correctness notion (faithful = sound+complete for entailment) covers R1 only. Weaker than LF adequacy.
- F03: object inference rules are axioms in the environment — exactly the "trusted rules hidden in the
  environment" pattern; Paulson explicitly says axioms encode semantic justification, so trust is semantic.
- R3: absent (no proof objects in this design).

---------------------------------------------------------------------------------------------------
## 6. Chihani, Miller, Renaud — "A Semantic Framework for Proof Evidence" (Foundational Proof Certificates)

- Bibliographic (as printed on HAL cover page): Zakaria Chihani, Dale Miller, Fabien Renaud. "A Semantic Framework
  for Proof Evidence". Journal of Automated Reasoning, 2017, 59(3), pp.287–330. DOI 10.1007/s10817-016-9380-6
  (DOI printed on HAL cover). HAL Id: hal-01390912 (v1, submitted 2 Nov 2016).
- URL retrieved: https://hal.inria.fr/hal-01390912/document (redirect to inria.hal.science). VERSION: author
  manuscript ("Journal of Automated Reasoning manuscript"), 48 PDF pp. incl. HAL cover. Printed page = PDF − 1;
  citations below give PRINTED page.
- Status: VERIFIED_SOURCE.

### Fixed kernel vs client definitions; trust boundary
- Kernel = implementation of the augmented focused sequent calculus LKFᵃ (classical) / LJFᵃ (intuitionistic),
  first-order. p.13: "An implementation of the augment focused proof system LKFᵃ will be called a kernel (for LKF)."
- Client-supplied FPC = five parameters (p.13): "The five parameters—polarization, certificate terms, indexes,
  clerks, and experts—are described below and are, collectively, called an FPC." p.13: "A foundational proof
  certificate consists of a proof object written in a suitable language along with the semantic definition of that
  language."
- Soundness by erasure (p.13): "The LKF proof system can be recovered from LKFᵃ by removing all occurrences of the
  syntactic variable Ξ and by removing all premises with a subscripted e or c ... For this reason, any proof in LKFᵃ
  is a proof in LKF, which guarantees the soundness of the LKFᵃ system."
  => INFERENCE: the client clerk/expert predicates can only RESTRICT/GUIDE search over a fixed sound calculus; they
  cannot add inference rules. Trust is in the kernel (LKF/LJF + logic-programming engine), not the FPC. This is
  the clearest prior-art design that AVOIDS F03 (client definitions are untrusted).
- Design desiderata (p.4): "D1: A simple checker can, in principle, check if a proof certificate denotes a proof.
  Simplicity is helped by the fact that the checker need only implement the atoms of inference and the rules of
  chemistry. Since both of these are small and closed sets, the checker size and complexity can, in principle, be
  limited." "D3: A proof certificate is intended to denote a proof in the sense of structural proof theory."
- Underlying theorem (cited, proved elsewhere, [60] = Liang & Miller): Theorem 1 (p.11): "Let B be a classical,
  first-order formula. 1. If B is a theorem then for every polarization B̂ of B, the sequent ⊢ · ⇑ B̂ has an LKF
  proof. 2. If B̂ is a polarization of B and if ⊢ · ⇑ B̂ has an LKF proof then B is a theorem. 3. If a sequent has
  an LKF proof, it has a cut-free LKF proof."

### What is preserved — derivability ONLY (explicitly)
- p.30 (§9 "Checking proofs instead of provability"): "when the checker has successfully executed a given FPC over a
  given proof certificate, the only guarantee our kernel provides is that the formula is, in fact, a theorem. The
  kernel, in and of itself, does not guarantee any other properties about certificates."
- p.21–22 (resolution FPC is not faithful to the proof format): "while we have described a sound checker, one might
  wish to have a converse guarantee, namely, that if the checker succeeds with a given certificate term, then that
  term denotes a proper resolution refutation. That property is not, however, the case for the certificate format
  that we have described above." The example uses "a unifier that is not most general and it has an additional
  literal. The proof certificate mechanism above will actually validate this entailment which is not a problem from
  the point-of-view of soundness."
  => INFERENCE: FPC gives R1-preservation (sound) for the target formula, NOT reflection of the client proof format
  and NOT a bijection on proofs; §9 shows one can write FPCs enforcing structural restrictions, case by case.
- p.13: "While a kernel based on it may not be able to deal with certain aspects of proofs—such as “is this proof
  minimal”—it can provide a means to ascertain that a given logical formula is a theorem."
- p.19: client code can include auxiliary predicates: "Note that the predicate lemma is not part of the kernel but
  is code supplied by the resolution refutation certificate" (it is search guidance, still under kernel soundness).

### Scope / limitations stated
- p.41: "In this paper, we have limited ourselves to first-order logic." Higher-order focusing: "more flexible
  polarity assignments have not yet been studied explicitly." LF/λΠ as FPC: "should be possible" (future work);
  linear logic kernel "should be a rather straightforward exercise" (future work).
- p.41 (Theories): "Proving theorems from theories can generally be encoded in logic by viewing theories as
  additional assumptions. ... Many questions related to reasoning with theories—such as how to related conclusions
  derived from different theories—are not immediately treated by reference to an underlying logic".
- p.41 (§12.4): parallelism / minimal commitment to rule order (expansion trees, proof nets, multifocusing) is
  listed as a kernel EXTENSION topic — i.e. not handled by the FPC kernel itself.

### Relevance (INFERENCE)
- F01: FPC = a fixed small kernel + untrusted client semantics, covering many proof FORMATS (resolution, CNF,
  matings, Horn, natural deduction etc. per the paper) — but within one or two FOUNDATIONS (first-order classical /
  intuitionistic). It is "many proof languages, one logic", not "many foundations".
- F03: FPC is the positive model for avoiding trusted rules in the environment (soundness by erasure).
- R1 reflect / R3: explicitly NOT provided (only theoremhood guaranteed); proof identity not addressed;
  causal/parallel structure deferred to multifocusing (R4 future work).

---------------------------------------------------------------------------------------------------
## 7a. Avron, Honsell, Mason (,Pollack) — "Using Typed Lambda Calculus to Implement Formal Systems on a Machine"

- Requested: Avron, Honsell, Mason, Pollack, J. Automated Reasoning 9(3), 1992, 309–354 (journal data
  UNVERIFIED-MEMORY) — JOURNAL VERSION NOT_ACCESSED.
- What WAS retrieved: the PRELIMINARY tech report: A. Avron, F. A. Honsell, I. A. Mason, "Using Typed Lambda
  Calculus to Implement Formal Systems on a Machine", LFCS Report ECS-LFCS-87-31 (also CSR-237-87), University of
  Edinburgh, July 1987 (no Pollack). URL: http://www.lfcs.inf.ed.ac.uk/reports/87/ECS-LFCS-87-31/ECS-LFCS-87-31.pdf
  — scanned image PDF, 40 pp.; text obtained by local OCR (tesseract 5.3.4) — quotes below may contain OCR noise;
  symbols garbled where noted. Printed page = PDF page − 2.
- Status: VERIFIED_SOURCE for the 1987 report (via OCR); the 1992 JAR paper's statements may differ.

### Adequacy notion in this (1987) report — weaker than HHP
- p.6: "An ELF translation of a language, however, will be satisfactory only if adequate. Informally an ELF
  signature will be adequate iff for each syntactic category of the language there is a compositional surjection
  from the ELF type, corresponding to that category, onto the category itself."  (SURJECTION, not bijection.)
- p.8: "Definitions of adequacy and faithfullness of signatures can be given even with respect to consequence
  relations and proofs thereof."
- Case studies (contents p.ii): Kleene 3-valued logic, FOL with choice, Hilbert-style modal logics, ND S4,
  classical λ-calculus, CBV λ-calculus, λI, linear λ-calculus, Hoare logic, two-register-machine Hoare logic; each
  with an "Adequacy and Faithfulness Property".
  - Property 1 (Kleene 3-valued, p.10): derivability iff inhabitation, and "Moreover, there is a compositional
    bijection between proofs in the natural deduction system and proof terms such as t above."
  - Property 3 (Hilbert S4, p.15): "1. There is a compositional surjection between proofs in the Hilbert-type system
    of S4 that ϕ1,...,ϕn ⊢ ψ and terms t such that: ... t : True(ϕ1) → ··· → True(ϕn) → True(ψ)" and "2. There
    is a compositional bijection between proofs in the Hilbert-type system of S4 that ϕ1,...,ϕn ⊢v ψ and terms t
    such that: ..." [Valid judgement] (OCR-normalised).
    => INFERENCE: for the impure (rule-of-proof) consequence relation, only a SURJECTION onto proofs is claimed —
    i.e. multiple LF terms per object proof: derivability is captured but proof identity is NOT reflected.
- Prawitz-style ND S4 (p.19): "The adequacy theorem above applied to proofs of theorems in Prawitz’ system. It does
  not applies to proofs of sequents. ... In order to fully and faithfully internalize also partial proofs in
  Prawitz we need to introduce a third judgement: True."

### Limitations stated
- p.7: "a constant ∧I of type T(ϕ) → T(ψ) → T(ϕ∧ψ) (which we have in the standard internalizations of classical and
  intuitionistic logics) would be inadequate for relevance or linear logic, despite the fact that ϕ∧ψ is a theorem
  of these logics whenever ϕ and ψ are." (OCR-normalised symbols)
- p.7: "A proof of a hypothetical judgement therefore corresponds to either a rule of derivation or a derivable rule
  of the system, not simply a rule of proof or an admissible rule."
- p.13–14 (necessitation): "It would not be sound, accordingly, to internalize the necessitation rule by the
  standard method of introducing a constant Nec ... since such a constant would force the deducibility of □ϕ from
  any set of assumptions which entail ϕ." Fix: two judgements "True" and "Valid".
- p.8 ("ELF thesis"): "It can be taken as a kind of an “ELF thesis” that well-behaved natural-deduction formalisms
  are those that can be directly encoded in the ELF".
- p.5–6: well-formedness of expressions "often defined by formal systems of a much higher complexity which cannot
  be directly encoded in the weak type theory of ELF."
- p.28: linear λ-calculus signature "can be taken as a basis for the ELF encoding of the external consequence
  relation of the minimal fragment of linear logic" (i.e. linear logic only via its external consequence relation).

### Relevance (INFERENCE)
- F04/R3: Early LF practice already shows adequacy degrading from bijection to surjection when the encoding must
  add judgement structure (impure modal rules). Different encodings of the SAME logic differ on proof identity.
- F08: choice of judgements (True/Valid/...) is an encoding decision; the "basis" is not canonical.

---------------------------------------------------------------------------------------------------
## 7b. Gardner — "Representing Logics in Type Theory" (PhD thesis)  *** NEGATIVE RESULTS ***

- Bibliographic: Philippa Gardner, "Representing Logics in Type Theory", PhD thesis, University of Edinburgh,
  January 1992 (graduation July 1992) (title page). LFCS report ECS-LFCS-92-227 (also CST-93-92) (per LFCS web page).
- URLs retrieved: http://www.lfcs.inf.ed.ac.uk/reports/92/ECS-LFCS-92-227/ (abstract page) and
  http://www.lfcs.inf.ed.ac.uk/reports/92/ECS-LFCS-92-227/ECS-LFCS-92-227.pdf — scanned image PDF, 161 pp.; text by
  local OCR (tesseract 5.3.4), so quotes may contain OCR noise (symbols normalised by me where obvious, e.g.
  ELF+ printed by OCR as "ELF*"; S4 as "Sq"/"S,"). Printed page = PDF page − 8.
- Status: VERIFIED_SOURCE (via OCR of the thesis/report).

### Setting
- ELF+ = ELF (LF) presented as a Pure Type System whose types are split into sorts, types and judgements, so that
  representation can be DEFINED uniformly (p.5): "The major advantage of ELF+ is that it allows us to give precise
  definitions of representation. Such definitions are not possible with ELF since information is lost during
  encoding; the adequacy theorems of ELF representations are only applicable to particular encodings and cannot
  be generalised. Using these definitions, we give examples of ‘good’ representations, prove that linear and
  relevant logics ... cannot be well-represented and show that the representation of Hilbert-style S4 ... is not as
  natural as, for example, the representation of first-order logic." (p.1)
- Critique of LF (p.4): "The adequacy theorem for first-order logic only applies to this particular representation,
  since it refers to specific constants ι, o and true declared in Σ. It cannot be stated generally as information
  is lost in the encoding ... in some cases, this results in logics with different consequence relations being
  specified by the same signature, which is clearly undesirable." Also p.93–94: "With representations in ELF it is
  not possible to define the basic notion of an encoding since, in some cases (example 5.1.15), a single signature
  is used to specify logics with different consequence relations."
- p.6: "Not all logics can be represented in ELF+ (or in ELF). There are various reasons for this: different
  behaviours of the logic variables, the consequence relation having properties incompatible with those of the
  entailment relation, rules with ‘awkward’ side-conditions."

### Definitions (OCR-normalised paraphrase + fragments)
- Def 5.1.1 (Encoding, p.94–95): triple (η, ε, δ): η maps syntactic classes to ELF+ sorts; ε_X, δ_X map term
  expressions / judgements with free variables in X to βη-long ELF+ terms, with variables mapped by fixed
  bijections; conditions: well-typedness, "3. the ε_X and δ_X are compositional" (commute with substitution),
  "4. the interpretation is sound" (j1..jm ⊢ j implies inhabitation of δ_X(j) in context of δ_X(ji)).
- Def 5.1.4 (Adequate, p.98): "An encoding (η, ε, δ) is adequate when 1. η: S → sort^Σ is a bijection; 2. for each
  finite sequence X ... of variables, the functions ε_X : T(X) → texp and δ_X : J(X) → judge are bijections;
  3. the interpretation is complete" (inhabitation implies consequence).  => adequacy at the level of the
  CONSEQUENCE RELATION (derivability, R1), with bijection on syntax & judgements only.
  Remark (p.99): "weakly adequate" = injective + complete.
- Def 5.2.1/5.2.3 (Complete / Natural encoding, p.116–118): add χ_{X,Δ} mapping proof expressions to ELF+ terms,
  compositional w.r.t. substitution of proofs; NATURAL iff (η,ε,δ) adequate, χ restricted to valid proof expressions
  is a BIJECTION onto inhabitants of the judgement, and completeness.  => bijection on DERIVATIONS (cf. HHP).

### Theorems (exact numbering from thesis)
- "5.1.7 THEOREM Logics which are adequately represented in ELF+ have intuitionistic consequence relations
  (definition 3.2.13)." (p.100) — proof: from substitution and thinning lemmas of ELF+, cut, weakening and
  substitution transfer back to the logic.
- "5.1.8 COROLLARY There are no adequate representations of linear and relevant logics [Gir87] [Dun84] in ELF+."
  Proof: "The consequence relations of these logics are not intuitionistic since they do not satisfy the
  weakening condition in definition 3.2.13." (p.100)
- "5.2.5 THEOREM Logics whose representations in ELF+ are natural have intuitionistic consequence relations with
  proofs." (p.118)
- 5.2.6 EXAMPLE (p.118–119): "Natural deduction-style S4 [Pra65] ... does not have a natural representation in ELF+
  since, although its consequence relation is intuitionistic, its consequence relation with proofs is not
  preserved under substitution of proof expressions." (substituting a derivation into a □-rule premise yields a
  non-derivation — a NON-LOCAL side condition breaks proof-level compositionality.)
- 5.2.7 / 5.2.9 THEOREM: signatures for first-order / higher-order logic provide NATURAL encodings (p.119).
- "5.2.11 THEOREM The representation of Hilbert-style S4 in ELF+, given in example 5.1.12, is not natural." (p.120;
  proof sketch: "eight possible shapes for the valid proof expressions and nine possible shapes for the
  inhabitants of judgements" + compositionality ⇒ no bijection). (S4 Hilbert IS adequately represented, 5.1.14.)
- "5.2.13 THEOREM The signature Σ_HPL does not provide a natural encoding of Hilbert-style propositional logic."
  (p.120) — Example 5.2.12: Hilbert propositional logic is adequately (consequence-level) encoded via the ND
  signature "although it is not natural as one would expect."
- "5.1.16 THEOREM The signature Σ_λI does not provide an adequate encoding of the λI-calculus in ELF+." (p.110)
- Ch.6 (p.129ff, not read in detail): adequate / natural encodings ⇔ indexed isomorphisms of indexed categories
  (Thm 6.4.4, 6.5.x — statements seen only as headings via grep; NOT verified in detail).
- Future work (p.139): "We cannot represent a multiset of assumptions using a context in a standard type theory
  since we have unrestricted use of declared variables in this context. In order to give a ‘true’ representation
  of a linear consequence relation in a type theory, it is necessary to adapt the standard notion of context."

### Relevance (INFERENCE) — strongest negative evidence in this batch
- This is a genuine NEGATIVE THEOREM (relative to a precise uniform definition): with a fixed LF-like machine whose
  hypothetical judgement is the framework's context, any adequately represented logic has an intuitionistic
  (cut + weakening + substitution) consequence relation; linear and relevant logics provably have NO adequate
  representation in that sense. Caveat: the impossibility is relative to Gardner's notion (logic consequence ↔
  framework entailment with object hypotheses as framework hypotheses); indirect encodings (contexts as data,
  cf. Cervesato–Pfenning p.37) are excluded by definition, not refuted.
- R3/F04: even for logics with an adequate (derivability-level) representation, the PROOF-level ("natural")
  representation can fail: Hilbert-style S4 and Hilbert propositional logic via ND signature; Prawitz ND-S4 fails
  because its consequence-with-proofs is not closed under proof substitution. So "preserve and reflect a declared
  proof identity" can fail even when R1 holds — directly supports F04.
- F01: Gardner explicitly frames ELF+ as giving "apparently for the first time, general definitions of correct
  representation" — prior art for a uniform "adequacy" definition across logics; any project claiming novelty for
  a general representation-correctness criterion must cite it.

---------------------------------------------------------------------------------------------------
## SYNTHESIS (INFERENCE unless quoted above)

1. Fixed machine vs environment.
   - LF: machine = λΠ (β or βη, canonical forms), decidable, "proof-theoretic strength quite low". Environment =
     signature Σ (syntax constants, judgement families, ONE CONSTANT PER INFERENCE RULE) + (Harper–Licata) a
     "world" of allowed contexts + subordination. ALL object-logic inference rules are trusted Σ-declarations.
   - Isabelle/Pure (Paulson 1989): machine = fragment of intuitionistic HOL with ⇒, ⋀, ≡; object rules = AXIOMS.
   - LLF/CLF: machine EXTENDED (⊸,&,⊤; then monad with ⊗,1,!,∃) precisely because LF could not directly encode
     resources/state/concurrency — the "fixed machine" was changed twice for new classes of logics.
   - FPC: machine = focused LKF/LJF kernel (first-order); client FPC (clerks/experts) is UNTRUSTED and can only
     restrict search (soundness by erasure). Only design here that structurally avoids F03 — but single foundation
     (FO classical/intuitionistic), and preserves theoremhood only.

2. Adequacy = bijection on DERIVATIONS (not just derivability) in LF:
   HHP Thm 4.1 / Pfenning Thm 3.2 / Harper–Licata Thm 3.11: bijection between object derivations (modulo α and
   explicit discharge labelling) and canonical LF terms, compositional = commutes with substitution of terms AND
   of derivations for hypotheses. So LF adequacy preserves+reflects derivability AND syntactic proof identity.
   It is a per-signature, informal (pen-and-paper, induction on canonical forms) meta-theorem, NOT a framework
   theorem; HHP call the scope a "thesis" and only prove FOL and HOL. Paulson's "faithful" = sound+complete for
   entailment only. FPC = soundness for theoremhood only. AHM 1987: some properties only "compositional surjection".

3. Proof identity beyond syntax (R3, F04):
   - LF definitional equality is explicitly NOT the object logic's equality (HHP p.3); HHP disclaim proof
     normalization (p.25). Object-level reductions are represented as user-declared judgements (Pfenning §3.6,
     =⇒R type family) — i.e. any declared proof-identity congruence lives in the trusted signature.
   - LLF: machine deliberately restricted so that no commuting conversions arise ("adding any other linear
     connective ... destroys the property that usable canonical forms exist by introducing commuting conversions").
   - CLF: ONE built-in congruence: permutation of independent monadic let-steps (variable-disjointness), decidable;
     claimed adequacy "between concurrent executions ... and equivalence classes of such objects modulo =" for
     labelled Petri nets (proof not seen). Requires labelled tokens (indistinguishable resources not handled).

4. Negative results / design constraints found in the sources (strongest for the audit):
   - Strengthening the fixed machine destroys adequacy (exotic terms): case analysis/induction over the
     representation type makes ∀I an ω-rule (Pfenning p.47; Harper–Licata p.24); adding ⊗/1/!/⊕/0 freely is
     "catastrophic" for adequacy of even nat (CLF p.13). => a universal fixed algebra must be weak/parametric, and
     extensions must be encapsulated.
   - Weakening/contraction forced by LF's function space; linear/relevant need different encodings or framework
     (HHP p.17; Pfenning p.65, p.70; AHM p.7).
   - Non-local applicability conditions (rules of proof, necessitation) are outside the LF thesis; need multiple
     judgements (HHP p.17, p.23; AHM p.13–15).
   - Admissible rules / induction over proofs not internal (HHP p.23; Pfenning p.47, p.50).
   - GARDNER 1992 (strongest): Thm 5.1.7 + Cor 5.1.8 — adequately represented logics in ELF+ have intuitionistic
     consequence relations; "There are no adequate representations of linear and relevant logics ... in ELF+."
     Thm 5.2.11/5.2.13 + Ex 5.2.6 — adequate-but-not-natural (no bijection on proofs) for Hilbert S4, Hilbert
     propositional logic; Prawitz ND-S4 has no natural representation. => R1 can hold while R3 fails.
   - LLF sequentialises independent steps: "this strengthened adequacy theorem does not hold" (CLF p.13).

5. Threat mapping:
   - F01: partially realised — LF (+ HHP/HL adequacy) already gives fixed finite machine + per-logic signature with
     bijection on derivations, for ND-style "pure" logics with structural contexts. Not realised: a general theorem
     covering "many foundations"; non-syntactic proof identity; substructural without changing the machine.
   - F03: LF/Isabelle put rules in the environment (signature/axioms) — exactly F03. FPC avoids it but at the cost
     of a single fixed logic.
   - F04: frameworks avoid object-level proof-identity in the machine except CLF's single permutation congruence.
   - F05: "pure" = no non-local applicability conditions (HHP) — global conditions excluded from the LF thesis.
   - F08: AHM show encoding choices (judgement structure) change whether adequacy is bijective or only surjective;
     Gardner shows the same logic (Hilbert prop. logic) can be adequately but not naturally encoded.

6. Sources NOT accessed: HHP LICS 1987 version; AHMP JAR 1992 journal version (only the 1987 AHM LFCS report);
   Paulson JAR 1989 journal version (only TR-130/arXiv); CLF companion TR II (CMU-CS-02-102) and TYPES 2003 paper;
   Cervesato–Pfenning LICS 1996; Harper–Licata JFP published version (preprint used). All journal volume/page data
   not printed on retrieved copies is UNVERIFIED-MEMORY.
