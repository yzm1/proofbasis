# Stage 0.6 — Source and argument notes for Report 005

Date: 2026-10-08. Scope: decisive passages for the atomic-profile obstruction and its positive counterchecks. Page numbers below distinguish journal pages from one-based PDF pages. No publication PDF or new research infrastructure is committed. Hashes identify the locally inspected downloads, not formal proof artifacts.

## 1. Repository evidence and freeze provenance

Baseline: integrated main at `9412a148717dfd3d50bf2e260af1fdf771f9bc9b`, including the separately preserved PR #1/#2 audits and later self-review, Tasks 002/003, their source notes, synthesis, and Stage-0.5 acceptance review. Read the repository instructions, charter, definitions, falsification plan, protocols, and research reports before the conjecture freeze. Existing agent arguments are evidence, not primary mathematical authorities.

- [Report 002 §2.1](002-fundamentality.md): independently specified finite schematic syntax/rules and sorted substitution. Report 005 adds finite schematic proof congruences explicitly.
- [Report 002 §§2.3–2.4](002-fundamentality.md): SN/HN/HOM; D1 versus D2; FULL is a strengthening. D2 T1 says atoms go to atoms of matching sort; T2 fixes the wrapper independently of S. Neither implies finite atomic profiles without further interface restrictions.
- [Report 002 §5 and fresh critique](002-source-notes/fresh-critique.md): a reflected finite signature can satisfy strong naturality and rule-template compositionality while interpreting a coded source signature. These alone do not exclude an interpreter. The construction's stronger adequacy is not independently certified here.
- [Report 003 and extraction notes](003-structural-fidelity.md): equality depends on the selected source congruence; a failure of declared-rule LF is not impossibility for other encodings. CLF/Petri correspondence has a specific labeled-resource and concurrent-trace scope. Prior primary extractions are reused for these contextual cautions, not promoted to a new universal theorem.
- [Stage-0.5 acceptance review](../docs/STAGE_0_5_ACCEPTANCE_REVIEW.md): neither old report resolves the original existence question. This report preserves that limitation when its additional finite-profile/fullness hypotheses are relaxed.

The provisional class/interface/equality/environment choices were written in `reports/005-negative-obstruction.md` before constructing the cyclic obstruction. The freeze block is preserved in the delivered report. An optional request for owner preference about source scope received no clarification during the investigation; the stated all-finitely-schematic choice governs this provisional report. It is not represented as an agreement with a separate positive-role investigator.

## 2. Cannon–Floyd–Parry: the positive countercheck

**Citation:** J. W. Cannon, W. J. Floyd, W. R. Parry, *Introductory notes on Richard Thompson's groups*, L'Enseignement Mathématique 42 (1996), 215–256.

