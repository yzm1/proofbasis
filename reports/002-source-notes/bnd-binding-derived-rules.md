# bnd — binding/substitution algebra; derived vs admissible rules; Gardner Ch.6; Twelf totality

Agent tag: bnd. Task 002 source extraction. All downloads in `t002/dl/bnd/`. Statuses per PROTOCOL.md.
"INFERENCE" = my own reasoning, not a claim of any source.

---

## S1. Fiore, Plotkin, Turi — "Abstract Syntax and Variable Binding (Extended Abstract)", LICS'99

- Bib: M. Fiore, G. Plotkin, D. Turi. Abstract Syntax and Variable Binding. Proc. 14th IEEE LICS, 1999,
  pp. 193–202 (page range as cited in Fiore–Mahmoud ref [11]; not printed on the retrieved copy). No DOI printed.
- URL retrieved: https://homepages.inf.ed.ac.uk/gdp/publications/Abstract_Syn.pdf (author-hosted extended
  abstract, 10 pp, no page numbers printed). Status: VERIFIED_SOURCE.
- Binding signature (§2): "A binding signature [31] Σ = (O, a) consists of a set of operations O equipped with an
  arity function a : O → N*. An operator of arity ⟨n1,...,nk⟩ has k arguments and binds ni variables in the
  i-th argument (1 ≤ i ≤ k)."
- Thm 2.1: "The presheaf of terms TVα associated to a binding signature Σ (equipped with the syntactic algebra
  structure) is a free Σ-algebra on the presheaf of variables V." (Setting: presheaves F̂ = Set^F, F = finite
  cardinals and all functions.)
- Monoids (§3): substitution tensor •, unit V. "Monoids in F̂, with maps f : (X, µ, ι) → (X′, µ′, ι′) given by
  morphisms f : X → X′ such that f ◦ ι = ι′ and f ◦ µ = µ′ ◦ (f • f), form a category Mon(F̂) ..."
  Prop 3.4: "The categories of clones and of monoids in F̂ = (F̂, •, V) are equivalent."
  Cor 3.6: "(TV, σ, ηV) is a monoid in F̂" with σ the simultaneous substitution.
- Σ-monoids (§4): "F-monoids, i.e., quadruples X = (X, µ, ι, h), where (X, µ, ι) is a monoid ... and (X, h) is an
  F-algebra such that [diagram (16): h compatible with µ via the strength] commutes; morphisms are maps of C which
  are both F-algebra and monoid homomorphisms."
  Thm 4.1: "T I = (T I, σ, ηI, φI) is an initial F-monoid." Hence TV = initial Σ-monoid.
  "By definition of morphism in Σ-Mon(F̂), the initial algebra semantics is compositional, it preserves the
  variables and it always satisfies the semantic substitution lemma [35, Lemma 4.6]."
  Thm 4.2: Σ-substitution algebras ≃ Σ-monoids.
- Scope/limits stated in source: UNSORTED (mono-sorted) binding signatures; intro says multi-sorted signatures
  and dependent types "are yet to be tackled" (paraphrase of the visible intro column; verbatim fragment:
  "...ies with dependent types are yet to be tackled"). No judgements, no derivations, no hypotheses-as-
  assumptions, no notion of derivability. Only TERMS with binding and substitution.
- Relevance (INFERENCE): A Σ-monoid morphism = a map that commutes with variables, the operators, and
  simultaneous substitution. This is a precise standard notion of "representation commuting with substitution"
  for SYNTAX. It does not by itself cover substitution of derivations for hypotheses, because FPT has no
  judgement/derivation layer; one must take a (multi-sorted, dependently indexed) extension where hypotheses are
  variables of a "proof sort". Not a solution to F01 by itself; it does sharpen R2.

## S2. Fiore & Mahmoud — "Second-Order Algebraic Theories (Extended Abstract)"

- Bib: M. Fiore, O. Mahmoud. Second-Order Algebraic Theories. arXiv:1308.5409v1 [cs.LO], 25 Aug 2013 (printed on
  PDF). Venue MFCS 2010, LNCS 6281 — UNVERIFIED-MEMORY (not printed on retrieved copy).
- URL: https://arxiv.org/pdf/1308.5409 (12 pp). Status: VERIFIED_SOURCE.
- Terms (§2): contexts with two zones, metavariables with arity m : [m] and variables:
  "m1 : [m1], ..., mk : [mk] ⊲ x1, ..., xn". Rules (Variables), (Metavariables) "Θ⊲Γ ⊢ ti (1≤i≤m) / Θ⊲Γ ⊢
  m[t1,...,tm]", (Operators) for o : (n1,...,nk).
- Metasubstitution: "maps m1:[m1],...,mk:[mk] ⊲ Γ ⊢ t and Θ ⊲ Γ, x⃗i ⊢ ti (1≤i≤k) to Θ ⊲ Γ ⊢ t{mi := (x⃗i)ti}"
  with clause "mℓ[s1,...,sm]{mi := (x⃗i)ti} = tℓ[s′j/xℓ,j]" (two-level substitution calculus).
