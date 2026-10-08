# Report 002: Fundamentality, environment separation, and non-vacuity

| | |
|---|---|
| **Task** | `tasks/002-fundamentality-and-anti-vacuity.md` (Stage 0.5) |
| **Base** | `research/stage-0-5-coordination` @ `62ec35d` |
| **Date** | 2026-10-08 |
| **Status** | Review requested. Nothing here is FORMALIZED; no checker was run. Every argument of my own is labelled INFERENCE (informal argument) or CONJECTURE. Source statuses use `docs/RESEARCH_PROTOCOL.md` vocabulary. |
| **Evidence log** | [`reports/002-source-notes/`](002-source-notes/README.md) |

**Disclosure.** This report was written in the same session, by the same model, that wrote PR #2 (report 001 and its self-review). PR #1 (Codex), PR #2 and its self-review, and the Stage-0 synthesis were read in full; their conclusions are treated as claims to check, not results.

**Revision history.** A first draft of this report was attacked by a separate agent with fresh context; its critique is `002-source-notes/fresh-critique.md`. The attack **broke the draft's central claim**. §12 lists exactly what was withdrawn and why.

---

## 0. Executive verdict

**Recommendation: NARROW.** Do not proceed to any algebra or implementation, and do not stop on the evidence gathered here.

1. **Two kinds of "universality" must be separated.**
   - **(U-inst) Universality that inspects instances.** A fixed mechanism decides acceptance by examining the instantiated formulas or a coding of them. Examples:
     - Mossakowski–Diaconescu–Tarlecki (MDT) flattening;
     - Jeřábek's ubiquitous conservative translations;
     - the Clavel–Meseguer universal theory on ground codes;
     - extended Frege plus reflection with a bit encoding;
     - a Turing machine running on serialized tapes.
     
     A strong, componentwise **substitution-naturality** condition (SN, §2.3) excludes all of them. SN is independently motivated: it is Łoś–Suszko structurality, HHP's compositional adequacy, Cook–Reckhow's substitution-closed Frege rules, and the morphisms of syntax with binding of Fiore–Plotkin–Turi and Fiore–Mahmoud. It has real force: there is no schematic conservative translation of IPC into CPC (Prop 4), although a non-schematic one exists (Jeřábek Thm 2.4).
   - **(U-schema) Universality at the level of schemas.** These mechanisms only *instantiate schemas*, so they pass SN, homomorphism and adequacy:
     - a fixed LF signature in which an object logic's rules are passed as data (construction B1);
     - a checker over atom-uniform certificates (B2);
     - inductive or impredicative definitions in a strong foundation (B5).
     
     **So a fixed, finite framework that adequately represents every finitely schematic calculus already exists, and in a trivial way.** "Representable in one finite framework" (definition D1) therefore cannot be what "fundamental" means. D1 only certifies an *honest* representation, together with its trust ledger.
2. **A definition of "fundamental" that excludes both kinds is the classical notion of a *logical translation* (definition D2, §2.4).** It has four requirements:
   - each source formula maps *componentwise* to a formula of the core's own logic;
   - the judgment wrapper does not depend on the source;
   - derivations map homomorphically, with every source rule becoming a *derived rule of the core*;
   - no source-specific environment item quantifies over propositions;
   
   plus reflection of derivability.
   
   Every interpreter-like construction found fails D2, because formulas become data or the translation is not componentwise (Table §5). The definition is not tailored to interpreters: it is the "schematic translation" of Prawitz–Malmnäs and Pelletier–Urquhart, and the "logical morphism" thm[x] ↦ thm′[k[x]] of Rabe. **Cost:** LF and deep embeddings are *not* fundamental cores under D2. They remain legitimate representation media under D1. That is a deliberate distinction, and §5 argues it is principled rather than a decree.
3. **At the level of derivability, a finite cross-foundation core is prior art, assembled here from cited parts (CONJECTURE until checked).** Composing three known translations gives D2 translations of NJ, LK and S4(□) into one adjoint logic whose modes carry σ(m) ⊆ {W, C}, alongside native ILL:
   - **Kolmogorov, LK → NJ.** MDT Ex 2.4 records it as conservative. Proof-level homomorphism needs a "stable sort" repair: INFERENCE.
   - **Girard, NJ → ILL.** Faithful for provability: Girard 1987 p. 81 [S0].
   - **Judgmental S4(□) in adjoint logic.** Pruiksma thesis, Example 4.
   
   So the question "does a finite fundamental basis exist?" has a known positive answer at R1–R2 for this benchmark. It is not a novel target.
4. **Anti-vacuity is not fidelity.** An LF encoding of multiplicative linear logic that uses unrestricted hypotheses passes SN and homomorphism, but derives p ⊢ p⊗p, which linear logic does not prove (§6.2). Reflection of derivability is a separate, necessary clause.
5. **Individual operations are never invariantly "fundamental".**
   - The Boolean clone has the disjoint bases {nand} and {∧, ¬}.
   - All Frege systems over the same connectives simulate each other rule by rule (Cook–Reckhow Thm 2.3, under its hypotheses).
   - Only the generated structure, and the preorder of D2-interpretability, are invariant (§7).
6. **PR #2's vacuity–identity dilemma is not exhaustive (§9).** Its lemma stays retracted. Its "horn (ii)" (environment equations make R3 vacuous) is false for schematic and generic equations. Its case split also missed the distinction that actually matters here: instance-level versus schema-level universality.

**Strongest remaining mathematical uncertainty.** The D2 core above preserves and reflects *theorems*. It is not known whether it preserves *proofs* in the following sense.

> **Is there a single finite core A, with one fixed proof equality, that admits D2 translations of an intuitionistic, a classical and a linear calculus which are all *full*?**
>
> *Full* means: every A-derivation of a translated sequent is equal, in A, to the translation of some source derivation.

Fullness is what separates "A proves the same theorems" from "A's operations generate exactly the source's proofs". The pairwise evidence is mixed:
- Girard's translation from STLC into linear λ is fully complete (Hasegawa 2000).
- Linear CPS is full for the computational λ-calculus (Hasegawa 2002, Thm 1).
- The ordinary CPS translation into STLC is "not full" (Hasegawa 2002, §1.3).

No *joint* result was found. This question touches proof identity (Task 003); see the coordination note in §10. The single next test is in §10.4.

---

## 1. Scope and method

- **Source agents.** Three source agents ran under a written protocol (`002-source-notes/00-extraction-protocol.md`), covering:
  - structurality and translations between logics (`str`);
  - binding algebra and derived/admissible rules (`bnd`);
  - generic-framework follow-ups (`gfu`).
