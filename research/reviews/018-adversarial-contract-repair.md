# S2-R1-B — Adversarial contract repair and falsification strategy

**2026-10-13. Baseline:** `f1ce6b9bcf205b440d109bb82b888fd9acc262d5` on main. **Assignment:** [Task 014](../../tasks/014-s2-contract-repair.md), independent adversarial submission. Candidate definitions below were formulated without reading report 017, Agent A's branch/PR, or communicating with Agent A. Read AGENTS.md and its prerequisite documents, RESEARCH_PLAN.md, CMP-01, integration 016, ALG-01, INST-01, OBS-01, the comparison rubric, and reports 009 and both 010 reviews. Earlier reports are evidence and counterexample leads, not authorities.

**Verdict: PIVOT.** Retain the cross-foundation objective as an open question, but stop treating an unmarked finite representation theorem as sufficient evidence of explanatory fundamentality. A decidable-equality strengthening is refuted under explicit hypotheses. The unrestricted fixed-core claim remains open and vulnerable to interpretation. A doctrine-indexed family can explain differences in resources and equality relative to designated structure; much of its abstract existence content is established prior art. Its scientific contribution would have to be an exact comparison/classification with negative controls, not another free-syntax construction. S3 and implementation should remain blocked.

**Status discipline:** VERIFIED_SOURCE = the identified primary passage was inspected in this investigation; INFERENCE = an informal mathematical argument reproduced here; CONJECTURE = a candidate statement; UNKNOWN = an unmet obligation. No new result is FORMALIZED, independently refereed, or claimed novel. Source verification is of statements and surrounding hypotheses, not a complete audit of their proofs.

## 1. The contract being repaired

### 1.1 Independently specified broad source class

Let `C_fin` consist of marked, finitely presented deductive systems with:

* finite sorted expression and judgment schemas, finite rule schemas, and finite schemas generating a **least typed proof congruence**;
* finite proof/certificate objects with decidable checking, including any side-condition evidence needed for checking; equality of proof classes need not be decidable;
* explicitly specified contexts, hypothesis/derivation-hole ports, typed substitution and partial composition, with finite schema presentations of their laws; binding may be second-order or dependently indexed;
* a designation of structural permissions, source machinery, environmental assumptions, definitions, and equality axioms. A rule's status is part of the input, rather than reconstructed from its type.

**Schema convention (for sources and targets):** a presentation is a finite string describing finitely many sorted constructors, each with a fixed finite list of ordinary or scoped-binding argument positions. A rule/equation schema is a finite typed tree pattern over these constructors and finitely many sorted metavariables; scoped metavariables are applied to explicitly listed bound variables. Rules have finitely many premises, including well-formedness, conversion or side-condition certificate premises where needed. Equations are finite parallel pattern pairs, possibly with finitely many displayed typed equality/certificate premises; their closure is the least equivalence congruence closed under those rules and the declared contexts/substitutions. Variable-length contexts/port lists are generated syntax with finite recursive rules, not infinitely many primitives. There is no unrestricted semantic side condition or arbitrary relation hidden in the word “schema.” A computable side condition must have its checking/evidence mechanism explicitly included in the presentation. For dependent typing that relies on conversion, a finite checked conversion witness may be part of the raw certificate; identity of its proof classes can still be undecidable. “Finite” counts this machinery too. A purported source not meeting this grammar/certificate convention is a boundary extension, not silently covered.

This definition uses syntactic specifications and their generated congruences, independently of any proposed target. It is not “systems representable in K.” No semantic soundness in a single preferred foundation is presumed: validity is relative to each system's designated assumptions and rules. Adequate syntactic representation does not certify those assumptions. Environments are finite scoped lists of object declarations, hypothetical assumptions and transparent definitions. A hypothetical assumption retains its whole premise boundary. Rule constants belonging to the source machinery are not reclassified as environmental axioms to obtain a translation.

The class includes NJ implication/product ND with alpha/beta/eta, the specified MLL control, finite typed rule tables/free categories, and finitely presented group and monoid word calculi. Those last calculi concern proof operations and identity, not theorem truth. Dependent systems belong when they meet the certificate/checking conditions. Cyclic/global validity is a **scope-boundary obligation**: a cyclic system enters only with its exact acceptance condition, finite checking mechanism/certificates, congruence and composition contract specified. A finite locally correct pre-proof alone is not a member's valid proof. This qualification does not remove cyclic reasoning from the north star.

There is no claim that every mathematical foundation lies in `C_fin`. Non-effective semantic consequence and genuinely infinitary proof objects remain outside this certificate class. Any later broader universal theorem must address them separately.

### 1.2 Typed boundaries, morphisms and two reflections

Write `b=(E; Delta; Gamma; H |- J)` for a well-formed boundary. `Delta` is an object/dependent-variable context; `Gamma` consists of labeled hypotheses with declared modes; `H` consists of scoped derivation holes. Write `P_S(b)=Der_S(b)/=_S`. One-output systems use multicategorical grafting; multiple-output systems use the supplied polycategorical cuts. Composition is defined only on matching typed ports. No Cartesian structural action is inferred from the existence of a list of inputs. For MLL, composing cut-free representatives means cut followed by elimination, or equivalently net composition with reduction; it is **not** naive cut-free-tree grafting. Its well-definedness on the chosen net quotient is an obligation.

A map `F:S -> T` includes effective maps on expressions, contexts, substitutions, boundaries, environments and derivations, and **open target templates** for every source rule. Each template has exactly its declared premise-hole boundary. Source-specific compound type images and blocks of ports are allowed, but their typing and resource mode must be explicit. For every well-typed object or proof substitution `theta`, and every defined grafting `d[e/h]`, require:

```text
F(id) =_T id;
F(d[e/h]) =_T F(d)[F(e)/F(h)];
F(d[theta]) =_T F(d)[F(theta)].
```

The right sides are actual typed target operations, possibly **derived** interface operations with displayed templates and laws. They cannot be an unspecified decode/recompile procedure. In dependent contexts the map must reindex types and compose substitutions coherently. Formula substitution requires an actual lift to target syntax, not substitution for an arbitrary compound substring of a type.

Use the CMP-01 letters with these exact meanings, for **all** well-formed `b`, all allowed extensions/fillings of holes, and all valid `d,e` at a common boundary:

| Obligation | Exact test |
|---|---|
| P | `P_S(b) != empty => P_T(Fb) != empty` |
| R_int | `P_T(Fb) != empty => P_S(b) != empty`, quantifying over **every** target inhabitant of `Fb` |
| R_rel | Declare separately a subinterface `B_F(b) subseteq P_T(Fb)`; only `B_F(b) != empty => P_S(b) != empty` is required |
| EP / ER | `d =_S e => Fd =_T Fe` / `Fd =_T Fe => d =_S e` |
| F | Every class in `P_T(Fb)` equals `Fd` for some `d`; implies R_int, independent of ER |
| U | Context maps and rule templates respect each designated permission, resource split, ordering and block boundary; any extra class-level usage observation must commute with F |
| TR | Every target assumption has the same source dependency, scope and mode; no new trusted source-rule or proof-equation schema is installed in the fixed-core target |

R_rel with `B_F=im F` supplies no reflection evidence: a witness already includes a source proof. For a useful relative interface, give its definition and any decision/certificate procedure independently, then prove adequacy. R_int allows a coded target judgment such as `Checked(code(S),code(b))`: “intrinsic” refers to all inhabitants of that target judgment, **not** independence from source data. This is the dangerous difference between genuine boundary reflection and an anti-interpreter claim. Context restrictions explicitly included in `Fb` are legitimate; a hidden image test is not.

Proof congruence and an internal equality proposition are separate. A certificate `q:EqCode(d,e)` is not target conversion unless the **fixed** contract includes a specified reflection law. In the latter case count that law and its certificate checker in the core, and audit it. EP/ER must use the stated target equality, not whichever equality the encoding happens to satisfy.

TR is a relative designation, not an intrinsic semantics of “reasoning.” Adding a transparent `r=template` is permitted with a definitional-expansion witness; adding an uninterpreted `r` of the same type is not. A source mathematical assumption may remain assumed; a source machinery rule must have a target derivation with its premise holes open. Soundness/admissibility and derivability of that rule are different obligations.

### 1.3 Finiteness vector

Count separately `(Sig, Rule, Eq, Norm, HC_n, Param, Interface, Cost)`:

* finite expression/operation schemas; finite typing/inference schemas; finite equality schemas;
* a finite terminating confluent oriented presentation, if demanded;
* a finite homotopy/coherence basis **at a named dimension**, if demanded;
* finite per-source parameter descriptions versus a uniform bound on them;
* finite interface schemas versus finitely many generated boundary objects;
* effective checking, effective equality, translation cost and search cost.

Infinite generated objects/proofs are allowed. A finite data signature with a variable-length table is not a bounded table. Finite equations do not imply finite convergence, finite coherence, decidable equality, or a basis of all admissible rules. No candidate below makes CF or all-dimensional HC automatic: raw event counts are already incompatible with beta-erasure. Unknown causal/coherence coverage is a material shortfall against the original objective.

## 2. Three candidate universal-generation statements

These are deliberately different claims, not three interchangeable phrasings of universality. None adds a verbal, undefined “non-interpreter” clause.

### K — fixed finite structural core

**CONJECTURE K:**

```text
exists K with fixed finite (Sig,Rule,Eq), effective certificate checking,
  forall S in C_fin,
    exists an effective typed/template map F_S into K,
      forall source environments and boundaries b:
        P, R_int, EP, ER, composition/substitution, U and TR hold.
```

K's typing and least proof congruence are fixed before S. No source-specific trusted inference/equation extension is allowed. Target environments contain only the mapped source assumptions, syntax declarations and transparent conservative definitions. Closed source-description data **in derived type images or terms** is allowed; it is not a new trusted rule. The existence of each effective `F_S` does not require an effective algorithm discovering all such maps. Fullness, decidable equality, normalization, finite coherence, bounded translation length and a finite menu of instantiated types are not required.

**Proof requirement:** give one K and maps covering the independently specified whole class, including hypothetical/dependent binding and equality; verify fixed-core dependencies. Two controls or a universal program are insufficient. **Refutation requirement:** find an S and a target-independent obstruction excluding **every** K and permitted map, or prove a general inconsistent consequence of these quantifiers. A failure of CCC, LF, a lookup construction or one primitive list does not suffice.

**Bridge:** this is a necessary structural interpretation of the original universal objective with meaningful fidelity. Even if true, it does not establish explanatory fundamentality. Its maps can still be interpreters. A non-vacuity property would require an additional explicit structure/realization contract, justified independently and tested below.

### K_dec — a usable canonical-equality strengthening

**CONJECTURE K_dec:** K with the additional requirement that `=_K` on all valid proofs at a common boundary is decidable by one algorithm, including environments and every translated type. All other quantifiers and trust conditions are exactly K's. Finite convergent normalization is **not** required; a decision procedure of any cost suffices. It remains `exists K forall S exists effective F_S`, not uniform synthesis.

**Proof/refutation requirement:** the same as K, plus total equality decision. The reduction in §4.1 refutes the **entire existential K_dec**, even without fullness, uniform synthesis, U, or a bound on cost. Requiring only decidable proof checking would not imply this result.

**Bridge:** this is a practically attractive but strictly stronger version of the north star, not an assumption in the charter. Its failure removes an attractive implementation expectation; it does not settle whether a finite explanatory core with undecidable equality exists.

### D — doctrine-indexed relative finite generation