- Second-Order Equational Logic (Fig. 1): (Axiom), (Equivalence), and "(Extended metasubstitution)" — the single
  congruence rule. "Second-Order Equational Logic is a conservative extension of (First-Order) Equational Logic"
  (stated as a result of Fiore–Hur [10]).
- Soundness & completeness (§3, quoted from [10]): "For an equational presentation (Σ, E), the judgement
  Θ ⊲ Γ ⊢ s ≡ t is derivable from E iff A |= (Θ ⊲ Γ ⊢ s ≡ t) for all (Σ, E)-models A."
- Def 4.1: "A second-order algebraic theory consists of a cartesian category T and a strict cartesian
  identity-on-objects functor M → T that preserves the exponentiable object (0)." Lemma 4.1: M is "initial amongst
  cartesian categories equipped with an exponentiable object".
- Algebraic translation: "a second-order algebraic translation T → T′ is a functor F : T → T′ such that T′ = F T."
- Syntactic translation (§5): "A syntactic translation τ : Σ → Σ′ between second-order signatures is given by a
  mapping from the operators of Σ to the terms of Σ′ ... o : (m1,...,mk) ↦ m1:[m1],...,mk:[mk] ⊲ · ⊢ τo"; extended
  by "τ(o((x⃗1)t1,...,(x⃗k)tk)) = τo{mi := (x⃗i)τ(ti)}".
  Lemma 5.1 (Compositionality): "The extension of a syntactic translation between second-order signatures commutes
  with substitution and metasubstitution."
  Equational translation: τ such that every axiom's image "is derivable from E′". Lemma 5.2: "preserves second-order
  equational derivability." Thm 5.2: "The categories SOAT and SOEP are equivalent."
  Abstract claims: "This gives the first formalisation of notions such as encodings and transforms in the context of
  languages with variable binding." Example 5.1: CPS transform as a syntactic translation.
- What is NOT there: unityped ("generalisation to the multi-typed case should be evident" — their words); only
  EQUATIONAL logic (no relational judgements, no hypotheses-as-proof-assumptions, no dependent types). Translations
  preserve derivability; there is no reflection/conservativity requirement in the definition of translation.
- Relevance (INFERENCE): A syntactic translation is EXACTLY "each operator realised as a term (with metavariables)
  in the target, extended homomorphically via the target's own metasubstitution". This is a standard, precise
  definition of "operator realised as a derived operation" for binding syntax — i.e. the second-order analogue of a
  Lawvere-theory morphism / Fujiwara "derivor". F08 threat: compositionality under substitution+metasubstitution
  holds AUTOMATICALLY for every such translation (Lemma 5.1), so it is not by itself discriminating; the
  discriminating content must be in reflection/faithfulness (not in their definition).

## S3. Gardner, "Representing Logics in Type Theory", PhD thesis, Edinburgh, CST-93-92 / ECS-LFCS-92-227, July 1992

- Source: local OCR `scratchpad/ocr/gardner_all.txt` (OCR of a scan; page numbers below are THESIS page numbers
  as printed; OCR-normalised; symbol noise corrected by me where obvious, flagged [norm]). Status: VERIFIED_SOURCE
  (via OCR text).
- Definitions needed:
  - Def 5.1.4 (thesis p.98) "An encoding (η, ε, δ) is adequate when 1. η : S → sort^Σ is a bijection; 2. for each
    finite sequence X = (x1^σ1,...,xn^σn) of variables, the functions εX : T(X) → texp^Σ and δX : J(X) → judge^Σ are
    bijections; 3. the interpretation is complete; that is ... ΓX, p1:δX(j1),...,pm:δX(jm) ⊢Σ _ : δX(j) implies
    {j1,...,jm} ⊢_X j" [norm]. (The underlying "encoding" (Def 5.1.1, not extracted) already requires compositional
    ε, δ and SOUND interpretation of the consequence relation — see proof of Thm 6.4.1.)
  - Thm 5.1.7 (p.100): "Logics which are adequately represented in ELF+ have intuitionistic consequence relations
    (definition 3.2.13)." Cor 5.1.8: "There are no adequate representations of linear and relevant logics [Gir87]
    [Dun84] in ELF+." Proof: "do not satisfy the weakening condition".
  - Def 5.2.1 (p.116) complete encoding (η, ε, δ, χ), with χX,Δ : P(X,Δ) → terms, satisfying
    "1. χX,Δ(p) = h(p) for p declared in Δ" (proof variables ↦ framework variables);
    "2. ... {p1:j1,...,pm:jm} ⊢ Π : j implies ΓX, ΓΔ ⊢ χX,Δ(Π) : δX(j)" (soundness);
    "3. the χX,Δ are compositional; that is, for proof expressions Π ∈ P(Y,Θ) and Σ1,...,Σm ∈ P(X,Δ) and term
    expressions t1,...,tn ∈ T(X), we have χX,Δ(Π[Σ⃗, t⃗/q⃗, y⃗]) = χY,Θ(Π)[εX(t⃗), χX,Δ(Σ⃗)/εY(y⃗), χY,Θ(q⃗)]" [norm].
    → This IS "commutes with substitution, including substitution of derivations for hypotheses, realised by the
    framework's own substitution", stated as a definition, in 1992.
  - Def 5.2.3 (p.118) natural: (1) (η,ε,δ) adequate; (2) χX,Δ : VP(X,Δ) → proof^Σ_{X,Δ} "is a bijection"; (3) complete.
  - Thm 5.2.5: natural representations ⇒ "intuitionistic consequence relations with proofs".
  - Thm 5.2.11 (p.120): "The representation of Hilbert-style S4 in ELF+, given in example 5.1.12, is not natural."
    Thm 5.2.13: "The signature Σ_PL does not provide a natural encoding of Hilbert-style propositional logic."
    (Proof idea: compositionality + counting of term shapes ⇒ χ cannot be bijection.) Example 5.2.12: same consequence
    relation, adequate but not natural. → proof identity / proof-shape is NOT determined by the consequence relation.
