# Notes, tag `can`: canonical representatives and the status of complexity "obstructions"

Agent: source-extraction subagent (tag `can`), REVIEW PHASE. Date: 2026-10-08.
I downloaded PDFs to `scratchpad/review/dl/can/` and converted them with pdftotext. Pre-existing local texts are under `scratchpad/ocr/` and `scratchpad/dl/`.
Quotes in "..." are verbatim from the retrieved text. OCR and pdftotext artifacts are kept or lightly normalised (for example, ligatures). Anything not marked as a quote is paraphrase or INFERENCE.

Questions:
(a) Can proof identity be realised by CANONICAL REPRESENTATIVES on the object side (focusing, multi-focusing, saturation), so that a fixed framework with syntactic equality represents identity classes bijectively?
(b) Do the complexity results cited as "obstructions" show impossibility, or only intractability of canonical forms?

---

## 1. Chaudhuri, Miller, Saurin, "Canonical Sequent Proofs via Multi-Focusing" (IFIP TCS 2008)

- Retrieved: https://www.lix.polytechnique.fr/~dale/papers/tcs08trackb.pdf (author copy, 15 pp.). Page numbers refer to this copy. The search engine reports that the IFIP volume 273, pp. 383–396 (Springer) holds the published version. I did not open the publisher version. **VERIFIED_SOURCE (author copy).**
- Setting: "the standard cut-free sequent calculus for multiplicative-additive linear logic (MALL), including units and literals" (Sec. 1, p. 2).
- Equivalence that is canonicalised: **iso-initial permutative equivalence**, not categorical equality.
  - Def. 1 (p. 4): "Two proofs D and E ⊢ Γ are iso-initial, written D ≃ E, if each can be rewritten to the other using local permutations and the set of initial sequents in both D and E are the same."
  - The authors' caveat (p. 4): "because we don't allow all permutations of ⊤, we are decidedly not equating all proofs that are equated in the standard categorical model of MALL proofs; i.e., ⊤ is no longer a terminal object in a suitable ⋆-autonomous category where & is the Cartesian product."
- Representatives are unique only up to a residual relation.
  - Def. 4: "Two proofs D and D′ ... are iso-polar, written D ≈ D′, if they are equal up to permutations restricted to the pos/pos and neg/neg types."
  - The paper says this residue can be removed: "A single representative of the ≈-classes can be constructed by treating the contexts ∆ ... as ordered contexts ... This order on the context induces a fixed but arbitrary order of the pos/pos and neg/neg rules" (p. 6).
- Main theorem. Def. 6 (maximal) is followed by "Theorem 7 (canonicity) If D ≃ E ⊢ Γ ⇑ · are both maximal, then D ≈ E."
- Proof nets. "Theorem 16 Two maximally multi-focused MLL− proofs of ⊢ · ⇑ Γ are iso-polar iff they have the same MLL− proof net." This holds only for unit-free, cut-free MLL (MLL−).
- Limitations stated in the paper (Sec. 6):
  - "we lack a cut-elimination theorem for multi-focused proofs ..."
  - "it is considerably unclear how maximality interacts with cut-elimination, for the standard procedure would not preserve maximality"
  - "multi-focusing generalizes easily to admit the exponentials and first-order quantification; however, the respective notions of maximality remain to be developed for these fragments"
  - "The problem of proof-nets for MALL with units is still open."
- The paper states no complexity bound.
- Follow-up (VERIFIED_SOURCE): Chaudhuri, Hetzl, Miller, "A Systematic Approach to Canonicity in the Classical Sequent Calculus", CSL 2012, LIPIcs 16, DOI 10.4230/LIPIcs.CSL.2012.183. Retrieved from DROPS.
  - Result for classical first-order LK: maximally multi-focused proofs are "action-canonical" and "isomorphic to expansion proofs".
  - It also restricts the equivalence: "we restrict permutation steps to cases where both of the rules being permuted have at least one premise. In other words, ⊤/r and init/r permutation steps are impossible ... If such permutation steps were to be allowed, then the induced equivalence on LKN proofs would equate arbitrary sub-proofs and defeat any attempt at canonicity."
  - It describes CMS08 as being "for ⊤-free multiplicative-additive linear logic (MALL)".