Define `D_fin` independently as the following restricted primary-source setting. D is an unsorted LNL doctrine with base chosen from the fixed standard subterminal bases `cat`, `cartmulti`, `symmulti`, `sympoly`, `lnlmulti`, or `lnlpoly` (Shulman's Remark 2.3/Examples 5.2–5.3), and finitely many **finite discrete cones**, each with a finite checked presentation of its objects, abstract projection generators and relations. The base actions use their standard finite identity/composition/structural schemas. “Discrete” here has Shulman's meaning: no nonidentity abstract transitions, not absence of projection operations. Allowed profile instances can be infinite. Inputs include a finite presentation `(Sigma,R)` of a small base polycategory, with a map to `|D|`, finitely many object/morphism generators and relations. The base map and typing of R are checked input obligations. This includes typed-path/monoid presentations; NJ and MLL require the particular doctrine and equality identifications in §5, rather than membership by assertion.

Independently define the source `S(D,Sigma,R)` by the ordinary equational deductive calculus for the designated base structural actions and D's universal operations, together with the declared generators and R. Its equality is the least congruence of these structural, universal-property and R laws, **not** arbitrary semantic equality in every model or a target image test. This is a class of relative algebraic proof theories, not “all logics admitting a chosen compiler.”

**Candidate D:**

```text
exists an effective finite-description schema construction Phi,
  forall D in D_fin,
    K_D := Phi(D) has finite (Sig,Rule,Eq),
    forall finite checked (Sigma,R) over |D|,
      exists an effective template map F_(D,Sigma,R),
        forall boundaries b:
          P_S(b) <-> P_(K_D[Sigma,R])(Fb)
```

Here `<->` denotes a **bijection of proof-class sets**, natural under typed cut, structural actions and allowed substitutions. Thus P/R_int/EP/ER/F/U hold at these boundaries. TR is relative: D's structural/universal-property laws and `(Sigma,R)` are **designated trusted parameters**, not derived in a source-independent K. The target grants exactly those parameters with their scopes; no extra theorem about their consistency or justification is inferred. Relations R must be treated as proof equations, not silently made definitionally true in another kernel. Each parameter description is finite, with no uniform size bound. Each K_D has finite schemas, with no uniform numerical bound independent of D. No finite convergent orientation, finite HC, decidable equality, global-validity theorem or polynomial cost is asserted.

For every **specified** doctrine map `u:D -> D'` and compatible interpretation of the generator/relations input, require the induced interpretations to compose coherently with F, up to the declared structural isomorphisms. The parameter map is trusted structural content: it sends generators to typed operations and equations to witnessed equations. It is not assumed conservative. Ordinary such maps preserve equations/derivations; R_int and ER across **different** doctrines require a separate conservative/faithful interpretation theorem. A displayed structure-preserving left inverse is one sufficient certificate, not the definition of a legitimate translation. This avoids the false claim that every doctrine adjunction is an embedding.

**Proof requirement:** extract the finite schema construction and exactly its congruence; compare with the free D-category theorem and verify named source identifications. **Refutation requirement:** a finite input for which the specified relative construction cannot have finite schemas or the comparison loses the independently fixed identity/typing. An infinite completion object alone is no refutation. **Evidence:** the abstract free-completion/universal-property part is established by Shulman; the effective finite-input extraction and matching the frozen controls require the precise restrictions and checks below. Do not report the whole strengthened contract as freshly proved.

**Bridge:** D offers a common explanation of why different resource and logical disciplines generate different proof theories. It gives up one unparameterized core and carries inference content in trusted D. It is a candidate **family/classification** answer to the original question, not a proof of K. A parameter schema that simply stores an arbitrary checker gives little explanatory gain; explicit accounting of what D explains and what it merely accepts is necessary. Free relative generation alone is largely prior art and risks redundancy.

## 3. Exact adversarial constructions

### 3.1 A checker that passes intrinsic reflection and even fullness

Take any finite directed multigraph G with distinct edge identifiers. The source has vertex judgments, one unary rule per edge, identity and typed composition; equality is associativity/unit, so proofs are paths. Empty-input proof judgments have no constructors. This entire independently described family lies in `C_fin`.

A fixed finite sorted target has graph/tree/list data, relational lookup and append, and a certificate judgment computed by these **fixed declarative** clauses:

```text
check(G,Id(u))       = (u,u,[])
check(G,Edge(a,t))   = (u,z,w ++ [a])
                       when check(G,t)=(u,v,w), lookup(G,a)=(v,z)
check(G,Cut(t,t'))   = (u,z,w ++ w')
                       when check(G,t)=(u,v,w), check(G,t')=(v,z,w')
```

“When” denotes certificate premises, not a trusted oracle. A proof is an opaque `box(w,t,c):Hom((G,u),(G,v))` with the corresponding checking certificate. A **fixed** equation identifies boxes with the same word and endpoints, irrespective of their tree and certificate. Typed composition concatenates words and builds a Cut certificate; unit/associativity are fixed equations. Source edge rules map to singleton-edge boxes using finite lookup witnesses for literal G; identity maps to the empty box. Open holes map to opaque Hom holes, and grafting is target composition. The core is fixed; G is source data in the boundary.

Opacity is essential: there is no proof-to-data projection or general eliminator on Hom holes. An unrestricted package eliminator could inspect a hole's word length and branch, destroying substitution-natural decoding. In the specified source contexts, data arguments are closed; only proof holes are open. Data/certificate operations cannot take Hom arguments. This makes the argument apply to the stated sorted checker, not every dependent-record implementation.

Induction on certificates proves that w is a path. Conversely, any path builds a checked tree. Flattening and the fixed box equation identify precisely the source associativity/unit classes. Interpret into the free path category to show distinct paths remain distinct. The decoder takes a box to its path, composition to source composition, holes to holes; it respects the equations and is inverse on classes. These maps commute with open grafting. The empty-input boundary maps to a constructor-free `Closed(G,v)`, not a closed data term masquerading as a theorem. Thus **P/R_int/EP/ER/F/U/TR all pass** for this graph family with empty environment, and composition passes. Binding is absent, rather than proved generically.

TR passes its literal contract: lookup entries are verified data and edge templates are core derivations, not imported proof constants. Yet this is plainly a rule-table checker. Rejecting it requires something beyond that ledger and those fidelity laws. This reproduces the bounded scope of report 009; it does not generalize flattening equality to NJ beta/eta or dependent/cyclic proofs.

### 3.2 The type-table loophole inside pure logical terms

An even smaller table test needs no checker primitive. Let the source have a constant judgment Q, a proof `u:Q`, an operation `r:Q -> Q`, and the equation `r^3(x)=x`. At a Q proof hole x the hole-dependent classes are `x,r(x),r^2(x)`; there are also the constant classes `u,r(u),r^2(u)`, which are exactly the closed classes. Other schematic atoms have hypotheses only. Map Q to

```text
D_3 = (1 + 1 + 1) x Nat,
u   = (tag_0,0),
r   = lambda (tag_i,n). (tag_(i+1 mod 3),n).
```

All templates are sum/product/Nat logical terms in one fixed STLC extension, with the usual sum beta/eta and commuting laws and Nat recursor beta laws. The table is expanded by case analysis; no new trusted generator or equality is needed. These sum laws give `r^3=id`. At these closed/one-hole boundaries, equality reflection follows by the Set model `D_3={0,1,2} x N`: the three rotations differ on `(0,0)`, and constant images differ from hole-dependent ones. Substitution is native. Derivability reflects: Q is already inhabited, and an empty interpretation for a fresh generic atom precludes a target closed proof of it. Its permitted unrestricted resource discipline is preserved. **Fullness fails:** `(tag_0,1)` is a target closed proof not equal to a translated closed source proof. Reflection of existence did not require fullness.

This is a **bounded table representation**, not an encoding of every finite group or arbitrary proof checker. Report 010 operational review §3 gives a broader finite-group and hypothetical-assumption argument with an infinite free-orbit separating model; that broader result is repository evidence, not a new theorem certified here. The bounded case already defeats “fixed wrapper + no data terms in types + only introduction/elimination primitives” as a sufficient interpreter filter: source-dependent table content can live in a closed type and its derived templates. Schematic variable genericity does not constrain a constant atom Q. Calling the same action genuine finite-group mathematics is also reasonable; that ambiguity exposes the missing criterion rather than proving that group representations are illegitimate.

Adding fullness would reject this particular table representation, but not §3.1's checker. Banning Nat or demanding native atom images rejects this construction, not every K. Such a ban also needs an independent reason to exclude legitimate indexed types or compound structural embeddings.

### 3.3 Conservative definitions and trust transport

In NJ add `k_(A,B):A -> B -> A` with the defining equation `k=lambda x.lambda y.x`. Inclusion and expansion are inverse on beta/eta/definition classes and commute with typed substitution. The same holds for a defined connective `M_D A := D -> D x A` with mutually inverse roll/unroll maps. A syntactic “only primitive introduction/elimination symbols” test changes its answer under these extensions while the operation theory does not. This refutes that **presentation-level test**, not an existential claim that some pure presentation exists.

Conversely, adding a derivable rule **without** its defining proof equation can add distinct proof classes. Closed-theorem conservativity alone is insufficient for EP/ER. Admissibility without an open derived template is also insufficient: in an atomic hypothesis-only calculus with no closed theorems, `p/q` is vacuously admissible for closed provability but has no proof template from `x:p` to q.

An unmarked proof interface also forgets assumed versus primitive machinery. For an implicational source with a primitive unary `r:p -> q`, compare ordinary ND with an assumption `k:p -> q`. Sending `r(t)` to `k t` and k to `lambda x.r(x)` gives inverse proof-class maps by beta/eta, commuting with substitution. It changes the trust ledger. TR can distinguish these only when the designation is preserved by the allowed equivalence. Moving r into a parameter is a **change in the contract**, not a derivation of r from an unchanged core.

## 4. Strongest supported obstructions and their exact limits

### 4.1 Whole-existential refutation of K_dec

**Established input, VERIFIED_SOURCE:** Boone's 1958 primary announcement, p. 1061, Result a, exhibits a group given by finitely many generators and relations with unsolvable word problem; Result b describes a recursive reduction from Thue-system equality. The announcement was inspected, not the full later proof (evidence §8).

For such a finite presentation G, form a one-object proof calculus: generator and inverse unary operations, typed composition, cancellation and finitely many relator equations. Raw words are valid finite derivations with trivial checking. The least composition congruence is exactly equality in G. No decidable congruence is required for membership in `C_fin`.

**INFERENCE — conditional reduction theorem:** For any target T with decidable equality and any effective map F on these word proofs, EP+ER would decide G's word problem: compute `F(w(x))` and `F(x)` at their common translated boundary and decide target equality. They are equal iff w represents the identity. Contradiction. Hence **no K_dec exists for C_fin**. This uses only one hard G, so no uniform discovery of F across sources is needed. The finite code of an effective F for that G suffices.

K survives this attack because its equality may be undecidable. Decidable certificate checking remains compatible with undecidable proof identity. If target equality is restricted to a decidable native fragment while the hard images lie outside it, K_dec's universal hypothesis has been dropped. Internal equality certificates do not repair a claim about decidable target conversion. Excluding groups is a source-class narrowing, not a solution for the unchanged program.

### 4.2 Finite coherence cannot be inferred or transported for free

The concrete monoid

```text
S_1 = <a,b,t,x,y | ab=1, xa=atx, xt=tx, xb=bx, xy=1>
```

is finitely presented, has decidable word problem, and lacks finite derivation type (FDT). The inspected Guiraud–Malbos text gives this finite presentation in Proposition 6.2.1 and the negative result in Theorem 6.1.1/Proposition 6.2.6. Its Theorem 4.2.3 makes FDT invariant between finite presentations of the same category, and Theorem 4.3.3 states finite convergent monoid presentation implies FDT. This is primary evidence for those authors' restatement/new proofs; Squier's original proof was not retrieved.

Its one-object word calculus is a finite-schema proof presentation. Consequently, a proposed **stronger D** demanding a finite homotopy basis for every such source, on an equivalent presentation of the same one-object category, is false. The same holds for finite convergence of every such monoid. This is a real conditional obstruction, stronger than a failure to find a completion.

Neither K nor D requires that property. A faithful embedding into a larger target does not supply a finite homotopy basis for the source; coherence cells might leave its image, and the source substructure might need infinitely many. Fullness just at selected proof boundaries also does not by itself transfer raw higher presentation data. One must prove a transport theorem with matching dimensions and allowable presentation changes. No such general transport theorem is asserted here. Rybakov's non-finite admissible-rule basis is similarly **not used** as an obstruction to ordinary finite deduction schemas; its exact admissibility hypotheses have not been freshly verified in this review.

### 4.3 Shared-boundary and resource obstructions to stronger uniformity

**INFERENCE:** if two sources have the same allowed environment and their chosen corresponding boundary b maps to the **same target boundary**, P+R_int force them to agree on whether b is inhabited. Therefore a stronger K requiring a source-independent boundary map for all calculi with shared syntax is impossible as soon as two such sources disagree on derivability. This is an elementary obstruction to that extra uniformity, not to K's permitted S-dependent images. Distinct source tags escape it, explaining both their mathematical utility and their interpreter risk.

For the frozen MLL control, `|- p^perp, p tensor p` is underivable by atom balance (one negative p versus two positive p occurrences). A Cartesian translation of the linear input as unrestricted x and tensor as product admits `(x,x)`. It fails R_int and U. This also warns against treating a change-of-doctrine adjunction as a faithful embedding. Modal/LNL translations with different boundaries are not excluded.

Requiring a structural retraction is not an interpreter solution. If a fixed finitely generated group U retracted onto every `C_p`, its finitely generated abelianization `Z^r + T` would have nonzero p-torsion for every prime. Choose p not dividing `|T|`; the composite `C_p -> U_ab -> C_p` cannot be identity. Thus some cyclic group has no splitting into that **fixed group interface**, despite possible faithful embeddings. This rejects a retraction-strengthened group construction, not every K with compound interfaces. Meanwhile §3.1's checker has a two-sided inverse. The condition has both false positives and false negatives as an interpreter test.

## 5. Frozen positive/negative controls and boundary obligations

### 5.1 NJ implication/products, exact beta/eta

Types are atoms, `A -> B`, `A x B`. Proof operations are hypothesis, lambda/application, pair/projections; composition is capture-avoiding substitution. Equality is the least typed alpha/beta/eta congruence for functions/products. Identity translation into this finite-schema calculus satisfies P/R_int/EP/ER/F/U/TR by identical derivation and equality judgments. The free Cartesian-closed interpretation explains implication/product operations relative to that doctrine; it is not an all-foundation theorem.

For an ordinary deep LF representation using uninterpreted `imp_i`, `imp_e`, the term `imp_e (imp_i (lambda z.z)) x` does not LF-beta-reduce to x. Raw proof adequacy does not give EP for the NJ beta quotient. Source-specific rewriting may repair that encoding, but changes the fixed-core/trust question and needs a conservativity argument.

A real cross-doctrine positive control is Hasegawa's **arrow-only** STLC Girard translation:

```text
b^o=b; (A -> B)^o = !A^o -o B^o;
(lambda x.M)^o = lambda y. let !x be y in M^o;
(MN)^o = M^o(!N^o); Gamma maps to Gamma^o ; empty.
```

Propositions 3.1, 3.3–3.4 and Lemma 3.2 give typing, equality preservation/reflection and substitution; Theorem 5.6 gives fullness at exactly those translated contexts/types in the specified linear calculus/equality. This freshly inspected theorem demonstrates that meaningful non-native boundaries can satisfy even stronger reflection. It does **not** certify products, classical MLL or arbitrary foundations; those extensions need their own theorem. Banning administrative steps, compound formula images or all context zones would produce a false negative here.

### 5.2 Unit-free cut-free MLL, exact net/permutation identity

Fix no MIX, occurrence-labeled atoms/formula forests, ordered tensor arguments, implicit exchange, atomic axioms, tensor and par. Equality is identical axiom matching on the concluding forest, equivalently rule-commutation equality for this cut-free fragment by van Glabbeek–Hughes Theorem 1 (the inspected theorem is for unit-free cut-free MALL, with or without MIX).

Reproduce the CMP fixture: `P=p tensor r`, `T=P tensor q`, `X=p^perp par r^perp`. Tensor the p and r axioms to obtain `D:|-p^perp,r^perp,P`. Either apply par to D before tensoring with the q axiom, or tensor first and apply par afterward. Both derive `|-X,T,q^perp` and have matching `(p-,p+),(r-,r+),(q-,q+)`. Their source classes coincide. A raw LF encoding gives respectively an outer `tensor` and an outer `par` head; both are normal with distinct uninterpreted constants, so EP fails. This defeats that equality pair, not LF in general.

Conversely, at `|-p_1^perp,p_2^perp,p_3 tensor p_4`, the straight and crossed axiom matchings are distinct valid nets. A proof-irrelevant target identifying all proofs of this sequent fails ER. Valid matching data therefore preserves exactly an identity the target must retain; provability alone cannot explain it.

Proof-to-net translation has P/R_int/EP/ER/F **at the sequent boundary** when target proofs are defined as correct occurrence-labeled nets; U follows the linear rule boundary. This supplies no fixed-core certificate-generation theorem. A D instance must prove that its *full ambient congruence*, including cut detours, induces exactly this identity on cut-free representatives. Shulman's free doctrine result or LSR's generic syntax alone is not that identification. Cut elimination/sequentialization and the equality correspondence must be supplied separately, with no accidental MIX or units. This named-control bridge remains unverified here for a particular generated D target.

### 5.3 Dependent binding boundary

In `x:A, y:B(x)`, replacing x by `a:A` sends the second declaration to `y:B(a)`. In `x:A,y:B(x),z:C(x,y)`, replacing y by b requires `z:C(a,b)`. Composition of these substitutions must agree with simultaneous substitution and preserve proof-hole scope. A simple port graph with unchanged labels `B(x),C(x,y)` fails well-formedness before P/EP can be asked.

K must handle such sources when they belong to `C_fin`; no impossibility follows from this port-only failure. Candidate D's discrete nondependent doctrine scope does **not** cover this test. This is a north-star gap requiring comprehension/reindexing or another explicit dependent structure, not N/A for the program. Uemura's bi-initiality is not used as a theorem that the specified D machinery supplies it.

### 5.4 Cyclic/global-validity boundary

A two-node LK-style pre-proof can loop from `P |- Q` to `P,P |- Q` and back: downward contraction gives the first step and downward weakening the second. Both steps are locally legal; the cyclic unfolding has no progressing inductive trace. Taking P true and Q false refutes its conclusion. It is not a valid cyclic proof.

Brotherston–Simpson Definition 5.5 requires every infinite path to have a tail admitting an infinitely progressing trace; Definition 7.3 applies that condition to finite cyclic graphs; Proposition 5.8 proves soundness for **standard models**, not arbitrary Henkin models. These primary passages were inspected. A proposed core accepting all locally checked cyclic edges fails validity/reflection. A fixed verified automata/trace-certificate or reset translation may avoid that failure; neither certificate irrelevance nor compositionality is automatic. The reset-construction lead in OBS-01 was not freshly verified and is not a proof premise here.

K's boundary extension must name how this global witness is generated, checked, transported under grafting, and quotiented. D as stated covers no such global acceptance predicate. A finite graph is neither a strict finite causal poset nor a global-validity proof; an unfolding could carry infinite occurrence order. These facts refute local-only/finite-poset stronger assumptions, not every finite generative mechanism.

### 5.5 Representation obligations, not framework rankings

`Y` = informal argument or cited theorem at stated scope; `N` = explicit failure; `?` = unknown; `—` = no such structure in this fixture. R means R_int in this table. A failed EP means there is no induced map on the claimed source quotient; ER then records only the raw equality implication where meaningful.

| Specified construction/equality | P | R | EP | ER | F | U | TR | Composition / limits |
|---|---|---|---|---|---|---|---|---|
| NJ identity, implication/products beta/eta | Y | Y | Y | Y | Y | Y | Y | Native substitution; no CF theorem |
| Hasegawa arrow-only STLC -> specified linear target | Y | Y | Y | Y | Y | Y | Y | Published substitution/fullness; no MLL/product extrapolation |
| Deep LF NJ with object beta/eta | Y | Y by canonical decoding in the NJ constructor fragment | N | Y as raw equality implication only | No induced map on quotient | Y for encoded unrestricted contexts | N for fixed-core derivedness | Imported source inference constants; raw adequacy is different |
| Cut-free MLL -> correct nets at a fixed sequent | Y | Y | Y | Y | Y | Y | Y, relative to MLL rules/correctness | Cut composition needs its own theorem; no universal core witness |
| MLL -> raw uninterpreted LF sequent rules | Y for displayed proofs | ? | N | ? | ? | Y for explicit context splitting | N for fixed-core derivedness | Commuted pair has distinct normal heads |
| Linear tensor/input -> unrestricted Cartesian product/input | Y in tensor fragment | N | ? | ? | N | N | No new imports in example | Specific map; other boundaries allowed |
| Opaque graph checker / typed paths, flattening equality | Y | Y | Y | Y | Y | Y, one-port | Y under literal ledger | Open grafting inverse; no binding/global coverage |
| Pure C3 type-table at stated closed/one-hole boundaries | Y | Y | Y | Y | N | Y, unrestricted | Y | Native substitution; bounded scope only |
| Bare graph labels for dependent substitution | ? | ? | ? | ? | ? | ? | ? | Fails well-formedness; no valid comparison map |
| Cyclic local-edge closure without progress | Locally valid proofs encode | N for acceptance | ? | ? | ? | — | N for claimed global justification | Invalid pre-proof accepted; no global witness |
| D abstract free equational calculus versus its exact presentation | Y | Y | Y | Y | Y | Y relative to base | Y relative to D,Sigma,R | Generic theorem baseline; named-source identifications separate |

## 6. Can fundamentality be intrinsic and presentation-invariant?

### 6.1 Strongest bounded indistinguishability statement

**INFERENCE — interface theorem:** Let N be a predicate of a structured diagram `P_S --F--> B_F`, invariant under isomorphisms preserving exactly its typed boundaries, proof classes, grafting, permissions and any designated annotations. If the native path realization and a checker realization are isomorphic such diagrams, N gives them the same answer.

Proof: conjugate F by that isomorphism and apply invariance. Section 3.1's flattening/decoder identifies the checker interface with the free-path source; a typed-path implementation provides the same diagram. Composition, empty/nonempty boundaries, open holes and one-port use are preserved. Thus **no intrinsic invariant of just that retained diagram** can accept the native free category and reject the specified checker. Fullness, structural reconstruction, representables/Yoneda, or naturality on all probes cannot separate isomorphic diagrams. This elementary theorem concerns information retained, not the computational difficulty of recognizing N.

It does not identify the whole ambient targets, their extra sorts, generating processes, reduction histories, or doctrine designations. A predicate inspecting those may distinguish them. Nor does the graph example prove a universal checker theorem for NJ beta/eta or all dependent sources: arbitrary equality would require normalization or a fixed certified equality-reflection mechanism. Never upgrade this example into a universal impossibility of explanation.

The k/roll extensions show that “is listed as primitive” is not invariant under conservative definitional change. Existence of a finite generating presentation can be invariant of the **generated structured object**, but the designated generator list, justification and implementation origin are additional data. Thus presentation-invariant finite generation is mathematically defensible; presentation-invariant identification of a particular implementation as fundamental requires a stated equivalence retaining more data.

### 6.2 Relative definitions, with errors they must tolerate

| Proposed extra designated structure | Genuine benefit | False positive / false negative / remaining obligation |
|---|---|---|
| Logical doctrine with designated products/implication/tensor and ambient universal properties | Controls which probes/resource maps participate; excludes naive Cartesianization of a linear interface | A checker can carry transported universal operations. A native path/table free category already satisfies its categorical doctrine. It does not certify nonlogical generators |
| Formula-variable fibration and substitution-natural templates | Rejects an encoding replacing a schematic formula variable by one fixed code | Constant Q type-table in §3.2 survives; banning all indices rejects direct dependent binding. Naturality alone is weaker than a parametricity theorem |
| Trusted parameter morphisms with derivations of rule/equality images | Keeps assumptions conditional; requires definitions to carry expansions; prevents LF declarations counting as derived core rules | Allowing arbitrary source logic as D can faithfully record the entire checker. Honest relative interpretation remains legitimate but explains less than K |
| Marked inference/computation events and an allowed macro-expansion relation | Can inspect generation rather than only quotient interface | Strict one-step identity rejects Girard's let administration and conservative k expansion; unrestricted macros may absorb an interpreter. Marks must be chosen before testing |
| Native atom images, finite menus, no table-bearing types | Rejects the displayed data-indexed checker | Rejects `Q -> X^tensor n` representations of cyclic permutations, and ordinary indexed/dependent types; does not exclude every algebraic universal-group interpretation |
| Effective structural left inverse | Gives reconstruction, stronger than faithful equality | Checker passes; fixed-group retraction obstruction gives false negatives (§4.3) |

For D, allowed presentation equivalences must preserve the base structural doctrine and trust designations, and extend/in-line definitions with explicit equations. A trusted parameter map is itself inference/equality content; it does not become harmless because it is called a mode, cone, or signature. Its generator equations must be witnessed in the destination and extra permissions recorded. Conservative interpretation is a further certificate; a doctrine adjunction alone need not reflect derivability or identity.

This relative account is stable under **designation-preserving** definitional expansions. If a checker is equipped with a transported designation making the enriched diagrams isomorphic, the same theorem still prevents separation. Distinguishing physical/procedural provenance therefore needs an operational realization contract whose observations are not merely transported from the quotient. No intrinsic universal discriminator of that richer sort has been established here. It would be false to conclude that none can ever exist.

## 7. Falsification tables for every candidate

“Whole claim” below means a contradiction for all permitted targets, not an encoding rejected by a reviewer. Each surviving candidate has a stated kill condition.

### K

| Attack / what an opposing investigator should exhibit | Present result | Logical reach / next decisive requirement |
|---|---|---|
| Graph checker with all fidelity/TR laws | §3.1 passes even F | Explanatory counterexample to sufficiency of the contract; neither proof nor refutation of all-C K |
| C3 table in logical types/derived rules | §3.2 passes fidelity except F | Refutes proposed purity/fixed-wrapper filter; construction only, not whole K |
| Conservative k/roll extension | Same proof operations after expansion | Refutes literal primitive/state bans; does not refute existence of an eligible presentation |
| Hard group congruence | Forces undecidable equality if effective EP/ER hold | Stronger decidability assumption only; K allows that equality |
| Cartesian MLL translation or raw LF net encoding | R/U or EP fails | Particular map/equality pair only; a different K/map remains possible |
| S1 finite-coherence requirement | Cannot supply finite FDT presentation of same monoid | Stronger HC/convergence requirement with transport, not K's finite schemas |
| Dependent/cyclic boundary | Simple ports/local checking fail | Particular constructions; **kill K** only by an obstruction for all allowed indexed/global mechanisms |
| Source-independent rigid boundaries | Inhabitance disagreements yield contradiction (§4.3) | Extra shared-boundary assumption only; S-dependent images are permitted |
| Target-independent structural obstruction | None supplied | **Whole K remains UNKNOWN**, not falsified. A proof must cover C_fin with fixed Eq/TR; no general proof attempt authorized |

### K_dec

| Attack | Present result | Logical reach |
|---|---|---|
| Boone group word calculus + effective EP/ER + decidable target equality | Word-problem decision algorithm (§4.1) | **Refutes whole existential K_dec** for C_fin |
| Allow only equality certificates / decidable raw checking | Does not decide identity | Escape changes K_dec; K remains possible |
| Use nonuniform but effective F_G | Its finite program still gives a decider for one hard G | No escape; uniform synthesis was unnecessary |
| Checker/type-table and definition attacks | Bounded easy-equality examples still pass weak purity contracts | Separately refute explanatory sufficiency; not needed for the whole refutation |
| NJ/MLL, dependency and cyclic failures | Fragment-specific constructions can work or fail | Cannot rescue all-source K_dec; narrowing C_fin would define a new claim |
| Add finite coherence/convergence | Stronger conditions, often independently obstructed | No need to assume them for the decisive refutation |

### D

| Attack | Present result | Logical reach / kill condition |
|---|---|---|
| Store arbitrary source rule table in Sigma,R or D | Relative generator clauses accept it | Explanatory/novelty weakness of family, not refutation of its honest relative statement |
| Conservative definitions | Designation-preserving expansion keeps relative theory | Stable only with retained designation; rule-to-assumption move is not an allowed equivalence |
| Group congruence | Eq can be undecidable with finite R | No refutation; **adding decidable equality for all inputs** fails |
| S1 coherence | Finite R, no finite homotopy basis | Refutes stronger universal coherent/convergent family, not D as stated |
| Doctrine map adding Cartesian permissions | May destroy R/ER/U across doctrines | Refutes “all doctrine maps are faithful”; D requests coherence of interpretation, separate faithfulness certificates |
| NJ beta/eta and MLL net quotient | Need exact free-doctrine/source equivalence, including ambient detours | **Kill proposed control bridge** by an extra target identity or inhabitant, or an unpreserved source equation; abstract relative free generation may survive |
| Dependent contexts and cyclic validity | Outside discrete nondependent doctrine contract | Scope failure against original objective, not a false theorem about D's stated class; require a new theorem before claiming coverage |
| Uniform effective finite-schema extraction for every specified D input | Supported by restricted §8 construction, not independently certified in full here | **Kill finite-schema clause** with a qualifying finite input requiring infinitely many independent rule/equality schemas under the declared schema convention; no such example supplied |

## 8. Primary evidence and remaining uncertainty

Sources were sought through author/publisher repositories and retrieved PDFs. Primary theorem passages were read, not inferred from titles. Downloaded texts are scratch evidence outside the PR; no implementation or checking code was added. Direct retrieval of the Edinburgh cyclic PDF was denied (403), but its primary text was accessible through the web PDF reader. The 1959 Boone scan failed (503); the 1958 primary announcement was read as a page image. No full-proof verification is claimed.

| Primary source / inspected location | Exact relevant hypotheses and conclusion | Use and status |
|---|---|---|
| W. W. Boone, *The Word Problem*, PNAS 44(10), 1061–1065 (1958), [primary archive](https://pmc.ncbi.nlm.nih.gov/articles/PMC528693/), [DOI](https://doi.org/10.1073/pnas.44.10.1061), p. 1061 Results a–b | Existence of a finite group presentation with unsolvable word problem; recursive reduction from Thue-system equality to word equality in finite group presentations | VERIFIED_SOURCE for the original statement, not full construction/proof. The EP/ER reduction in §4.1 is INFERENCE; no machine certification |
| R. J. van Glabbeek and D. J. D. Hughes, *MALL proof nets identify proofs modulo rule commutation*, [author text](https://arxiv.org/abs/1609.04693), §§2–4, Theorem 1, Tables 2–4 | Cut-free MALL without units, occurrences tracked, with or without MIX: same translated net iff finite succession of rule commutations | VERIFIED_SOURCE. MLL specialization used. No substitution of cut-normal-net equality for their distinct Theorem 2 |
| M. Hasegawa, *Girard translation and logical predicates*, JFP 10(1), 77–89 (2000), [DOI/primary PDF](https://doi.org/10.1017/S0956796899003615), §§2–3, Props. 3.1/3.3/3.4, Lemma 3.2, Thm. 5.6 | Arrow STLC beta/eta, specified dual-context linear calculus with !/linear arrow and its equations; equality and substitution preservation/reflection, fullness at `Gamma^o;empty |- sigma^o` | VERIFIED_SOURCE. No product or arbitrary-MLL extension inferred |
| R. Harper, F. Honsell, G. Plotkin, *A Framework for Defining Logics*, [primary manuscript](https://era.ed.ac.uk/bitstreams/f02739c7-c52e-4764-9229-a1fcb46daad6/download), Thm. 4.1 and declared first-order signature | Bijection of the specified valid first-order proof expressions with canonical LF terms in Sigma_FOL and the encoded contexts; simultaneous term/proof substitution | VERIFIED_SOURCE. Raw proof adequacy with imported constants, not source NJ beta/eta or MLL net identity |
| M. Shulman, *LNL polycategories and doctrines of linear logic*, LMCS 19(2:1) (2023), [publisher](https://lmcs.episciences.org/11160), [author PDF](https://arxiv.org/pdf/2106.15042), Thm. 7.4, §8/Props. 8.2–8.3, Thms. 9.1–9.2 | Any **small** LNL doctrine and sketch have D-completion with hom-category surjective-equivalence universal property in the (2,1)-category retaining invertible 2-cells. §8 first restricts to unsorted/subterminal base and finite discrete cones; constructs sequent generation plus quotient equations. Doctrine maps induce **pseudo 2-adjunctions**, not automatically faithful embeddings | VERIFIED_SOURCE. “Small” does not mean finite. Finite-input schema extraction is an additional restricted analysis, not the unrestricted Thm. 7.4. Cut elimination is explicitly left for future study in §8; named net identity is not inferred |
| Y. Guiraud and P. Malbos, *Polygraphs of finite derivation type*, [author text](https://arxiv.org/abs/1402.2587), Def. 4.1.3, Thms. 4.2.3/4.3.3/6.1.1, Props. 6.2.1/6.2.6 | Finite homotopy basis for specified (2,1)-category; FDT invariant under finite presentations of same category; finite convergent monoid presentation implies FDT; S_k finite with decidable word problem but no FDT, k>=1 | VERIFIED_SOURCE for inspected survey/new-proof text; Squier original not directly inspected. Transfer to arbitrary proof embeddings UNKNOWN |
| J. Brotherston and A. Simpson, *Sequent calculi for induction and infinite descent*, [primary text](https://www.pure.ed.ac.uk/ws/portalfiles/portal/12304236/bs_journal.pdf), Defs. 5.4–5.5/7.3, Prop. 5.8 | Every infinite path admits a tail with infinitely progressing trace; cyclic proofs are finite graphs satisfying this condition; soundness for standard models | VERIFIED_SOURCE. No generic composition/certificate-identity theorem inferred |
| D. Licata, M. Shulman, M. Riley, *A Fibrational Framework for Substructural and Modal Logics* (2017), [extended author text](https://dlicata.wescreates.wesleyan.edu/pubs/lsr17multi/lsr17multi-ex.pdf), Thm. 8.4, Conj. 8.5, §9.1 | Soundness of permutative equality is proved; converse `d=d' => d-down =_p d'-down` is explicitly labeled a conjecture; §9.1 anticipates full/faithful object-logic encodings | VERIFIED_SOURCE for manuscript status. A targeted current search did not verify its resolution; **UNKNOWN in 2026**, not “proved open.” A later cross-reference saying Theorem 8.5 does not establish it |

The new checker, table, presentation, reduction and boundary arguments are informal and deliberately bounded. They are not upgraded to established universal theorems by agreement with reports 009–010. No theorem inspected here settles K or supplies a source-independent anti-interpreter invariant. No novelty claim about D is justified.

## 9. Deliverable decisions and the next discriminating gate

**Strongest supported theorem/obstruction:** the interface-isomorphism discriminator limitation is unconditional under its explicitly restricted invariance hypothesis; the effective EP/ER reduction, using Boone's established finite-group existence input, refutes the entire K_dec statement. S1 additionally defeats universal finite coherence/convergence **only with matching presentation/transport hypotheses**. None refutes K.

**Most dangerous interpreter loophole:** source-specific reasoning can be relocated into a derived, data-indexed target judgment, closed type image, or doctrine parameter while all inhabitants satisfy intrinsic reflection and rule templates are genuinely core-derived. Transparent expansion and fixed certificate irrelevance can make it indistinguishable from native proof composition on the chosen quotient. Rejecting a symbol named `eval`, adding a provenance ledger, or demanding fullness does not close that loophole. A generic all-C compiler satisfying every binding/equality obligation has **not** been constructed here.

**Smallest concrete positive case worth accepting:** NJ implication/products with its displayed finite beta/eta schemas, native scoped substitution, marked Cartesian permission and definitional-expansion equivalences. Accept it as finite explanatory generation **relative to its doctrine**, with the honest limitation that it is established textbook-level structure. Require the MLL commuted pair **and** distinct-matchings negative control alongside it before crediting a common comparison. Hasegawa's arrow fragment is the smallest freshly sourced positive change-of-doctrine result; do not announce a product/MLL generalization on that evidence.

**PIVOT for the whole program, with decisive reasons:**

1. K is not refuted, but its stated mathematical fidelity/TR contract admits explicit interpreter controls. Its truth alone would underdetermine the intended explanation. More operation enumeration or an existence proof now would attack the wrong evidential gate.
2. K_dec is false on the independently declared broad class. Decidable checking cannot be advertised as deciding faithful proof identity. Convergence/coherence expectations also require substantial extra restrictions.
3. D offers an intelligible relative account of resource and logical structure, with established free-construction baselines. It accepts trusted doctrine content and currently lacks dependent/global coverage. Success would be a precise classification or separation result with a visible scope bridge, not universal-core confirmation or a new framework by default.

One bounded, reviewable next gate is worthwhile: **freeze a designated doctrine/realization contract and its allowed conservative expansions before testing it; determine whether the explicit graph checker/path isomorphism lifts to that enriched contract, and test the C3 type-table plus k expansion against the same rule.** If it lifts, abandon that discriminator. If it does not, identify the failed law and show that the law accepts the NJ beta/eta positive and the specified Girard translation while handling the MLL equality controls. Separately audit the exact MLL free-doctrine equality bridge; an extra ambient equation is a decisive counterexample. No prover or general existence proof is needed for either decision.

If the proposed contribution reduces to the known free-doctrine theorem, record redundancy and **STOP that contribution**. If no independently motivated realization distinction survives these finite tests, stop the claim that the current invariants establish fundamentality; the broad existential question can remain open without implying a reason to continue funding it. This report proposes no charter/canonical-plan edits, no implementation, and no change in Agent A's independent task.