- Chapter 6 (pp.122–137):
  - Def 6.1.1 strict indexed category = functor F : C^op → Cat. Def 6.1.2 indexed functor = (base functor, natural
    transformation F → G ∘ base^op).
  - **Def 6.1.3 (p.124)**: "An indexed isomorphism is an indexed functor whose base functor is an isomorphism and
    whose natural transformation is a natural isomorphism." [norm: OCR "isomorphisms an"]
  - §6.2: "We provide a methodology for presenting logics with intuitionistic consequence relations as indexed
    categories, where the term expressions provide the base category and the consequence relation the fibres."
    Prop 6.2.1: term category (objects: sequences of distinct logic variables; morphisms: tuples of terms;
    composition = substitution). Prop 6.2.3: indexed category L with fibres = PREORDERS of judgement sequences under
    ⊢_X; reindexing = substitution. Remark: needs closure under substitution and cut.
  - §6.3 Prop 6.3.3: ELF+ side E: base = sort category, fibres = preorders under inhabitation.
  - Thm 6.4.1: every encoding (η,ε,δ) of LOG "with an intuitionistic consequence relation" determines an indexed
    functor (ε_base, ε): L → E. Text after Def 6.4.2: "The converse of theorem 6.4.1 does not hold; that is, not all
    indexed functors give rise to encodings. For example, there is no guarantee that an indexed functor preserves the
    ordering, or even the length, of tuples."
  - **Thm 6.4.4 (p.132)**: "Let (η, ε, δ) be an encoding of a logic LOG with an intuitionistic consequence relation
    in ELF+ and let (ε_base, ε) : L → E be the indexed functor determined by (η, ε, δ), where L : A^op → Cat and
    E : B^op → Cat. Then (η, ε, δ) is adequate if and only if (ε_base, ε) is an indexed isomorphism." [norm]
  - §6.5 Prop 6.5.1: complete indexed category Lp — base = term category, fibre objects = sequences of proof
    assumptions, morphisms = tuples of proof expressions, composition = substitution of proofs for proof variables;
    hypothesis: "LOG ... with an intuitionistic consequence relation with proofs"; "consequence relation being closed
    under substitution of logic and proof variables". Prop 6.5.3: Ep analogously with ELF+ terms.
  - Thm 6.5.5: a complete encoding determines an indexed functor (ε_base, cε) : Lp → Ep. Remark: "we believe that,
    with more analysis ..., the converse may be proved. This analysis is beyond the scope of this thesis."
  - **Thm 6.5.7 (pp.136–137)**: "Let (η, ε, δ, χ) be an encoding of a logic with an intuitionistic consequence relation
    with proofs in ELF+, and indexed functor (ε_base, cε) : Lp → Ep be the indexed functor determined by (η,ε,δ,χ)
    ... Then (η, ε, δ, χ) is natural if and only if (ε_base, cε) is an indexed isomorphism." Proof: "Adapt lemma
    6.4.3 ... similar to that of theorem 6.4.4."
