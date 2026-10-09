<!-- Fresh-context adversarial critique of the FIRST DRAFT of report 010 (commits 24f27f7/ea3011d). Verbatim except paths. Responses: report 010 §10. -->

# Hostile referee critique of draft report 010 (reports/010-cross-review-algebraic-fundamentality.md)

Labels on my claims: VERIFIED (checked by me this session: by reading the repo, by hand computation, or by running code), INFERENCE (my argument, with any gap named), UNVERIFIED-MEMORY (literature recalled, not re-read).

Files read: AGENTS.md, charter, STAGE_0_7_RECONCILIATION.md, 009 (origin/research/009-adversarial-definitions), 008 (origin/research/008-constructive-definitions), the draft, reports/010-checks/*, and the relevant passages of 005/006/007.
Check script: `scratchpad/t010/p6check.py`. It verifies P6 and the counterexample in M2.

---

## FATAL

### F1. N_amb is not a well-defined predicate, so the verdict table in §5.6 cannot be computed

**Passage:** §5.6 definition; table rows 1′, 1″, 2′; §6.2.

**Argument (INFERENCE; the repo facts are VERIFIED).**

(a) **A is not a category.** In 009 §2.1, A is a finite signature of typed schemas with several sorts and judgments: data, certificates, Hom. "The ambient D_S-structure" therefore needs a chosen category built from A, and the draft never says which one.
- In 009's A_check, data and certificate operations cannot take Hom proofs as inputs (009 §4, "opaque sort"). So no judgment of the form Γ × F(φ) → F(ψ) has Γ a data type and F(φ) a Hom object.
- The 1′ argument ("probes Γ = data types admit code-inspecting maps") therefore tests probes in a category that A does not have.

(b) **Φ(A) is quantified existentially, and the admissible class is left open (Q1).** Q1 itself admits that Φ(A) := an internal term model would make N_amb vacuous. Until Q1 is settled, N_amb is a schema and not a predicate. Under the reconciliation this is the same status as H1, but the draft presents ✔/✘ verdicts as if the predicate were fixed.

(c) **Rows 1′ and 1″ collapse.** For S = NJ(→) with hypothetical holes, I3 (009 §2.2) requires grafting into open holes under binders.
- An opaque Hom sort cannot do that through data projection. 009 removed projection precisely to obtain N_split.
- It therefore needs Hom-level lam/app schemas with βη, uniform in the code. That is case 1″, not 1′.
- If Φ(A) is taken to be the Hom-sort category, F becomes a cartesian closed functor and 1′ turns ✔.
- So the ✘ in 1′ depends on choosing a code-inspecting ambient category that the faithful realization does not even use.

**Fix.** Before giving any verdict:
- define the ambient category Cat(A) for a sorted A;
- fix Φ as a specified list of constructions;
- fix D_S as a function of S (see M3).
Then mark 1′/2′ OPEN rather than ✘.

### F2. N_amb accepts a fixed universal rule-table checker, so it fails the reconciliation's controls by design; "suffice in every case tested", "the form is determined" and "no narrowing" are false

**Passage:** §1.3, §5.5, the §5.6 table (rows 1, 2, 3, 1″), §6.2 and §6.5.

**Argument (INFERENCE).** Combine row 1 (checkers for S_G accepted), row 1″ (an opaque-sort checker with generic ambient currying accepted) and P7 (Σ is "freely interpreted"). Then one fixed A works for every S whose connective doctrine is contained in CCC. A consists of:
- a universal data-level checker for arbitrary rule tables;
- generic code-indexed CCC schemas on the Hom sort.

For each such S, the non-logical rules run as table lookups and the connectives go to the generic structure, so N_amb holds.

For every S ∈ C whose connectives have no universal property (raw-α identity, β without η, Hilbert systems, arbitrary sequent calculi), D_S has no logical part. N_amb is then vacuous and the whole calculus may be checker-interpreted. The draft itself marks LF raw-α ✔ as "vacuous".

The reconciliation (VERIFIED) requires that N "reject explicitly constructed universal proof checker and encoded rule-table examples". It names the typed-path, universal-group and checker controls (a), (b) and (e). N_amb accepts (a), (b) and (e).

009's own gate (009 §9.3, VERIFIED) is: "If they [H,K] lift … any invariant of that enriched diagram still cannot separate these controls." Under N_amb they do lift, because both are accepted. The draft therefore answers 009's gate **negatively** for 009's controls, but presents the result as a positive separation. Calling the controls "ill-posed because they have no logic" re-decides the reconciliation's test protocol (AGENTS.md rule 10), and the draft does this without flagging it as a proposal.

The ledger cannot rescue this. It is not part of N_amb. Checker boxes are also data lookups, not new trusted constants, so they already pass 009 §2.3 provenance.

**Fix.**
- State plainly that N_amb restricts only universal-property connectives. It is not an anti-interpreter filter for rules, and on most of C, H1 under N_amb reduces to H0.
- Present the reinterpretation of controls (a), (b) and (e) as a proposal for human decision.
- Delete "no narrowing" and "form is determined".

---

## MAJOR

### M1. §5.4″ (LF βη) is not a case where "derived holds but ambient fails" among admissible realizations

**Passage:** §5.4″; §1.3(b), last bullet; the table row "4. βη ✘".

**Argument (VERIFIED from 009 §7, plus INFERENCE).**
- Under βη, 009 shows that this encoding does not even induce a map on the β-quotient. It fails I2 and H0 before N_amb is consulted.
- `imp` is a declared Σ_FOL constant (009 §7), not a derived operation of a fixed core. Derivedness in 002-T1/008's sense therefore fails too, unless Σ_FOL is put into the fixed A, which makes A source-specific.
- So the only argument offered for preferring N_amb over derivedness is void.
- The draft's stated "gap" can in fact be closed:
  - With LF canonical forms (HHP, as cited in 009), any g : (true φ → true ψ) → true(imp φ ψ) has a body whose head is a constant, because h-headed terms have type true ψ.
  - So g ∘ f cannot be βη-equal to a variable, and no isomorphism exists (INFERENCE).
  - The real defect is that the example fails I2 anyway.

**Fix.** Withdraw §5.4″ as the motivation for N_amb. Together with the P6 caveat and P6′, the draft currently has **no** example that separates derivedness from ambient preservation inside H0. State that as OPEN.

### M2. P6′: the top hypothesis is shown to be essential; it is automatic under I1; the result is a routine instance of known facts

**Passage:** §5.4′ ("whether a counterexample exists without it was not determined").

**Counterexample (VERIFIED by `p6check.py`).**
- Setup:
  - H = 2;
  - K = H₃ × 2, where H₃ = {0 < m < 1};
  - F(0) = (m, 0) and F(1) = (1, 0);
  - t(x, y) = (x ⇒ y) ∧ ¬¬y.
- F has these properties:
  - it is injective;
  - it is monotone;
  - it preserves meets;
  - t realizes F's implication table.
- Yet F(1 ⇒ 0) = (m, 0), while Fx ⇒ Fy = (m, 1).

**What the proof actually gives without top preservation (INFERENCE, checked on this example).**
- The same proof yields F(x ⇒ y) = (Fx ⇒ Fy) ∧ F(1). This is preservation of the relative implication of ↓F(1).
- Injectivity of F is not used anywhere. VERIFIED by reading the proof: only monotonicity, meets, F(1) = ⊤ and congruence-compatibility of t are used.
- The proof needs t only to be **compatible**, not to be a term.

**Why the hypothesis costs nothing (INFERENCE).** F(1) = ⊤ follows from I1 at the empty context once the empty context goes to ⊤, so it is not an extra assumption.

**Prior art.** UNVERIFIED-MEMORY: Caicedo–Cignoli, "An algebraic approach to intuitionistic connectives" (JSL 2001). Compatible functions on Heyting algebras satisfy (x ⇔ y) ∧ f(x) = (x ⇔ y) ∧ f(y). P6′ is a two-line instance of this, and also of Belnap-style uniqueness of ⇒.

**Fix.**
- Add the counterexample and the relativized formula.
- Relabel P6′ as a routine consequence, with prior art to be checked.
- Note that P6′ undercuts §1.3's preference for N_amb over derivedness.

### M3. Property-likeness fails exactly where most of C lives, and the Kelly–Lack paraphrase is wrong

**Passage:** §3.6 ("every morphism automatically preserves it … Finite products are an example"); §1.3(a); §6.2.

**The paraphrase is false as written (VERIFIED).** An arbitrary functor between categories with finite products does not preserve them; a constant functor at a non-terminal set is an example.

UNVERIFIED-MEMORY on what Kelly–Lack actually say: a lax-morphism structure on a 1-cell is unique when it exists, and "fully property-like" adds that lax morphisms are pseudo. Neither statement says that every functor preserves the structure.

**Substantive problem (INFERENCE).**
- With β but no η, or with raw identity, connectives satisfy at most *weak* universal properties. These are not unique up to isomorphism.
- D_S must then be structure-like, for example S's own second-order theory. "A D_S-structure on Φ(A)" then just means "a model of S in A", and N_amb degenerates into H0.
- So "operations survive P1 by property-likeness" covers only βη-complete fragments.

**Fix.**
- Restate Kelly–Lack from the source.
- Define D_S as a function of S. "The doctrine whose UPs S's connectives satisfy" is not canonical: should it be the maximal one, including accidental limits?
- Classify sources that have weak or no UPs.

### M4. The "preserved / lost" theorem (§1.2, §4.3) is misstated, and Corollary P1′ contains a false claim

**Passage:** P1′, last bullet; §4.3, "What is lost"; §1.2.

**P1′'s irredundant-basis claim (VERIFIED by hand).** "e belongs to some irredundant basis of the clone" is an Aut-invariant element property, of exactly the ∃-form the draft itself endorses.
- It holds for ∧ (basis {∧, ¬}) and for the constant 0 (basis {→, 0}).
- It fails for projections, which are redundant in every basis.
- The Boolean example shows only that membership in a *given* basis is presentation-relative.

**Things listed as "lost" that survive as ∃/min invariants:**
- basis size: rank, i.e. the minimal number of generators;
- irredundancy: whether an irredundant basis exists;
- the 2-cells of the relations: FDT, and the homotopy type of polygraphic resolutions. §1.2 already says "up to homotopy".

**"Preserved only in two forms" (VERIFIED by definition).** "∃ P with X" is itself a property of M up to isomorphism, so the two forms are one.

**Facts checked by hand and correct (VERIFIED):**
- Stone's formulas;
- the irredundancy of {NAND}, {∧, ¬} and {→, ⊥}.

UNVERIFIED-MEMORY but standard: Post's lattice result that all clones on {0,1} are finitely generated, and Janov–Mučnik.

**Fix.** Separate "data of a given presentation" (lost) from "extremal or existential quantities over presentations" (kept), and rewrite the list accordingly.

### M5. §3.7 (rules vs derived operations) is wrong as stated

**Argument (INFERENCE, using 009 §2.4, VERIFIED).**
- **Derivable rules.** Adding a derivable rule is a Tietze move only together with the defining *proof equation* r(x) = its derivation. Without that equation, the new primitive creates new proof classes. 009 §2.4's r versus k·f is exactly this phenomenon.
- **Admissible cut.** Cut added together with cut-elimination equations does not change the hom-sets: every cut proof is equal to a cut-free one. Moreover, in a cut-free calculus the categorical composition *is* the admissible cut. So "the generated proof algebra correctly distinguishes derivable from admissible" is false in general.
- **What the true distinction is.** It is between a schematic term operation (an element of the clone) and an operation defined on the quotient by recursion.

**Fix.** Rewrite §3.7 so that the presence or absence of proof equations is explicit.

### M6. P1/P2 are correct but folklore; there are unstated assumptions; and the scope is overclaimed

**Passage:** §4.2 proof, step 1; §3.8 ("invariance … built in" for binding-aware structures); §4.1; Q4.

**The core argument is sound (VERIFIED by checking the proof):**
- Q is identical whichever side it is built from.
- The T2 moves are valid because θ⁻¹ is a homomorphism.
- g is never removed.
- Finiteness is kept.
- θ is used only to choose the terms t_{x′} and s_x.

**Gaps and overclaims:**
- (i) **Renaming.** Step 1 renames g′ to g and implicitly separates X₀ from X′₀. This requires Φ to be invariant under renaming of generators, which is not a Tietze move and is not stated as a hypothesis.
- (ii) **Sorts are not covered.** T1/T2 add operations and equations, not sorts. Proof systems' relevant re-presentations are *equivalences*: adding a defined formula or atom q with q ≅ p, or compound atom images (009 §2.1). Isomorphism of many-sorted structures across different sort sets is not even defined in the draft. P1 is silent on these moves, and they are exactly the ones that matter for "atomic versus compound interfaces".
- (iii) **Scope contradiction.** §3.8 asserts Tietze invariance "built in" for binding-aware and dependent structures, while Q4 lists it as OPEN. Pick one.
- (iv) **Credit.** P2 is Tietze's theorem in its general form. P1 is its pointed version. Both should be credited to the general Tietze argument and to definitional equivalence / synonymy of theories (UNVERIFIED-MEMORY: de Bouvère 1965, "Synonymous theories"). They should not be labelled as new.

### M7. The "logical versus non-logical" split is a free choice, and that choice narrows the ambition

**Passage:** P7, "Reading"; §6.5.

**Argument (INFERENCE).**
- Classical axioms, modal K or 4, induction, and Hilbert's modus ponens without the deduction theorem at proof level all become "non-logical Σ" whenever D_S is chosen without them. They are then freely interpretable, checkers included.
- P7 is fine as a universal property, but with non-logical generators of compound type it needs computad- or polygraph-style signatures, which the draft does not mention.
- The charter's object is fundamental proof-construction operations across foundations. Saying "non-logical sources are fully covered because N_amb is vacuous" amounts to H0 on those sources. The reconciliation says (VERIFIED) that H0 "may be satisfied by generic encoding techniques. Do not promote its existence to the project's desired theorem."

**Fix.** Call this what it is: a restriction of H1's non-vacuity content to UP-connectives. List it as an owner decision.

### M8. Unbacked ESTABLISHED claims and unlabelled verdicts

**Missing source notes (VERIFIED: `ls reports/` shows no `010-source-notes/`).**
- §3 points to `reports/010-source-notes/sources.md` for all statuses, and that file does not exist.
- Every claim in §3 except Lawvere/TAC is therefore currently unbacked: Squier FP₃, SOK FDT invariance, Kapur–Narendran, Cartmell, Gabriel–Ulmer, Uemura, Fiore–Mahmoud, Lafont–Métayer.
- UNVERIFIED-MEMORY: these attributions look broadly right. Kapur–Narendran is the B₃⁺ / ⟨a,b | aba = bab⟩ example, where adding c = ab gives a finite complete system. Squier 1987 proved left FP₃.

**Row 5 of the table.** "Cartesian closed functor into the co-Kleisli category of !" carries no status label. That this co-Kleisli category is cartesian closed requires additive products or Seely structure in Hasegawa's DILL fragment, and this was not checked (UNVERIFIED-MEMORY).

**P3 step 3.** It mixes "ESTABLISHED, secondary/memory". Report 006 calls the S_n fact "elementary reasoning", and 005 labels it INFERENCE (VERIFIED by grep).

---

## MINOR

1. **P3 is mostly a corollary of 009's lemma, and its statement has errors.**
   - 009's lemma covers any finitely generated target group. V has trivial abelianization, so P3(b) is literally 009's argument with t = 1.
   - "Every odd prime" understates the result: the n-cycle in S_n has no retraction for every n ≥ 3 (for even n, S_n → C_n factors through C_2).
   - In (c), "|G^ab| coprime to p" is meaningless when G^ab is infinite. The correct criterion is that a retraction exists iff the image of the generator is nonzero in G^ab ⊗ ℤ/p.
   - The script's logic is correct. Assigning values to generators and checking consistency over all Cayley edges is equivalent to the existence of a homomorphism. I re-ran it (VERIFIED). But it checks a trivial fact (S_p^ab = C_2).
   - The multi-object structure of B_F does not matter. G restricted to End(T) must be a monoid homomorphism, and extra objects only add constraints (INFERENCE). Mac Lane's End(X^{⊗p}) ≅ S_p is correct (UNVERIFIED-MEMORY; standard).
   - Credit 009 for the method. Note that 009 §9.2's "varying compound interfaces escapes" is refuted only for this one interface.
2. **P4 is 009's own result.** 009 §3 (VERIFIED) already states that N_rep is automatic for every small faithful interface. P4 is not "PROVED HERE" and does not "make it exact".
3. **P5 assumes "full and faithful" means isomorphism.** That also requires F to be injective on objects and its inverse to preserve the structure. Say "isomorphism of structured categories" explicitly.
4. **Misattributions to 009.**
   - 009 already proposed "inspecting the entire target rather than only B_F" (009 §9.2, VERIFIED); credit it in §1.1(3).
   - 009 never claimed its controls concern logical rules. They are the reconciliation's mandated controls.
   - §2.1's scope caveat largely repeats 009 §4's "Scope" paragraph.
5. **Kleisli(Reader_E).** The exponential object is X ⇒ Y (VERIFIED by the hom-set computation, given that A is cartesian closed). Kleisli *arrows* still depend on E, so "cannot alter the logical part" holds only for the structure maps (P7). Note also that Kleisli categories of general strong monads lack the A-products, so "Kleisli categories are admissible" will rarely give a cartesian closed Φ(A).
6. **P7 for pseudo-morphisms.** Free_D(Σ)/E need not be flexible, so "up to equivalence" for pseudo-morphisms out of a quotient is UNVERIFIED. Cite Blackwell–Kelly–Power rather than Kelly–Street.
7. **Row 1″ invokes P1.** That is a non sequitur. The argument actually used is uniqueness of universal properties.
8. **P6 is a standard fact.** An order-embedding of Heyting algebras need not be a Heyting homomorphism. Calling R₂ a "rule-table interpretation" is rhetorical. P6's computations are correct (VERIFIED):
   - m ⇒ 0 = 0 in H₃;
   - a ⇒ 0 = b in B₄;
   - the probe b is right;
   - the chain is isomorphic to the image;
   - the coordinatewise argument showing that the table is not a term operation is right.
9. **Row 3, "rejected for nothing else", is garbled.** Also, "D = groupoids" is property-like only because inverses are unique; say so.
