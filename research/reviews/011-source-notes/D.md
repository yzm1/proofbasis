# Cluster D: higher-dimensional structures. Source notes (agent D, 2026-10-09)

Downloads are in `t011/dl/D/` (arXiv PDFs, HoTT book, Licata–Harper preprint). The text was extracted with pdftotext into `t011/txt/D/`. No downloaded file was executed.
Labels: VERIFIED_SOURCE = text retrieved and read in this session (URL, version, locus). SECONDARY_ONLY = known only through another source. UNVERIFIED-MEMORY = recalled, not checked. NOT_ACCESSED = not obtained.
Quotes are copied from the extracted text, each ≤80 words.

---
## D1. HoTT / univalent foundations

**(1) Object.** Intensional Martin-Löf type theory (MLTT) with identity types x =_A y, a univalent universe, and HITs. There are two equalities: judgmental x ≡ y (metatheoretic, not a type) and propositional (a type whose elements are proofs).

**(2) Results.**
- *HoTT Book* (Univalent Foundations Program, IAS 2013). The copy read is "Book version: first-edition-82-g578b85c" from https://hott.github.io/book/hott-online-82-g578b85c.pdf. VERIFIED_SOURCE.
  - §1 (p. ~ch.1, line 1075): "we can assume a propositional equality (by assuming a variable p : x = y), but we cannot assume a judgmental equality x ≡ y, since it is not a type that can have an element."
  - Ch.1 Notes: UIP is "stating that any two proofs of equality are judgmentally equal", and Axiom K is "stating that the only proof of equality is reflexivity". Both are optional restrictions.
  - Ch.1 Notes / §1.12: the reflection rule "implies that all the higher groupoid structure collapses ... and hence is inconsistent with the univalence axiom (see Example 3.1.9)".
  - **Example 3.1.9**: "The universe U is not a set." The swap equivalence on 2 gives a path 2 = 2 that is not refl. So identity proofs are provably non-unique under univalence.
  - Thm 7.2.5 (Hedberg): a type with decidable equality is a set.
- *van den Berg–Garner*, "Types are weak ω-groupoids", arXiv:0812.0298v2. VERIFIED_SOURCE (abstract): "each type bears a canonical weak ω-category structure obtained from the tower of iterated identity types over that type ... the ω-categories arising in this way are in fact ω-groupoids."
- *Lumsdaine*, "Weak ω-categories from intensional type theory", LMCS 6(3:24) 2010, arXiv:0812.0409v4. VERIFIED_SOURCE (abstract): "we construct a contractible globular operad P_MLId of definable 'composition laws', and give an action of this operad on the terms of any type and its identity types."
- *Kapulkin–Lumsdaine*, "The simplicial model of univalent foundations (after Voevodsky)", arXiv:1211.2851v5. VERIFIED_SOURCE (abstract): there is a model in Kan simplicial sets with a univalent universe. Consequence: "Martin-Löf type theory with one univalent universe ... is at least as consistent as ZFC with two inaccessible cardinals." (Journal venue: JEMS 2021. UNVERIFIED-MEMORY.)
- *Shulman*, "All (∞,1)-toposes have strict univalent universes", arXiv:1904.07004v2. VERIFIED_SOURCE (abstract): every Grothendieck (∞,1)-topos is presented by a model category that interprets HoTT with strict univalent universes.

**(3) Represents / cannot.**
- It represents proof-relevant identity *inside the object language*: proofs of equality, equalities between them, and so on. It also shows that the composition laws on such proofs form a contractible globular operad (Lumsdaine). This is the most precise existing statement that the structural operations on identity proofs are "uniquely determined up to higher cells".
- It does *not* give a theory of identity of arbitrary derivations. Proof identity of a derivation of A is judgmental equality of terms (βη etc.), and that is a metatheoretic choice. The identity type internalises identity only for *elements of types*, not for derivations of judgments.

**(4) Strongest limitation.** The choice of foundation decides what proof identity is. Under UIP/K or the reflection rule (ETT), the higher structure collapses. Under univalence, U is not a set. So "proof identity" is foundation-relative, not invariant. Book HoTT with univalence as an axiom also lacks canonicity: Sterling–Angiuli, verified below, say "unlike homotopy type theory [65], both enjoy canonicity".