- Character of the theorem (my reading): it is a CHARACTERISATION of adequacy/naturality FOR A GIVEN encoding
  (the indexed functor "determined by" a given syntactic encoding is iso iff the encoding is adequate/natural). It is
  NOT a classification theorem "every indexed isomorphism comes from an adequate encoding" — Gardner explicitly
  disclaims the converse of 6.4.1 / 6.5.5. Lemma 6.4.3 depends on the particular functor preserving order and length
  of tuples. Proofs are informal (thesis, not machine-checked). Hypotheses: intuitionistic consequence relation
  (weakening, substitution closure, cut — Def 3.2.12/3.2.13 not re-extracted here), "with proofs" for 6.5;
  framework fixed as ELF+ (Gardner's variant of LF); fibres are preorders in §6.4 (derivability only); in §6.5
  fibres carry proof expressions but NO equations on proofs (identity of proofs = syntactic identity of proof
  expressions / canonical terms).
- Relevance (INFERENCE): F01 — Gardner already gives, for one framework, (i) the definition "natural encoding"
  = adequacy + bijection on proofs + compositionality w.r.t. substitution of terms AND proofs for variables, and
  (ii) an algebraic (indexed-category) reformulation. The project's R1+R2 for LF-style encodings is therefore
  ESTABLISHED TERMINOLOGY, not new. Negative results: weakening-free (linear/relevant) logics have no adequate
  ELF+ encoding (F05/F04 threat: resource discipline breaks "hypotheses as framework variables"); Hilbert-style
  systems are adequate but not natural (proof identity is presentation-dependent ⇒ F04).

## S4. Pfenning — "Logical Frameworks", Ch. 17 (draft numbered "Chapter 1") of Handbook of Automated Reasoning

- Bib: F. Pfenning. Logical frameworks. In A. Robinson, A. Voronkov (eds), Handbook of Automated Reasoning, Elsevier
  (printed: "c Elsevier Science Publishers B.V., 1999"; published 2001 — UNVERIFIED-MEMORY). Second readers Harper,
  Sannella, Smith.
- URL: https://www.cs.cmu.edu/~fp/papers/handbook00.pdf (author preprint, 87 pp; page numbers below = preprint).
  Status: VERIFIED_SOURCE.
- Thm 3.2 (Adequacy), p.29: "1. If D is a derivation of A from hypotheses ⊢N A1,...,⊢N An labelled u1,...,un ... then
  a1:i,...,p1:o,...,u1:nd⌜A1⌝,...,un:nd⌜An⌝ ⊢ND ⌜D⌝ ⇑ nd⌜A⌝. 2. If [same context] ⊢ND M ⇑ nd⌜A⌝ then M = ⌜D⌝ for a
  derivation D as in part 1. 3. The representation function is a bijection, and is compositional in the sense that
  the following equalities hold. ⌜[t/a]D⌝ = [⌜t⌝/a]⌜D⌝ ; ⌜[C/p]D⌝ = [⌜C⌝/p]⌜D⌝ ; ⌜[E/u]D⌝ = [⌜E⌝/u]⌜D⌝".
  → explicit compositionality for substitution of a DERIVATION E for a HYPOTHESIS u, realised by LF substitution.
- p.11: "Substitution in the object language is modeled by β-reduction in the meta-language." p.11: open-world:
  "we can always add further constants without destroying the validity of earlier representations. In logic
  programming, this is called the open-world assumption."
- §4.5, pp.45–46 derived rules: global definitions c:A = M "can be viewed as ... introducing a derived rule A with
  derivation M (if the type A represents a judgment)". "The cut rule for LF is admissible, which means that any
  instance of this rule can be eliminated from a derivation."
- §5, pp.47–48 (why admissible ≠ representable as LF term): "If the framework permitted an induction principle over
  the representation type i, we would no longer have an adequate encoding of first-order logic with two
  uninterpreted function constants. The encoding of the universal introduction rule ... now represents an ω-rule,
  since objects of type Πa:i. nd (A a) allow case analysis on a and are therefore no longer necessarily parametric
  in a. ... the adequacy of the representation is destroyed."
- §5.1, p.49 (relational metatheory): "type-checking the signature declaring hilnd does not guarantee the validity
  of the meta-theorem we were trying to prove. For this, some additional conditions have to be satisfied: mode
  correctness ..., termination ..., and coverage which guarantees that for each possible combination of input
  values a case in the definition of hilnd will be applicable."
- p.57: "While the result of each individual computation of this form is guaranteed to be correct, the
  higher-level judgment is only partially verified since termination and coverage of all possible cases are
  properties outside the scope of the type-checker." (Status as of the 1999 preprint; Twelf later added these
  checks — see S7.)
- Relevance (INFERENCE): Pfenning gives the operative distinction: derived rule = closed LF term of higher type
  (stable under signature extension, by weakening); admissible rule = total relation established by induction over
  canonical forms of a FIXED (closed-world) signature, not an LF term. Adding induction to the framework destroys
  adequacy (F03/F02: an environment that can do case analysis on parameters is an ω-rule machine).

## S5. Harper, Honsell, Plotkin — "A Framework for Defining Logics"

- Bib: R. Harper, F. Honsell, G. Plotkin. A Framework for Defining Logics. J. ACM 40(1):143–184, 1993
  (UNVERIFIED-MEMORY for journal data; not printed on the typescript).
- URL: https://homepages.inf.ed.ac.uk/gdp/publications/Framework_Def_Log.pdf (author typescript, 37 pp; pages =
  typescript page numbers). Status: VERIFIED_SOURCE.
- §1, p.2: "it is possible to view inference rules as primitive proofs of higher-order judgements. This allows us to
  collapse the notions of rule and proof into one, and eliminates the distinction between primitive and derived rules
  of inference." Adequacy: "A signature is said to be an adequate presentation of a logical system iff there an
  encoding which is a compositional bijection between the syntactic entities (terms, formulas, proofs) of the
  logical system and certain valid LF terms (the so-called 'canonical forms') in that signature. By 'compositional'
  we mean that substitution commutes with encoding; in particular substitution in the logical system is encoded as
  substitution in LF (which relies on the identification of object-logic variables with the variables of LF). By
  'adequate' we mean 'full' (does not introduce any additional entities) and 'faithful' (encodes all entities
  uniquely)." Also: "it is possible to express the derivability of inference rules and to consider proofs under the
  assumption of these new rules of inference. The adequacy theorem ensures, however, that this additional
  structure is a conservative extension of the underlying logic."