- Third-party characterisation (Heijltjes–Houston, LMCS 2016, p. 3): "focusing retains classical linear logic but weakens the notion of proof equivalence. This gives canonical representations in focused proof nets [AM99] and multi-focused proofs [CMS08]."
- INFERENCE: This answers (a) positively, but only locally. Canonical representatives exist for the cut-free proofs of specific fragments, relative to a deliberately weakened equivalence. In each case the equivalence is one where ⊤ and initial-rule permutations that create or delete subproofs are excluded. Neither paper gives a cross-foundation construction. Neither handles cuts (identity "modulo cut elimination"), and neither handles exponentials, units in the categorical sense, or dependent types.

## 2. Scherer, "Deciding equivalence with sums and the empty type" (POPL 2017), and Scherer & Rémy, "Which simple types have a unique inhabitant?" (ICFP 2015)

### Scherer 2017

- Retrieved: arXiv:1610.01213v3 (8 Nov 2016), 17 pp., https://arxiv.org/pdf/1610.01213. This is a preprint with appendices. **VERIFIED_SOURCE.**
- The paper says: "For lack of space, our statements do not come with their proofs, but proof outlines are given in Appendix B." So the proofs are outlines only, and I did not check them.
- System: ΛC(X, →, ×, 1, +, 0), with "the strong equivalence on sums. It corresponds to equality of morphisms in the free bi-cartesian closed category".
- Contributions, quoted:
  - "Saturated terms provide a notion of quasi-normal form; equivalent quasi-normal forms are not necessarily α-equivalent, but are related by a local, easily decidable relation of invertible commutation conversions (≈icc)."
  - "βη-equivalence is decidable."
  - "βη-equivalence and contextual equivalence coincide ..."
  - "The finite model property holds."
- Key results, quoted:
  - "Theorem 13 (Saturated terms are canonical). In the system with only positive atoms, if ∅; Σp ⊢sinv t ≉icc t′ : N | Pa then t ≉ctx t′."
  - "Corollary 7. Equivalence in the full simply-typed λ-calculus with sums and the empty type is decidable."
  - Proof of Cor. 7: "Those two transformations are computable and (≈icc) is decidable, so equivalence is decidable."
- Canonicity depends on the selection function: "Completeness of saturation is relative to a specific choice of selection function." With 0 present, "not all ways to select neutrals for saturation preserve canonicity ... we need a provability completeness requirement".
- Scope limits stated in the paper:
  - "Saturation is a technique specific to intuitionistic logic ... Note this strategy would be invalid in an effectful language, or a resource-aware logic where introducing unused sub-derivations can consume necessary resources and get you stuck."
  - "Being such a reordering of another term is a highly global property, that cannot be decided locally like invertible commuting conversions."
  - "in general there is no goal-directed proof search (or term enumeration) procedure that generates only maximally multi-focused derivations".
  - "adding parametric polymorphism (System F and beyond) makes βη-equivalence strictly weaker than contextual equivalence."
  - "Untyped β-reduction is not normalizing, so equivalence is undecidable."
  - The paper gives no complexity bound. Future work: "we would rather use an algorithm that does not need to compute full saturated normal forms".

### Scherer & Rémy 2015

- Retrieved: the author long version, https://www.lix.polytechnique.fr/Labo/Gabriel.Scherer/research/unique_inhabitants/unique_stlc_sums-long.pdf. It states it is "identical to the short version, except for the Appendix". **VERIFIED_SOURCE (long version).**
- System: atoms, →, ×, + (no empty type), modulo βη.
- Results, quoted:
  - "Theorem 1 (Canonicity of saturating focused logic). If we have Γ; ∆ ⊢sinv t : A and Γ; ∆ ⊢sinv u : A in saturating focused logic with t ≠icc u, then t ≠βη u."
  - "Theorem 2 (Computational completeness ...). If we have ∅; ∆ ⊢inv t : A in the non-saturating focused logic, then for some u =βη t we have ∅; ∆ ⊢sinv u : A".
  - "Theorem 4. Our unicity-deciding algorithm is terminating and complete for unicity."
  - On efficiency: "not designed for efficiency, and in particular saturation duplicates a lot of work".