- **Own extractions and spot checks.** I re-checked decisive passages myself (`own.md`, O3) and extracted Holliday–Hoshi–Icard (Public Announcement Logic, PAL) and Yamada directly. Pruiksma's Example 4 and MDT Ex 2.4 were also re-read directly.
- **Adversarial attack.** A fresh-context agent attacked the first draft (`fresh-critique.md`). Its findings are incorporated, with credit, throughout.
- **Reused logs.** Stage-0 logs [S0] and PR #2 review logs [R] are reused where cited.
- **Access limits:**
  - **Not accessed:** Sheffer 1913, Post 1941, Łoś–Suszko 1958 (SEP used), Feitosa–D'Ottaviano 2001 (via Jeřábek and MDT), Wójcicki, Prawitz–Malmnäs (cited via Pelletier–Urquhart), Zolin 2000, Girard's LU, Buszkowski 1982 (via KKS), Chvalovský–Horčík 2016, Iemhoff, Humberstone, Schürmann, Hofmann–Streicher, Berdine–O'Hearn–Reddy–Thielecke.
  - **Not found:** the LSR dependent sequel, which is unpublished.
  - **Literature search:** about 60 citing papers of LSR were screened via Semantic Scholar. No Google Scholar sweep was done.
  - **Page numbers** refer to the versions read, mostly preprints.

---

## 2. Definitions

### 2.1 Source class: finitely schematic calculi

A **finitely schematic calculus** S = (Σ, 𝒥, ℛ) consists of:
- a finite *sorted second-order signature* Σ for object syntax;
- a finite set 𝒥 of judgment forms;
- finitely many rule schemas ℛ.

Each rule r has:
- sorted formula metavariables, possibly with binding arities;
- premises, which may be *hypothetical* or *parametric*;
- a conclusion.

There are **no side conditions** beyond what sorts and binding express. Consequently, calculi with a computational side condition, such as a conversion rule "A ≡ B", are *outside* the class unless they are re-presented declaratively (with an explicit conversion judgment).

**Schematic derivations** may contain:
- formula metavariables;
- hypothesis and parameter variables;
- **derivation metavariables**: open premise holes, of every judgment form.

They are closed under three operations:
- sort-respecting metasubstitution;
- proof substitution, including the second-order case;
- *grafting* into derivation metavariables.

**Why sorting matters.** PAL is "not closed under uniform substitution". Its reduction axiom (i) ⟨ϕ⟩p ↔ (ϕ ∧ p) has the invalid instance ⟨p⟩K_i p ↔ (p ∧ K_i p) (Holliday–Hoshi–Icard 2011 §§1.1–1.2, VERIFIED_SOURCE). PAL is finitely schematic once atoms form their own sort.

**Why finiteness matters.** If every formula is re-declared as an atom, every map becomes "uniform" (Caleiro–Gonçalves p. 7, VERIFIED_SOURCE). Finiteness of Σ and ℛ blocks this sort-splitting attack.

### 2.2 Targets, environments and the trust ledger

**Framework conditions.** A framework A has:
- fixed typing rules;
- substitution;
- a definitional equality ≡_A, with typing and ≡_A stable under substitution.

For λΠ-modulo this requires, beyond rewriting being stable under substitution, subject reduction (well-typed rules) and product compatibility (Dedukti manuscript Lemma 4 and Thm 8 [S0]). These conditions are part of the hypothesis.

**The ledger is descriptive, not definitional.** The first draft classified environment items *one at a time* by "logical role". The fresh critique showed this is ill-defined (critique §D1):
- `raa : ΠA.((A→⊥)→⊥)→A` is at once an axiom (role b) and a rule (role c);
- removal tests are not item-wise: redundant rules, mutually redundant pairs, and admissible primitives such as Cut do not fit;
- "structural datum" was defined only by examples.

The ledger is therefore kept **only as a descriptive report**. Each representation lists:
- declared syntax;
- declared rule-typed items;
- declared axioms;
- structural data;
- extensions of ≡_A (rewrite rules or equations);
- external procedures (confluence, termination and totality checks).

Admissible primitives (for example, Cut declared in an encoding of LK) get a separate slot.

**One well-defined, syntactic test is used *definitionally* (in D2):**

> An environment item is **logical** iff its type quantifies over formulas: over the sort or type that interprets source formulas, or over the core's propositions.

- So `raa`, every schematic axiom, and every rule constant are logical.
- Atoms, function symbols, and axioms about specific atoms are not.
- This fixes the b/c ambiguity. Declaring all of a Hilbert logic as schematic axioms makes every one of them logical, so it is excluded.

### 2.3 Representation properties

A representation (E_S, ⌜·⌝, F) maps:
- syntax to A-terms, with variables going to variables;
- judgments to A-types through a *judgment wrapper* W;
- derivations to A-terms.

| Name | Statement |
|---|---|
| **SN** (strong naturality) | F is defined on all schematic derivations, and F(d[θ]) ≡_A F(d)[⌜θ⌝] for every metasubstitution θ, with ⌜θ⌝ the *componentwise* image of θ. This covers formula metavariables **and** derivation metavariables (grafting) |
| **WN** (weak; for contrast) | ∀θ ∃θ\* with F(d[θ]) ≡ F(d)[θ\*] |
| **HN** (hypothetical) | F(d[d′/u]) ≡_A F(d)[F(d′)/u] (with the second-order case), where S's hypotheses are realised as A-variables of the matching structural kind |
| **HOM** | Each rule r has a fixed template M_r with F(r(d⃗)) ≡_A M_r[⌜θ⌝][λu⃗.F(dᵢ)] |
| **ADQ1** | S ⊢ J ⇔ W(⌜J⌝) is inhabited over E_S |
| **ADQ2** | F is a bijection from S-derivations modulo α onto the canonical (β-normal, η-long) inhabitants |
| **FULL** | Every A-inhabitant of a translated judgment is ≡_A to some F(d). The choice of ≡_A is the identity question of Task 003 |

**Sources for these notions.**
- HHP define compositionality as "substitution commutes with encoding; in particular substitution in the logical system is encoded as substitution in LF" (p. 2). Their Thm 4.1 gives SN and HN for first-order natural deduction (FOL ND) [S0, bnd].
- Pfenning Thm 3.2(3) gives SN and HN, including proposition substitution [S0].
- For syntax alone, SN is the condition that makes a map a Σ-monoid morphism (Fiore–Plotkin–Turi, Thm 4.1 / 4.2) or a syntactic translation (Fiore–Mahmoud, arXiv:1308.5409, Lemma 5.1: syntactic translations "commute with substitution and metasubstitution") [bnd].
- Extending this to judgments and derivations is INFERENCE. Following the bnd notes: for *homomorphic* translations, SN holds automatically. Its discriminating content is that it rules out *non-homomorphic* maps.

### 2.4 Three inequivalent definitions

**D1, honest framework representation (not fundamentality).** SN + HOM + ADQ1, with the full trust ledger. HN is required when S's hypotheses are to be realised natively; this is an R2 choice (cost listed in §5). ADQ2 is the strong form.