- Thm 4.1 (Adequacy for Proofs, I), p.21: εX,Δ bijection between valid proofs of φ wrt (X,Δ) and canonical terms of
  type true(εX(φ)); compositional: "εX′,Δ′(Π[t1,...,tm, Π1,...,Πn]) = [εX′(t1),...,εX′,Δ′(Π1),...,εX′,Δ′(Πn) /
  x1,...,xm, ξ1,...,ξn] εX,Δ(Π)". → substitution of PROOFS for proof-assumption variables ξi.
- p.21–22: "The adequacy theorem is a minimal correctness criterion, and does not delineate the extent to which the
  type structure of LF may be exploited in representing forms of inference that are not characteristic of the
  logical system being represented."  Derived rule example: Schroeder-Heister ∀-elim witnessed by an LF term.
- p.23 (admissible rules NOT encodable): "With regard to derived rules, it is important to stress that in view of
  the fact that weakening is an admissible rule of the LF type theory, judgements are 'open' concepts. This
  precludes the encoding of a proof of admissibility of an inference rule that makes use of a principle of induction
  over a type of proofs. For example, the proof of the deduction theorem for a Hilbert-style formalization of
  first-order logic cannot be encoded as an LF term in the usual encoding of Hilbert systems in LF. A closely-related
  point is the representation of rules of proof in a Hilbert system, which are rules that may be applied only if the
  premises are pure theorems (the rule of necessitation ...). In many cases it is possible to exploit multiple
  judgements to achieve a faithful representation of such a system."
- Relevance (INFERENCE): HHP is the primary source that "compositional" = commutes with substitution INCLUDING proof
  substitution, realised by framework substitution. So hypothesis (1) is ESTABLISHED (for LF), dating to 1987/1993.
  The F03 issue is real and named in HHP: primitive rules are signature constants (trusted environment content).

## S6. Fiore & Hur — "Second-Order Equational Logic (Extended Abstract)", CSL 2010

- Bib: M. Fiore, C.-K. Hur. Second-Order Equational Logic (Extended Abstract). CSL 2010, LNCS 6247, pp. 320–335
  (venue/pages from web-search snippet only — UNVERIFIED; not printed on retrieved copy).
- URL: https://www.cl.cam.ac.uk/~mpf23/papers/Types/soeqlog.pdf (author preprint, 15 pp). Status: VERIFIED_SOURCE.
- §2 Signatures: "A (second-order) signature Σ = (T, O, |−|) is specified by a set of types T, a set of operators O,
  and an arity function |−| : O → (T* × T)* × T. This definition is a typed version of the binding signatures of
  Aczel [1]". Contexts: "Metavariable typings are parameterised types: a metavariable of type [σ1,...,σn]τ, when
  parameterised by terms of type σ1,...,σn, will yield a term of type τ."  (SIMPLY typed; no dependent sorts.)
- Abstract: the logic "is synthesised from the model theory. Hence it is necessarily sound"; "conservative extension
  of Birkhoff's (First-Order) Equational Logic"; "Two completeness results ... semantic completeness of equational
  derivability, and the derivability completeness of (bidirectional) Second-Order Term Rewriting."
- (Soundness) §6: "if the judgement Θ ⊲ Γ ⊢ s ≡ t : τ is derivable from E then A |= (Θ ⊲ Γ ⊢ s ≡ t : τ) for all
  (Σ, E)-models A." (Conservativity) §7. (Completeness) §8: "if A |= (Θ ⊲ Γ ⊢ s ≡ t : τ) for all (Σ, E)-models A then
  Θ ⊲ Γ ⊢ s ≡ t : τ is derivable from E." "(Completeness of Second-Order Term Rewriting) For every equational
  presentation, Θ ⊲ Γ ⊢ s ≡ t : τ iff Θ ⊲ Γ ⊢ s →* t : τ" [norm: arrow is bidirectional rewriting].
- No translation/morphism notion in this paper (that is in Fiore–Mahmoud S2).
- Relevance (INFERENCE): this is a logic of EQUALITY between binding terms. It can host a declared proof-identity
  congruence (R3) for proof terms written in a second-order signature, but it has no judgement of derivability with
  hypotheses; dependency (proof terms indexed by formulas) needs a dependently sorted version — Fiore's
  "Second-order and dependently-sorted abstract syntax" (LICS 2008) exists per UNVERIFIED-MEMORY; not retrieved.

## S7. Hofmann — "Semantical Analysis of Higher-Order Abstract Syntax", LICS 1999

- Bib: M. Hofmann. Semantical Analysis of Higher-Order Abstract Syntax. Proc. 14th IEEE LICS, Trento, July 1999,
  pp. 204–213 (from lics.siglog.org BibTeX, retrieved). DOI 10.1109/LICS.1999.782616 (from web-search snippet —
  UNVERIFIED).
- URL: author PostScript lics99hoas.ps.gz via https://web.archive.org/web/20250829115603id_/https://www.dcs.ed.ac.uk/home/mxh/lics99hoas.ps.gz
  (gz header: "last modified: Fri Apr 30 17:07:44 1999"; converted ps2pdf→pdftotext; pagination from conversion,
  section numbers used). Status: VERIFIED_SOURCE (conversion lost some math symbols; [norm] where restored).