- INFERENCE for (a): Canonical forms here are quasi-normal: unique modulo ≈icc, and relative to a fixed selection function. They exist only for pure, intuitionistic, simply-typed systems. In Scherer's own words, the technique does not transfer to resource-sensitive logics, which is the project's requirement R2. For System F-like foundations, βη is not even the observational identity. For untyped or non-normalising foundations, equivalence is undecidable, so no computable canonical-form map exists for that identity.

## 3. Statman, "The typed λ-calculus is not elementary recursive", TCS 9 (1979) 73–81

- DOI 10.1016/0304-3975(79)90007-0 (from Crossref).
- Retrieved: a scan of the journal version from a Cornell course page, https://cs.cornell.edu/courses/cs6110/2012sp/Statman-typed-lambda-calculus.pdf. Header (OCR): "Theoretical Computer Science 9 (1979) 73-?? North-Holland". **VERIFIED_SOURCE (OCR'd scan of the published version; OCR noise in Greek letters).**
- Abstract (OCR, β restored): "We prove that the problem of deciding for closed terms t1, t2 of the typed λ-calculus whether t1 β-converts to t2 is not elementary recursive."
- Exact claim: **β-conversion of closed terms that may contain redexes.** It is not a claim about comparing normal forms.
- Upper bound (p. 75): "The problem ... is decidable. By analyzing the normal form algorithm ... the problem can be solved in E4 time ... our lower bound (E3 = elementary) is best possible."
- Corollary, p. 80: for each suitable type σ there is a closed t such that deciding "r β-conv. t, r β-red t, or t is the β-normal form of r cannot be solved in elementary time".
- p. 80–81: for terms whose subterm types have rank ≤ n, the problem "can be solved in elementary time".
- Secondary sources:
  - Mairson, "A simple proof of a theorem of Statman", TCS 103(2):387–394, 1992, DOI 10.1016/0304-3975(92)90020-G. **NOT_ACCESSED**: ScienceDirect returned 403. I confirmed only the bibliographic data (Crossref, Utah bib).
  - Nguyễn, "Simply typed convertibility is TOWER-complete even for safe lambda-terms", arXiv:2305.12601v3. **VERIFIED_SOURCE.**
    - "Theorem 1.1. Simply typed β-convertibility is Tower-complete".
    - "Theorems 1.1 and 1.2 also hold for βη-conversion."
    - On how the problem is decided: "testing whether two terms are βη-convertible can be done by comparing their βη-normal forms for equality".
- INFERENCE for (b): This is an intractability result for *normalisation* (cut elimination), not an impossibility of canonical representatives.
  - βη-normal forms are canonical representatives, and comparing them is syntactic.
  - Statman's result says that any total computable map from arbitrary (cut-containing) terms to canonical forms needs non-elementary time in the worst case. More strongly, any decision procedure for the identity does too.
  - It applies equally to any representation, canonical or not, that must decide identity on proofs with cuts. It does not apply if the represented objects are already cut-free or normal.

## 4. Heijltjes & Houston, "Proof equivalence in MLL is PSPACE-complete", LMCS 12(1:2) 2016

- DOI 10.2168/LMCS-12(1:2)2016 (printed on the document).
- Retrieved: arXiv:1510.06178, 34 pp. This is the LMCS-formatted version (header "Vol. 12(1:2)2016, pp. 1–34"). **VERIFIED_SOURCE.**
- Main result, p. 32: "Theorem 9.1. MLL proof equivalence is PSPACE-complete."
  - Membership: "MLL proof equivalence has at most non-deterministic polynomial space complexity ... by Savitch's Theorem ... in PSPACE."
- Abstract: "An important consequence of the result is that the existence of a satisfactory notion of proof nets for MLL with units is ruled out (under current complexity assumptions). The PSPACE-hardness result extends to equivalence of normal forms in MELL without units".
- The decisive wording (Sec. 1, p. 2): "which is generally supposed to preclude the existence of a polynomial-time algorithm for this problem. So there can be no canonical proof nets in the usual sense: if the proof nets are syntactically equal just when their corresponding proofs are equivalent, then the translation from proofs to proof nets must be intractable."
  - So the paper itself claims only conditional intractability of a canonical-form map. It does not claim that a faithful or canonical representation is impossible.
  - The problem is decidable, so a computable canonical-form map does exist. For example, pick the least element of the finite equivalence class (INFERENCE, see Hughes below).