**D2, fixed-core logical translation (fundamentality).** A finite core logic A is **fundamental for a class C** iff every S ∈ C has a representation satisfying all of the following:
- **(T1) Formulas.** ⌜·⌝ maps S-formulas to A-*formulas* (A's own propositions or types) componentwise. Each connective goes to a fixed A-formula context, and atoms go to atoms of the matching sort. Formula metavariables may be sent to metavariables of a designated A-sort (see the stable-sort repair, §5 L-g).
- **(T2) Judgments.** The wrapper W is fixed by A and **independent of S** (for example Γ ⊢ Δ ↦ Γ′, ¬Δ′ ⊢ ⊥, or !Γ′ ⊢ ?Δ′).
- **(T3) Derivations.** SN (including derivation metavariables) and HOM, with each template M_r a derivation in A itself.
- **(T4) Environment.** E_S contains **no logical items** (§2.2).
- **(T5) Adequacy.** ADQ1.

*Strengthenings:* D2 + ADQ2 and D2 + FULL.

**D3, D2 relative to a fixed family.** A family {A_K : K ∈ 𝒦} of cores indexed by structural data from a menu 𝒦 that is **fixed in advance**. Examples:
- adjoint logics with modes carrying σ(m) ⊆ {W, C};
- LSR mode theories in a specified class.

C is D3-covered iff each S ∈ C is D2-translatable into some A_K.

**Inequivalence** (INFERENCE, using cited theorems).

| Example | D1 | D2 | D3 |
|---|---|---|---|
| LF with declared rule constants, for FOL ND (HHP Thm 4.1) | Yes | **No** (formulas become data of type `o`; rule constants are logical items) | — |
| B1, the universal reflected signature (§5) | Yes, for *every* finitely schematic class | **No** | — |
| Shallow STLC (⊃ ↦ →), for NJ(⊃) | — | Yes | — |
| Kolmogorov, for LK into NJ (with stable sorts) | — | Yes | — |
| A single adjoint logic, for {NJ, ILL, S4(□)} (Pruiksma Ex 4) | — | — | Yes |

So D1 is satisfiable for every class (B1), while D2 is not (Prop 4). At the level of classes the definitions therefore differ. In particular, IPC has no D2 translation into CPC.

---

## 3. Results

All results in this section are **INFERENCE** (informal arguments) unless marked.

**Lemma 1 (SN at derivation metavariables gives HOM).**
- *Claim.* Let M_r := F(r(ξ⃗)), where the ξ⃗ are derivation metavariables. Grafting d⃗ into ξ⃗ gives r(d⃗), and SN at the derivation sort gives F(r(d⃗)) ≡ M_r[F(d⃗)/ξ⃗].
- *Status.* With this hypothesis, HOM is close to a reformulation. The first draft derived it from SN at *formula* metavariables plus HN. That is false: for sources without hypotheses, the critic's counterexample (map each K/S/MP Hilbert derivation to its weak-normal combinatory form) satisfies formula-level SN and ADQ1, but not HOM. The Fiore–Plotkin–Turi analogy covers only the substitution half (critique §A2).

**Lemma 2 (acceptance is invariant under instantiation).**
- *Claim.* If M_r is well typed at generic formula metavariables, then every instance M_r[⌜θ⌝] is well typed, because typing and ≡_A are stable under substitution.
- *Consequence.* The representation can neither accept nor reject a step by inspecting *which formulas* instantiate the schema.
- *What it does not say.* It is a statement about validity, not about cost. A checker can still do unbounded work on the *derivation* (certificate) while being stable under formula substitution (critique §A3).

**Lemma 3 (WN is vacuous).**
- *Claim.* WN is satisfied by:
  - MDT Prop 2.25, with θ\*(α(φ)) := α(θφ);
  - Jeřábek's most general translations, up to CPC-equivalence (Def 2.3: for structural L, f∘σ is again a translation).
- *Status.* Credited to the str agent. Only the componentwise SN has force.

**Proposition 4 (componentwise translation has teeth).** There is no schematic (componentwise, finite-variable) conservative translation of IPC consequence into CPC.

*Argument.*
1. A schematic translation sends one-variable formulas into a finite-variable fragment of CPC.
2. CPC is locally finite, so there are only finitely many classes there.
3. IPC has infinitely many pairwise non-interderivable one-variable formulas (Rieger–Nishimura; UNVERIFIED-MEMORY).
4. Conservativity for consequence would identify two of them. Contradiction.

By contrast, Jeřábek's Thm 2.4 (VERIFIED) gives a non-schematic conservative translation of every finitary deductive system over a countable set of formulas into CPC. His conclusion, p. 14: bare conservativity "does not provide useful information … a more refined criterion is needed".

**Proposition 5 (schema-level universality is trivial).** There is a fixed finite LF signature Σ_univ (critique §B1) through which *every* finitely schematic calculus S has a representation satisfying SN, HN, HOM and ADQ1, plausibly also ADQ2, with E_S = ∅.

*Construction.*
- The signature contains:
  - HOAS syntax `tm`;
  - rule codes;
  - `Prf : sig → tm → type`;
  - relational `mem` and `inst`;
  - one rule `use`.
- The wrapper is ⌜⊢_S φ⌝ := Prf code_S ⌜φ⌝, so S's rules enter as the data term code_S.

*Consequence.* "A fixed finite framework representing all schematic systems" is not a meaningful achievement.

*Status.* Construction from the critique; checked by me in outline; ADQ2 unverified.

*Effect on D2.* Under D2, Σ_univ fails twice:
- T1: formulas become `tm` data;
- T2: the wrapper depends on S through code_S.

The critic's partial repair for D1 (an S-independent wrapper plus a declared `theSig`) only moves code_S into the ledger.

**Proposition 6 (D2 excludes every construction examined).** By the table in §5, each U-inst and U-schema construction fails at least one of T1, T2 and T4.

**Proposition 7 (a D2/D3 core at R1 for a cross-foundation benchmark; CONJECTURE assembled from cited components).** Let A be adjoint logic with modes V > U > L, σ(V) = σ(U) = {W, C} and σ(L) = {}. Then the following have D2 translations into A satisfying ADQ1:

| Source | Translation | Evidence |
|---|---|---|
| **ILL** | Native, at mode L | Pruiksma's linear instance (gfu) |
| **NJ** | Native, at mode U | (gfu) |
| **S4(□)** | V for validity, U for truth, □A := ↓_VU ↑_VU A_U | Pruiksma thesis Example 4, VERIFIED (own check). ◇ is *not* covered ("we cannot easily model ♦A") |
| **LK** | Kolmogorov translation into the U mode, with W(Γ ⊢ Δ) = Γᴷ, ¬Δᴷ ⊢ ⊥ | Kolmogorov K is a conservative entailment-relation morphism (MDT Ex 2.4, VERIFIED) |

*Proof-level homomorphism for LK (INFERENCE).* It needs a uniform stability template for ¬¬-prefixed and ¬-prefixed images. That template exists once formula metavariables are sent to a "stable" sort (⌜X⌝ := ¬¬X′, with componentwise bodies; critique §C2 repair).

*Composition.* D2 translations compose, so NJ also goes into mode L by Girard's !A ⊸ B, faithful for provability (Girard 1987 p. 81 [S0]).

**Not claimed:** ADQ2 or FULL for any of these.

---

## 4. Machinery versus environment: (i) assumption, (ii) derived rule, (iii) declared rule, (iv) checker

### 4.1 Stability

- **Derivability is stable.** PFPL Thm 3.1 (Stability), VERIFIED.
- **Admissibility is not.** Harper gives a counterexample.
- **"Derivable iff admissible in every extension" depends on the class of extensions.** It fails under the substitution-closed propositional reading: the Kreisel–Putnam rule is admissible in every intermediate logic but not derivable in IPC (UvA handout Prop 8, Thm 9; SECONDARY).
- **In frameworks.** Derived rules are framework terms: LF "eliminates the distinction between primitive and derived rules" (HHP p. 2). Admissible rules are not: LF "precludes the encoding of a proof of admissibility … that makes use of a principle of induction over a type of proofs" (HHP p. 23).
- **Admissible primitives**, such as a declared Cut in LK, are a fourth status: their removal is conservative, but they are not definable. They need their own slot in the ledger.

### 4.2 The four kinds in existing frameworks

| Framework | (i) Assumption | (ii) Derived | (iii) Declared object rule | (iv) Checker / reduction | D2 status |
|---|---|---|---|---|---|
| LF (HHP; Pfenning) | Context variable or base-typed constant | LF term | Constant of rule type (logical item) | Admissibility via Twelf totality: trusted mode, world, termination and coverage checkers [bnd] | Not a core: formulas are data |
| Isabelle/Pure (Paulson) | Meta-hypothesis | Meta-proof | Axiom of M_L | ≡-definitions | Not a core: object formulas are data of type `prop` |
| Rewriting logic | Equation / rule instance | Proof term | Rewrite rule | Universal U on ground codes | Not a core; U fails SN |
| Dedukti / λΠ-modulo | Constant `Prf φ` | λΠ term | Constant of rule type | Rewrite rules; confluence and termination "out of the scope of Dedukti itself" [S0] | Not a core, except shallow decodings (`Prf(imp A B) ↪ Prf A → Prf B`), which pass SN/HN as D1 |
| Focused LL (Miller–Pimentel) | Theory formula | Synthetic bipole derivation | Bipole clauses + Cut, Init, Pos/Neg (logical items) | Polarity assignment; cut-coherence decidable (Thm 22) | D1 with declared clauses |
| FPC | — | — | None (fixed kernel) | Clerks and experts *untrusted*: "soundness by erasure" [S0] | Benign checker: only filters a fixed sound kernel |
| Adjoint / LSR / Shulman | Context hypothesis | Generated rules | None for connectives | Mode theory (structural data); mode equality assumed decidable, or quotient metatheory assumed | D3 cores |
| Linear-logic cores (ILL + !, LU, Yamada's ILCρ) | Hypothesis | Rule combinations | None | None | D2 cores, via Girard, Kolmogorov or Yamada translations |

**The (iv) distinction (INFERENCE):**
- A checker is **benign** when it only filters derivations of a fixed sound core (FPC).
- It is **generative** when a premise of the form "checker accepts" yields a conclusion (an `acc` rule). Such a checker always makes formulas data, so D2 excludes it via T1.

### 4.3 Environment-supplied equivalence rules (PR #2 horn (ii))

The equations split into three kinds:
- (α) equations computing on coded data;
- (β) schematic equations between proof constructors;
- (γ) equations generated from universal properties.

What happens to each:
- **(α)** is excluded by SN when the computation inspects formula instances. Recursion on *certificates* survives SN (B2), and is excluded by D2's T1.
- **(β)** gives preservation by declaration, but *reflection* (that nothing more is identified) is a theorem that can fail:
  - Felicissimo–Winterhalter FSCD 2024, Table 1: no conservativity proofs, and non-confluent encodings [S0];
  - Felicissimo FSCD 2022, Thm 46: reduction preserved and reflected for functional explicitly typed PTSs [S0].
- **(γ)** is the generic-framework route (§8).

So horn (ii), "E may extend ≡ ⇒ vacuous", is **false** as a general claim.

---

## 5. Adversarial counterconstructions

**Notation.**
- Columns T1, T2 and T4 refer to the clauses of D2 (§2.4).
- **D1** in the last column means: passes D1 (SN, HOM, ADQ1).

**Constructions that inspect instances (U-inst):**

| # | Construction | Status of source | SN | T1/T2/T4 | Verdict |
|---|---|---|---|---|---|
| I-H | MDT flattening: φ ↦ fresh variable α(φ); Δ = whole consequence relation | MDT Prop 2.25 V [S0] | **Fails** (passes only WN) | Fails T1 (not componentwise) | Excluded |
| I-J | Jeřábek's most general translation into CPC (γₙ ∨ pₙ ∧ δₙ) | Jeřábek Thm 2.4, pp. 4–5, V | **Fails** | Fails T1 | Excluded |
| I-U | Clavel–Meseguer U with T as data | Thm 3.2, for ground t, t′, V [S0] | **Fails** (object variables are ground codes) | Fails T1 | Excluded |
| I-R | EF + Refl_S with bit encoding | Krajíček Thm 8.4.3, S [S0] | **Fails** (bit encoding is not componentwise) | Fails T1/T4 | Excluded. An atom-uniform variant survives SN: see B2 |
| I-S | Turing-machine step checker over serialized tapes | INFERENCE | **Fails** (a metavariable cannot be serialized homomorphically) | Fails T1 | Excluded |
| I-C | Dedukti `acc` checker recursing on φ | INFERENCE | **Fails** (stuck at generic X) | Fails T1 | Excluded |

**Constructions that instantiate schemas (U-schema):**

| # | Construction | Status of source | SN | T1/T2/T4 | Verdict |
|---|---|---|---|---|---|
| B1 | Universal reflected LF signature Σ_univ (rules as data in the wrapper) | Critique §B1, INFERENCE | **Passes** (also HN, HOM, ADQ1) | Fails T1 (formulas as `tm` data) and T2 (wrapper depends on S) | D1 yes, D2 no |
| B2 | Checker-as-proof over atom-uniform Frege/EF certificates, with a per-rule certificate map π, `getcert` and non-left-linear `eq` | Critique §B2, INFERENCE | **Passes**, with HOM via `getcert`, for sequent and Hilbert sources | Fails T1 (formulas as data under `acc`) | D1 yes, D2 no |
| B3 | B2 extended to natural-deduction sources with `hypcert ψ (getcert u)` leaves and higher-order patterns | Critique §B3, plausible, unchecked | Plausibly passes, with HN | Fails T1 | D1 plausibly, D2 no |
| B4 | Fixed universal environment E_fix (universal Horn program over codes) | INFERENCE | Fails (stuck), unless it is a rules-as-data instantiator, i.e. B1 | Fails T1 | Excluded or reduces to B1 |
| B5 | Inductive or impredicative definitional embedding in HOL/CIC: Deriv_S defined as a least fixed point (definitional, hence conservative) | INFERENCE; Smullyan-style universality | Passes for metavariables of sort `Form`; HN fails for ND (contexts are data) | Fails T1 (Deriv_S(⌜φ⌝): formulas as data) | D1 for sequent/Hilbert sources; D2 no |
| B6 | Lemma-1 counterexample: map each K/S/MP derivation to its weak-normal combinatory form | Critique §A1, INFERENCE | Formula-level SN passes; derivation-level SN fails | — | Excluded by derivation-level SN (Lemma 1) |
| I-K | Sort-splitting: every formula an atom | Caleiro–Gonçalves p. 7, V | Trivially passes | Infinite Σ | Excluded by finiteness |

**Completion test (task requirement).**
- **The universal interpreter violates T1 (and SN).**
  - The instance-inspecting interpreters violate SN.
  - All of them, together with the schema-level universal frameworks, violate T1: formulas are not mapped componentwise to the core's own formulas. Most also violate T2 or T4.
- **T1 is not tailored to interpreters.** It is the classical definition of a translation between logics:
  - Prawitz–Malmnäs "schematic interpretation", which Pelletier–Urquhart (Def p. 6–7, V [str]) call "essentially the same";
  - Caleiro–Gonçalves Def 2.4 "uniform" translation (primitive connectives ↦ derived connectives), motivated by effectivity, not by interpreters;
  - Rabe's logical morphisms l(thm[x]) = thm′[k[x]] (Def 3.35 [S0]).
  
  The standard positive examples of the field (Kolmogorov, Gödel–Gentzen, Girard, CPS) were designed before and independently of any anti-interpreter purpose.
- **Caveat on how much T1 excludes.** T1 also excludes LF and every deep embedding *as cores*. They remain D1 representation media. This is a deliberate separation:
  - under D2, the question is whether the core *generates* the source's logic;
  - in LF, all of the source's logical content is declared.
  
  Reviewers should judge whether this counts as "excluding frameworks by fiat". I argue it does not, because D1 still admits them with an honest ledger.

**Loopholes and over-exclusions.**

- **L-a. Schema-by-conversion.** A deep certificate embedding with a schematic checker passes D1 for sequent and Hilbert sources (B2), and plausibly for ND sources (B3).
  - The first draft called it "isomorphic to the LF image". **That claim is withdrawn**: the certificates live in a different calculus (critique §B2).
  - It is excluded only at D2.
- **L-b. Undecidable sources.** A finitely schematic source may itself have undecidable derivability:
  - a single subexponential with non-local contraction (KKNS Thm 8; the computation lies in the end-sequent, i.e. undecidability of the *logic*, confirmed);
  - finitely many non-logical axioms over the Lambek calculus (Buszkowski via KKS Thm 10; role (b); finiteness of A unverified).
  
  This is fidelity to an undecidable logic, not vacuity of the representation.
- **L-c. Second-order HN.** HN's second-order case quantifies over an LF-style extension of S's derivations. This is mildly framework-shaped (critique §A4.4).
- **L-d. Interpreter-shaped sources.** A source presented deliberately as an interpreter (for example "c ⊢ φ whenever check(c, φ)") lies outside the finitely schematic class. Choosing the source class is a modelling decision (Stage-0 synthesis, requirement (i)).
- **L-e. Admissible but non-derivable rules.** These have no template. They need a Twelf-style external check or a declared rule (§4.1).
- **L-f. Computational side conditions** (type theories with conversion; proofs by reflection in Coq/Lean). These are outside the source class (§2.1) unless re-presented declaratively, with explicit conversion derivations and their size cost (F09).
  - The first draft listed this as an SN over-exclusion. **Corrected**: it is a source-class restriction (critique §A4.2).
- **L-g. Negative translations at proof level.** In Gödel–Gentzen (and Kolmogorov) proof translations, RAA needs ¬¬φᴺ → φᴺ, built by induction on φ. There is no fixed template at generic X (critique §C2).
  - *Repair:* send metavariables to a stable sort, as in Prop 7. INFERENCE; needs checking.
  - Call-by-value CPS commutes with substitution only for values (UNVERIFIED-MEMORY).
- **L-h. Top-level non-componentwise translations.** MDT note that schematic preservation "rules out e.g. the standard translation of modal logic to first-order logic, which adds a quantifier at the very top" (VERIFIED).
  - The T2 wrapper repairs the top level, but needs second-order metavariables (ST_x as λx…).
  - ADQ1 still fails for logics that are Kripke-incomplete or not first-order definable (critique §C3).
- **L-i. HN excludes deep embeddings with explicit contexts:** rewriting-logic ND, Metamath, Coq/Lean/HOL embeddings with explicit contexts, de Bruijn encodings (critique §C1). These pass D1 only without HN. HN is therefore an *optional* R2 strengthening, not an anti-vacuity condition.

---

## 6. Required tests

### 6.1 Reference calculus NJ(⊃)

| Representation | SN (formulas + derivations) | HN | ADQ1 | ADQ2 | D1 | D2 | Notes |
|---|---|---|---|---|---|---|---|
| LF {o, imp, pf, impi, impe} | Yes | Yes | Yes | Yes (HHP Thm 4.1 / Pfenning Thm 3.2, of which NJ(⊃) is a fragment) | **Yes** | **No** (formulas are `o` data; impi and impe are logical items) | Honest framework encoding |
| Shallow STLC (⊃ ↦ →) | Yes | Yes | Yes | Bijection on raw terms modulo α | — | **Yes** | Trivial core |
| Universal machine (I-U; I-S with tapes) | **No** | — | Yes | — | **No** | **No** | — |
| B1, universal reflected signature | Yes | Yes | Yes | Plausibly | **Yes** | **No** | Shows D1 is trivially universal |

### 6.2 Resource-sensitive negative control: MILL (⊗, ⊸)

| Representation | SN / HOM | ADQ1 | D2 into ILL | Verdict |
|---|---|---|---|---|
| LF with unrestricted hypotheses, `tensI : ΠA B. pf A → pf B → pf(A⊗B)` | Yes | **No**: x:pf p ⊢ tensI p p x x : pf(p⊗p), but p ⊢ p⊗p is not MILL-derivable | — | **FALSE**: duplication masquerading as linear inference |
| LF with contexts as data | Yes (no HN) | Expected yes ([S0] Cervesato–Pfenning p. 53: "complex proofs") | — | D1 without HN |
| LLF with `pf A ⊸ pf B ⊸ pf(A⊗B)` | Yes, with linear HN | Expected yes (INFERENCE; LLF is conservative over LF, Thm 2.9 [S0]) | — | D1 with HN |
| Identity into ILL (or adjoint mode L) | Yes | Yes | **Yes** | Trivial D2 |

**Lesson.** Anti-vacuity (SN, T1) and resource fidelity (ADQ1) are separate requirements, and both are needed. This matches Gardner Cor 5.1.8: "There are no adequate representations of linear and relevant logics" in ELF+ [S0, bnd].

### 6.3 Trust ledger (descriptive)

| Representation | Fixed machine | Declared logical items | Structural data | ≡-extensions | External checks | Adequacy evidence |
|---|---|---|---|---|---|---|
| LF / FOL ND | λΠ (HHP Thm 2.6) | One per rule | Intuitionistic contexts | none | none | HHP Thm 4.1 (informal, per signature) |
| Dedukti / functional PTS | λΠ-modulo | Per-PTS constants | — | εₛ / Π̇ decodings | Confluence, termination | Cousineau–Dowek Thm 1 (needs termination); Assaf Thm 5.24 [S0] |
| Theory U (Blanqui et al. 2021) | λΠ-modulo | 38 declarations (fixed once) | — | 28 rules (fixed once) | Confluence proved (Thm 9) | Fragment theorem; *not* provability-conservative [S0] |
| Rewriting-logic U | Rewriting logic | none (T as data) | — | U's rules | none | Thm 3.2 on ground terms; fails SN |
| Focused LL / LK (Miller–Pimentel) | Focused LLF | Bipole clauses + Cut/Init/Pos/Neg | Polarity | none | Cut-coherence (Thm 22) | Thm 6 (provability); "full completeness of proofs" asserted, not written out [gfu] |
| Adjoint logic / {ILL, NJ, S4(□)} | Adjoint connectives + shifts | none | Modes, σ ⊆ {W, C} | none | none | Cut elimination and identity proved by hand (Pruiksma) |
| LSR | F, U; cut and identity once (Thm 2.1) | none | Mode theory | none | Mode equality | Logical adequacy proved; equational adequacy Conj 8.5 open |
| Kolmogorov LK → NJ (Prop 7) | NJ | none | — | none | none | MDT Ex 2.4 (conservativity); proof-level homomorphism is INFERENCE |
| Yamada ILCρ | ILCρ | none | — | none | none | **Restricted:** Cor 3.37 holds only for LKρ, which carries a hereditary, non-schematic "tractable"/purity condition. Cor 3.18's target ILCι lacks cut elimination ("we cannot show that this translation T! is conservative"). Cut uses ?!R!?, forbidden in ILCρ (critique §E1, confirmed against unity.txt) |
| FPC | LKF/LJF kernel | none | Polarization | none | Clerks/experts untrusted | Soundness by erasure; theoremhood only [S0] |

---

## 7. Minimality and invariant comparison

1. **Primitive counts are not invariant.**
   - Böhler et al. Ex 1.3: "[nand] = BF". BF also has the base {and, not}. So no operation is in every basis (V for the bases; the corollary is elementary).
   - Clones, "considered up to term equivalence", are in one-to-one correspondence with fragments of CPC (Jeřábek Def 3.4, V).
2. **Basis-independence within Frege.**
   - Cook–Reckhow Thm 2.3 / Cor 2.4: any two Frege systems over the *same* adequate connective set K (finite sets of sound, *implicationally complete* rule schemas; classical propositional) p-simulate each other with linear line and size overhead, via substituted fixed derivations, i.e. HOM translations [S0, V].
   - The case with different connective sets is Reckhow's thesis (SECONDARY).
   - **This does not cover** the {nand} versus {∧, ¬} comparison in item 1. That comparison concerns connective bases, not rule bases (critique §E5).
3. **Invariant equivalences** (all formula-level; none addresses proofs or binders):
   - **Synonymy = translational equivalence.** Pelletier–Urquhart Thm 2.6, V. Invariant: number of reduced algebraic models per cardinality (Cor 3.2). K, T, B, S4 and S5 are pairwise non-equivalent (Thm 4.5). Mutual exact translatability is strictly weaker (2006 correction).
   - **Equipollence.** Caleiro–Gonçalves Def 4.1 / Prop 4.3.
4. **Proposal (CONJECTURE about usefulness).** Compare cores by A ≼ A′ ⇔ A has a D2 translation into A′.
   - The invariant objects are the ≼-classes, and the minimal classes covering a given C. These are invariant under re-presentation; primitive counts are not.
   - Translation costs (template size, polynomial versus linear overhead) are reported separately (F09). A small basis does not imply computational efficiency.
   - *Expected (CONJECTURE):* several known cores fall into one class (ILL with !; adjoint logic with a {W, C} menu; LU; CLL⁻). So "the" fundamental basis is not unique.

---

## 8. Generic frameworks: what exists and what remains unproved

**Established** (VERIFIED_SOURCE unless marked):

- **LSR 2017** (LIPIcs 84, art. 25):
  - F and U are generic;
  - cut and identity are proved once for all mode theories (Thm 2.1);
  - one uniform equational theory, "the βη-laws for F and U" [R].
- **LSR equational adequacy is open.** p. 25:17: "We conjecture that the converse is true …". Extended version: "CONJECTURE 8.5. Completeness of Permutative Equality".
  - No proof or refutation was found in about 60 citers, 2017–2026 [gfu].
  - Shulman (MATT, MFPS 2023) calls LSR's "definitional equality … ill-behaved". His Remark 2.6: "L[S†] can fail to have decidable equality even if L does". He leaves open "which (L, S) are decidable?" [own].
- **Clarke–Scherer–Zeilberger** (arXiv:2511.07314v3, Jan 2026, preprint), for the *unary* case only:
  - Thm 1.17: "Λp : Bif(p) → C is the free bifibration on p". The cut-free calculus modulo permutation presents it: the unary analogue of LSR Conj 8.5.
  - Thm 3.27: permutation equivalence of proofs is undecidable for some base "with locally finite factorizations". That base has infinitely many generating arrows, and the result concerns proof *identity*, not derivability.
  - Thm 3.28: decidable when the base is locally finite or factorization-preordered [own].
- **Shulman 2023** (LNL polycategories, LMCS 19(2)):
  - reaches classical *linear* logic;
  - "We leave cut-elimination for future study" [R].
- **Adjoint logic** (Pruiksma thesis CMU-CS-24-103):
  - per-mode σ(m) ⊆ {W, C};
  - "only models intuitionistic logics";
  - S4's ◇ is not modelled;
  - cut elimination and identity proved by hand [gfu, own].
- **No generic type-theoretic framework covers LK natively.** LK reaches generic cores only by translation (Prop 7) or by declared clauses (Miller–Pimentel).

**Structural data and computation.** These must be stated carefully:
- Decidability of *equality* of structural data can fail (Shulman Remark 2.6; CSZ Thm 3.27, infinite base).
- Undecidability of *derivability* in KKNS and Buszkowski is a property of the *logic*, not evidence that the environment acts as an interpreter (L-b).
- *My conjecture (UNVERIFIED):* directed 2-cells in a finite LSR mode theory behave like string rewriting, so derivability may be undecidable for some finite mode theory. No source proves this.

**Answer to problem 4.** Yes: these frameworks provide a meaningful fixed generative mechanism for *logical* rules (D3). What remains unproved:
- multi-ary equational adequacy (LSR Conj 8.5);
- decidability criteria for mode theories;
- cut elimination for Shulman's doctrines;
- a classical non-linear instance.

---

## 9. Is PR #2's vacuity–identity dilemma exhaustive?

**No.**

1. **The lemma stays retracted.** It swapped preservation and reflection, and in corrected form it is a near-tautology (PR #2 review §3.1). It is not cited here.
2. **Horn (ii) is false for (β) and (γ) equations (§4.3).**
3. **Horn (iii)** ("A natively contains each foundation's structure, so it is a union, not a basis") is refuted as a dichotomy:
   - by D2 cores that *derive* other foundations' rules (Prop 7);
   - by D3 generic frameworks.
4. **The dilemma also missed a distinction.** The real line between "algebra" and "interpreter" is not about equations at all. It runs between *instance-level* universality (excluded by SN) and *schema-level* universality (B1, B2, B5), which is excluded only by requiring a logical translation (T1–T4).
5. **What survives** (INFERENCE): under D1 with rule constants and a fixed ≡_A, only identities generated by permutations of independent rule instances can be reflected (fresh-critique N3 of PR #2). Recorded as C2 and handed to Task 003.

---

## 10. Formulations, recommendation and next test

### 10.1 Theorem-shaped formulations

**T1 (Schematic invariance; INFERENCE).** Assume:
- a finitely schematic S;
- a framework whose typing and ≡ are stable under substitution;
- SN at both formula and derivation metavariables.

Then F is HOM, with templates F(r(ξ⃗)) (Lemma 1), and acceptance is invariant under formula instantiation (Lemma 2).

*Falsifier:* an SN representation in which acceptance of some rule instance depends on the instantiating formulas.

**P-D2 (Prop 4 + Prop 6; INFERENCE).** D2 is non-vacuous (no IPC → CPC translation). It excludes every interpreter construction examined, including the schema-level ones.

*Falsifier:* a D2 representation (T1–T5) of a finitely schematic calculus that encodes a universal checker. For example, one whose core A is fixed and whose translated derivations encode certificates of an arbitrary Cook–Reckhow system.

**C1 (Collapse; CONJECTURE).** Every SN ∧ HN ∧ ADQ2 representation in LF of a pure ND calculus with intuitionistic hypotheses is a judgments-as-types encoding, up to:
- ≡_LF;
- definitional re-factoring;
- renaming.

Gardner Thms 6.4.4 / 6.5.7 characterise a given encoding: adequate (resp. natural) iff the induced indexed functor is an indexed isomorphism. They do *not* classify all encodings [bnd].

**C2 (Permutation-only reflection; CONJECTURE, for Task 003).** See §9.5.

**C3 (Joint fullness; OPEN).** Is there a finite core A, with one fixed ≡_A, admitting D2 + FULL translations of:
- an intuitionistic calculus (NJ with βη);
- a classical calculus with a declared identity (cbn λμ with Selinger's Table 6 theory, or LK with a chosen identity);
- a linear calculus (ILL)?

### 10.2 Decision-gate check (`docs/STAGE_0_SYNTHESIS.md`)

| Requirement | Status |
|---|---|
| (i) Exact quantified conjecture, with the source class fixed independently | **Partly.** The class is finitely schematic calculi (§2.1). C3 is stated over a named benchmark. |
| (ii) Anti-vacuity test that excludes a real interpreter without excluding legitimate structural encodings by fiat | **Partly.** SN excludes the instance-level interpreters. T1–T4 exclude all constructions found, and T1 is the standard notion of translation. But T1 deliberately excludes LF and deep embeddings *as cores* (they remain D1 media), which a reviewer may regard as fiat. HN is optional and over-excludes deep embeddings (L-i). |
| (iii) Testable fidelity specification | **Met** at derivability and derivation level (ADQ1, ADQ2). FULL is specified; its identity relation belongs to Task 003. |
| (iv) Trust and equality boundaries | **Met descriptively** (ledger), with one definitional test (logical items). |
| (v) A concrete unsolved lemma or a checked counterexample | **Partly.** C3 is a concrete open question. LSR Conj 8.5 is a published open lemma, but it is theirs. No counterexample has been independently checked. |

### 10.3 Recommendation: NARROW

- **Do not PROCEED.**
  - At R1–R2, a finite cross-foundation core is prior art: Prop 7, assembled from Kolmogorov, Girard and Pruiksma, pending checking.
  - Universal *framework* representation is trivial (Prop 5).
  - Nothing here warrants building anything.
- **Do not STOP.**
  - The definitional question now has a defensible answer: D2 for fundamentality, D1 with a ledger for representation.
  - The proof-level question C3 is precise, open as far as found, and bears directly on whether a finite core is fundamental for *proofs*, which is the charter's distinctive ambition.
- **Narrow the program to:**
  1. adopting D1 (representation) and D2 (fundamentality) as the working definitions, together with the descriptive ledger;
  2. retiring "a finite framework representing all systems" as a research target (Prop 5);
  3. the single test below.

**Coordination.** C3 involves proof identity. It should be run jointly with, or after, Task 003's fixing of identity relations.

### 10.4 Single next test (literature and pen-and-paper; no implementation)

> **Take ILL with ! as the core, using its standard βη-equality for DILL. Hasegawa 2000, Thm 5.6, makes Girard's translation of STLC into linear λ fully complete (VERIFIED [R]). Determine whether some D2 translation of a classical calculus with a declared identity into the same core is FULL.**

**Candidates:**
- linear CPS: full for the *computational* λ-calculus (Hasegawa 2002, Thm 1, VERIFIED [R]). Its extension to λμ is unchecked (Berdine–O'Hearn–Reddy–Thielecke, UNVERIFIED);
- the Kolmogorov translation composed with Girard's.

| Outcome | Meaning |
|---|---|
| **(a) A full translation exists** | ILL + ! is a finite core fundamental *for proofs* of one intuitionistic, one classical and one linear calculus. Check whether this is already in the literature. If it is, the charter's core aim at R3 is prior art for this benchmark. |
| **(b) A proof that no D2 translation of the chosen classical calculus into ILL + ! is full** (for example, an ILL derivation of a translated sequent outside every image class) | A genuine obstruction to proof-level fundamentality with a fixed core. It would be the first one found. |
| **(c) Neither** | Record the exact missing lemma: the full-completeness step for the classical component. |

---

## 11. Limitations

1. **The results in §3 are informal.**
   - Prop 4 relies on Rieger–Nishimura (UNVERIFIED-MEMORY).
   - Prop 5's ADQ2 is unverified.
   - Prop 7 is an *assembly* of cited results, with a stable-sort repair that has not been checked.
2. **D2's T1 is a deliberate design choice.** Its acceptability (gate (ii)) needs review by a human proof theorist.
3. **The trust ledger is descriptive.** An item-wise role classification was found to be ill-defined (§2.2).
4. **The resource control relies on *expected* LLF adequacy for MILL.** No MILL adequacy theorem was extracted.
5. **Yamada's results are restricted and not schematic** (§6.3). Girard's LU, which Yamada cites as prior art, was not accessed.
6. **Independence.** The author also wrote PR #2. A fresh-context critique was used, but outside review is still required.
7. **Scope.** Proof identity, causal order and the MLL net example belong to Task 003.

---

## 12. Withdrawn or corrected claims from the first draft (transparency)

| # | Draft claim | Status now | Why |
|---|---|---|---|
| W1 | "SN ∧ HN ⇒ HOM" | **Withdrawn**; replaced by SN at derivation metavariables (Lemma 1) | Weak-normal-form counterexample (critique §A1) |
| W2 | "No per-instance computation" | **Corrected**: invariance under formula instantiation, not cost (Lemma 2) | Critique §A3 |
| W3 | "SN excludes every interpreter, including checker-as-proof" | **Withdrawn**; SN excludes only instance-inspecting interpreters | B1, B2 |
| W4 | "Loophole L-a is isomorphic to the LF image (benign)" | **Withdrawn** | Certificates live in another calculus (critique §B2) |
| W5 | D2 = "no role-(c) items" | **Replaced** by T1–T5, with a syntactic logical-item test | B1 makes the old D2 vacuous; role classification is ill-defined (critique §B1, §D1) |
| W6 | Recommendation "adopt SN + ADQ1 + ledger" | **Replaced** by D1/D2 | It dropped HN, the clause doing the excluding (critique §B4) |
| W7 | "Yamada: LK, LJ, ILL translate connective-wise and conservatively" | **Corrected** | Restricted, non-schematic purity condition; Cor 3.18's target lacks cut elimination (critique §E1, confirmed) |
| W8 | §0 use of KKNS, Buszkowski and CSZ as "the environment becomes a universal rewriting layer" | **Corrected** | Logic-level undecidability; role (b); infinite base and identity-level (critique §E2–E4) |
| W9 | Conversion-based foundations as an SN over-exclusion | **Corrected** | They are outside the source class (critique §A4.2) |
| W10 | Next test "LK in adjoint logic, possibly with multiple conclusions" | **Replaced** by the fullness test | The original test was ill-posed; outcome (a) could be manufactured; the cheaper Kolmogorov route answers it at R1 (critique §F) |
| W11 | Cook–Reckhow applied to connective bases | **Corrected** (§7.2) | Critique §E5 |

---

## 13. Source table (edition and location)

Statuses: **V** = VERIFIED_SOURCE in the version stated; **S** = SECONDARY_ONLY; **N** = NOT_ACCESSED. Notes: own, str, bnd, gfu, fresh-critique (this task); [S0] = PR #2 Stage-0 logs; [R] = PR #2 review logs.

### Logical frameworks, adequacy and derived rules

| Source | Version | Location used | Status |
|---|---|---|---|
| Harper, Honsell, Plotkin (JACM 1993) | Author typescript | p. 2; p. 17; p. 23; Thm 2.6; Thm 4.1 p. 21 | V [S0, bnd] |
| Pfenning, "Logical Frameworks" (Handbook of Automated Reasoning) | Preprint | Thm 3.2 p. 29; §3.6; p. 47; p. 70 | V [S0, bnd] |
| Gardner, PhD thesis (1992) | OCR | Def 5.2.1/5.2.3; Cor 5.1.8; Def 6.1.3; Thms 6.4.4, 6.5.7 | V [bnd] |
| Harper, *Practical Foundations for Programming Languages* | Ch. 3 | Thm 3.1 | V [bnd] |
| UvA lecture handout on admissible rules | — | Prop 8, Thm 9 (Kreisel–Putnam) | S [bnd] |
| Twelf User's Guide 1.4 | — | §9 | V [bnd] |
| Cervesato, Pfenning, LLF | Author manuscript | Thm 2.9; p. 53 | V [S0] |
| Chihani, Miller, Renaud (JAR 2017) | — | p. 13 | V [S0] |
| Dedukti manuscript | arXiv:2311.07185 | Lemma 4; Thm 8; §3.1 | V [S0] |

### Syntax with binding

| Source | Version | Location used | Status |
|---|---|---|---|
| Fiore, Plotkin, Turi (LICS 1999) | — | Thms 2.1, 4.1, 4.2 | V [bnd] |
| Fiore, Mahmoud | arXiv:1308.5409 | Lemma 5.1 | V [bnd, own] |

### Translations between logics and invariant comparison

| Source | Version | Location used | Status |
|---|---|---|---|
| Jeřábek, "The ubiquity of conservative translations" | arXiv:1108.6263v2 | Defs 2.2–2.3; Thm 2.4; Def 3.4; Thm 3.6; p. 14 | V [str, own] |
| Pelletier, Urquhart (+ 2006 correction) | Preprints | Translation definition pp. 6–7; Thm 2.6; Cor 3.2; Thm 4.5 | V [str] |
| Caleiro, Gonçalves | — | Def 2.4; p. 7; Def 4.1; Prop 4.3 | V [str] |
| Böhler, Creignou, Reith, Vollmer | — | Ex 1.3 | V [str] |
| SEP, "Algebraic Propositional Logic" (Jansana) | — | Łoś–Suszko | S [str] |
| Mossakowski, Diaconescu, Tarlecki | Preprint | Ex 2.4 (Kolmogorov); Prop 2.25; §2.1; conclusion | V [S0, own] |
| Rabe, "How to identify, translate and combine logics?" | Preprint | Def 3.35 | V [S0] |
| Cook, Reckhow (JSL 1979) | — | Thm 2.3; Cor 2.4; Lemma 2.5 | V [S0] |
| Girard, "Linear logic" (TCS 1987) | Scan | §5.1, p. 81 | V [S0] |

### Interpreter constructions and Dedukti encodings

| Source | Version | Location used | Status |
|---|---|---|---|
| Clavel, Meseguer (ENTCS 4, 1996) | — | Thm 3.2 | V [S0] |
| Felicissimo (FSCD 2022) | — | Thm 46 | V [S0] |
| Felicissimo, Winterhalter (FSCD 2024) | — | Table 1 | V [S0] |
| Krajíček, *Proof Complexity* (2019) | — | Thm 8.4.3 | S [S0] |
| Blanqui et al., "Some axioms for mathematics" (FSCD 2021) | — | Thm 9; §4 | V [S0] |

### Proof identity and fullness

| Source | Version | Location used | Status |
|---|---|---|---|
| Hasegawa (JFP 2000) | Preprint | Thm 5.6 | V [R] |
| Hasegawa (FLOPS 2002) | — | Prop 5; Thm 1; §1.3 | V [R] |
| Selinger (MSCS 2001) | — | Table 6; Thm 6.12; Rem 8.2 | V [R] |

### Generic frameworks and structural data

| Source | Version | Location used | Status |
|---|---|---|---|
| Licata, Shulman, Riley (FSCD 2017) + extended version | — | Thm 2.1; §4; p. 25:17; Conj 8.5 | V [R, gfu] |
| Shulman (LMCS 2023) | — | Remark 2.7; cut-elimination remark | V [R] |
| Shulman, MATT (MFPS 2023) | — | Remark 2.6; question (iv) | V [gfu, own] |
| Pruiksma, thesis CMU-CS-24-103 | — | σ(m) ⊆ {W, C}; Example 4 (judgmental S4); limitations | V [gfu, own] |
| Clarke, Scherer, Zeilberger | arXiv:2511.07314v3 | Thms 1.17, 3.27, 3.28 | V [gfu, own] |
| Kanovich, Kuznetsov, Nigam, Scedrov | arXiv:1709.03607 | Thms 8, 15 | V [gfu, own] |
| Kanovich, Kuznetsov, Scedrov | arXiv:1608.02254 | Thms 9–10, restating Buszkowski | V; Buszkowski S [gfu] |
| Miller, Pimentel (TCS 2013) | — | Defs 3, 4; Thms 6, 22 | V [S0, gfu] |
| Marin, Miller, Pimentel, Volpe (APAL 2022) | — | Thms 12, 13, 16, 17 | V [gfu] |

### Other sources

| Source | Version | Location used | Status |
|---|---|---|---|
| Yamada, "Sequent calculi for a unity of logic" | arXiv:2001.06138v3 (preprint) | Cor 3.18; Thm 3.26; Cor 3.37; p. ~3 | V [own, fresh-critique] |
| Holliday, Hoshi, Icard (LORI-III 2011) | Author copy | §§1.1–1.2 | V [own] |

### Not accessed (N)

Girard, LU; Laurent–Regnier; Buszkowski 1982; Chvalovský–Horčík; Zolin; Sheffer; Post; Łoś–Suszko; Prawitz–Malmnäs; Berdine–O'Hearn–Reddy–Thielecke; Hofmann–Streicher.