- What HOAS types denote (§3–4): base category S = finite sets of variables with λ-substitutions as morphisms;
  Tm = presheaf of λ-terms mod α ("In fact, Tm is the representable presheaf S(−, {y})"). Key iso (18):
  "(Tm ⇒ F)X ≅ F(X ∪ {x}) when x ∉ X. Therefore, in particular (Tm ⇒ Tm)X ≅ Tm(X ∪ {x}). Note that Tm ⇒ Tm is not
  representable." Lam : (Tm⇒Tm) → Tm natural "Since λ-abstraction also commutes with substitution".
- Prop 4.1: "If M(x1,...,xn) is a meta-language term of type tm with free variables xi : tm then there exists an
  object level term t(x1,...,xn), namely t = dec([[M]]) such that [[M]] = [[⌜t⌝]]". "Using a logical relation it is
  possible to show the stronger result that M =βη ⌜dec([[M]])⌝ [norm] (23) which is the usual statement of adequacy.
  Notice that our proof of existence of object-level terms corresponding to meta-language terms did not rely on any
  notion of term rewriting in the meta-language."
- §7 (Var ⇒ −) in presheaves over the category of variables (renamings): Prop 7.2 gives a right adjoint; Var ⇒ Tm
  carries the initial-algebra / recursion principle used "to define substitution".
- Scope: SYNTAX (untyped λ-terms; π-calculus mentioned), induction principles, tripos/predicate logic; NOT a theory
  of encodings of derivations or of proof identity.
- Relevance (INFERENCE): semantic justification that HOAS function types over the term presheaf denote "terms with
  one more free variable", i.e. compositional adequacy is a Yoneda-style fact in the substitution-presheaf model —
  supports that hypothesis (1) is a standard notion for syntax, and that its content is "naturality in the
  substitution category". It says nothing about reflection of derivability.

## S8. Derived vs admissible rules — precise statements

### S8a. Harper, PFPL 2nd ed., Ch. 3 "Hypothetical and General Judgments"
- Bib: R. Harper. Practical Foundations for Programming Languages, 2nd ed., Cambridge University Press 2016;
  chapter DOI printed on retrieved pages: "https://doi.org/10.1017/CBO9781316576892.005".
- URL: https://khoury.northeastern.edu/~cmartens/Courses/7400-f24/pfpl/3-hypothetical.pdf (course-hosted copy of the
  CUP chapter; book pp. 23ff). Status: VERIFIED_SOURCE.
- Chapter opening: "We will consider two notions of entailment, called derivability and admissibility. Both express a
  form of entailment, but they differ in that derivability is stable under extension with new rules, admissibility
  is not."
- §3.1.1: "J1,...,Jk ⊢_R K ... to mean that we may derive K from the expansion R ∪ {J1,...,Jk} of the rules R with
  the axioms ... We treat the hypotheses ... as 'temporary axioms'". "Theorem 3.1 (Stability). If Γ ⊢_R J, then
  Γ ⊢_{R∪R′} J."
- §3.1.2: "Admissibility, written Γ |=_R J, is a weaker form of hypothetical judgment stating that ⊢_R Γ implies ⊢_R J."
  "In contrast to derivability the admissibility judgment is not stable under extension to the rules. For example,
  if we enrich rules (2.8) with the axiom succ(zero) even, then rule (3.6) is inadmissible". "Theorem 3.2. If Γ ⊢_R J,
  then Γ |=_R J." Converse fails: "succ(zero) even ⊬(2.8) zero odd ... Yet ... succ(zero) even |=(2.8) zero odd is
  valid, because the hypothesis is false". "Evidence for admissibility can be thought of as a mathematical function
  transforming derivations ∇1,...,∇n of the hypotheses into a derivation ∇ of the consequent."
- INFERENCE (informal argument, not machine-checked): with PFPL's definitions the converse stability
  characterisation is immediate: Γ ⊢_R J iff for every rule set R′ ⊇ R, Γ |=_{R′} J. (⇐: take R′ = R ∪ Γ; then
  ⊢_{R′} Γ, hence ⊢_{R∪Γ} J, which is by definition Γ ⊢_R J. ⇒: Thm 3.1 + 3.2.) Note this needs extensions by
  CLOSED (non-schematic, "temporary") axioms — i.e. hypotheses whose metavariables/atoms are frozen as fresh constants.

### S8b. Propositional-logic notion (substitution-based)
- Lecture handout "Admissible rules" (UvA, Proof Theory 2014, B. van den Berg course page), dated "November 21, 2014",
  https://staff.fnwi.uva.nl/b.vandenberg3/Onderwijs/Proof_Theory_2014/admissible%20rules.pdf (3 pp; author not
  printed on the pages I read). Status: VERIFIED_SOURCE (but a secondary teaching note, not primary literature).
  Def 1: "A rule ϕ/ψ is said to be admissible if for all substitutions σ, if ⊢ σϕ, then ⊢ σψ. A rule ϕ/ψ is said to be
  derivable if ⊢ ϕ → ψ." Def 2: "A logic L is structurally complete if every admissible rule of L is derivable."
  Thm 3: "CPC is structurally complete." Prop 8: "The Kreisel–Putnam rule is not derivable in IPC." **Thm 9: "The
  Kreisel–Putnam rule is admissible in every intermediate logic."** (intermediate logic: contains IPC, closed under
  substitution and MP, "⊥ ∉ L"). Rybakov: IPC admissibility decidable; no finite basis (stated, citations not checked).