- Also on p. 2: "This is in sharp contrast with many intuitionistic calculi such as the simply typed lambda-calculus, where normal forms are unique. However, it does not impact the complexity of proof equivalence for MELL in general, which is dominated by cut-elimination (MELL encodes the simply-typed lambda-calculus, which is not elementary recursive [Sta77])."
- Alternatives the paper lists (p. 3):
  - intuitionistic MLL: canonical by directing rewiring, "folklore";
  - tensorial logic;
  - the polarised fragment, which "has canonical proof nets [Lau99]";
  - focusing or multi-focusing, which "weakens the notion of proof equivalence".

### Hughes, "Simple free star-autonomous categories and full coherence"

- Retrieved: arXiv:math/0506521v4 (27 Mar 2012). The PDF header says "To appear in Annals of Pure and Applied Algebra, 2012" (sic); the arXiv comment and the requested citation say JPAA 216 (2012). **VERIFIED_SOURCE (arXiv v4).** I did not check volume or pages.
- "THEOREM 3 (FREENESS) For any category A, the category NA of A-nets is the free star-autonomous category generated by A."
- "THEOREM 4 (FULL COHERENCE) Equality of morphisms in the free star-autonomous category generated by a category is decidable."
- "Equivalence modulo rewiring is decidable, by finiteness."
- Table 1 caption: "In each case a morphism of the free category is a finite equivalence class, hence equality of morphisms is decidable."
- Linkings are checkable "in linear time".
- So this is a positive *faithful* representation: equivalence classes of linkings, decidable but not polynomial. It is not a canonical-syntax representation. The paper makes no canonical-form claim.

## 5. Gardner, *Representing Logics in Type Theory*, PhD thesis, Edinburgh, 1992 (CST-93-92 / ECS-LFCS-92-227)

- Source: local OCR, `scratchpad/ocr/gardner_all.txt`. **VERIFIED_SOURCE (OCR).** OCR page p-NNN is printed page NNN−8.
- Framework: ELF*, a variant of ELF/LF.

### Definitions

- **Def 3.2.12** (printed p. 61, OCR p-069). A proof system's consequence relation satisfies the cut condition. Def 3.2.13: "A consequence relation is intuitionistic if it satisfies 1. (weakening) ... 2. (substitution) ...".
- **Def 5.1.1** (pp. 94–95). An encoding (η, ε, δ):
  - variables go to sort variables;
  - terms and judgements go to βη-long normal forms;
  - the maps are compositional;
  - "the interpretation is sound": j1..jm ⊢ j implies Γ_X, p1:δ(j1),…,pm:δ(jm) ⊢ _:δ(j).
  - So hypotheses become **context assumptions**, which is judgements-as-types.
  - Remark (p. 96): "we do not link derivations in the logic and inhabitants of ELF* judgements ... we are interested in the inhabitation of ELF* judgements, rather than particular ELF* terms."
- **Def 5.1.4** (p. 98). The encoding is adequate when:
  1. η is a bijection onto sort^{βη};
  2. ε_X and δ_X are bijections onto the βη-long normal forms;
  3. the interpretation is complete.
  - The thesis also notes a weaker notion: "if we only require that the functions are injective and that the completeness condition (part 3) holds; we call such an encoding weakly adequate."
- **Def 5.2.1** (p. 116). A complete encoding adds χ_{X,Δ}: proof expressions → terms, with χ(p) = h(p) for proof variables and soundness for proofs. It is "compositional": χ(Π[Ξ,s/y,x]) = χ(Π)[…].
- **Def 5.2.3** (p. 118). "A complete encoding (η, ε, δ, χ) is natural if":
  1. (η, ε, δ) is an adequate encoding;
  2. "the function χ_{X,Δ}: VP(X,Δ) → proof^{βη}_{…} is a bijection";
  3. the interpretation is complete.
  - INFERENCE: naturality is exactly a canonical-representatives criterion. Valid proof expressions are in bijection with βη-long normal ELF* inhabitants, and proof identity is syntactic identity of proof expressions (no quotient).

