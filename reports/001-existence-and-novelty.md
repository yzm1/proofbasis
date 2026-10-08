# Report 001: Adversarial existence and novelty audit

| | |
|---|---|
| **Task** | `tasks/001-existence-and-novelty-audit.md` |
| **Claim version audited** | `docs/DEFINITIONS_AND_CONJECTURES.md` at commit `e3d2e6e` (called **CV0** below) |
| **Date** | 2026-10-08 |
| **Status of this report** | Requests review. It does **not** claim research closure. Nothing here is FORMALIZED. Every new argument by the author is labelled INFERENCE or CONJECTURE and is an *informal argument*, not a proof. |
| **Evidence log** | [`reports/001-source-notes/`](001-source-notes/README.md): verbatim quotes, retrieval URLs, versions read, statuses |

---

## 0. Executive verdict

**Recommendation: do not advance. Stop the program as chartered. At most, narrow to a single bounded literature gate (§10), with stop as the default outcome.**

The four outcomes the task asks about, in order:

**(a) Already known (F01): yes, for R0–R1 and largely for R2.**
- *R1 (preserve and reflect derivability).* A fixed, finitely presented theory that preserves and reflects derivability for a whole class of finitely presented systems is a published theorem: Clavel–Meseguer, universal rewrite theory U, Thm 3.2; extended by Clavel–Meseguer–Palomino, Thms 1, 4, 5, 6.
- *Logic representations.* The derivability-level notion of "a logic represented in a fixed framework" is defined and studied uniformly by Harper–Sannella–Tarlecki.
- *R2 (composition, substitution, binding, discharge).* LF achieves R2 as a compositional bijection on *derivations* for natural-deduction-style logics, proved encoding by encoding: HHP Thm 4.1; Pfenning Thm 3.2; Harper–Licata Thm 3.11. Nigam–Miller and Miller–Pimentel do the same for many sequent, natural-deduction and tableau systems in focused linear logic, with graded adequacy levels.
- *Many foundations on one kernel.* A single finite environment covering about 13 systems on one fixed kernel already exists: theory U in Dedukti, 38 declarations and 28 rules.
- *R4 (causal fidelity).* Prior art exists at the level of the encoding: CLF's concurrent equality, and rewriting logic's exchange law.

**(b) Vacuous under the current definitions (F02, F10): yes.**
- CV0 quantifies the class C *existentially*. It is therefore satisfied by C = {one system} (§2.2).
- Even with C fixed, R0 and R1 are achieved by published "universal interpreter" constructions. The most extreme is Mossakowski–Diaconescu–Tarlecki Prop. 2.25: three-rule propositional Horn logic conservatively represents *every* compact countable entailment relation.
- The authors of that result state that a formal "structurality" condition to exclude such flattenings is an *open question*.

**(c) Defeated by established counterexamples: yes, for the uniform version of R3, and for local-only R4/R5 on cyclic proofs.**
- *Classical and intuitionistic identity together.*
  - Joyal / Lambek–Scott / Došen Props 1–3: categorical proof identity for classical logic collapses to a preorder under the CCC-with-initial-object hypotheses.
  - Classical proof identity has no agreed definition (Straßburger).
  - Call-by-name and call-by-value λμ have different equational theories (Selinger, Rem. 8.2).
- *Linear logic with units.* Proof identity in MLL with units is PSPACE-complete (Heijltjes–Houston, Thm 9.1).
- *Standard translations.* The textbook Girard call-by-value translation does not reflect equality (Maraist–Odersky–Turner–Wadler §8.3).
- *Natural encodings.* Gardner proves that "natural" (bijective-on-proofs) encodings fail for Hilbert S4 and other systems.
- *Cyclic proofs.*
  - Validity is a global ω-regular condition (Brotherston, Prop. 5.1.10).
  - Validity is PSPACE-complete for µMALL threads (Nollet–Saurin–Tasson 2019; abstract only).
  - Validity is Σ⁰₁-complete once cuts are allowed under bouncing threads (Baelde et al., Cor. 6.6).

**(d) Defensible open target after narrowing: only a narrow, possibly already-known, residue survives** (conjecture C\*, §10).

The adversarial analysis below yields a **vacuity–identity dilemma (§6.3)**.
- If the environment may add equations or rewrite rules, R3 and the interpreter constructions are vacuous.
- If it may not, the fixed algebra must natively contain the identity-carrying structure of every foundation it covers. Universality is then achieved by *inclusion of each foundation's structure*, not by a small "basis".

That conclusion is an INFERENCE from verified sources, not a theorem. If it holds, it removes the main motivation of the charter.

---

## 1. Scope, method and research-access limits

**Method.**
- Six extraction agents retrieved primary texts over the open web: author homepages, arXiv, DROPS/LIPIcs, HAL, LMCS, technical-report servers, and university-hosted copies.
- They extracted definitions and theorems with locations, under a protocol that forbids unverified citations (`001-source-notes/00-extraction-protocol.md`).
- I then read all six logs, and re-located ten decisive passages directly in the downloaded texts (listed in `001-source-notes/README.md`).
- Agreement between agents is *not* formal verification.

**Access limits.** These materially affect certainty.
- **Paywalls and bot walls** blocked:
  - Lambek & Scott 1986: Joyal collapse location known only secondhand, p. 67.
  - Brotherston & Simpson, JLC 2011: content verified via Brotherston's 2006 thesis instead.
  - Clavel & Meseguer, TCS 285 (2002).
  - Simpson, FoSSaCS 2017.
  - Berardi & Tatsuta, LICS 2017.
  - Nollet–Saurin–Tasson, TABLEAUX 2019: abstract only.
  - Ben-Sasson–Impagliazzo–Wigderson: abstract only.
  - Statman 1979 (both papers), Orevkov, Boolos.
  - Hofmann–Streicher 2002.
  - Krajíček's books.
  - Saillard's thesis.
  - Danos–Regnier 1989.
- **Preprints read instead of journal versions:**
  - HHP: author typescript.
  - Paulson: TR-130.
  - Harper–Sannella–Tarlecki: draft of Dec 1992.
  - Maraist et al.: MFPS'95 version.
  - Rabe: preprint.
  - Mossakowski–Diaconescu–Tarlecki: preprint.
  - Clavel–Meseguer–Palomino: extended preprint.
  
  Theorem numbers and pages refer to the version read.
- **OCR'd scans:** Gardner's thesis and Avron–Honsell–Mason 1987. Quotes may contain OCR noise.
- **No mechanised checking** was performed. No new implementation was written, per AGENTS.md rule 9.

**Status vocabulary.** As in `docs/RESEARCH_PROTOCOL.md`: VERIFIED_SOURCE, SECONDARY_ONLY, INFERENCE, CONJECTURE, UNKNOWN, REFUTED. UNVERIFIED-MEMORY marks an author recollection that has not been checked.

---

## 2. Work package 1: formalization audit

### 2.1 Unresolved terms in CV0

Each term below can change the truth value of the conjecture.

| # | Term in CV0 / charter | Why it is unresolved | Consequence if left open |
|---|---|---|---|
| T1 | "system S", "effectively presented" | Candidates include:<br>• Cook–Reckhow (any poly-time onto function; no structure);<br>• a finite rule-schema calculus;<br>• an LF signature;<br>• a Meseguer entailment system or proof calculus (an arbitrary structure P(T));<br>• a free category or multicategory (carries identity).<br>Also unclear whether "effective" means decidable validity of finite objects (fails for cyclic proofs with bouncing threads: Σ⁰₁-complete) or r.e. proofs. | The same S yields different questions. Cook–Reckhow systems make R1 a p-simulation question that is settled by EF + reflection (§6.1). |
| T2 | "judgments", "environments", "verifiable inference steps" | "Verifiable" is undefined: decidable per step? poly-time? local? Cyclic proofs have locally checkable steps but global validity. | F05 cannot be evaluated. |
| T3 | Environment E: "ordinary propositions/definitions" vs "certificates for extensions" | No criterion separates a definition from a rule. Examples:<br>• Isabelle definitions are ≡-axioms;<br>• Dedukti definitions are rewrite rules;<br>• in LF, rules *are* declarations (HHP p. 17: "there is no distinction between rules and proofs"). | The trust boundary is undefined (F03). |
| T4 | "finite algebra A": "typed operation schemas", "composition", "equations or congruence", "terms/diagrams" | Schemas over what parameters? Is the congruence fixed in A, or extendable by E? Terms, string diagrams, polygraphs and proof nets have different identity theories. | Whether E may extend A's congruence decides whether R3 is vacuous (§6.3). |
| T5 | "representation F_S" | The following are all left open:<br>• injective, full, faithful, or only sound and complete;<br>• effective;<br>• compositional with respect to *which* substitution;<br>• whether F is uniform in S (a single function of S's presentation) or chosen per S. | Every published framework proves adequacy *per encoding*. HHP p. 17 calls the general scope a "thesis". Gardner and Harper–Sannella–Tarlecki give uniform definitions, but only at derivability level. |
| T6 | "proof equivalence ~_S" (declared) | The same S carries several incompatible identities:<br>• call-by-name vs call-by-value λμ;<br>• Prawitz normalization vs Lambek generality, which already disagree for intuitionistic →∧ (Došen 2003). | R3 must be indexed by the pair (S, ~_S), not by S. |
| T7 | "causal relation", "independence", "conflict" | Relative to the encoding's term structure. Rewriting logic's exchange law is *finer* than the CCS causal model, which needs an extra quotient (Meseguer survey 2012). | R4 is not invariant across encodings (F06). |
| T8 | "nontrivial class C" | Undefined, and *existentially* quantified (see 2.2). | The conjecture is trivially true. |
| T9 | "preservation and suitable reflection", "compatibility", "specified relation", "agreed subset" | Placeholders for choices. | The conjecture has no fixed truth value. |
| T10 | "mathematically meaningful operations" (README) | No formal content. The closest literature notion, "structurality" of translations, is stated as **open** by Mossakowski–Diaconescu–Tarlecki (preprint p. 26). | The anti-vacuity criterion is undefined (F02). |
| T11 | "fixed" algebra | Is A fixed before C is chosen? Is A allowed to contain a universal machine as data or rules? | Interpreter constructions (§6.1). |
| T12 | "translated environment" | May the translation of S's environment introduce new axioms or rules (Meseguer's maps send signatures to *theories*) or reflection schemata? | EF + Refl_S, and MDT's Δ. |