- Iemhoff, "The rules of intermediate logic", Festschrift for D. de Jongh (65th birthday),
  https://festschriften.illc.uva.nl/D65/iemhoff.pdf, 16 pp. Status: VERIFIED_SOURCE. §1: "A rule A/B is admissible
  for a theory if B is provable in it whenever A is. The rule A/B is said to be derivable if the theory proves that
  A → B. Classical propositional logic CPC does not have any non-derivable admissible rules ... but ... IPC has many
  admissible rules that are not derivable". Thm 1 [10]: "If V is admissible for L then V is a basis for the admissible
  rules" (V = Visser's rules); Cor 2: "If V is derivable for L then L has no non-derivable admissible rules".
- Iemhoff, "Intermediate logics and Visser's rules", NDJFL 46(1), 2005 — NOT_ACCESSED (abstract seen only via search).
- COUNTEREXAMPLE to a naive stability characterisation (INFERENCE): "derivable iff admissible in every extension"
  is FALSE if "extension" ranges only over consistent substitution-closed logics: KP rule is admissible in all
  intermediate logics but not derivable in IPC. (Reason, my inference: the critical extension IPC + (¬p → q∨r) closed
  under substitution is inconsistent — put p:=⊥, q,r:=⊥ — so it is excluded.) The characterisation holds when
  extensions may add the premise as a non-substitutable hypothesis (fresh atoms as constants) or may be inconsistent.
  So the precise standard statement is the PFPL/LF one (S8a), and the quantifier over "extensions" must be stated.
- Humberstone "The Connectives" (MIT 2011), Rybakov's book (1997) — NOT_ACCESSED.

## S9. Twelf: admissibility via totality checking — what is trusted

- Twelf User's Guide §9 "Coverage" (HTML), https://www.cs.cmu.edu/~twelf/guide-1-4/twelf_9.html (URL path says
  guide 1.4; version not otherwise printed in the page I read). Status: VERIFIED_SOURCE.
  - "totality checking verifies both coverage and termination, thereby ensuring that any mode-correct invocation of
    the type family considered as a logic program will succeed. Hence, a total type family represents a total,
    possibly non-deterministic, function and can thus be often seen to realize a meta-theoretic proof."
  - §9.1: "The adequacy of an encoding using higher-order abstract syntax usually relies on a characterization of the
    possible parameters and hypotheses that may be introduced." Worlds: %block / %worlds; "Coverage checking is
    always relative to a world declaration."
  - "Coverage checking takes dependent types and subordination into account, but it is a decidable, syntactic test
    rather than a semantic criterion."
  - §9.3: "Checking that a type family is total requires, in this order, mode checking, world checking, termination
    checking, and coverage checking." Steps: Modes ("Indefinite modes (*) are not allowed"), Worlds, Termination
    ("any well-moded query ... terminates, either with success or failure"), Input Coverage, Output Coverage.
  - Subordination/§9.4: "Sometimes it is necessary to ensure that a given type family is not extended with additional
    constructors that might invalidate meta-theorems or add new (unwanted) axioms to a theory represented in LF. In
    order to prohibit further extensions ... issue %freeze a1 ... an ."
- Twelf wiki "%total" https://twelf.org/wiki/percent-total/ (VERIFIED_SOURCE): "these analyses verify that if the type
  family is run as a logic program in Twelf with ground derivations in the input positions, then it the execution
  will terminate successfully ... This proves the totality assertion for the type family: in any context conforming
  to the %worlds declaration, for any ground derivations in the input positions ..., there exist ground derivations
  for the output positions such that the type family is inhabited." Keyword list on same page includes %trustme,
  %assert, %establish, %theorem, %prove, %freeze, %thaw (names only seen; semantics not read).
- Twelf wiki "Totality assertion" https://twelf.org/wiki/totality-assertion/ (VERIFIED_SOURCE): "For all contexts Γ,
  for all inputs M in Γ, there exist outputs N in Γ such that the type a M N is inhabited in Γ." "Proving a relation
  total is different from showing that the relation defines a function". "We may prove a totality assertion by
  induction on canonical forms."
- Schürmann thesis (2000) — NOT_ACCESSED.
- What is TRUSTED when an admissible rule is established in Twelf (INFERENCE from the above): (i) the LF type
  checker; (ii) mode checker; (iii) world/regular-world checker and the user's %block declarations (which define
  the quantifier domain "all contexts in W"); (iv) termination checker (user-supplied termination order);
  (v) input+output coverage checkers (syntactic, conservative, decidable); (vi) the CLOSED-WORLD assumption on the
  relevant families (enforced by %worlds/%freeze/subordination); (vii) absence of %trustme/%assert-style escape
  hatches. The resulting object is NOT an LF term of the rule's type (contrast derived rule = LF term) but a
  relation + checker certificate; its validity is relative to the frozen signature — exactly the non-stability of
  admissibility. Pfenning handbook (S4) p.57 confirms that at that time (1999 preprint) termination/coverage were
  "outside the scope of the type-checker".