### Results

- **5.1.7 THEOREM** (p. 100): "Logics which are adequately represented in ELF* have intuitionistic consequence relations (definition 3.2.13)."
  - Proof: the cut, weakening and substitution conditions come from ELF*'s substitution and thinning lemmas.
  - Status: a **general** impossibility relative to Def 5.1.4. It quantifies over all signatures. But it depends on Def 5.1.1 mapping logic hypotheses to framework context assumptions.
- **5.1.8 COROLLARY** (p. 100): "There are no adequate representations of linear and relevant logics [Gir87] [Dun84] in ELF*."
  - Proof: "The consequence relations of these logics are not intuitionistic since they do not satisfy the weakening condition".
  - Status: **general relative to the definition**, for all signatures.
  - INFERENCE: it does not exclude sequent-as-object encodings, where a whole sequent is the judgement and no logic hypotheses are mapped to context entries. Those satisfy 5.1.1 vacuously with m = 0 hypotheses, and the "consequence relation" being represented is then a different one. MDT 2009 make the parallel point: "substructural logics can be encoded into Tarskian entailment relations by considering whole sequents as sentences."
- **5.2.5 THEOREM** (p. 118): "Logics whose representations in ELF* are natural have intuitionistic consequence relations with proofs."
  - Status: **general**, for all signatures, relative to Def 5.2.3.
- **5.2.6 EXAMPLE** (p. 118): "Natural deduction-style S4 [Pra65] (example 3.2.15) does not have a natural representation in ELF* since, although its consequence relation is intuitionistic, its consequence relation with proofs is not preserved under substitution of proof expressions."
  - Status: general over signatures, by 5.2.5. But it is specific to **Prawitz's** S4 presentation and its proof expressions, where substituting into the □-rule premise breaks the side condition. Other S4 proof syntaxes are not addressed.
  - Note: it is labelled EXAMPLE, not theorem.
- **5.2.11 THEOREM** (p. 120): "The representation of Hilbert-style S4 in ELF*, given in example 5.1.12, is not natural."
  - Proof (sketch): "there are eight possible shapes for the valid proof expressions and nine possible shapes for the inhabitants of judgements. Since χ_{X,Δ} satisfies the compositionality property ... cannot be a bijection."
  - Status: about **one particular signature**, that of example 5.1.12. The proof is only a sketch.
- **5.2.13 THEOREM** (p. 120): "The signature Σ_{HPL}[OCR: 'Dy,,'] does not provide a natural encoding of Hilbert-style propositional logic."
  - Proof: "Similar analysis to the proof of theorem 5.2.11."
  - Status: about **one particular signature**, the ND propositional signature reused for Hilbert PL (example 5.2.12). There is no general impossibility. A Hilbert-specific signature with axiom constants and an MP constant is not excluded (INFERENCE).
- Gardner's own caveat (p. 121): "Our approach for reasoning about representations of derivations ... is not completely satisfactory. Although the natural encoding definition (definition 5.2.3) is general ..., we do not have a methodology for giving an explicit account of proofs."

## 6. Maraist, Odersky, Turner, Wadler; Hasegawa (FLOPS 2002): is the cbv equality failure a property of one translation?

### Maraist, Odersky, Turner, Wadler

- Text: `scratchpad/dl/adq/linearcall.txt`. Header: "Electronic Notes in Theoretical Computer Science 1 (1995) to appear", so this is the preprint. **VERIFIED_SOURCE (preprint).**
- Section 8.3: "The call-by-name translation is complete for equality."
- Also 8.3: "The other translations are not complete for equality. For instance, the λval terms (M N) and ((λz. z N) M) are not equal in λval, but their translations are equal in λlin. The same example adopts to λlet and λneed."
- They then ask whether laws could be added "so that the corresponding translations are sound and complete for equality as well as reduction". They cite Moggi's λc as a hint, and say: "It is interesting open question whether there is an extension of λlet that has the same equalities as λcomp. It is a further interesting question to know if there is an extension of λlin such that the encoding of the extended λlet into the extended λlin via ° is sound and complete."
- Also: "Plotkin showed that the CPS translation from λval into itself is sound but not complete ... Sabry and Felleisen verified that the CPS translation from λcomp into λval is both sound and complete".
- Reduction is sound and complete for each translation, per the abstract and introduction.