**Inspected copy:** [journal scan hosted at Paris-Saclay](https://www.imo.universite-paris-saclay.fr/~emmanuel.breuillard/Cannon.pdf).

**SHA-256:** `ee23fe9fe5a2044e25df4f9cdc83cfb3e81f7ef025eb519724983097fc3f4530`.

**Status: VERIFIED_SOURCE** for the passages below. The paper's introduction and §6 identify unpublished Thompson notes as antecedents. This is an inspected published presentation with arguments; it does not imply novelty of the group facts or of their use here.

- §6, p. 240 / PDF 27: defines V as right-continuous circle bijections with finitely many dyadic breakpoints and linear pieces of slope a power of 2. Labeled binary-tree leaf pairs encode the bijections.
- p. 241 / PDF 28, paragraph immediately before Lemma 6.1: the displayed finite sets of leaf permutations generate subgroups isomorphic to symmetric groups on the specified dyadic interval partitions. In particular V contains symmetric groups of unbounded finite degree and cyclic subgroups of every finite order.
- Lemma 6.1, pp. 241–242 / PDFs 28–29: A, B, C, π₀ generate V and satisfy fourteen displayed relations. **This lemma alone gives only a surjection from the abstract presented group.**
- Definition of V₁ and subsequent paragraph, p. 243 / PDF 30: V₁ is the group presented by these four generators and fourteen relations; proving it simple will make the surjection V₁→V an isomorphism.
- Theorem 6.9, p. 248 / PDF 35: “V₁ is simple.” Together with the already defined nontrivial V and surjection, this proves completeness of the finite presentation. Report 005 cites this combined argument, not the insufficient assertion that the generators merely satisfy the relations.

**Reproduction / INFERENCE:** choose a finite binary tree with n leaves and the cyclic leaf permutation. It has exact order n because every smaller positive power moves some leaf interval. The generator theorem gives a finite word w_n representing this element. The unary proof-category construction in Report 005 §4.1 uses group words and the fixed presentation; equation certificates are finite chains of group/congruence axioms. The per-n translation is effective once a finite w_n is selected. No algorithm for finding minimal words is asserted or needed. The embedding is faithful but not full, because End(P)=V rather than its selected finite cyclic subgroup.

## 3. Hasegawa: genuine proof equality and fullness

**Citation:** Masahito Hasegawa, *Linearly Used Effects: Monadic and CPS Transformations into the Linear Lambda Calculus*, FLOPS 2002, LNCS 2441, 167–182.

**Inspected author copy:** [flops02.pdf](https://www.kurims.kyoto-u.ac.jp/~hassei/papers/flops02.pdf).

**SHA-256:** `d2de8e8880445d8de6eb87200d678b6846991b925569df3c00d0f9576c946fee`.

**Status: VERIFIED_SOURCE.** The introduction, definition of the linear CPS translation in §4, and §§5–6 are the relevant scope. Crucial passages were reread directly rather than relying on Report 002.

- Proposition 4, p. 176 / PDF 10: type soundness for the translation from the specified computational lambda calculus into the linear lambda calculus, with unrestricted translated context Γ° and empty linear context.
- Proposition 5, same page: source equality iff target equality at `(σ°→o)⊸o`. The paper calls it “equational completeness of Sabry and Felleisen [16]”; the original [16] proof was not re-extracted for this report. The exact primary statement checked is Hasegawa's attributed proposition.
- §5 explicitly assumes o is a target base type absent from the source calculus.
- Theorem 1, p. 177 / PDF 11: every target inhabitant of that translated context/type is provably equal to a translated source term. This is fullness for this CPS translation, with the source/target equations of the paper.
- §6, pp. 177–178: recursion can retain type/equational soundness with target fixpoint operators; the author says fullness for the extension remains an open issue in that paper. This report does not assert its current status or extend Theorem 1 to it.

**Limit:** translated proof boundaries are compound CPS types. This result is not a theorem about all finitely schematic calculi, and it does not meet the frozen native atomic-interface requirement for source computation judgments.

## 4. Clarke–Scherer–Zeilberger: free unary bifibrational proof structure

**Citation/version:** Bryce Clarke, Gabriel Scherer, Noam Zeilberger, *The free bifibration on a functor*, [arXiv:2511.07314v3](https://arxiv.org/pdf/2511.07314v3), 15 January 2026. The inspected version is a preprint; no journal acceptance or subsequent version is presumed.

**SHA-256:** `89f6f9f7b80104c4bc7a58f4c2a5ce1a95710a5262993a58198068af8ec6eb73`.

**Status: VERIFIED_SOURCE** for the construction's definition and Theorem 1.17. Checked pp. 3–4, §1 formula/sequent definitions, Definition 1.4, and Lemma 1.16/Theorem 1.17 directly.

- pp. 3–4: p:D→C is an arbitrary functor. The free bifibration has a generator functor η_p:D→Bif(p) over C. For each bifibration q:E→C and θ:D→E over C, there is a unique bifibration morphism extending θ. Morphisms preserve the chosen cartesian/opcartesian liftings. This is the relevant quantified universal property.
- §1, p. 8: formula constructors include push/pull indexed by base arrows; atomic formulas come from D. These parameters are not a finite fixed native atom menu.
- Definition 1.4, pp. 13–14: permutation equivalence is the least typed congruence containing four displayed equations. Arrows of the constructed category are unary derivations modulo this relation; admissible cut defines composition.
- Lemma 1.16 and Theorem 1.17, p. 20 / PDF 20: the interpretation is the unique extending bifibration morphism; “Λ_p:Bif(p)→C is the free bifibration on p:D→C.”

**Limit:** the theorem does not say η_p is full faithful for every p, or that arbitrary external proof calculi have full faithful encodings with no supplied rule/equality machinery. It is not the general multiary equality-reflection theorem still missing from the inspected LSR template.

## 5. LSR: exact conjecture/theorem discrepancy

**Citation:** Daniel R. Licata, Michael Shulman, Mitchell Riley, *A Fibrational Framework for Substructural and Modal Logics*, 2017 extended version.

**Inspected author copy:** [lsr17multi-ex.pdf](https://dlicata.wescreates.wesleyan.edu/pubs/lsr17multi/lsr17multi-ex.pdf).

**SHA-256:** `7f04277218da9f12e7cf36cf487b4004ddfa1914bb7a4b364f74ab86bca1a7db`.

**Status: VERIFIED_SOURCE** for the printed statement, not for conjecture resolution.

- p. 59 / PDF 59, Conjecture 8.5: if d≡d′ then d↓≡_p d′↓.
- §9.1, pp. 59–61: proposed full faithful translation of object proofs modulo selected categorical βη equality. Derived rules, normal-form inverse laws, and reflection of permutations are explicit obligations.
- Remark 9.2 p. 60 refers to “Theorem 8.5.” This conflicts with the immediately preceding label **Conjecture**; it cannot certify the missing result.
- p. 61: the authors do not abstract the template as a lemma because the class of input native sequent calculi is not precisely defined.

**Limit:** absence of a verified resolution here is UNKNOWN, not evidence that the conjecture is unsolved today. Arbitrary mode theories or base arrows do not establish a fixed finite-profile target.

## 6. Argument provenance, access limits, and remaining search leads

The S_n class calculation, atomic-profile pigeonhole argument, A_V embedding, Z-set endomorphism calculation, and tensor-only first subcase are **INFERENCE / informal arguments** developed and checked by hand. No existing proof checker was run. Their status is independent of source hashes, source quotation, and agent agreement. These arguments do not justify a novelty claim.

An attempted stronger positive route via Higman's group-embedding theorem was not used as established evidence: the original Royal Society PDF request returned HTTP 403. The accessible Cannon–Floyd–Parry result already suffices for the positive countercheck needed here.

A targeted search for the final type-endomorphism test found Soloviev, *Automorphisms of types in certain type theories and representation of finite groups* (MSCS 29(4), 2019, 511–551; DOI [10.1017/S0960129518000129](https://doi.org/10.1017/S0960129518000129)). Only the publisher abstract was inspected at this point; full theorem hypotheses/proofs were not recovered. It advertises finite-tree automorphism groups for simple types and arbitrary finite-group representations at second-order/dependent types. **UNKNOWN for the exact theorem package relevant here:** automorphisms alone do not classify all endomorphisms, and the proposed test concerns a specifically linear/exponential core. This lead prevents treating the test as novel or assuming higher-order types cannot host cyclic identities. The follow-up author paper's official PDF endpoint returned 503/502 in attempted retrieval. No obstruction or positive universality claim rests on that abstract.