### 2.2 A logical defect in CV0 (F10)

Status: INFERENCE. The argument is elementary.

CV0 has the form

> ∃A ∃C ∀S∈C ∃F_S [properties], with "nontrivial" undefined.

Take any finite calculus A that satisfies the listed properties for itself. For example, the simply typed λ-calculus read as natural deduction for intuitionistic implication. Let C = {A} and F = id. Then:
- derivability is preserved and reflected;
- substitution and binding are preserved;
- βη is preserved and reflected.

So CV0 as written is **true and uninformative**.

**Fix (proposed amendment A1):** C must be fixed *before* A, by a named, independently motivated benchmark list or a formally defined class. The statement becomes ∀S∈C (or ∃A for a given C).

### 2.3 Rigorously distinct candidate versions

The task requires at least two. Four are given here; they differ in what is fixed, what is preserved, and what is excluded.

**V1: Uniform framework adequacy (LF-style; targets R1 + R2).**
- C: deductive systems presented by finitely many rule schemas over second-order abstract syntax, with "pure" hypothetical judgments (no non-local side conditions).
- A: a fixed weak dependent type theory with decidable conversion.
- E_S: constant declarations only.
- Requirement: a *uniform* map S ↦ (E_S, F_S). Each F_S is a compositional bijection between S-derivations (modulo α) and canonical A-terms, commuting with substitution of both terms and derivations.
- Trade-off: closest to existing practice. Per-system it is largely known: HHP Thm 4.1; Pfenning Thm 3.2; Nigam–Miller Props 2–3, 7, 9, 13, 15, 17, 19. It excludes linear and relevant logics under the direct definition (Gardner Cor. 5.1.8). The open part is uniformity over a class, which HHP p. 17 explicitly calls a "thesis". **Novelty: low.**

**V2: Quotient adequacy with fixed identity (targets R3).**
- As V1, but each S comes with a declared congruence ~_S.
- Requirement: F_S induces a bijection between S-derivations/~_S and A-terms/≡_A, where ≡_A is A's *fixed* definitional equality and E_S may not extend ≡_A.
- Trade-off: this is the version that would make the project non-trivial. It runs directly into the collapse and complexity obstructions (§7) and the vacuity–identity dilemma (§6.3). **Novelty: UNKNOWN** for specific benchmark sets (§10).

**V3: Complexity-sensitive simulation (Cook–Reckhow style).**
- C: Cook–Reckhow proof systems.
- A: a fixed proof system.
- Requirement: F_S is a p-simulation (poly-time proof translation preserving the conclusion).
- Trade-off: precise and well studied, but structure-blind. Within Frege systems, basis-independence is established: Cook–Reckhow Thm 2.3 / Cor 2.4 / Cor 3.4; Reckhow 1976, SECONDARY_ONLY. Universality is trivialised by EF + Refl_S ≥p S (§6.1). **Novelty: none for the universality claim.**

**V4: Concurrency/causal fidelity (targets R4).**
- A: a fixed framework with a fixed independence congruence, as in CLF's =c or rewriting logic's exchange law.
- Requirement: F_S maps S's independence relation onto A's.
- Trade-off: prior art exists. CLF claims a bijection between concurrent Petri-net executions and terms "modulo =", stated in prose with no proof seen. It requires labelled tokens. Rewriting logic needs object-specific extra quotients. **Novelty: low to unknown.** The relation is encoding-relative.

---

## 3. Work package 2: strongest prior art (verified extractions)

Full quotes and locations are in the source notes. Status is VERIFIED_SOURCE unless stated.

### 3.1 Comparison matrix