**(5) Relation to ProofBasis.** Adjacent, with strong precedent. It already gives a principled two-level answer: judgmental (computational, metatheoretic) identity versus propositional (internal, proof-relevant, higher) identity. Any ProofBasis notion of "proof identity" must say which level it means, or it conflates rubric items 4/5. A deep dive could change the framing: it shows that "proof identity" is not one relation but a tower, and that the tower's coherence is already governed by a contractible operad.

**(6) Neighbours.** D2 makes univalence compute. D4/D5 supply the operadic/(∞,1) semantics. D3: Kraus–von Raumer use Squier-style rewriting to build HoTT coherence (D7).

---
## D2. Cubical type theory

**(1) Object.** A dependent type theory with an interval I, path types, a face lattice, and Kan composition/coercion operations. Glue types give univalence. There are De Morgan (CCHM) and Cartesian (ABCFHL) variants.

**(2) Results.**
- *Cohen–Coquand–Huber–Mörtberg*, arXiv:1611.02108v1. VERIFIED_SOURCE (abstract): "function extensionality is directly provable in the system. Further, Voevodsky's univalence axiom is provable in this system ... we provide semantics for this cubical type theory in a constructive meta-theory." (The TYPES 2015 / LIPIcs 2018 venue is UNVERIFIED-MEMORY.)
- *Huber*, "Canonicity for cubical type theory", arXiv:1607.04156v2. VERIFIED_SOURCE: "any natural number in a context build from only name variables is judgmentally equal to a numeral". The intro says normalization and decidability of type checking are "not yet established" (as of 2016–17).
- *Coquand–Huber–Sattler*, "Canonicity and homotopy canonicity for cubical type theory", LMCS 18(1:28) 2022, DOI 10.46298/LMCS-18(1:28)2022, arXiv:1902.06572v6. VERIFIED_SOURCE. Homotopy canonicity: "every natural number is path equal to a numeral, even if we take away the equations defining the lifting operation on the type structure". The value is "independent of these non-canonical choices". Caveat: the initial model "which we conjecture to be the term model".
- *Sterling–Angiuli*, "Normalization for cubical type theory", arXiv:2101.11479v2 (IEEE LICS 2021). VERIFIED_SOURCE. Normalization for *Cartesian* cubical type theory, "yielding a bijection between equivalence classes of terms in context and a tractable language of β/η-normal forms". Corollaries: decidability of judgmental equality (Cor. 47) and injectivity of type constructors (Thm 43). Explicit scope caveat: "The present paper does not describe universes or the modifications necessary to prove normalization for De Morgan cubical type theory". The paper says it can be adapted "without conceptual changes" (a claim, not a proof).

**(3) Represents / cannot.**
- It represents *computation of higher paths*: transport and composition reduce, and univalence has computational content.
- It cannot remove the "non-canonical choices" in the equations for Kan operations at each type former. These are presentation-dependent (CHS). Homotopy canonicity shows the *values* are independent of them, but the judgmental theory is not.

**(4) Strongest limitation.**
- Several inequivalent cube categories and interval structures (De Morgan vs Cartesian) each support a theory. So there is *no unique* cubical presentation.
- Decidability of conversion is proved only for the Cartesian variant without universes, in the paper read.
- Equations for Kan operations at type formers are added per connective (a schema, not a finite fixed algebra).

**(5) Relation.** Adjacent, and an important control case. It is a worked example where the *same* homotopical content gets multiple non-unique computational presentations. That counts against any claim that a finite generative basis for proof computation is canonical. A deep dive could reframe ProofBasis's "computation vs proof identity" distinction: CHS separates strict canonicity from homotopy canonicity.

**(6) Neighbours.** D1 (semantics), D7 (directed cubes in Riehl–Shulman), D3 (cubical Squier, Lucas).

---
## D3. Higher-dimensional rewriting and polygraphs

**(1) Object.** An n-polygraph is a system of generators in each dimension of a free strict n-category (or (n,1)-category). 2-polygraph = rewriting system; 3-cells = relations among rewrite paths ("homotopy basis", "coherent presentation").

