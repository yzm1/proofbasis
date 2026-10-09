# Cross-review B: operational fundamentality

**Assignment:** Task 008 Cross-Review B — Codex. **Date:** 2026-10-09.

**Research baseline:** main at `9c8776231cf97f4da35e7c201516f9be3607a198`.
**Reviewed:** [PR #13](https://github.com/yzm1/proofbasis/pull/13), including its source notes and fresh critique, at `b16f4330b1812097a0b1a83fadf84c51118278a9`; [PR #14](https://github.com/yzm1/proofbasis/pull/14), including its internal self-critique, at `e4855a82b3c6fcd58aa16a3a69b8bb75bcb9f50a`. Neither PR had a mathematical review in GitHub's comments/reviews when inspected; both had an automated review-limit notification. The substantive critique of #13 is its checked-in `fresh-critique.md`.

Read AGENTS.md, the charter, definitions, falsification criteria, protocol, prior-art record, reconciliation, Task 008, and the preceding reports, especially 002, 005, 006, 007. No charter, conjecture, assignment, or earlier report is changed here. This is a definition audit, not a universal existence attempt.

**Statuses:** ESTABLISHED means a result verified against the primary text identified in §10. INFORMAL ARGUMENT means an independently reproduced mathematical argument, not machine-checked or refereed. OPEN identifies a remaining obligation. CHOICE identifies a proposed restriction, not a theorem.

## 1. Executive verdict

**DEFINITION UNRESOLVED.** The repaired #13 correctly withdraws its first draft's universal claims. Its fixed-interface condition excludes the particular reader and state wrappers used against that draft. It does not establish that interpreted rule tables cannot relocate into translated source types. Section 3 gives an actual finite-group table interpretation with fixed identity interfaces, a pure logical target, native substitution, derivability reflection and faithful proof equality, conditional on retaining hypothetical environment premises as explained there. It satisfies the stated genericity restrictions through the unconstrained constant-atom clause. It is not a universal group or universal checker construction.

The most immediate problem with **I** is independent of non-vacuity: its displayed environment translation discards the antecedent of a hypothetical assumption. On its literal reading this breaks I2, even for ordinary propositional natural deduction. Its nonidentity atom-substitution clause also requires an actual substitution operation that is not specified. These are fixable interface defects, not impossibility results.

**N_log** captures a meaningful discipline for a *chosen logical presentation*, but fails invariance under adding a derived generator with its defining equation. **N_gen** contains a meaningful generic-variable requirement alongside restrictions on how to write types. Neither finite menus nor the exclusion of type computation follows from faithful representation. The proposed harmonious propositional class has an independent proof-theoretic motivation, but is not yet a formally delimited class and relinquishes substantial parts of the original scope. Local β/η witnesses alone admit arbitrary definitional packaging (§4).

**Decision: UNRESOLVED.** Keep the original cross-foundation objective unresolved. Harmonious propositional calculi are defensible as a separately labelled diagnostic class, not an approved replacement for it. A generation-sensitive criterion is worth testing, but needs specified marks and admissible presentation changes; the word “operational” supplies neither.

## 2. Exact definitions under review

Report 008 proposes

\[
  \exists(A,\mathcal M_A)\ \forall S\in C_{\rm harm}^{\rm prop}\
  \exists F_S:\ I(A,F_S)\land N_{\rm gen}(A,F_S),
  \qquad N_{\rm log}(A).
\]

The finite target calculus and finite menu are fixed before S; translation synthesis need not be uniform. The menu contains atom contexts α, strong-monad wrappers W, and context disciplines. Schematic variables map to α(X_p); constant atoms may map to arbitrary closed target types. Connectives map componentwise to type contexts, rules to derived closed templates, and contexts componentwise without extra hypotheses. I demands preservation, inhabitation reflection, equality preservation **and** reflection, composition, permitted substitution, and effectiveness. It does not demand fullness.

N_log permits only introduction/elimination constants and their local β/η and positive commuting equations; inductive formers with β only are expressly allowed. N_gen requires generic atom images, no term subexpressions or foreign variables in connective images, no target type-level computation, and closed templates. N** is their conjunction with the fixed-interface condition. The source class permits only harmonious connective rules, identity/cut, a specified structural menu, local proof equations, and provenance-tagged environments. Classical membership is unresolved; first-order sources are outside the current class.

These are the definitions tested below. The broad reconciliation H0/H1 is kept distinct from this proposed restricted H1. A counterexample outside the restricted class does not refute its existential quantifier. A failed encoding does not refute all permitted representations.

## 3. An actual table interpretation passing fixed interfaces

### 3.1 Source and target

**INFORMAL ARGUMENT.** For any finite group G, take a source S_G with schematic formula variables p and one constant atom Q. Its contexts are unrestricted. Besides hypotheses and ordinary substitution, it has a closed proof `u : Q` and a unary operation r_g on Q for each g∈G. Its proof equations are exactly

\[
 r_e(d)=d,\qquad r_g(r_h(d))=r_{gh}(d).
\]

There are finitely many operations and equations. A normal Q-proof is a group element acting on a head: u, a hypothesis, a proof hole, or an application of a named hypothetical assumption. Other atomic proofs have hypothesis/assumption heads. This follows by combining consecutive r's; there are no other equations. In particular, a fresh p has no closed proof in the empty environment. This source differs deliberately from the earlier uninhabited one-atom group calculus: **u is present**.

Fix once and for all a target A: the simply typed λ-calculus with arrows, products, sums, unit and natural numbers with primitive recursors. Equality has the logical β/η and commuting laws, with β only for Nat, as expressly permitted by N_log. No universes, dependent types, source constants, or added equations occur. Choose the singleton interface menu α(X)=X, W=id, unrestricted contexts.

Let B_G be the sum of |G| copies of unit, and put

\[
 D_G=B_G\times\mathsf{Nat},\qquad F(Q)=D_G,\qquad F(p)=X_p.
\]

Map u to `(e,0)`. Define a pure logical term

\[
 \pi_g:D_G\longrightarrow D_G,\qquad (h,n)\longmapsto(gh,n)
\]

by sum elimination and product introduction, and set F(r_g(d))=π_g(F(d)). This is literally a case program for the multiplication table. Its branches and the closed type B_G depend on G; **the core and interface menu do not**. Every rule template is derived. No translated proof is decoded into data and no checker is imported through an axiom. Nevertheless the rule-table interpretation has moved into a constant image and case templates.

### 3.2 Checks, including environments and holes

Use the context-preserving environment reading required in §5.1: an assumption `v:(A₁,…,A_k ⊢ B)` is interpreted by a parameter of curried type `F(A₁)→…→F(A_k)→F(B)`, applied to translated arguments. This is not a new trusted source rule: it is precisely the given conditional assumption. δ-definitions are expanded. Without this reading, I already fails the elementary test in §5.1.

* **I1 and equality preservation:** unit/sum/product reductions prove π_e=id and π_gπ_h=π_gh. Hypotheses and assumption applications translate natively.
* **I2, for arbitrary environments:** Q is already source-derivable. For any generic atom p not derivable under E and Γ, interpret X_p as empty. Interpret each other X_q as a singleton exactly when q is derivable under E and Γ, otherwise as empty. Interpret D_G as G×ℕ. Each environment assumption has a set-function interpretation: if all its premises have nonempty interpretations, its conclusion is source-derivable, hence nonempty; otherwise its domain is empty. Every Γ-hypothesis is inhabited in this valuation. A target term of the allegedly underivable X_p is impossible in this sound set model. Preservation gives the converse. This argument applies to finite or countable r.e. E, not just E=∅.
* **I3, equality reflection:** form the free source term algebra under E and the chosen proof holes, adding countably many formal generators at each atomic sort **for the separating model only**. They are not translated assumptions. Its Q-sort is a countably infinite free G-set: each Q-head generates a free G-orbit, and the displayed equations identify only the group prefix. Choose a G-equivariant bijection of this sort with G×ℕ. Interpret generic X_p by its free term-algebra sort and each environment/hole symbol by the corresponding constructor function, transported across this bijection. All target logical equations, including Nat's recursor β-laws, are sound in Set. Translated unequal normal source terms have unequal denotations. Consequently target equality cannot identify them. The same construction handles hypothetical holes by their argument-taking constructor operations. Definitions with certificates are expanded rather than given extra equations. Preservation and reflection therefore apply to open proof terms as well as closed words.
* **I4/I5:** α=W=id. Grafting, hypothesis substitution, and formula substitution are ordinary target substitution. The translation is defined recursively by fixed term templates; substituting p by Q simply substitutes D_G for X_p. There is no binding beyond the native abstraction used to interpret hypothetical parameters.
* **I6:** all types, branches and templates are effectively computable from a finite multiplication table.

The ℕ factor matters. A finite carrier by itself would require a new faithfulness argument for arbitrary hypothetical endomorphisms, whose free iterates need not have a faithful finite interpretation. The infinite free-G-set model avoids that gap. It is a separation argument using an established mathematical model, not a formal verification.

N_log holds by the allowed target presentation. N_gen holds: generic variables stay fresh; Q's image is closed; there are no term expressions in types or type computations; templates are closed. Thus the construction passes N** with fixed identity interfaces. The I checks above are conditional on the explicitly stated premise-retaining environment reading; they are not a claim that the defective literal environment display already works.

### 3.3 What this defeats—and what it does not

It defeats a general inference that fixed wrappers prevent per-source state/table interpretations. In report 008 §6.1 A9, “templates can thread only state that a fixed W provides” is false once state is source-type content. It also supplies a concrete version of constant-atom acceptance, rather than assuming Church encodings are automatically faithful.

It does **not** give a checker for arbitrary calculi, host a universal finitely presented group, or refute restricted H1: S_G has nonlogical operations/equations and is not in C_harm. Report 008 explicitly intends some constant-atom table interpretations to pass. The issue is therefore an unresolved boundary: under the original broad objective, passing N** does not establish operational fundamentality; under “logical schemata only,” this example can be accepted deliberately. Calling it a theory rather than a logic records that choice but does not prove the full objective non-vacuous.

**OPEN:** an arbitrary source proof checker satisfying all of I and N** on C_harm has not been constructed here. Nor has its exclusion been established. The opaque checker in #14 preserves its selected proof-class interface, but its coded atom judgments do not satisfy #13's generic-variable condition. Moving that checker into a pure dependent-free target while retaining generic substitution is an additional obligation, not a cosmetic renaming.

## 4. State inside connectives and the meaning of harmony

**INFORMAL ARGUMENT.** Start with propositional STLC and a fixed closed finite data type D. Extend its syntax by a unary connective M_D and rules

\[
 \mathsf{roll}:(D\to D\times A)\to M_D A,\qquad
 \mathsf{unroll}:M_D A\to(D\to D\times A),
\]

with `unroll(roll t)=t` and `roll(unroll m)=m`. Erase M_D A to D→D×F(A), and roll/unroll to identity. The equations give local reduction and reconstruction. Conversely, recursively insert roll/unroll coercions at every translated type, extending them through arrows/products/sums. The composites are identities modulo the displayed equations and the ordinary logical laws. This is a conservative definitional extension with inverse maps on typed proof classes; binding, substitution and derivability are preserved and reflected. It needs no per-source wrapper or hidden hypothesis. The connective image contains state and satisfies N_gen.

This is **not** an arbitrary checker counterexample. It shows why “no auxiliary state” is not a structural invariant: ordinary logical definitions can describe state functions. It also tests the proposed harmony definition. Under the bare local β/η reading of h2 this extension qualifies. Under Pfenning–Davies' stronger meaning explanation, introduction/elimination rules should rely on judgmental concepts, not other connectives ([P], pp. 4–5). Our displayed rules are not primitive rules in that stricter sense; they are a notational/definitional extension. Report 008 has not specified which sense determines membership.

More generally, the same roll/unroll construction works for **any** well-formed nonrecursive type context K(A). Local invertibility alone cannot make the chosen K a fundamental connective. This is a concrete reason O3 must be resolved before claiming a well-formed class. Conversely, forbidding all such derived connectives would make membership depend on whether a definition is expanded or named.

The suggested “linear in its holes” repair has a second cost. The legitimate derived connective K(A)=A×A repeats its argument. Product introduction/projection supply its meaning; banning the translation solely because A occurs twice measures textual occurrence, not whether source contraction has been respected. In a linear calculus a corresponding A⊗A definition demands two resources through its introduction rule; it still repeats a formula hole. Type-hole multiplicity and proof-hole use must be distinguished. This rejects a particular definitional representation, not every possible representation of that source.

## 5. Faithful interface I: necessary clarifications

### 5.1 Hypothetical assumptions lose their premises as written

Report 008 §3.1 permits `u:(Γ_u ⊢ J_u)`, but §3.3 writes `F(E)={u:W[F(J_u)]}`. Consider ordinary natural deduction with E consisting of `u:(p⊢q)`, and no other assumptions. Applying u requires a proof of p; closed q is not derivable. For example, p=q=false is a sound valuation of the conditional assumption. With identity interfaces, the displayed target environment instead contains a closed `u:X_q`, so target q is inhabited. I2 fails.

This is a literal-definition counterexample, not a claim that the intended interpretation of hypothetical assumptions is inconsistent. Minimal repair: retain Γ_u as a contextual parameter or abstract over its assumptions in the correct resource zones. With W≠id, specify the corresponding value/computation type rather than dropping Γ_u. Restricting E to closed assumptions also repairs the display, but sacrifices hypothetical mathematical lemmas and changes the specified source interface.

### 5.2 Formula substitution through α is not automatically type substitution

I5 says replace the subexpression α(X_p) by F(θ). A proof template may use X_p internally, so replacing a compound type subexpression does not define its action on terms. For example α(X)=¬¬X is allowed. If a disjunction maps to ordinary sum, F(q∨r)=¬¬X_q+¬¬X_r is not syntactically α(T) for any T: its outer constructor is sum, not arrow. There is no ordinary substitution for X_p producing that type from α(X_p).

This example diagnoses the missing operation; it is not claimed to satisfy the other I obligations. Minimal repair: require an actual capture-avoiding lift of each source formula substitution to the target type/context theory, together with coherent coercions if substitution is only up to isomorphism. Alternatively require all formula images to factor through α with a specified factorization. The latter sacrifices some admissible componentwise connective choices. Native substitution with α=id is already well-defined.

### 5.3 Kleisli composition needs the relevant sorts

A strong monad supplies composition for `A→WB`, not arbitrary replacement of a context-bound proof hole by a wrapped computation. Formula variables, hypothesis values and derivation holes are different sorts. A call-by-value source additionally distinguishes values from computations. Writing “Kleisli” does not by itself define those sorts, discharge operations, or the substitution action on open templates. Report 008's restriction to permitted value substitutions is an improvement, but a formal interface must state the value/computation judgments and laws before asserting I4/I5 for every source.

There is no incompatibility between equality faithfulness and derivability reflection in general: [H] gives both, and more (§8). The problem is not demanding too much in principle, but leaving the maps insufficiently typed.

### 5.4 Resource and causal obligations

I2 checks which judgments are inhabited; I3 checks a congruence on proof terms. Neither by itself names the use of each hypothesis occurrence or independence/conflict between events. For resource-sensitive sources, require the context action and rule templates to be typed in a specified resource discipline; do not infer proof-level linearity from formula-hole multiplicity. Report 008 already records this gap as O8.

Commuting conversions can identify two orders of independent inferences. β-reduction may also erase an unused argument or duplicate it after substitution. Thus raw event sets are not invariants of all βη proof classes. Reconciliation D5 is appropriate: choose an event semantics and congruence-compatible residual/causal relation separately. N** currently proves no preservation of partial orders, conflicts, cyclic trace conditions, or global proof validity. This is an explicit scope limit, not a mathematical impossibility claim.

## 6. Presentation invariance: a decisive elementary test

**INFORMAL ARGUMENT.** Let A₀ be pure STLC with its ordinary βη presentation. Let A₊ add a schematic generator

\[
 k_{A,B}:A\to B\to A,\qquad
 k_{A,B}=\lambda x^A.\lambda y^B.x.
\]

Inclusion A₀→A₊ and expansion A₊→A₀ preserve all types, contexts, binding and substitution. Expansion after inclusion is identity. Inclusion after expansion is identity on proof classes by the defining equation. The two presentations therefore have exactly the same derived operations and proof equalities. No unverified operation is added.

Nevertheless A₀ passes literal N_log and A₊ fails: k is not an introduction/elimination form of a type former, and its defining equation is an extra δ-equation. Declaring k merely an abbreviation avoids the failure precisely by making a presentation policy. Likewise, adding a derived rule to a source can violate literal h1 without changing its mathematical proof theory.

Report 008 admits that N_log is presentation-level; this counterexample quantifies the cost. It does **not** refute its existential H1: A₀ remains an eligible presentation. It does prevent N_log from being advertised as an invariant of mathematical proof construction, or from assigning a stable verdict to encodings under conservative changes in primitive generators.

In clone language, for an ordinary one-sorted theory let C(n) be the n-input terms modulo equations, with projections and substitution. For the typed example use profiles `C(A₁,…,A_n;B)` instead. The k-extension induces an isomorphism on every such profile, preserving projections and composition; type formation is also unchanged. In the ordinary case the associated Lawvere theory has arrows n→m given by m-tuples of operations. The corresponding sorted operation theory of our example is unchanged. Any predicate depending only on this operation theory must give the same verdict to A₀ and A₊. This is a conditional invariant argument, not a no-go theorem for predicates inspecting more target structure.

For binding, [F] supplies the established analogue: Lemma 5.1 proves syntactic translations commute with substitution and metasubstitution; Lemma 5.2 proves equational derivability preservation; Theorem 5.2 identifies the categories of second-order equational presentations and second-order algebraic theories up to equivalence. The theorem does **not** assert that every translation reflects equations, preserves linear use, or excludes interpreters. Its setting handles binding and parameterized metavariables, not automatically all dependent/resource-sensitive proof interfaces. Typed/contextual versions must retain those structures rather than apply ordinary cartesian clones blindly.

Minimal repair: test N_log after explicitly permitted expansion of conservative definitions, or require a *witness* of a pure presentation. This sacrifices literal presentation-level rejection: disguised encodings may have the same witness. A stronger marked operational criterion requires additional, independently justified data (§9).

## 7. Which restrictions are mathematically justified?

| Restriction | Formal reason or counterexample | Assessment and minimum unresolved decision |
|---|---|---|
| Fixed trusted core; provenance-preserving environment | Conditional assumptions must remain conditional (§5.1); source rule templates must be derivations, not imported declarations | Essential to the agreed trust claim. Provenance must specify obligations, not just tags |
| Equality preservation **and reflection** | [H] verifies coexistence; [T] shows preservation can fail in a familiar encoding | Essential once source proof identity is selected; not automatic from equal conclusions |
| Native composition, binding and substitution | Clone/second-order theory morphisms formalize these operations ([L], [F]) | Essential structural obligations; neither interpreterness nor fullness follows |
| Generic schematic variables | Prevents replacing arbitrary logical variables by fixed data codes; code-based checker and rule-table tests fail this condition | Independently meaningful for schematic logics. It is not semantic relational parametricity and leaves constants/connectives unconstrained |
| Finite menu of compound atom interfaces | Fixed finite generators do not imply finitely many derived type contexts: `X⊗n`, for every n, uses only one fixed tensor former | Additional CHOICE. The earlier permutation representations are legitimate derived operations even when this menu rejects that interface. Rejection of that representation is not nonexistence of others |
| No extra hypotheses | Prevents assuming a source inference in a reader context rather than deriving it | Important for the chosen componentwise interface, but verified encodings with explicit discharge need a scoped alternative; no universal prohibition follows |
| No state in connective images; holes occur once | State definitions and A×A/A⊗A definitions (§4) | Presentation filter unless a separate resource semantics justifies it. Currently not part of N**, and not a proven repair |
| Only logical constants and local equations | k-extension (§6) changes verdict without changing operations | Meaningful as a marked proof-theoretic discipline; not an invariant of the unmarked theory |
| No term-dependent types/type-level computation | Predicate substitution and dependent families require operations the literal grammar cannot express | Excludes direct LF/dependent representations, not all representations of their sources. Needs an independently defended scope restriction |
| Nonlogical proof equations excluded from source class | Group/action equations are ordinary mathematical structure; [O] shows universal-property equality can exceed local recursor β | Narrows the objective. “Not logical” is not evidence that the mathematical proof construction is irrelevant |
| Harmony | [P] gives concrete local reduction/reconstruction criteria; arbitrary roll/unroll packaging also meets a weak version | Independent motivation, but O3 unresolved. Specify primitive vs derived formers and closure under definitional extensions |

Two exclusions merit separate detail.

**Type computation.** In a dependent representation, an atomic predicate P(t) maps to a type-family application X_P(t). Substituting P:=λz.ψ(z) requires family substitution and β at that level. N_gen prohibits term subexpressions in types, so the direct representation fails. Ordinary equality types and indexed mathematical objects fail for the same syntactic reason. This removes established representations from eligibility, not necessarily their mathematical foundations from every possible source translation. Defunctionalizing syntax introduces new obligations for native substitution and equality; no impossibility follows here. Conversely, System F's term equation `(ΛX.t)[T]=t[T/X]` must not be confused with β between type expressions: banning the latter does not automatically ban System F. Report 008's first-order/universe questions remain substantive open scope decisions.

**Local equations and normalization.** Local soundness is a reduction of an introduction immediately followed by elimination; local completeness reconstructs an introduced form. Neither definition alone is a theorem of global normalization, confluence or equality decidability. [O], Theorem 3.10, establishes undecidability for typed λ-calculus with Nat recursors and their universally quantified uniqueness rule; §5.2 gives the corresponding undecidable coherence problem for cartesian closed categories with strong natural numbers objects. This is not a theorem about C_harm as currently undefined. It shows that even a mathematically natural universal-property requirement can introduce equality beyond the chosen local β-only Nat laws. Admitting Nat with β only is a defensible intensional choice, not a complete characterization of arithmetic proof structure.

**Admissibility is weaker than definability.** In a purely atomic calculus with hypotheses but no closed theorems, the fixed rule “from p infer q” is admissible for closed provability: its premise is never provable, even under atomic substitutions. It has no open derived template `x:p ⊢ q`. This elementary vacuous-admissibility example prevents replacing the requirement that source rules be derived by theorem-set conservativity. Conversely, the k-rule is genuinely definable, so rejecting it solely because it was named adds no trust protection. [P]'s discussion following Theorem 6 explicitly uses *derived*, not merely admissible, rules to retain proof structure.

## 8. Established results and the five adversarial controls

**Strongest verified structural result relevant here:** Hasegawa's *Girard translation and logical predicates* [H], §§3–5. Its source is the simply typed arrow λ-calculus with βη; its target is the paper's dual-context linear calculus with `!` and linear arrow and its stated equations. Set

\[
 b^\circ=b,\quad(A\to B)^\circ={!A^\circ}\multimap B^\circ,
\]

and translate abstraction by `λy. let !x be y in M°`, application by `M°(!N°)`. Proposition 3.1 proves typing preservation into `Γ°;∅`; Lemma 3.2 proves literal capture-avoiding substitution compatibility. Propositions 3.3 and 3.4 prove equality preservation and reflection. The latter uses erasure of linearity as a sound inverse. Theorem 5.6 says **every** target term `Γ°;∅ ⊢ M:σ°` equals N° for some typed source N. This supplies reflection and even fullness on precisely those contexts/types. No assertion about all logical foundations follows. Report 008's “Girard-translation I3” uncertainty can be replaced by this verified fragment result, not a general claim about all Girard translations.

There is another directly relevant established result: [P], Theorem 8, gives derivability biconditionals, reduction simulations, and proof-equality biconditionals for its translations of the specified lax λ-calculus terms/expressions into its modal λ-calculus. The separate term/expression judgments are important; it is not a theorem for an unspecified single Kleisli interface. These two results independently justify studying logical translations rather than only computational interpreters.

For impredicative definability, [T] §2 shows Russell–Prawitz images of η- or generalized permutation-equivalent source derivations need not even be βη-equivalent. Its Proposition 4.7 proves preservation of generalized disjunction permutations with ε equations; Proposition 4.9 treats the corresponding source η equation. These are preservation statements, not the equality-reflection theorem needed for I3 over all source proofs.

Moreover, [T] Proposition 4.5 proves that βηε **strictly extends** βη. Its open-term example is the naturality equation

\[
 u[B](f\,a)=f(u[A]a),\qquad
 u:\forall X.(X\to X),\ f:A\to B,\ a:A.
\]

The two terms have distinct βη normal forms. Thus System F with its unchanged arrow/∀ formers and these extra equations fails literal N_log: this is not just uncertainty about whether ε is redundant. A different presentation with additional logical structure is a separate question. Failure of this encoding under plain βη, or its exclusion under N_log after adding ε, does not prove that all encodings fail.

| Required control | Cross-review finding |
|---|---|
| Explicit proof checker | #14 supplies an opaque interface counterexample to weaker structural criteria. It fails #13's generic atom requirement in that encoding. Universal relocation satisfying I and N** is OPEN, not disproved |
| Typed paths/rule tables | Some constant-atom cases are explicitly accepted by #13. Section 3 now supplies a fully specified pure-core table interpretation with arbitrary hypothetical interfaces; no blanket exclusion follows |
| Universal finitely presented groups | Literal group generators/relators fail N_log. That is presentation rejection, not a theorem against every pure representation. Our finite-G construction must not be promoted to the universal-group case |
| Standard LF adequacy | Importing source inference constants is inadequate under the trust condition. The ordinary dependent LF representation also violates the chosen type grammar. Adequacy of LF is not a claim that its target supplies source rules without signatures |
| Genuine linear translations | [H] passes structural equality/substitution tests and gives a sound positive control. Arbitrary exclusion of derived type contexts or multiple administrative steps must be checked against such translations |

None of [L], [F], [H], [P], [T], or [O] proves or refutes the proposed universal quantified statement. Together they settle specific structural questions and locate the missing non-vacuity question.

## 9. Generation-sensitive criteria and the next gate

A possible operational account retains more than the quotient of proof terms: a typed/binding-aware raw term theory, a specified set of generating inference operations, oriented reduction cells, context/resource actions, and **marks** distinguishing formation, introduction, elimination, assumption use, and administrative computation. A translation supplies derived macros and witnesses that their marked actions match the source's. This uses established presentation/translation mathematics rather than inventing an algebra here.

What would it resolve? It could distinguish the chosen generation process of a checker from a native logical rule, even when their selected proof-class interfaces are isomorphic, as in #14. But that distinction comes from the marks and allowed macro expansions, not from isomorphism of unmarked clones. Strict one-step/event preservation rejects honest Girard translation, whose abstraction inserts a `let !`; arbitrary macro expansion may make a checker look native. Adding k, inlining it, or inserting an identity step changes raw histories without changing proof construction. These are concrete opposing tests for any proposed operational predicate.

**OPEN:** no independently justified rule for which marked expansions are allowed is supplied in either PR or proved here. If all markings are chosen after seeing the encoding, the criterion is circular. If only the favored presentation's labels are allowed, it is arbitrary. Harmony or universal-property witnesses offer real evidence, but §4 shows why local invertibility alone is too weak. A process-based definition is a research option, not a solved anti-interpreter theorem.

**Minimal repairs, separately proposed:**

1. Retain hypothetical environment contexts and specify actual atom-substitution lifts. This repairs I's typing/scope and sacrifices no intended conditional reasoning; forbidding hypothetical assumptions instead would sacrifice it.
2. Specify harmony and whether definitional extensions preserve source membership. Closure under expansion avoids the k/roll presentation artifacts but weakens literal rejection by syntactic purity.
3. Specify N's intended treatment of the §3 table construction. Accepting it makes N a filter on schematic logical reasoning only; rejecting it needs an invariant beyond finite menus and must explain why genuine group representations are not excluded arbitrarily.
4. If adopting operational marks, declare admissible conservative expansions before testing encodings. This adds chosen structural data and abandons invariance under arbitrary unmarked presentations; that cost must be explicit.

**Single most valuable next test:** with an explicitly marked operational definition and explicit admissible presentation equivalences, require one stable classification across (i) native group actions, (ii) the pure-core table construction of §3, and (iii) their expansions into introduction/elimination terms—while still accepting the exact Girard translation [H]. Prove the claimed distinction or produce a marked-equivalence counterexample. This finite, pen-and-paper test is cheaper and more decisive for operational non-vacuity than an unrestricted existence attempt. If no independent distinction can be stated, report that failure rather than change the universal source class.

The original objective remains unresolved: there is no theorem here establishing fundamental finite generation across foundations, nor an impossibility theorem against every permitted target. The concrete progress is an informal argument relocating a rule table past the repaired interface filter, two explicit interface/presentation defects, and a precise remaining obligation for an operational invariant. **Decision: UNRESOLVED. Stop at cross-review.**

## 10. Primary-source verification record

The papers below were inspected at the cited statements, not used solely through abstracts. None is a machine-checked verification of this report's arguments. No novelty is claimed.

| Key | Primary publication and retrieved text | Exact use and limitations |
|---|---|---|
| [H] | M. Hasegawa, *Girard translation and logical predicates*, J. Functional Programming 10(1), 77–89 (2000), [DOI](https://doi.org/10.1017/S0956796899003615) | pp. 81–82, Prop. 3.1, Lem. 3.2, Props. 3.3–3.4; p. 86, Thm. 5.6. Specified arrow/linear calculi, not arbitrary foundations. Journal PDF independently recovered in earlier research and re-read here |
| [P] | F. Pfenning and R. Davies, *A judgmental reconstruction of modal logic*, MSCS 11(4), 511–540 (2001), [author preprint](https://www.cs.cmu.edu/~fp/papers/mscs00.pdf) | Preprint pp. 3–5 local soundness/completeness and primitive vs notational meaning; discussion after Thm. 6; pp. 27–28 Thm. 8 and inverse translations. Page numbers refer to the preprint |
| [L] | F. W. Lawvere, *Functorial semantics of algebraic theories*, PNAS 50(5), 869–872 (1963), [primary scan](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/lawvere.pdf) | p. 869 defines theories, operations, presentation correspondence and product-preserving models. Does not establish one finite universal theory with the required faithful embeddings |
| [F] | M. Fiore and O. Mahmoud, *Second-Order Algebraic Theories*, MFCS 2010 extended abstract, [author arXiv version 1308.5409](https://arxiv.org/abs/1308.5409) | §5, Lemmas 5.1–5.2, Thm. 5.2: substitution/metasubstitution, equality preservation, categorical equivalence SOEP/SOAT. Reflection and the desired resource/trust filters are additional requirements |
| [T] | L. Tranchini, P. Pistone and M. Petrolo, *The naturality of natural deduction*, [arXiv:1607.06603v2](https://arxiv.org/abs/1607.06603v2) | §2, p. 7 η/permutation nonpreservation under βη; Prop. 4.5 proves βηε strictly extends βη; §4.2 Props. 4.7 and 4.9 preservation with ε. These propositions do not themselves give universal equality reflection |
| [O] | M. Okada and P. J. Scott, *A note on rewriting theory for uniqueness of iteration*, TAC 6(4), 47–64 (1999), [journal text](https://www.tac.mta.ca/tac/volumes/6/n4/n4.pdf) | §3.8–3.10 states the universally quantified recursor uniqueness rule and proves undecidability; §5.2 interprets coherence for CCCs with strong NNO. This equality is stronger than local Nat β and is not automatically in the proposed C_harm |

The §3 free-algebra separation, §4 conservative extension, §5 scope/substitution counterexamples and §6 k-extension are informal mathematical arguments reproduced for this review. Their limitations are stated where used; no independent-agent agreement is counted as verification.