---

## INFERENCE summary for the hypotheses

H1 ("representation commuting with substitution incl. derivations-for-hypotheses, realised by the framework's own
substitution" is standard): **Supported — and already established terminology, not novel.**
- HHP (S5, 1987/1993) define "compositional" exactly so ("substitution in the logical system is encoded as
  substitution in LF ... identification of object-logic variables with the variables of LF"), and Thm 4.1 states it
  for substitution of PROOFS for proof-assumption variables. Pfenning Thm 3.2(3) (S4) states ⌜[E/u]D⌝ = [⌜E⌝/u]⌜D⌝.
  Gardner Def 5.2.1(3) (S3) makes it part of the definition of "complete encoding", and Def 5.2.3 "natural encoding"
  = adequate + bijective on valid proofs + complete.
- Category-theoretic standard form: for SYNTAX, maps commuting with variables, operators and simultaneous
  substitution = morphisms of Σ-monoids (FPT S1) / second-order syntactic translations (Fiore–Mahmoud S2, Lemma 5.1).
  For derivations-with-hypotheses: Gardner's indexed functors over the term category with fibres of proof
  assumptions, composition = proof substitution (Prop 6.5.1), and Thm 6.5.7 natural ⇔ indexed iso. I did NOT find
  (in retrieved sources) a single theorem stating "naturality under proof substitution = Σ-monoid morphism for a
  dependently sorted signature"; treating it as a Σ-monoid morphism for a sorted signature with a proof sort is my
  INFERENCE (plausible; dependently-sorted version by Fiore 2008 UNVERIFIED-MEMORY).
- Caveats (adversarial): (a) Compositionality is AUTOMATIC for any syntactic translation (S2 Lemma 5.1) and for any
  indexed functor determined by an encoding (S3 Thm 6.4.1/6.5.5) — so naturality alone does not exclude vacuous
  encodings (F02); discriminating power comes from bijectivity/fullness/faithfulness (adequacy). (b) "Hypotheses as
  framework variables" forces weakening/contraction/exchange: Gardner Cor 5.1.8 — no adequate ELF+ encodings of linear
  or relevant logics; Pfenning §8.1 p.70 (VERIFIED): LF "can encode linear and other substructural logics ..., but their
  encodings are not as direct as one might hope. The reason is that linear assumptions (each of which must be used
  exactly once) can not be modeled as hypotheses in the meta-language (which satisfy weakening and contraction)." So the criterion as stated is NOT foundation-neutral (F04/F05).
  (c) Proof identity: Gardner Thm 5.2.11/5.2.13 — Hilbert-style systems have adequate but NOT natural encodings in
  the obvious signatures; identity of proofs is presentation-dependent, and Gardner's §6.5 fibres carry no proof
  equations.
- Which encodings satisfy it (as stated in sources): LF/ELF+ encodings of natural-deduction FOL (HHP Thm 4.1;
  Pfenning Thm 3.2; Gardner Thm 5.2.7 "natural encoding of first-order logic"), HOL (Gardner Thm 5.2.9). Not:
  Hilbert-style S4 / propositional logic in the given signatures (Gardner 5.2.11/5.2.13); linear/relevant logics in
  ELF+ (Cor 5.1.8).

H2 (derived / admissible / declared primitive / checker distinction is standard with a precise stability
characterisation): **Partly supported.**
- Derived vs admissible: standard; precise stability statement PFPL Thm 3.1 (derivability stable under adding rules)
  + explicit counterexample for admissibility. The biconditional "derivable iff admissible in every extension" is
  an easy consequence of PFPL's "temporary axioms" definition (my informal argument) but is FALSE for the common
  propositional reading where extensions must be substitution-closed and consistent (KP rule, S8b). So any project
  definition must fix the class of extensions (new rules / new non-substitutable hypotheses / new atoms).
- Derived rule ≡ framework term of higher type (HHP p.2: "eliminates the distinction between primitive and derived
  rules"; Pfenning §4.5 definitions c:A = M). Admissible rule ≢ framework term: HHP p.23 (open judgements because of
  weakening preclude encoding admissibility proofs by induction; deduction theorem for Hilbert systems is the
  example); Pfenning pp.47–48 (adding induction over i turns ∀I into an ω-rule and destroys adequacy).
- Declared primitive rule = signature constant (HHP; trusted environment content — F03).
- Checker/decision procedure: Twelf totality = mode+worlds+termination+coverage, trusted checkers, closed world
  (%freeze); this is a standard but TOOL-SPECIFIC notion; I found no general theorem classifying "checker-established
  rules" alongside derived/admissible. The four-way distinction is therefore standard in pieces (derived/admissible:
  textbook; primitive: HHP; checker: Twelf docs) but the unified "stability characterisation" of all four is NOT
  found in retrieved sources — open/uncertain.