**(2) Results.**
- *Ara–Burroni–Guiraud–Malbos–Métayer–Mimram*, *Polygraphs: From Rewriting to Higher Categories*, arXiv:2312.00429v2 (4 Sep 2025), published by CUP, DOI 10.1017/9781009498968. VERIFIED_SOURCE.
  - **Thm 7.3.5 (Squier coherence):** for a convergent 2-polygraph P, the generating confluences, one per critical branching, form an acyclic extension, so (P,P3) is coherent.
  - **Thm 8.1.2:** FDT is Tietze-invariant among finite presentations.
  - **Thm 8.2.1:** "If a category admits a finite convergent presentation, then it has finite derivation type." Squier first proved this for monoids.
  - **Thm 8.2.4 (Squier's S1):** S1 is finitely presented with decidable word problem, but has no FDT and no finite convergent presentation.
  - **Thm 9.3.4/9.3.5:** FDT ⇒ left-FP3. Finite convergent ⇒ left-FP3.
  - **Thm 9.3.15:** S1 is left-FP∞ but not FDT, "the converse implication is false in general". For k≥2, S_k is not FP3.
  - **§4.2.7:** for a finite 2-polygraph it is undecidable whether it is terminating or confluent, and whether "there is a finite convergent polygraph presenting the same category".
  - **§10.4:** "a finite convergent polygraph might give rise to an infinite number of critical branchings", which blocks direct generalisation of Squier to dimension 3.
  - **Thm 13.4.8:** every TRS is presented by a 3-polygraph that makes variable duplication and erasure explicit, and is finite if the TRS is. Scope: first-order terms / Lawvere theories. A text search of the book for binders/λ-calculus found no treatment of variable binding.
- *Guiraud–Malbos*, "Higher-dimensional categories with finite derivation type", arXiv:0810.1442v2 (TAC 2009, UNVERIFIED-MEMORY venue). VERIFIED_SOURCE (§4.3): Squier generalises to n-polygraphs, but "this result fails to generalise to higher-dimensional polygraphs ... for every n ≥ 3, there exists at least a finite and convergent n-polygraph with an infinite number of critical branchings."
- *Guiraud–Malbos*, "Polygraphs of finite derivation type", arXiv:1402.2587v2 (survey). VERIFIED_SOURCE (abstract).
- *Gaussent–Guiraud–Malbos*, "Coherent presentations of Artin monoids", arXiv:1203.5358v4. VERIFIED_SOURCE (abstract): homotopical completion-reduction, "the so-called Tits-Zamolodchikov 3-cells extend Artin's presentation into a coherent presentation".
- *Mimram*, "Towards 3-dimensional rewriting theory", LMCS 10(2:1) 2014, arXiv:1403.4094. VERIFIED_SOURCE: "contrarily to string or term rewriting systems, these generalized rewriting systems can give rise to an infinite number of critical pairs, even when they are finite!" (attributed to Lafont).
- *Lucas*, "A cubical Squier's theorem", arXiv:1612.06541. VERIFIED_SOURCE (intro only).
- **Direct prior art:** *Guiraud*, "The three dimensions of proofs", arXiv:math/0612089v1 (APAL 141 (2006) 266–295, as cited in 0810.1442 [12]). VERIFIED_SOURCE (abstract, Thms 2.4.3, 3.3.1).
  - "the free 3-category generated by this 3-polygraph describes the proofs of classical propositional logic modulo structural bureaucracy".
  - Thm 2.4.3 is a two-way *provability* correspondence between SKS (calculus of structures) and the 3-polygraph Σ_K.
  - Thm 3.3.1 says SKS bureaucracy permutations correspond to exchange relations of 3-cells.
  - Section 6 sketches SLLS (linear logic).
  - Scope: propositional, deep-inference. No quantifiers or binders.

**(3) Represents / cannot.**
- It represents: syntax as cells, derivations as higher cells, and relations among derivations as further cells. There is an exact finiteness invariant (FDT) that is independent of presentation, and a homological shadow (FP3, H3).
- It cannot represent, in this framework as found: variable binding (first-order Lawvere/TRS only), or dependent types. In dimension ≥3, finiteness of critical branchings fails.

**(4) Strongest limitations.**
- (a) FDT and finite-convergent presentability are presentation-invariant *obstructions*. Some decidable, finitely presented theories have no finite coherent basis (Squier S1). Any claim that "a finite basis for proof identity exists" must at least clear an FDT-type obstruction.
- (b) Existence of a finite convergent presentation is undecidable.
- (c) In dimension ≥3, finite convergent ≠ finitely many critical branchings.

**(5) Relation.** **Direct prior art** for the "finite generators + composition + higher cells for proof identity" part of ProofBasis, at least for propositional and first-order algebraic fragments (Guiraud 2006 for proofs; the book for TRS). A deep dive should change the framing. The natural precise form of the ProofBasis question is "does the relevant (n,1)-category have FDT / a finite polygraphic resolution in low dimensions?". The answer is already known to be "not always" for decidable monoids.

**(6) Neighbours.** D4 (Mac Lane coherence becomes a rewriting result; Guiraud–Malbos 1004.1055). D6 (homology). D7 (Kraus–von Raumer HoTT version). D5 (string diagrams = 2-polygraph cells).

---
## D4. Coherence theorems

**(1) Object.** Free structured categories (monoidal, symmetric, braided, closed, ...). Coherence = characterisation of which formal diagrams commute, or strictification (pseudo-algebras equivalent to strict ones).

**(2) Results.**
- *Selinger*, "A survey of graphical languages for monoidal categories", arXiv:0908.3347v1. VERIFIED_SOURCE. **Thm 3.1** (coherence for planar monoidal categories, citing Joyal–Street): "A well-formed equation between morphism terms in the language of monoidal categories follows from the axioms of monoidal categories if and only if it holds, up to planar isotopy, in the graphical language."
  - Caveat 3.2: the Joyal–Street proof covers "recumbent" (progressive) isotopies, and the general case is "conjecture".
  - Selinger distinguishes Mac Lane's form ("all diagrams built from only α, λ, ρ, id, ∘, ⊗ commute") from Kelly-style characterisation of all derivable equations.
- *Guiraud–Malbos*, "Coherence in monoidal track categories", arXiv:1004.1055v2. VERIFIED_SOURCE. The intro restates Mac Lane as reducing "every diagram commutes" to a finite "coherence basis". Braided case: "a diagram is commutative if and only if its two sides correspond to the same braid". The paper proves coherence via convergent presentations: "the confluence diagrams of critical branchings form a coherence basis".
- *Lack*, "Codescent objects and coherence", JPAA 175 (2002) 223–241. SECONDARY_ONLY (web search; TAC 31-9 citing statement: with strict codescent objects preserved by the 2-monad, the strict→pseudo inclusion has a left 2-adjoint with unit an equivalence). NOT_ACCESSED primary.
- Power, "A general coherence result" (JPAA 1989): NOT_ACCESSED; venue and statement are UNVERIFIED-MEMORY. Mac Lane 1963; Kelly; Kelly–Mac Lane (closed categories): NOT_ACCESSED.

**(3) Represents / cannot.**
- It represents: proof identity for *structural* operations is decidable and characterised by a geometric invariant (isotopy, braid, permutation).
- It cannot: "all diagrams commute" fails beyond the simplest cases. In the braided case, commutation = same braid. For closed and other structures, coherence needs side conditions (UNVERIFIED-MEMORY for Kelly–Mac Lane).

**(4) Limitation.** The structural part of proof identity is not "all equal" in general. It is equality *modulo a nontrivial invariant* (braid group, isotopy class), and the invariant is structure-specific. No single coherence theorem covers all foundations.

**(5) Relation.** Adjacent, with strong analogy. Coherence theorems are the established, exact model for "a finite set of generating 2-cells determines all identities of structural proofs". A deep dive would sharpen ProofBasis by giving a baseline control (rubric item 9). It is unlikely to change the framing beyond D3.

**(6) Neighbours.** D3 (proof method), D5 (string diagrams), D1 (Lumsdaine's contractible operad is an ∞-coherence statement).

---
## D5. (∞,1)/higher-categorical semantics; string diagrams; globular operads

**(1) Object.** Proofs as morphisms, proof transformations as 2-cells, and so on. Weak ω-groupoids/categories via contractible globular operads (Batanin/Leinster). (∞,1)-toposes as models of HoTT. Graphical languages.

**(2) Results.** Selinger Thm 3.1 (above). Lumsdaine / van den Berg–Garner (D1). Shulman 1904.07004 (D1). All VERIFIED_SOURCE at the level stated. Batanin, Leinster, Joyal–Street primary texts: NOT_ACCESSED.

**(3)/(4) Represents / cannot; limitation.**
- These are *semantic* (models), not generative bases.
- String diagrams are sound and complete only relative to a fixed doctrine (planar, braided, symmetric, ...), and only with technical caveats (Selinger 3.2).
- Weak ω-structures are specified by contractible operads, so "all composites agree up to a contractible space" rather than a finite set of generators.

**(5) Relation.** Adjacent. They give the semantic target any finite basis would need to present. No deep dive is expected to alter framing beyond D1/D3.

---
## D6. Homological / topological invariants of rewriting and proof systems

**Results.**
- Squier: finite convergent ⇒ left-FP3 (book Thm 9.3.5). FDT ⇒ FP3 (9.3.4). Converse false (S1: FP∞ but not FDT, Thm 9.3.15). The preface says that for groups, FDT ⇔ FP3 (text truncated in my read; book line ~9868). VERIFIED_SOURCE (2312.00429v2).
- Anick and Kobayashi resolutions: mentioned in the book preface (SECONDARY_ONLY via book).
- *Guetta*, "Homology of categories via polygraphic resolutions", arXiv:2003.10734v2. VERIFIED_SOURCE (abstract): "the polygraphic homology of a small category ... is naturally isomorphic to the homology of its nerve, thereby extending a result of Lafont and Métayer."
- Lafont–Métayer "Polygraphic resolutions and homology of monoids" (JPAA 2009): NOT_ACCESSED primary (SECONDARY_ONLY via Guetta).
- Persistent homology of proofs: no real literature found. Not searched in depth.

**Limitation.** Homological invariants are strictly weaker than homotopical (FDT) ones for monoids. They are *obstructions*, not constructions.

**Relation.** Analogy/tool. Useful as a falsification test: compute H3 or FP3 of a candidate "proof-identity" presentation. If it is not FP3, then no finite convergent basis exists.

---
## D7. Missing / adjacent families found

- *Kraus–von Raumer*, "A rewriting coherence theorem with applications in HoTT", arXiv:2107.01594v2. VERIFIED_SOURCE.
  - Thm 14: "Let (Σ0, Σ1, Σ2) be a terminating generalised 2-polygraph which is closed under congruence and which cancels inverses. If it has a Winkler-Buchberger structure WB, then it has a homotopy basis."
  - Thm 30 translates this into HoTT.
  - Thm 41: fundamental groups of free higher groups on a set are trivial.
  - This is the bridge D3↔D1: confluence + well-foundedness suffice for coherence. It only reaches low truncation levels ("approximate" open questions).
- *Licata–Harper*, "2-Dimensional Directed Type Theory", MFPS 2011 preprint, https://www.cs.cmu.edu/~rwh/papers/2dtt/mfps.pdf. VERIFIED_SOURCE (abstract): "whereas in symmetric type theory proofs of equivalence can be internalized using the Martin-Löf identity type, in directed type theory the two-dimensional structure must be made explicit at the judgemental level". It has a model in Cat. ENTCS 276, DOI 10.1016/j.entcs.2011.09.026: SECONDARY_ONLY (web search).
- *North*, "Towards a directed homotopy type theory", arXiv:1807.10566v1. VERIFIED_SOURCE (abstract): a hom type former interpreted in Cat.
- *Riehl–Shulman*, "A type theory for synthetic ∞-categories", arXiv:1705.07442v5. VERIFIED_SOURCE (abstract): Segal types, in which composition is "automatically ... coherently associative and unital at all dimensions"; a directed Yoneda lemma.
- Recent directed TT (arXiv titles only, NOT read): 2409.10237 (Di- is for Directed), 2410.19520, 2510.17494, 2602.17480, 2604.18668. Recent activity shows this is a live area.
- Not found / not searched in depth: "proof-relevant rewriting" as a named family; "rewriting modulo homotopy"; categorical combinators. NOT_ACCESSED.

**Relation.** Directed TT is the natural home for *non-invertible* proof transformations (rewrites, cut-elimination steps). HoTT's symmetric identity cannot model these without collapsing direction (rubric item 7: direction/time vs identity). Adjacent; a deep dive is worthwhile if ProofBasis treats transformations as directed.