| Result | Fixed machine | Environment holds | Class / hypotheses | R1 preserve / reflect | R2 compositional | R3 identity | Trust gap |
|---|---|---|---|---|---|---|---|
| **HHP 1993, Thm 4.1** (typescript p. 21) | LF λΠ, decidable (Thm 2.6) | All object rules as constants (p. 17) | First-order ND (Thm 4.2: HOL); scope beyond these is a "thesis" (p. 17); excludes "non-local applicability conditions" | Yes / yes | Yes: commutes with substitution of terms **and proofs** | Syntactic only: bijection on derivations modulo α. LF equality "is not to be confused with any equality … in a represented logic" (p. 3) | Adequacy is an informal per-signature meta-theorem |
| **Pfenning, handbook, Thm 3.2** (preprint p. 29) | LF | Signature | FO ND | Yes / yes | Yes, incl. [E/u]D | Object reductions declared as *signature judgments* (§3.6, pp. 32–33) | Same |
| **Harper–Licata 2007, Thm 3.11** | Canonical LF | Signature + "world" + subordination | Example languages | Bijection on typing derivations | Proved for terms; for derivations stated "possible", elided (p. 33) | Syntactic | Same |
| **Gardner 1992** (thesis, OCR) | ELF+ | Signature | Uniform definitions of "adequate" and "natural" | **Thm 5.1.7**: adequately represented ⇒ intuitionistic consequence. **Cor 5.1.8**: "There are no adequate representations of linear and relevant logics" | Natural = compositional bijection on proofs | **Thms 5.2.11, 5.2.13; Ex 5.2.6**: Hilbert S4, Hilbert PL via ND signature, and Prawitz ND-S4 are not natural | — |
| **Harper–Sannella–Tarlecki** (draft 1992, Defs 5.3, 6.13) | LF | Signature | Consequence relations *with weakening* (Def 2.1) | Uniform, conservative | — | None: LF consequence is inhabitation "for some M" | Proofs omitted in Sec. 6 |
| **Paulson 1989** (TR-130, Def 1, Thms 2–5) | Isabelle/Pure (⇒, ⋀, ≡) | Object rules as **axioms** | IPL, IFOL | "Faithful" = sound + complete for entailment | — | None: no proof objects (p. 33) | Axioms are trusted |
| **LLF** (Cervesato–Pfenning) | λΠ⊸&⊤ | Signature | Conservative over LF (Thm 2.9) | — | Linear contexts direct | "adding any other linear connective … destroys … usable canonical forms … by introducing commuting conversions" (p. 64) | Machine changed to fit substructural logics |
| **CLF** (TR CMU-CS-02-101) | LLF + monad (⊗, 1, !, ∃) | Signature | — | — | — | Fixed decidable concurrent equality =c: let-permutation of independent steps (Def 5, Thm 6). Petri-net adequacy "modulo =" claimed; proof not seen. LLF version "does not hold … forces a sequentialization" (p. 13) | Free ⊗/!/⊕ would be "catastrophic" for adequacy (p. 13) |
| **FPC** (Chihani–Miller–Renaud, JAR 2017) | LKF/LJF kernel | Untrusted clerks and experts (soundness by erasure, p. 13) | First-order only (p. 41) | Preserve only: "the only guarantee … is that the formula is … a theorem" (p. 30) | — | Not faithful to the client format (pp. 21–22) | None for client content; single foundation |
| **Nigam–Miller JAR 2010; Miller–Pimentel TCS 2013** | Focused LL (LLF) | Introduction clauses **and** Cut, Init, structural clauses Pos/Neg (environment); polarity assignment | LM/LJ/LK, NJ, GE, free deduction, KE, analytic cut | Yes / yes | "Full completeness of derivations" for listed encodings (sketched proofs). Level depends on clause shape (MP Ex 7–8) | Bijection with *focused* proofs; no proof-equality congruence | Structural rules and cut are trusted theory clauses. Non-commutative, hypersequent and light systems not covered |
| **Clavel–Meseguer 1996, Thm 3.2** (ENTCS 4, p. 9) | One finitely presentable rewrite theory U (≈14 rule schemas), U ∈ C | Object theory **as data term** | Unconditional, unsorted, finitely presentable; var(t′) ⊆ var(t); ground t, t′ | **Yes / yes** (Thms 3.11, 3.19) | No: one object step = many U steps | No. Proof-level U′ "can similarly" be exhibited: *claimed only* (p. 7) | U's own rules |
| **Clavel–Meseguer–Palomino** (extended preprint, Thms 1, 4, 5, 6) | U_mel, U_rl | Theory as data | Finitely presentable; nonempty kinds; conditional mel-based rewrite theories | Yes / yes. Def 3 requires the representation to be recursive and injective "to rule out unfaithful representations" | No | Lemma 1: "an infinite number of uninteresting derivations" per equation | — |
| **Martí-Oliet–Meseguer** (ENTCS 4; SRI TR 1993) | Rewriting logic | Object rules as rewrite rules; binding via equations | Linear logic (Thms 4.1, 6.1). "Any finitely presented logic" is an explicit **conjecture** (ENTCS p. 31) | Yes / yes (LL) | — | Fixed true-concurrency equations on encoded proofs. Linear-logic models need an *extra quotient* (TR p. 34: "weak product instead of a product") | Rules in environment |
| **Mossakowski–Diaconescu–Tarlecki 2009, Prop 2.25, Cor 2.26** | PHCL (3 rules) | Δ = the *entire* entailment relation as Horn clauses | Every compact countable entailment relation | Yes / yes (conservative) | — | — | **Vacuity theorem.** "Structurality" open (p. 26) |
| **Rabe, JLC 2017** (preprint) | MMT/LF | Syntax and inference system as declarations in Syn | Per encoding | Preserve (Thm 2.31). Reflection = "proof-conservativity", which Rabe calls "impractically strong" (p. 29) | Homomorphic translation of proofs | Framework βη preserved (Rem. 2.32), not reflected | Rules in environment |
| **Cousineau–Dowek 2007** (arXiv posting) | λΠ modulo | Per-PTS signature + 2 rewrite schemas | Functional PTS. Conservativity (Thm 1) needs λΠ_P terminating, closed inhabitation | Yes / conditional | Substitution and β-steps preserved (Prop 1) | No bijection (Remark 1; Examples 4–5) | Rewrite rules trusted |
| **Assaf 2015, Thm 5.24** | λΠ modulo | Same | Functional PTS, *no* normalization assumption | Yes / yes (inhabitation) | — | No | — |
| **Dedukti manuscript** (arXiv:2311.07185) | λΠ modulo; only declarations and rewrite rules | Every logic | — | — | — | — | "Checking confluence is out of the scope of Dedukti itself" (§3.1). Subject reduction needs confluence (Thm 8) |
| **Blanqui et al., "Some axioms for mathematics", FSCD 2021** | λΠ modulo | **One** finite theory U: 38 declarations, 28 rules | ≈13 systems (predicate logics, STT variants, CoC). Classical logic not a sub-theory. No inductive types or universes | Fragment theorem (Thm 7, Cor 8). **Not** provability-conservative: "it does not imply that if A is in Λ(Σ1) and A has a proof in U, then it has a proof in Σ1, R1" (§4) | — | None | Confluence and type preservation proved (Thm 9). Consistency of U not found in paper |
| **Felicissimo, FSCD 2022, Thm 46** (arXiv long version) | Dedukti | Annotation-heavy encoding with rewrite rules | Functional *explicitly typed* PTS, incl. non-normalizing | Yes | Commutes with substitution | **Bijection modulo ≡_H on framework-β-normal forms, and "M ↪* N iff ⟦M⟧ ↪* ⟦N⟧"**: object reduction preserved *and reflected* | ≈16× slower on one benchmark (§10). Needs environment rewrite rules |
| **Felicissimo–Winterhalter, FSCD 2024, Table 1** | Dedukti | — | Cumulative CoC encodings | None of four prior encodings has a conservativity proof; three have flawed soundness proofs; three are not confluent | — | — | Documented trust gap in real use |
| **Selinger, MSCS 2001** | — | — | Call-by-name / call-by-value λμ with ∧, ∨ | — | — | Structure Thm 3.18. Props 6.5, 7.6: categorical theories = CPS theories. Thm 6.12: finite axiomatisation. Prop 8.1: cbn ↔ cbv mutually inverse up to type iso. Note cbn equality is **defined** via CPS images (Def 6.2) | — |
| **Hasegawa 2000** (JFP preprint), **2002** (FLOPS) | — | — | STLC → linear λ (→, ⊸, !); computational λ → linear λ via linear CPS | — | — | Full completeness (2000 Thm 5.6; 2002 Thm 1). Ordinary CPS into STLC "not full" (2002 §1.3) | — |
| **Maraist–Odersky–Turner–Wadler** (MFPS'95) | — | — | Girard cbn / cbv into linear λ | Typing iff | — | cbn: complete for β-equality. cbv: **not complete**, counterexample (M N) vs ((λz.zN) M) (§8.3). Neither preserves η (§8.2) | — |
| **van Glabbeek–Hughes** (arXiv:1609.04693, Thm 1) | — | — | Cut-free MALL⁻ (no units) | — | — | Same proof net ⇔ related by rule commutations | — |
| **Heijltjes–Houston, LMCS 2016, Thm 9.1** | — | — | MLL with units | — | — | Proof equivalence (free ∗-autonomous word problem) is **PSPACE-complete**; canonical nets would require an intractable translation (§1) | — |

### 3.2 What the matrix establishes

Status: INFERENCE from the verified rows.

1. **"Fixed finite machine + environment + per-system adequacy" is the established paradigm.** It exists in four independent traditions: LF, Isabelle, rewriting logic and λΠ-modulo. A fifth, focused linear logic, has explicit adequacy levels. *Any* ProofBasis claim at R1–R2 is a claim inside this paradigm.
2. **The "environment" always holds the object system's inference rules.** The only exception is FPC, which is single-foundation and derivability-only. Correctness is an *external* adequacy or conservativity meta-theorem. Where it is missing, real libraries have been checked in environments of unestablished correctness (Felicissimo–Winterhalter, Table 1).
3. **Proof identity beyond syntactic equality is never part of a general framework theorem.** It is either:
   - a declared signature judgment (Pfenning §3.6);
   - a fixed framework congruence of a specific kind (CLF =c; rewriting-logic exchange); or
   - a per-encoding result for specific pairs of systems (Selinger, Hasegawa, Felicissimo Thm 46, van Glabbeek–Hughes).
4. **Strengthening the fixed machine breaks adequacy.** Induction over the representation type turns ∀I into an ω-rule (Pfenning p. 47). Case analysis creates exotic terms (Harper–Licata p. 24). A single constant of positive linear type is "catastrophic" (CLF p. 13). A universal fixed algebra must therefore stay weak, which conflicts with R3 (§6.3).

---

## 4. Work package 3: red team (F01–F10 register entries)

Each entry follows the template in `docs/FALSIFICATION.md`. Date 2026-10-08; claim version CV0 throughout.

| ID | Evidence (source, location) | Status of evidence | Result for CV0 | Follow-up |
|---|---|---|---|---|
| **F01** Already solved | R1: Clavel–Meseguer Thm 3.2; CMP Thms 1, 4, 5, 6; HST Defs 5.3 / 6.13. R2: HHP Thm 4.1; Pfenning Thm 3.2; Nigam–Miller Props; Miller–Pimentel Thm 6 + text. Many foundations: theory U; Cousineau–Dowek / Assaf. R3 for specific pairs: Selinger; Hasegawa; MOTW cbn; Felicissimo Thm 46; vGH Thm 1. R4: CLF Def 5 / Thm 6; rewriting-logic exchange law | VERIFIED_SOURCE (CLF Petri adequacy: claimed, proof not seen) | **Fatal for R0–R1. Requires scope change for R2** (only *uniformity over a class* is not a published theorem; HHP call it a thesis). **Partially fatal for R3/R4** (pairwise results exist) | §10 test |
| **F02** Trivial encoding | MDT Prop 2.25 / Cor 2.26; Clavel–Meseguer U; EF + Refl_S ≥p S (Krajíček 2019 Thm 8.4.3 per Arteche et al.; mechanism in Pudlák 2020 Cor 4.4 proof); constructions I-S and I-C in §6.1 | VERIFIED (MDT, CM). SECONDARY (EF+Refl location). INFERENCE (I-S, I-C) | **Fatal to CV0 without an anti-vacuity criterion.** MDT state the needed "structurality" notion is open | §6.2 proposal |
| **F03** Hidden inference rules | HHP p. 17; Paulson Def 1; Rabe §3.1; Miller–Pimentel Fig. 5 (Cut, Init, Pos/Neg in theory); Dedukti §3.1, Thm 8; Lambdapi manual; Blanqui 2020 §1; FW2024 Table 1; Berardi–Tatsuta Thm 8.4 (adding an inductive predicate is non-conservative) | VERIFIED | **Not fatal by itself, but the charter's framing is wrong** (see §9, CA1). The rules *must* live in the environment. The real question is the adequacy obligation, not "justification via common machinery" | Amendment A2 |
| **F04** Incompatible identities | GLT App. B p. 151 (Joyal); Došen 2003 Props 1–3; Selinger Cor 3.8, Rem 8.2; Straßburger RR-6013 §5 ("neither notion has a commonly agreed definition"; "Make a nice theory out of this mess"); Lamarche–Straßburger; Došen: normalization vs generality disagree for →∧; Gardner 5.2.x; MOTW §8.2–8.3; LLF p. 64 | VERIFIED (Lambek–Scott itself SECONDARY_ONLY) | **Fatal for a uniform R3** that is both CCC-with-initial-⊥ and a symmetric classical identity. **Not fatal for indexed R3**: faithful translations exist for chosen pairs (Selinger, Hasegawa). R3 must be per (S, ~_S, translation) | §7, §10 |
| **F05** False graph locality | Brotherston thesis Def 5.1.6 + text before Prop 5.1.10 ("a global condition … only by examining the entire pre-proof"); Das 2020 §3.2 (PSPACE upper bound, no lower bound for CA); NST 2019 (PSPACE-complete, µMALL; ABSTRACT_ONLY); Cohen et al. 2024 (PSPACE-complete abstract Infinite Descent, citing); BDKS Cor 6.6 (Σ⁰₁-complete); NST 2018 (local criterion only for a fragment "too constrained"); Girard 1987 Rem 2.6 ("the soundness condition is not feasible … an abstract notion"). Note: MLL⁻ correctness is linear time (Guerrini, SECONDARY_ONLY), so global ≠ infeasible | Mixed (see cells) | **Fatal for "finitely many local operators decide validity"** on full CLKIDω-style cyclic proofs, unless the global check is a primitive of A or trusted in E. Requires scope change | §7.4 |
| **F06** False order invariance | GLT App. B (Lafont's weakening/weakening example: LK cut elimination not Church–Rosser); CLF labelled-token requirement (footnote 2); Meseguer 2012 survey (CCS causal model and parallel λ are quotients of the rewriting-logic model) | VERIFIED | **Not fatal, but R4 is encoding-relative**: independence must be defined against a fixed encoding | Amendment A4 |
| **F07** Infinite / effective boundary | Brotherston thesis Ch. 5 intro (LKIDω proofs not semi-decidable); Frittaion Thm 2.3 (ω-proof codes Π¹₁-complete; Shoenfield completeness SECONDARY); Väänänen SEP §5.1 (SOL "not completely axiomatizable by effective means") | VERIFIED (secondary references) | **Confirmed boundary.** The charter already restricts to finite effective systems. Record "across foundational traditions" as excluding ω-logic and standard-semantics SOL | — |
| **F08** Minimality ambiguity | Cook–Reckhow Thm 2.3, Cor 2.4, Cor 3.4, Thm 4.5 / Cor 4.7; Reckhow 1976 (SECONDARY); Miller–Pimentel Ex 7–8 and Nigam–Miller p. 2 (adequacy level depends on clause shape and polarity); Avron–Honsell–Mason 1987 (surjection vs bijection by encoding choice); CMP §7 (two encodings of U "computational" vs "logical"); Akbar Tabatabai–Jalali (arXiv:1808.06258v2, Thm 4.3, Cor 4.5: K4 and S4 lack a terminating semi-analytic calculus; their earlier work, cited there: most superintuitionistic logics lack semi-analytic calculi) | VERIFIED (Akbar Tabatabai–Jalali Cor 4.5 read by me; the "except at most seven" claim is as stated in their text about [2], i.e. SECONDARY for [2]) | **Fatal for "minimal/fundamental basis" without a fixed translation notion and cost measure.** Within Frege, basis choice is irrelevant up to p-simulation (established). Across shape disciplines it is not (F09). Defining "meaningful operations" by rule *shape* excludes many logics | Amendment A5 |
| **F09** Efficiency | Buss 2012 Thm 2 (cut-free height ≥ tower of height ℓ); Statman / Orevkov (SECONDARY); BIW 2004 tree vs DAG exp(Ω(n/log n)) vs O(n) (ABSTRACT_ONLY); Das Thm 6.10 (CA → PA exponential); Bruscoli–Guglielmi 2009 (analytic deep inference, exponential speed-up); Felicissimo §10 (16× slowdown); Wehr 2023 via Cohen et al. (reset proofs poly-checkable, exponential conversion; SECONDARY) | Mixed | **Confirmed.** Derivability-equivalent bases are not cost-equivalent. Any basis claim must state the size measure | — |
| **F10** Weak quantifier | §2.2 | INFERENCE (elementary) | **Fatal to CV0 as written.** Fix by A1 | A1 |

---

## 5. Concrete counterexample dossier

Each item is a mathematical statement that defeats a specific reading of CV0.

| # | Defeats | Statement | Source and status |
|---|---|---|---|
| **CX1** | R1 as evidence of anything | PHCL with three rules conservatively represents every compact countable entailment relation, via an environment Δ containing the entailment relation itself | MDT Prop 2.25. VERIFIED |
| **CX2** | Finite environment + finite machine + R1 | One finitely presentable rewrite theory U, with T ⊢ t→t′ ⇔ U ⊢ rep(T ⊢ t→t′), for all unconditional unsorted finitely presentable T (var(t′) ⊆ var(t)) | Clavel–Meseguer Thm 3.2. VERIFIED. Extensions: CMP Thms 1, 4, 5, 6 |
| **CX3** | Size-respecting universality | EF + Refl_S p-simulates every Cook–Reckhow system S | Krajíček 2019 Thm 8.4.3 per Arteche et al. SECONDARY_ONLY. Mechanism: VERIFIED in Pudlák 2020 |
| **CX4** | Uniform R3 over classical + intuitionistic | A CCC with initial ⊥ and a *natural* ζ_A : ¬¬A → A is a preorder (Došen Prop 2). Likewise a bicartesian closed category with dinatural ⊤ → A + ¬A (Prop 3). Original (Joyal): GLT App. B p. 151, citing Lambek–Scott p. 67 | VERIFIED (Došen, GLT). Lambek–Scott SECONDARY_ONLY |
| **CX5** | Polynomial canonical identity for linear logic | MLL proof equivalence (with units) is PSPACE-complete | Heijltjes–Houston Thm 9.1. VERIFIED (journal version) |
| **CX6** | Standard cross-foundation translation reflects identity | The Girard cbv translation identifies λ_val-distinct terms (M N) and ((λz.zN) M). Neither Girard translation preserves η | MOTW §8.2–8.3. VERIFIED (MFPS version) |
| **CX7** | R1 ⇒ R3 in a fixed framework | Hilbert-style S4 is adequately but not naturally representable in ELF+ (Thm 5.2.11). So is Hilbert PL via the ND signature (Thm 5.2.13). Prawitz ND-S4 has no natural representation (Ex 5.2.6) | Gardner thesis. VERIFIED (OCR) |
| **CX8** | Fixed intuitionistic-context framework covers resource logics | "There are no adequate representations of linear and relevant logics in ELF+" | Gardner Cor 5.1.8. VERIFIED (OCR). Relative to her direct definition: indirect encodings are excluded, not refuted |
| **CX9** | Cyclic ≡ inductive (same theorems) | 2-Hydra H: provable in CLKIDω(Σ_N, Φ_N), not in LKID(Σ_N, Φ_N) + (0,s)-axioms | Berardi–Tatsuta LMCS 2019 Thm 8.3. VERIFIED |
| **CX10** | Decidable validity of finite proof graphs | Circular pre-proof validity for µMLLω under bouncing threads is Σ⁰₁-complete | Baelde–Doumane–Kuperberg–Saurin Cor 6.6 (arXiv v1). VERIFIED |
| **CX11** | Normalization-based identity for cyclic proofs | Cut is not eliminable in CLKIDω, even with unary predicates | Oda–Kimura Cor 31 (arXiv). VERIFIED. Masuoka–Tatsuta original SECONDARY |
| **CX12** | Finite generation under resource discipline | Permutation (reversible) Boolean circuits S[2] are not finitely generated in Lafont's setting (Lemma 14, parity) | Lafont 2003 preprint. VERIFIED |
| **CX13** | Single environment for many foundations is conservative | Theory U explicitly does not give provability conservativity over its sub-theories | Blanqui et al. 2021 §4. VERIFIED |
| **CX14** | Adding environment content is inert | Some LKID(Σ₂, Φ₂) extends LKID(Σ₁, Φ₁) non-conservatively | Berardi–Tatsuta Thm 8.4. VERIFIED |

---

## 6. Work package 4: non-triviality benchmark

### 6.1 Explicit universal-interpreter constructions

Three are published; two are mine. Each satisfies more of CV0's stated constraints than the last.

**I-H (published, MDT Prop 2.25): Horn flattening.**
- A = PHCL.
- E_S = Δ_S, all Horn clauses α(φ₁)∧…∧α(φₙ) → α(φ) with {φᵢ} ⊢_S φ.
- Conservative.
- Excluded by: requiring E_S finite, or at least that it contain no member of S's consequence relation that is not one of S's rules.

**I-U (published, Clavel–Meseguer): data-level universal theory.**
- A = U, finite.
- E_S = the finite data term T̄.
- Preserves and reflects derivability.
- Excluded by: rule locality (one S-step needs unboundedly many U-steps), or by bijectivity on derivations (CMP Lemma 1: many U-derivations per object derivation).

**I-R (published; theorem location SECONDARY): reflection axiom.**
- A = EF.
- E_S = Refl_S, a polynomial-size scheme encoding S's checker.
- p-simulates S.
- Excluded by: forbidding axiom schemes that mention S's proof predicate.

**I-S (mine; INFERENCE): step-checker framework.** This is constructed to survive finiteness, data-only environments, rule locality and bijectivity.
- A = LF plus a fixed finite signature for a universal machine:
  - trace constants for each transition of a fixed universal TM;
  - a type family `Rule : Code → type`;
  - one generic constant
    `step : Πr:Code. Πψ̄. Πφ. Rule r → Prf ψ̄ → Trace(run r ⟨ψ̄,φ⟩ = 1) → Prf φ`.
- For a Hilbert-style S (no hypotheses, no binders) with rule schemas r₁…r_k: E_S = {ruleᵢ : Rule ⌜cᵢ⌝}, where cᵢ decides whether ⟨ψ̄, φ⟩ is an instance of rᵢ.
- Because traces of a deterministic machine are unique, canonical A-terms of type Prf ⌜φ⌝ over E_S are in bijection with S-derivations of φ.
- F_S(rᵢ(d̄)) = step ⌜cᵢ⌝ … ruleᵢ F_S(d̄) trace, a fixed context per rule apart from the trace, whose size depends only on the formulas.
- So I-S passes:
  - finite A;
  - finite, declaration-only E_S;
  - rule locality (modulo trace size);
  - bijection on derivations;
  - preservation and reflection of derivability.

**I-C (mine; INFERENCE): conversion interpreter in λΠ-modulo.**
- E_S declares `valid : Cert → Form → Bool`, with rewrite rules computing S's (poly-time) checker by structural recursion.
- It also declares `acc : Πc φ. IsTrue (valid c φ) → Prf φ`, with `IsTrue true ↪ Unit`.
- A total poly-time checker can be written as a terminating, confluent, type-preserving rule set. Hence I-C passes the properties Dedukti/Lambdapi check or assume (Dedukti §2.3, Thm 8; Lambdapi manual).

### 6.2 A checkable restriction that excludes I-H, I-U, I-R, I-S and I-C

Status: PROPOSAL / CONJECTURE about its adequacy.

**NCE-H** ("no computation in the environment + homomorphic adequacy"). A representation (A, E_S, F_S) qualifies iff:

- **H1, fixed conversion.** ≡_A is fixed once for A. E_S consists only of constant declarations c : T, with no rewrite rules, equations, definitional axioms, or axiom schemes indexed by codes.
- **H2, rules as types.** There is a bijection r ↦ c_r between S's rule schemas and constants of E_S. The S-instances of r are *exactly* the instances of type(c_r) under A-substitution of adequately encoded parameters. There are no side premises discharged by computation.
- **H3, compositional (quotient) adequacy.** F_S is a bijection between S-derivations (modulo α and the declared ~_S, see §6.3) and canonical A-terms (modulo ≡_A) of the encoded judgment. It commutes with substitution of terms *and* of derivations for hypotheses. S's hypotheses and bound variables are realised by A's own variables and abstraction.
- **H4, rule locality.** F_S(r(d₁…dₙ)) = c_r t̄ (λ-abstracted F_S(dᵢ)).

**Exclusions** (INFERENCE):

| Construction | Fails |
|---|---|
| I-H | H2 (Δ contains non-rules) |
| I-U | H2, H4 |
| I-R | H1 (axiom scheme over codes), H2 |
| I-S | H2 (the instances of `step` with ruleᵢ are determined by running cᵢ, not by instantiating a type). For systems with hypotheses or binders it also fails H3 |
| I-C | H1 |

**Inclusions** (non-exclusion by fiat):

| Framework | Verdict |
|---|---|
| LF encodings of FOL/HOL | Satisfy H1–H4 (HHP Thm 4.1; Pfenning Thm 3.2) |
| Focused-LL encodings at "full completeness of derivations" (Nigam–Miller) | Satisfy H2–H4, with Cut, Init and structural clauses counted as rule declarations. Whether the bijection-with-focused-proofs matches H3's substitution clause is **UNKNOWN** |
| Isabelle/Pure | Satisfies H1 only if object definitions (≡-axioms) are excluded from E. H3 is not established, since Paulson proves only sound and complete entailment |
| Dedukti encodings using environment rewrite rules (Cousineau–Dowek, Felicissimo, theory U) | **Fail H1** |
| Variant H1′ | Admits them if A is redefined to include a *fixed* finite rule set (e.g. λΠ + U's 28 rules) rather than per-S rules |

**Known costs and open objections to NCE-H:**
1. H2 forbids proof by computational reflection. A conversion-based certificate must be expanded into explicit conversion derivations, which can be exponentially or worse larger (INFERENCE; ties to F09).
2. H1 excludes Felicissimo's encoding, the only verified result where object *reduction* is reflected (Thm 46). This is not an accident; see §6.3.
3. H2 is checkable for a given encoding (compare instance sets syntactically). H3 is a meta-theorem per encoding, exactly as in LF practice. "Checkable" here means "has a precise proof obligation", not "decidable by a tool".
4. MDT state that a general structurality notion, especially with binders, is open. NCE-H is one candidate. It has not been compared with the notions MDT cite ([48, 9] in their paper; not accessed).

### 6.3 The vacuity–identity dilemma

Status: INFERENCE from verified sources, plus an elementary lemma.

**Lemma (informal, elementary).** Suppose:
- F_S is injective on S-derivations (as in LF adequacy, H3 without a quotient), and
- ≡_A restricted to the image of F_S is syntactic identity (as for LF and LLF canonical forms, and CLF outside the monad).

Then F_S reflects ~_S only if ~_S is syntactic identity.

*Argument:* F(d) ≡_A F(d′) ⇔ F(d) = F(d′) ⇔ d = d′.

Consequently, a non-trivial R3 requires one of:
- **(i)** a *quotient* adequacy notion: a bijection between S-derivations/~_S and A-terms/≡_A. CLF's Petri-net statement has exactly this form.
- **(ii)** E_S may extend ≡_A, through declared equations or rewrite rules. This is Dedukti-style; Felicissimo Thm 46 reflects reduction this way. But then R3 holds by declaration (put ~_S's generators in E_S) and I-C enters: **vacuity**.
- **(iii)** ≡_A natively contains the identity-carrying structure of S. Example: NJ(→) encoded *shallowly*, with object → as A's own →. Canonical forms are then βη-classes, by Curry–Howard.

Under NCE-H, (ii) is excluded, so R3 needs (iii). For a class C spanning several foundations, A must then natively contain each foundation's identity-bearing structure: → with βη; ⊸/⊗ with permutation equivalence; continuations; and so on. These must coexist without collapse (CX4). The framework then is *the union of the foundations' structures*, not a small universal basis. That is the opposite of the charter's motivating picture.

Counter-consideration: CPS and linear translations reduce several structures to fewer. Classical cbn λμ → →-structure via CPS is faithful on equality (Selinger Def 6.2 / Prop 6.5 / Thm 6.12); STLC → linear λ is fully complete (Hasegawa). So the union may be *small* for well-chosen benchmark sets. Whether it is small for a meaningful set is the residual question, C\* in §10.

---

## 7. Work package 5: cross-foundation stress tests

Which preservation goals survive, given current evidence.

### 7.1 Classical vs constructive

| Level | Evidence |
|---|---|
| R1 | Survives, and is *known*. Kolmogorov translation is a conservative entailment-relation morphism CPL → IPL (MDT Ex 2.4, VERIFIED). LF encodes classical ND by adding a constant `raa` (HHP p. 19) |
| R2 | Survives (LF; Nigam–Miller LK/LJ encodings) |
| R3 | **Survives only indexed by choice.** Faithful for cbn λμ ↔ CPS/→ (Selinger) and cbn ↔ cbv duality (Prop 8.1, up to type isomorphism, needs ∧ and ∨). **Fails uniformly** for any identity with CCC + initial ⊥ + natural ¬¬-elimination (CX4). The symmetric classical identities (Lamarche–Straßburger B-nets; Došen–Petrić; Führmann–Pym, last two not accessed) are a different, incompatible choice (Straßburger §5). cbn and cbv λμ have different theories (Selinger Rem. 8.2) |
| R4 | No evidence found |

### 7.2 Linear / resource-sensitive

| Level | Evidence |
|---|---|
| R1 | Survives via indirect encodings (Cervesato–Pfenning p. 53: possible in LF, with "complex proofs"). Fails for direct context-as-hypotheses encodings in an intuitionistic framework (Gardner Cor 5.1.8) |
| R2 | Survives only by **changing the machine** (LF → LLF → CLF) or by **declaring structure in the environment** (Miller–Pimentel Pos/Neg clauses; subexponential signatures, SECONDARY). Evidence of "framework creep", not of one fixed basis |
| R3 | Unit-free MALL: canonical (vGH Thm 1). With units: PSPACE-complete (CX5). Intuitionistic → linear: cbn β-complete, cbv not (CX6). Hasegawa: full completeness for DILL. **Unresolved tension:** MOTW say no Girard translation preserves η, while Hasegawa (with η in DILL) says Girard translation soundness/conservativity "at the proofs level" is "widely known". Probably different target calculi (λlin without η vs DILL with η). Not checked |
| R4 | CLF =c gives a fixed independence congruence. Requires labelled tokens; indistinguishable resources open (CLF footnote 2) |

### 7.3 Dependent types and binding

| Level | Evidence |
|---|---|
| R1–R2 | Survive. HOAS adequacy for FOL/HOL (HHP Thms 3.1–4.2). PTS: Cousineau–Dowek (no bijection; conservativity conditional on termination) and Assaf Thm 5.24 (unconditional, inhabitation level) |
| R3 | Object *reduction* is preserved and reflected only in Felicissimo Thm 46 (functional EPTS), via environment rewrite rules (fails H1; vacuity horn of §6.3) and at a ≈16× cost. For cumulative CoC, no encoding had a full conservativity proof as of FW2024 |
| Single environment | Theory U is not provability-conservative (CX13) |

### 7.4 Cyclic proofs and global validity

| Level | Evidence |
|---|---|
| R0 | Representation of finite pre-proof graphs by local operators: survives |
| R1 | Validity is a global ω-regular condition (Brotherston Prop 5.1.10; decidable, PSPACE upper bound). Lower bounds: PSPACE-hard for µMALL threads (NST 2019, ABSTRACT_ONLY) and abstract infinite descent (Cohen et al., citing Lee et al. 2001). Status for CLKIDω specifically: UNKNOWN (Das 2020: no lower bound known). With cuts and bouncing threads: undecidable (CX10). A finite *local* algebra must take the global condition as a primitive, trust it in the environment (F03), or restrict to locally certifiable fragments (NST 2018 labellings, "too constrained"; reset proofs, exponential conversion, SECONDARY) |
| Translation to inductive systems | Not derivability-preserving in general (CX9). Equivalent under arithmetic (SECONDARY for LICS 2017 / Simpson 2017; VERIFIED intuitionistic Thm 6.14). CA → PA exponential (Das Thm 6.10) |
| R3 | Normalization-based identity unavailable (CX11). Uniform translation to System T with contraction is open (Kuperberg–Pinault–Pous) |

### 7.5 Infinitary boundary

ω-logic and standard-semantics second-order consequence lie outside any finite effective certificate system (F07). They should be declared out of scope explicitly rather than silently, since the charter's "across foundational traditions" would otherwise include them.

### 7.6 Summary of surviving goals

| | R0 | R1 | R2 | R3 (uniform) | R3 (indexed) | R4 |
|---|---|---|---|---|---|---|
| Status | Known / vacuous | Known / vacuous without anti-vacuity | Known per encoding; uniform version a "thesis" | **Obstructed** (CX4, CX5, CX6, CX7; §6.3) | Partially known; residue open (C\*) | Prior art; encoding-relative |

---

## 8. Unresolved objections

These are recorded for reviewers; none is resolved here.

| # | Objection |
|---|---|
| U1 | **Is NCE-H the right anti-vacuity notion?** It excludes Dedukti-style computation, which practitioners regard as legitimate. An alternative is to allow a *fixed* rewrite set inside A (H1′). The comparison with the structurality notions MDT cite is not done |
| U2 | **The vacuity–identity dilemma is an informal argument.** Option (i), quotient adequacy, may allow A to be smaller than "the union of all structures" if quotients are taken on the S side. That is a matter of how H3's quotient is formulated. Not settled |
| U3 | **Uniform adequacy theorems.** HHP p. 22 call a general adequacy theorem for extensions of FOL "interesting". Gardner Ch. 6 (indexed isomorphisms) was **not read in detail** and may already contain a uniform derivation-level theorem. Must be checked before any V1 novelty claim |
| U4 | **MOTW vs Hasegawa on η** (§7.2). The apparent conflict needs resolution from the TCS 1999 journal version and Hasegawa's cited sources (not accessed) |
| U5 | **Dedukti manuscript Lemma 32** ("|M| ≡βηΣ M′") appears stronger than Assaf Thm 5.24 as read. The dk agent flagged a possible overstatement; unresolved |
| U6 | **CLF Petri-net adequacy "modulo ="** is claimed in prose; the proof was not seen (companion TR II not accessed) |
| U7 | **Possibly decisive leads not verified** (UNVERIFIED-MEMORY of the author): <br>• Chaudhuri, Miller, Saurin, "Canonical sequent proofs via multi-focusing" (2008): maximal multi-focusing as canonical representatives for unit-free MALL; would bear on R3 in focused frameworks;<br>• Hasegawa, "Classical linear logic of implications" (CSL 2002 / MSCS 2005): a possibly full and faithful embedding of classical MLL-type structure into intuitionistic linear structure via linear CPS;<br>• Statman (TCS 1979): βη-equality of simply typed terms is not elementary recursive. If confirmed, deciding an LF-style ≡_A is already non-elementary, which weakens the complexity reading of CX5. CX5 rules out *polynomial canonical forms*, not decidable ≡_A |
| U8 | **"Except at most seven" superintuitionistic logics** lacking semi-analytic calculi: read only as Akbar Tabatabai–Jalali's summary of their own earlier paper. SECONDARY |

---

## 9. Contradictions with charter assumptions

Recorded explicitly, as AGENTS.md rule 8 requires.

| # | Charter assumption | What the evidence shows |
|---|---|---|
| **CA1** | Trust boundary (RESEARCH_CHARTER, "Critical distinctions"): "An imported rule must either be justified via the common machinery, be explicitly marked as an additional trusted primitive, or be recognized as an unproved extension." | In every multi-foundation framework examined (LF, Isabelle/Pure, rewriting logic, MMT, Dedukti, focused LL), a foundation's *primitive* rules are environment declarations. Their correctness is certified only by an external adequacy or conservativity meta-theorem. They cannot be "justified via the common machinery": they are what defines the foundation. The only design where client content is untrusted (FPC) is single-foundation and derivability-only. **The first branch of the trichotomy is empty for primitive rules.** The useful notion is an adequacy *obligation* (H3), not justification |
| **CA2** | Machine/environment as an informative split (README, charter) | Where the split is drawn changes what is "fixed": LF→LLF→CLF moved structure into the machine; Miller–Pimentel moved structural rules and cut into the environment. Nigam–Miller show the same theory yields different object systems under different polarity assignments (an extra out-of-theory parameter). The split is a design choice, not an invariant |
| **CA3** | R0–R4 as nested targets to pursue (DEFINITIONS) | R1–R2 are known. R3 conflicts with anti-vacuity (§6.3). The levels are not a ladder to climb; R3 forces a different design |
| **CA4** | Initial scope "finite, effectively described formal proof systems" (charter) | Cyclic proofs are finite objects whose validity is global and, with cuts and bouncing threads, undecidable (CX10). "Effectively described" must specify *decidable validity of finite certificates* |
| **CA5** | "Proof equivalence ~_S: an explicitly declared equivalence" (DEFINITIONS) | The same S has multiple incompatible standard identities (T6). R3 must be stated per (S, ~_S, translation) |
| **CA6** | README's "mathematically meaningful operations" | No formal content; the related literature notion is stated as open (MDT) |

---

## 10. Decision memo

### 10.1 Recommendation

**Do not advance. Stop the program as chartered.**

The universal finite basis with R0–R4 fidelity across foundations is either:
- already established (R0–R2 within the LF / rewriting / λΠ-modulo / focused-LL paradigm);
- vacuous (R0–R1 without an anti-vacuity condition; R3 if the environment may extend equality); or
- obstructed (uniform R3: CX4–CX7; local R4/R5 for cyclic proofs: F05).

**Optionally, narrow to one bounded literature gate (Gate 0.5 below), with stop as the default outcome.** Approve it only if the owners value a small, specific question in categorical proof theory and logical frameworks, which is much narrower than the charter's ambition.

### 10.2 Strongest remaining conjecture

Status: CONJECTURE. Novelty: UNKNOWN; it may be a corollary of existing results.

**C\* (quotient adequacy for a fixed benchmark).** Let

> B = { NJ(→,∧) with βη ; call-by-name λμ (Selinger's Table 6 theory, restricted to the connectives of the chosen fragment) ; cut-free MLL⁻ (unit-free) with rule-commutation equivalence }.

There exists an existing, fixed framework A satisfying NCE-H (H1–H4, with H3 in quotient form), and encodings F_S for each S ∈ B, such that for all derivations d, d′ of the same judgment:

> d ~_S d′ ⇔ F_S(d) ≡_A F_S(d′),

where ≡_A is A's fixed definitional equality.

**Boundary conditions:**
- Adding MLL *with units* forces ≡_A to decide a PSPACE-complete problem (CX5).
- Adding a symmetric classical identity alongside NJ's CCC identity, with ¬¬-elimination encoded as a natural family, forces collapse (CX4).
- Adding cbv λμ alongside cbn with shared encodings of connectives is not covered: the theories differ (Selinger Rem. 8.2).
- Cyclic systems are excluded (CX10, CX11).

**Why this is the strongest survivor.** It is the smallest statement that:
- is not vacuous under §6;
- is not refuted by §5;
- spans three foundations (intuitionistic, classical, linear); and
- tests R3 rather than R1.

**Strongest counter-argument.** C\* may follow directly by composing published theorems:
- shallow NJ in a CLF-like framework (canonical forms = βη-classes);
- Selinger Def 6.2 / Prop 6.5 / Thm 6.12 for cbn λμ via CPS;
- vGH Thm 1 plus a linear-CPS embedding of MLL⁻ (Hasegawa 2005 lead, U7) for MLL⁻.

If so, it is not novel, and the project should stop.

### 10.3 The single discriminating next test (Gate 0.5)

Literature and pen-and-paper. No implementation.

**Question.** Is C\* already a consequence of published theorems, with A = CLF (or LLF)?

**Procedure** (bounded; each step has a yes/no outcome):

1. Retrieve and verify:
   - Hasegawa, "Classical linear logic of implications";
   - Chaudhuri–Miller–Saurin, "Canonical sequent proofs via multi-focusing";
   - the CLF companion report (CMU-CS-02-102);
   - Hofmann–Streicher 2002;
   - the MOTW TCS 1999 version (resolves U4).
2. For each S ∈ B, state the candidate translation into CLF and check H1–H4 on paper.
3. Determine whether each faithfulness theorem lands in CLF's *fixed* =c (α plus monadic let-permutation), or needs equations CLF lacks. Example: whether MLL⁻ rule commutations become CLF let-permutations or require ⅋-specific equations.

**Decision rule.**

| Outcome | Decision |
|---|---|
| (a) All three faithfulness results exist and land in =c | C\* is known (F01) → **stop**. Optionally publish this report as a survey or position note |
| (b) A specific step provably fails (e.g. MLL⁻ commutations not expressible in =c without new framework equations) | Record a precise obstruction. **Stop**, or narrow once more to an obstruction theorem |
| (c) A specific lemma is genuinely open after the checks | Write it as a formal Stage-1 conjecture. Only then consider a small mechanised experiment with an *existing* tool (e.g. Celf for CLF), justified per AGENTS.md (it would test a specific open lemma that the literature does not settle) |

**Why this test is discriminating.** It separates "known" from "obstructed" from "open" for the only surviving version, using existing results and existing frameworks. No implementation is needed unless outcome (c) occurs.

---

## 11. Proposed minimal amendments to definitions

These are *proposals*. They are **not applied** to `docs/`, and the mission is not changed.

| ID | Amendment | Reason | Test |
|---|---|---|---|
| A1 | Fix C before A: replace "∃ a nontrivial class C" by a named benchmark list or formally defined class, quantified universally | F10 / §2.2: CV0 is trivially true | Does any single-system C satisfy the amended statement? It must not |
| A2 | Make an explicit anti-vacuity condition part of "representation". Candidate: NCE-H (H1–H4), with H1′ as a declared variant | F02 / F03; CX1–CX3; I-S; I-C | I-H, I-U, I-R, I-S and I-C must all fail it, while the HHP FOL encoding passes (§6.2) |
| A3 | Index R3 by (S, ~_S, translation) and require quotient adequacy (§6.3). State whether ~ is realised by ≡_A or by declared judgments | T6; CA5; §6.3 lemma | — |
| A4 | Define "effective" as decidable validity of finite certificates. Define R4 independence relative to a fixed encoding | CA4; F06 | — |
| A5 | Any "basis" or "minimality" claim must name the translation notion and the cost measure (p-simulation, linear rule-locality, etc.) | F08 / F09; Cook–Reckhow; Buss; BIW | — |

---

## 12. Bibliography (as consulted)

The version read is given; page and theorem numbers refer to it. DOIs are listed **only** where printed on the retrieved document. Others are marked "(from search listing)" or omitted. Full URLs are in the source notes.

### Logical frameworks

| Source | Version read | Status |
|---|---|---|
| R. Harper, F. Honsell, G. Plotkin, "A Framework for Defining Logics", JACM 40(1), 1993 (journal data UNVERIFIED-MEMORY) | Author typescript, homepages.inf.ed.ac.uk/gdp | VERIFIED_SOURCE |
| R. Harper, D. R. Licata, "Mechanizing metatheory in a logical framework", JFP 17, 2007 (volume data UNVERIFIED-MEMORY) | Preprint | VERIFIED_SOURCE |
| F. Pfenning, "Logical Frameworks", Handbook of Automated Reasoning, Elsevier, 2001 | Author preprint, cs.cmu.edu/~fp | VERIFIED_SOURCE |
| I. Cervesato, F. Pfenning, "A Linear Logical Framework", Inf. & Comput. 179, 2002 (UNVERIFIED-MEMORY) | Author manuscript | VERIFIED_SOURCE |
| K. Watkins, I. Cervesato, F. Pfenning, D. Walker, "A concurrent logical framework I", CMU-CS-02-101, 2002, rev. 2003 | Tech report | VERIFIED_SOURCE |
| L. C. Paulson, "The Foundation of a Generic Theorem Prover", JAR 5, 1989 | UCAM-CL-TR-130 / arXiv cs/9301105 | VERIFIED_SOURCE |
| Z. Chihani, D. Miller, F. Renaud, "A Semantic Framework for Proof Evidence", JAR 59(3), 2017, DOI 10.1007/s10817-016-9380-6 (printed) | HAL manuscript | VERIFIED_SOURCE |
| A. Avron, F. Honsell, I. Mason, ECS-LFCS-87-31, 1987 | OCR | VERIFIED_SOURCE. JAR 1992 version with Pollack: NOT_ACCESSED |
| P. Gardner, "Representing Logics in Type Theory", PhD thesis, Edinburgh, 1992 (ECS-LFCS-92-227) | OCR | VERIFIED_SOURCE (Ch. 6 not read in detail) |
| R. Harper, D. Sannella, A. Tarlecki, "Structured theory presentations and logic representations", APAL 67, 1994 | Draft of 10 Dec 1992 | VERIFIED_SOURCE |
| V. Nigam, D. Miller, "A framework for proof systems", JAR 45(2), 2010 | Author preprint | VERIFIED_SOURCE |
| D. Miller, E. Pimentel, "A formal framework for specifying sequent calculus proof systems", TCS 474, 2013 (volume from search listing) | Author preprint | VERIFIED_SOURCE |

### Rewriting logic and general logics

| Source | Version read | Status |
|---|---|---|
| M. Clavel, J. Meseguer, "Reflection and Strategies in Rewriting Logic", ENTCS 4, 1996 | Author PostScript | VERIFIED_SOURCE |
| M. Clavel, J. Meseguer, M. Palomino, "Reflection in membership equational logic, many-sorted equational logic, Horn logic with equality, and rewriting logic" | Extended preprint, Palomino's site. TCS 2007 venue SECONDARY. Also ENTCS 71 (WRLA'02) | VERIFIED_SOURCE |
| M. Clavel, J. Meseguer, "Reflection in conditional rewriting logic", TCS 285(2), 2002 | — | NOT_ACCESSED |
| N. Martí-Oliet, J. Meseguer, "Rewriting logic as a logical and semantic framework" | ENTCS 4 (1996) and SRI TR (1993). Handbook 2002 version: NOT_ACCESSED | VERIFIED_SOURCE |
| J. Meseguer, "General Logics", Logic Colloquium '87, North-Holland, 1989 | Course-hosted copy; provenance unconfirmed | VERIFIED_SOURCE |
| J. Meseguer, "Twenty years of rewriting logic", JLAP 81, 2012 | — | VERIFIED_SOURCE |
| T. Mossakowski, R. Diaconescu, A. Tarlecki, "What is a logic translation?", Logica Universalis 3, 2009 | DFKI preprint | VERIFIED_SOURCE |
| F. Rabe, "How to identify, translate and combine logics?", JLC 27(6), 2017 | Author preprint | VERIFIED_SOURCE |
| J. Goguen, R. Burstall, "Institutions", JACM 39(1), 1992 | Scan | VERIFIED_SOURCE (definition only) |

### λΠ-modulo / Dedukti

| Source | Version read | Status |
|---|---|---|
| D. Cousineau, G. Dowek, "Embedding pure type systems in the lambda-Pi-calculus modulo", TLCA 2007 | arXiv:2310.12540 posting | VERIFIED_SOURCE |
| A. Assaf, "Conservativity of embeddings in the λΠ calculus modulo rewriting" (long version) | arXiv:1504.05038 | VERIFIED_SOURCE |
| A. Assaf et al., "Dedukti: a logical framework based on the λΠ-calculus modulo theory" | arXiv:2311.07185 | VERIFIED_SOURCE |
| F. Blanqui, G. Dowek, É. Grienenberger, G. Hondet, F. Thiré, "Some axioms for mathematics", FSCD 2021, LIPIcs 195, art. 20, DOI 10.4230/LIPIcs.FSCD.2021.20 (printed) | Publisher version | VERIFIED_SOURCE |
| T. Felicissimo, "Adequate and computational encodings in the logical framework Dedukti", FSCD 2022, LIPIcs 228, art. 25, DOI 10.4230/LIPIcs.FSCD.2022.25 (printed) | Publisher version + arXiv:2205.02883 | VERIFIED_SOURCE |
| T. Felicissimo, T. Winterhalter, FSCD 2024, LIPIcs 299, art. 21, DOI 10.4230/LIPIcs.FSCD.2024.21 (printed) | Publisher version | VERIFIED_SOURCE |
| F. Blanqui, G. Genestier, O. Hermant, FSCD 2019 | — | VERIFIED_SOURCE |
| F. Blanqui, FSCD 2020, DOI 10.4230/LIPIcs.FSCD.2020.13 (printed) | — | VERIFIED_SOURCE |
| Lambdapi manual, "Commands" | Retrieved 2026-10-08 | VERIFIED_SOURCE |
| G. Dowek | arXiv:1501.06522 | VERIFIED_SOURCE |

### Proof identity

| Source | Version read | Status |
|---|---|---|
| J.-Y. Girard, Y. Lafont, P. Taylor, *Proofs and Types*, CUP 1989 | Web reprint 2003, App. B p. 151 | VERIFIED_SOURCE |
| J. Lambek, P. Scott, *Introduction to Higher Order Categorical Logic*, CUP 1986 | — | NOT_ACCESSED (p. 67 via three secondary sources) |
| K. Došen, "Identity of proofs based on normalization and generality", BSL 9(4), 2003 | arXiv math/0208094v12 | VERIFIED_SOURCE |
| W. Heijltjes, R. Houston, "Proof equivalence in MLL is PSPACE-complete", LMCS 12(1:2), 2016 | — | VERIFIED_SOURCE |
| D. Hughes, R. van Glabbeek, TOCL 6(4), 2005 | Author version | VERIFIED_SOURCE |
| R. van Glabbeek, D. Hughes | arXiv:1609.04693 | VERIFIED_SOURCE |
| J.-Y. Girard, "Linear logic", TCS 50, 1987 | Scan | VERIFIED_SOURCE |
| V. Danos, L. Regnier, 1989 | — | NOT_ACCESSED |
| L. Straßburger, "Proof nets and the identity of proofs", INRIA RR-6013, 2006 | arXiv cs/0610123 | VERIFIED_SOURCE |
| F. Lamarche, L. Straßburger, TLCA 2005 | — | VERIFIED_SOURCE |
| D. Hughes, "Proofs without syntax", Annals of Math. 164, 2006 | arXiv | VERIFIED_SOURCE |
| A. Guglielmi, TOCL 8, 2007 | — | VERIFIED_SOURCE |
| P. Bruscoli, A. Guglielmi, TOCL 10, 2009 | — | VERIFIED_SOURCE |
| P. Selinger, "Control categories and duality", MSCS 11, 2001 | — | VERIFIED_SOURCE |
| M. Hasegawa, JFP 2000 | Preprint | VERIFIED_SOURCE |
| M. Hasegawa, FLOPS 2002 | — | VERIFIED_SOURCE |
| J. Maraist, M. Odersky, D. Turner, P. Wadler | MFPS'95 / ENTCS 1 | VERIFIED_SOURCE |
| N. Benton, P. Wadler, LICS 1996 | — | VERIFIED_SOURCE |
| N. Benton, UCAM-CL-TR-352, 1994 | — | VERIFIED_SOURCE |
| M. Hofmann, T. Streicher, 2002 | — | NOT_ACCESSED |

### Cyclic, infinitary and complexity

| Source | Version read | Status |
|---|---|---|
| J. Brotherston, PhD thesis, Edinburgh, 2006 | — | VERIFIED_SOURCE |
| J. Brotherston, A. Simpson, JLC 21(6), 2011 | — | NOT_ACCESSED |
| S. Berardi, M. Tatsuta, LMCS 15(3:10), 2019 | — | VERIFIED_SOURCE |
| S. Berardi, M. Tatsuta, intuitionistic version | arXiv:1712.03502 | VERIFIED_SOURCE |
| S. Berardi, M. Tatsuta, LICS 2017 | — | NOT_ACCESSED |
| A. Simpson, FoSSaCS 2017 | — | NOT_ACCESSED |
| A. Das, LMCS 16(1), 2020 | — | VERIFIED_SOURCE |
| R. Nollet, A. Saurin, C. Tasson, CSL 2018 | — | VERIFIED_SOURCE |
| R. Nollet, A. Saurin, C. Tasson, TABLEAUX 2019 | — | ABSTRACT_ONLY |
| D. Baelde, A. Doumane, D. Kuperberg, A. Saurin | arXiv:2005.08257v1 | VERIFIED_SOURCE |
| L. Cohen, A. Jabarin, A. Popescu, R. Rowe, POPL 2024 | — | VERIFIED_SOURCE |
| S. Cook, R. Reckhow, JSL 44(1), 1979 | — | VERIFIED_SOURCE |
| E. Ben-Sasson, R. Impagliazzo, A. Wigderson, Combinatorica 24, 2004 | — | ABSTRACT_ONLY |
| S. Buss, JSL 77(2), 2012 | — | VERIFIED_SOURCE |
| Statman 1979 (both papers), Orevkov, Boolos 1984 | — | NOT_ACCESSED |
| E. Frittaion | arXiv:2110.01270 | VERIFIED_SOURCE (secondary for Shoenfield) |
| J. Väänänen, SEP "Second-order and Higher-order Logic", rev. 2024 | — | VERIFIED_SOURCE (secondary) |
| D. Kuperberg, L. Pinault, D. Pous, POPL 2021 | — | VERIFIED_SOURCE |
| S. Oda, D. Kimura | arXiv:2203.05791v2 | VERIFIED_SOURCE |
| A. Akbar Tabatabai, R. Jalali, "Universal Proof Theory: Semi-analytic Rules and Uniform Interpolation" | arXiv:1808.06258v2 (Thm 4.3, Cor 4.5), read by the author | VERIFIED_SOURCE |

### Reflection, polygraphs and circuits

| Source | Version read | Status |
|---|---|---|
| J. Krajíček, P. Pudlák, JSL 54(3), 1989 | Scan, Thm 5.1 | VERIFIED_SOURCE |
| P. Pudlák | arXiv:2007.14835 | VERIFIED_SOURCE |
| G. Arteche, A. Atserias, S. de Rezende, E. Khaniki | arXiv:2506.16956v2 | VERIFIED_SOURCE. Used as SECONDARY for Krajíček 2019 Thm 8.4.3 |
| J. Krajíček, books (1995, 2019) | — | NOT_ACCESSED |
| D. Ara, A. Burroni, Y. Guiraud, P. Malbos, F. Métayer, S. Mimram, *Polygraphs* | arXiv:2312.00429v2 | VERIFIED_SOURCE (grepped) |
| Y. Lafont, "Towards an algebraic theory of Boolean circuits", JPAA 184, 2003 | Preprint | VERIFIED_SOURCE |

---

*This report is an informal research audit. No theorem in it is new and proven. The lemma in §6.3 and constructions I-S and I-C are informal arguments by the author and need independent review. Review is requested on:*
- *the verdict;*
- *NCE-H (§6.2);*
- *the dilemma (§6.3);*
- *C\* and Gate 0.5 (§10).*