### Hasegawa, FLOPS 2002

- Text: `scratchpad/dl/pid/hflops.txt`. Hasegawa, "Linearly Used Effects: Monadic and CPS Transformations into the Linear Lambda Calculus". Header page numbers are 168–177. **VERIFIED_SOURCE.**
- The direct (identity-monad, Girard-style) cbv translation from the computational λ-calculus is not equationally complete: "This translation is not equationally complete – it validates the commutativity axiom ... which is not provable in the computational lambda calculus. Also it is not full".
- But the CPS translation into linear λ is equationally complete. Proposition 5, with the paper's attribution: "Proposition 5 (equational completeness of Sabry and Felleisen [16]). Γ ⊢ M = N : σ holds in the computational lambda calculus if and only if Γ° ; ∅ ⊢ M° = N° : (σ° → o) ⊸ o holds in the linear lambda calculus."
- It is also full: "Theorem 1 (full completeness of the CPS transform). Given Γ° ; ∅ ⊢ N : (σ° → o) ⊸ o in the linear lambda calculus, we have Γ ⊢ M : σ in the computational lambda calculus such that Γ° ; ∅ ⊢ N = M° : (σ° → o) ⊸ o."
- Hasegawa conjectures, for the direct translation, that adding val_b would give fullness.
- INFERENCE: The cbv equality failure is a property of **one translation together with one source theory** (Girard's second translation from λval/λlet). It is not an impossibility of faithfully representing cbv equality in linear λ.
  - A different translation (CPS with linear answer type) from a different source theory (Moggi's λc) is sound, complete and full.
  - The commutativity in the direct translation's target reflects a different identity: the direct translation validates commutativity, which is not a λc law. This shows that choosing a target identity is substantive (F04).

## 7. Mossakowski, Diaconescu, Tarlecki, "What is a Logic Translation?" (Logica Universalis 2009)

- Text: `scratchpad/dl/rwl/mdt.txt`. Header "c 2009 Birkhäuser Verlag Basel/Switzerland", pp. "1–29", preprint layout. **VERIFIED_SOURCE (preprint).**
- Def 2.1: an entailment relation (ER) is ⊢ ⊆ P(S) × S satisfying reflexivity, monotonicity and transitivity. It is "compact when for each E ⊢ ϕ there exists a finite subset E0 ⊆ E such that E0 ⊢ ϕ."
- Def 2.22: "a simple theoroidal ER morphism (α, ∆) : S1 → S2 is a function α : S1 → S2 together with a theory ∆ ⊆ S2 such that Γ ⊢1 ϕ implies ∆ ∪ α(Γ) ⊢2 α(ϕ)".
  - **∆ is any subset of S2.** There is no finiteness, recursiveness or r.e. condition.
- "Call an ER countable if its set of sentences is countable." Then: "Proposition 2.25. The entailment relation of PHCL has maximal expressiveness among compact countable ERs (when admitting simple theoroidal ER morphisms)."
- Proof: "∆ consist of all sentences α(ϕ1) ∧ ... ∧ α(ϕn) → α(ϕ) such that {ϕ1, ..., ϕn} ⊢ ϕ in S."
  - So ∆ is in general **infinite**. It is exactly as recursive as S's finite-premise entailment: r.e. iff S is, and **non-recursive** if S's entailment is undecidable.
  - Hypotheses are only *compact* and *countable*. Decidability or effectiveness is not assumed. α must be a function, and it need not be computable.
- Corollary 2.26 embeds every compact countable ER into CPLω using "the conjunction of all elements of ∆", which is infinitary.
- The authors' own caveat (concluding section): "An interesting open question is the formalisation of 'structurality' of translations between logics, such that translations flattening out the structure (like that in Prop. 2.25) are ruled out."
- INFERENCE: Prop 2.25 is the F02/F03 "everything in the environment" trivialisation in pure form. The entire consequence relation is placed in the trusted theory ∆. It addresses derivability only and says nothing about proof identity.

---

## Synthesis (INFERENCE, adversarial)

### (a) Canonical representatives

**Partial yes, locally. No known general result.**

Where they exist:
- MLL− (CMS08 Thm 16; proof nets);
- ⊤/init-restricted MALL (CMS08 Thm 7);
- classical first-order LK (CHM12, expansion proofs);
- simply typed λ with →×1 (βη-long normal forms);
- →×+ (Scherer–Rémy 2015, Thm 1–2) and →×1+0 (Scherer 2017, Thm 13 / Cor 7);
- intuitionistic MLL (folklore, according to Heijltjes–Houston);
- polarised linear logic (Laurent, cited by Heijltjes–Houston, which I did not check).

Caveats a report must not drop:
1. Each result is for one logic or fragment and one chosen identity. The linear cases use weakened identities (iso-initial, which excludes ⊤ and init permutations). These are not the categorical identities. This makes F04 sharper, not weaker.
2. The forms are unique only modulo a residual local relation (≈ iso-polar, ≈icc), and in Scherer's case relative to a selection function. Fixing an order removes the residue in CMS08, which says so explicitly. For ≈icc I found no statement that a canonical choice is given.
3. The forms are cut-free. Identity "modulo cut elimination" is decided by normalising first, and maximality is not preserved by cut elimination (CMS08 §6).
4. Saturation is explicitly invalid for resource-aware logics (Scherer 2017 §4), which conflicts with R2. Multi-focusing maximality is undeveloped for exponentials and quantifiers in linear logic (CMS08 §6).
5. In Gardner's framework the canonical-representative criterion ("natural encoding", Def 5.2.3) is already formalised and fails. It fails for Prawitz-S4 in general (5.2.5 / 5.2.6) and for specific Hilbert signatures (5.2.11, 5.2.13).

So a fixed framework with syntactic equality can represent identity classes bijectively only object-logic by object-logic, through logic-specific normal-form disciplines. Those disciplines would live in the environment or signature, which is an F03-style concern. A single, uniform construction across foundations is not provided by any source I examined.

### (b) Complexity "obstructions"

None of them is an impossibility theorem for faithful or canonical representation.

- **Statman 1979**: a non-elementary lower bound for deciding β-conversion of terms *with redexes*. Nguyễn 2023 shows Tower-completeness, and that it also holds for βη. This bounds the cost of any procedure that decides identity on cut-containing proofs, canonical or not. Canonical normal forms exist, and comparing them is syntactic and cheap.
- **Heijltjes–Houston 2016**: PSPACE-completeness of MLL-with-units proof equivalence. The paper's own conclusion is conditional and about tractability: "if the proof nets are syntactically equal just when their corresponding proofs are equivalent, then the translation from proofs to proof nets must be intractable", "under current complexity assumptions".
  - Decidability is in PSPACE, so computable canonical forms exist. Hughes 2012 gives a faithful presentation (finite rewiring classes) with decidable equality.
  - It does extend to cut-free (normal-form) MELL without units. That is a genuine barrier to *polynomial* canonical forms even without cuts.
- **Only true impossibilities for computable canonical forms**: cases where the target identity is undecidable. Examples are untyped λ under βη, where Scherer notes that equivalence is undecidable, and contextual equivalence in richer systems (not checked here).

Recommendation for the reviewed report: if it cites Statman or Heijltjes–Houston as showing that a faithful representation of proof identity is "impossible", downgrade the claim to "computing canonical forms or deciding identity is intractable (non-elementary / PSPACE-hard)". This is a resource cost (F09), not an existence obstruction.

## Sources not accessed

- Mairson 1992, TCS 103: full text **NOT_ACCESSED** (ScienceDirect 403). Only bibliographic data, plus a description in Nguyễn 2023.
- Published versions of CMS08 (Springer) and of Scherer–Rémy ICFP 2015 (ACM): not opened. I used the author copy and the author long version.
- JPAA final version of Hughes: not opened (arXiv v4 only).
- Laurent 1999 (polarised proof nets) and Lindley 2007 / Balat–Di Cosmo–Fiore 2004: known only from citations (SECONDARY_ONLY).
