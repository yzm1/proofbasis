# Task 017 — Independent adversarial atomic-endomorphism test

**Verdict: UNRESOLVED.** No certified negative witness was obtained. The strongest fully typed attempt below duplicates a genuinely closed modal name, reconstructs two linear identities, and cancels under the frozen equations. A compact-model trace suggests a separated value but does not supply a permitted term. Neither observation establishes the universal atomic proposition.

**Provenance:** Agent B, 2026-10-14; isolated clone `/tmp/proofbasis-atomic-b`, branch `research/atomic-endomorphism-adversarial`, exact baseline `f2d7fcb1b00c36fdc4dfc3ab2a3e9ac487f566e7`. The replacement launch used gpt-6.1-sol; the failed predecessor did no mathematical work. No rebase, contact with Agent A, reading of its developing work, additional agents, implementation, or canonical-document changes. AGENTS.md and its required documents, RESEARCH_PLAN.md, research/OPERATING_PROTOCOL.md, reports 017/020/021/corrected 022, and Tasks 016/017 were read. This report is the sole assigned change.

All constructions and model checks here are **INFERENCE: informal mathematical arguments**, not mechanically checked results. VERIFIED_SOURCE below means direct inspection of the specified original statement and relevant definitions, not independent certification of its entire proof.

## 1. Frozen contract

The target is exactly `B=A*(∅,{p})`, with arity base `lnlpoly`. Its mutually generated objects remain

```text
N ::= 1_N | N×N | N⇒N | U A
A ::= p | I | bottom | A⊗A | A⅋A | A* | F N.
```

Empty nonlinear **atom declarations** do not remove nonlinear objects. The nonlinear terminal/products/homs, linear tensor/cotensor/unit/counit/dual, and covariant F/U have Shulman's specified universal properties. Linear homs are `B_L(Θ | Γ ; Δ)` and nonlinear homs `B_N(Θ ; N)`. Only nonlinear slots admit contraction/deletion. Linear cut joins one matching port in two proofs; it is not a self-trace or a rule for disconnected juxtaposition.

E* is the entire structural and principal universal β/η congruence, with all admissible ambient contexts, not a modal-free subset. No MIX, `I=bottom`, `FU=id`, proof irrelevance, nonidentity proof constants, additional equalities, or substituted atom image `p=FX` is used. Raw duality is not made strictly involutive; canonical comparisons implement derived closed structure.

The tested assertion is

```text
∀t∈B_L(∅ | p ; p), t = id_p under E*.
```

The independently specified unit-free no-MIX source has exactly one class at this boundary: its two atomic leaves must be connected by their sole axiom link. Thus a definable separated t refutes frozen SC's intrinsic fullness. This source observation does not depend on accepting report 022's pure bridge or unit-extension identification.

## 2. Exact closed-name reformulation, without a normalization assumption

Let `H=p*⅋p`, the derived linear hom `p⊸p`, and `N=UH`. The universal linear evaluation

```text
e : ∅ | H,p ; p
```

is obtained by cutting the cotensor projection `H→p*,p` against the dual evaluation `p*,p→()` on its p* port. Its universal property follows by composing those two universal bijections (Shulman Prop. 2.16), with the frozen dual comparisons. In particular,

```text
B_L(∅ | p ; p) ≅ B_L(∅ | ; H) ≅ B_N(∅ ; UH).
```

The first map is linear hom factorization; the second is U-right factorization. Both bijections are on E*-classes at the full ambient target, because their principal β and η reconstruction are part of E*. No bound on nesting or choice of interior operations occurs here.

Write `n:∅|;H` for the transpose of `id_p` and `q:∅;N` for `UR(n)`. The inverse takes a closed nonlinear `r:∅;N`, substitutes r into `u_H:N|;H`, then cuts the result into e's H port. Consequently the exact unresolved construction problem can also be stated as finding a definable closed r unequal to q. This reformulation is not a classification of those closed proofs: nonlinear homs, U-derived objects, modalities, duals and units may all occur inside r.

No linear p hypothesis has been promoted. The input p is discharged by the *linear* hom universal property before U-right is applied; U-right itself is used only at empty linear input with exactly one linear output.

## 3. Strongest completed attempted witness: duplicate a closed identity name

We make the attempt more demanding than a bare F/U triangle by copying a nonlinear value that encodes a linear function, evaluating both copies, composing the resulting functions, and applying the result to p. Unary arrows below have empty nonlinear context unless shown otherwise; `I→A` corresponds to `∅|;A` by the unit bijection.

Let `n̂:I→H` be the unit-form representative of n. Let `φ:I≅F1_N` be the canonical strong-monoidal unit comparison and `m:F(N×N)≅FN⊗FN` the canonical tensor comparison. These are obtained by composing the designated universal morphisms and inverse factorizations, not new generators. Set `q₁=q∘!:1_N→N`, where `!` is substitution into the empty nonlinear context (weakening), not a nonlinear morphism with an empty output.

| Step | Type | Exact generating/derived operation |
|---|---|---|
| identity | `∅|p;p` | Linear identity schema |
| n, n̂ | `∅|;H`, `I→H` | Derived linear hom factorization of identity; unit factorization |
| q, q₁ | `∅;N`, `1_N→N` | U-right applied to n; nonlinear terminal substitution |
| d | `N→N×N` | Product pairing of two nonlinear identities, using nonlinear contraction |
| b | `I→FN` | `Fq₁∘φ`; F on arrows is obtained from its universal morphism and F-left factorization |
| Δ | `FN→FN⊗FN` | `m∘Fd`; tensor/product comparison from universal uniqueness |
| ε_H | `FN→H` | F-left factorization of `u_H:N|;H` |
| a | `I→H⊗H` | `(ε_H⊗ε_H)∘Δ∘b`; tensor functoriality via tensor projection/factorization and cut |
| C | `H⊗H→H` | Two cuts of e, followed by linear hom and tensor factorization; `C(f,g)(x)=f(g(x))` |
| z | `I→H` | `C∘a` |
| t | `p→p` | `e∘(z⊗id_p)∘λ_p⁻¹`; tensor construction, linear cuts and the canonical left unitor |

For C explicitly: use two copies `e:H,p→p`, cut the output of the second into the p input of the first, obtaining `H,H,p→p`; transpose the final p input/output to get `H,H→H`, then bundle its two H inputs by tensor factorization. The two linear H occurrences are distinct; nonlinear contraction occurs only in d. Every table entry is therefore generated by the frozen operations and structural laws, without nonlinear promotion of the final input.

### Cancellation in the full congruence

The nonlinear product equations give

```text
d∘q₁ = ⟨q₁,q₁⟩.
```

F functoriality and the natural strong-monoidal comparison, with the canonical unitors, therefore give

```text
Δ∘b = (b⊗b)∘λ_I⁻¹.
```

This is simply the interpretation of the preceding product equation through the universal tensor comparison; it is not a newly imposed equation saying arbitrary linear elements are copyable. Modal principal β and reconstruction give

```text
ε_H∘b = n̂.
```

Indeed, cut `f_N:N|;FN` into the F-left definition of ε_H to obtain u_H by F-β; then substitute q into N and use U-β, `cut_N(q,u_H)=n`. The unit comparison supplies the displayed unary version.

Thus

```text
a=(n̂⊗n̂)∘λ_I⁻¹,
z=C∘(n̂⊗n̂)∘λ_I⁻¹=n̂,
t=e∘(n̂⊗id_p)∘λ_p⁻¹=id_p.
```

The middle equality applies hom-β twice to the displayed definition of C, then hom-η identifies the reconstructed name with n̂. The final equality is hom-β for the original transpose. Structural associativity/interchange and unit naturality account for the displayed bundlings. This cancellation is an E* derivation; it remains licensed when the construction is inserted into admissible larger contexts.

### Extra triangle and nonlinear-hom wrappers do not rescue it

Two competing covariant modal loops can be inserted before copying:

```text
R₁=ε_(FN)∘Fη_N : FN→FUFN→FN,
R₂=FUε_H∘Fη_N : FN→FUFN→FUH=FN.
```

Here `N=UH`, `η_N:N→UFN` is U-right factorization of `f_N:N|;FN`, and `ε_(FN)` is F-left factorization of `u_(FN):U(FN)|;FN`. All intermediate objects are retained. R₁ is identity by the F-triangle. R₂ is `F(Uε_H∘η_UH)`, hence identity by the U-triangle and F functoriality. These are reconstruction consequences of the same modal universal bijections, not `FU=id`.

One can also replace q₁ by `eval_N(k,q₁)`, where `k:1_N→(N⇒N)` is nonlinear transpose of `id_N`. Nonlinear hom-β makes this q₁; hom-η reconstructs the same function. Such a wrapper explicitly uses the target-only nonlinear hom constructor but has no separated effect. These computations settle these specific attempts, not every alternating mixed interior.

## 4. A sound whole-doctrine model, and why it does not certify a witness

Use nonlinear FinSet and linear finite-dimensional F₂-vector spaces. Let F send a finite set S to its free vector space with basis `[s]`; let U take the underlying finite set. The natural adjunction is

```text
Hom_Vec(FS,V) ≅ Hom_Set(S,UV).
```

The basis bijection makes F strong symmetric monoidal: `F(S×T)≅FS⊗FT`, and `F1≅F₂`. FinSet supplies terminal/product/exponential universal properties, including all N⇒M objects. Finite-dimensional vector spaces are compact closed, hence star-autonomous; their usual chosen tensor, dual, units and cotensor satisfy the required linear universal properties.

By the directly inspected Shulman Prop. 3.15(iii), this adjunction gives the requisite classical LNL polycategory. Its mixed homs can be represented as

```text
Hom_Vec(F(∏Θ)⊗(⊗Γ), ⅋Δ),
```

and nonlinear homs as finite-set maps. All finite products, units and hom objects are included. Ambient F-left factorization is the basis/product isomorphism and linear currying; U-right is the displayed adjunction at empty linear input. The other universal factorizations are the chosen CCC/star-autonomous bijections. Thus each principal β and η equation holds at every stipulated ambient profile; structural equations hold for ordinary composition and structural actions. This establishes informal soundness for the **entire** E*, not just a small tested fragment.

This model identifies tensor with cotensor and I with bottom by its own chosen compact structure. Such additional model equalities do not add equations or constructors to B. Soundness permits a model to satisfy stronger equations, but prohibits importing its extra arrows as syntactic proofs.

Interpret p as `V=F₂²`. Then H is End(V) (dimension 4), N is its underlying 16-element set, and FN has dimension 16. Our closed q denotes the single element `id_V∈N`; b sends 1 to `[id_V]`. Δ sends this basis element to `[id_V]⊗[id_V]`; ε_H sends `[h]` to h. Consequently a denotes `id_V⊗id_V`, z denotes composition of identity with identity, and t denotes `id_V`. Neither triangle wrapper changes this calculation.

The zero map, a nonidentity projection, and a swap are all actual model endomorphisms of V. For example the projection annihilating one basis vector differs from identity. None is a proof generator in B. Choosing one as r's semantic value would be a separation certificate **only after producing a definable r**. Declaring a closed r to name that value changes the empty proof ledger and is inadmissible.

## 5. Strongest uncompleted separation idea: compact trace

The same sound model has compact evaluation/coevaluation and `trace(id_V)=2=0` in F₂. If one could define that scalar by the permitted B-operations and tensor it with p, its interpretation would be `0_V≠id_V`. This is a strong negative **semantic suggestion**, not a witness.

The actual frozen universal dual operations have boundaries

```text
coev : ∅|;p,p*,          ev : ∅|p*,p;.
```

After allowed bundling these are

```text
I→p⅋p*,                 p*⊗p→bottom.
```

A compact scalar trace instead needs the correctly ordered versions of

```text
I→p⊗p*,                 p*⊗p→I.
```

The cotensor and terminal linear output discrepancies cannot be corrected by exchange. Directly joining both coev ports to both ev ports is also not a permitted polycategory composite: after one cut, the remaining pair belongs to a single already composed proof, and there is no self-cut/feedback generator. A model's compact interpretation supplies these missing maps, but freeness does not lift them to B.

This identifies the unresolved construction obstacle precisely: obtain a permitted modal/CCC/dual/unit composite that realizes a nonidentity closed name (or that supplies the trace scalar's missing interface) **without** adding MIX, `I=bottom`, feedback, or a proof constant, and then show its separated interpretation. The report does not assert those missing interfaces are impossible to derive by some other mixed construction. The final linear p cannot simply be moved into U p: U-right requires empty linear input. Nor may p be replaced by FN to exploit that object's copying maps.

## 6. Primary sources checked directly, and their exact reach

Original PDFs/extracted texts supplied in `/tmp/proofbasis-sources` were inspected directly at these locations. Repository evidence labels were not used as substitutes. No new remote literature search or claim of exhaustive coverage is made.

| Primary text/version and inspected location | Hypotheses, translation/equality, and use/limit |
|---|---|
| Shulman, *LNL polycategories and doctrines of linear logic*, published LMCS 19(2:1), 2023, [text](https://arxiv.org/pdf/2106.15042), Defs. 2.1/2.8/2.10/2.14/2.15, Props. 2.9/2.16/3.15, §8 Figure 2/Prop. 8.3 and following quotient paragraph, pp. 1:44–47 | VERIFIED_SOURCE. Linear contexts have permutation actions; nonlinear contexts finite-function actions. F/U have exactly the displayed ambient and empty-linear-input bijections. Derived linear hom and strong-monoidal comparisons arise by composing universal morphisms. §8 assumes unsorted doctrine, subterminal arity base, finite discrete cones; its quotient is structural plus principal β and ambient η. Prop. 8.3 is surjectivity of its calculus onto completion, not pure-boundary conservativity. The text explicitly leaves cut elimination for future study. These definitions license our constructions/model; they do not classify all closed UH names. |
| van Glabbeek–Hughes, *MALL proof nets identify proofs modulo rule commutation*, [2016 text](https://arxiv.org/pdf/1609.04693), §2–4, Tables 2–4, Thm. 1 p. 7 | VERIFIED_SOURCE. Unit-free cut-free MALL− proofs have the same translated net iff related by the specified rule commutations; MIX is optional and absent by default; subformula occurrences are tracked. Restriction to no-MIX MLL gives the independent source equality at our two-leaf boundary. No target F/U congruence is part of that theorem. |
| Shulman, *Star-Autonomous Envelopes and Conservativity*, [EPTCS 353, 2021 text](https://arxiv.org/pdf/2004.08487), §10 Thm. 10.1, Cor. 10.6, Remark 10.7 | VERIFIED_SOURCE. Universal functor from a small polycategory with specified tensor/cotensor products to a star-autonomous category, preserving those products up to isomorphism, is fully faithful. This is a universal **linear** extension, not adjoining the nonlinear CCC and F/U of B. Remark 10.7 identifies an internal-hom preservation gap in older ordinary-presheaf double gluing. No SC gluing/recovery conclusion is inferred. |
| Hasegawa, *Categorical glueing and logical predicates for models of linear logic*, [author text](https://www.kurims.kyoto-u.ac.jp/~hassei/papers/full.pdf), Thms. 5.3/5.6, Apps. A/B | VERIFIED_SOURCE at statement/syntax level. Thm. 5.3 states full faithfulness of the relatively free star-autonomous extension of a small SMCC; its older proof must be qualified by the preceding Remark 10.7. Thm. 5.6 states full completeness of MILL→DILL at `∅;Δ⊢σ`; DILL has two contexts and intuitionistic tensor/unit/hom/!, rather than B's classical multiple outputs with native nonlinear CCC and U on all generated linear types. Neither statement is an equality theorem for our complete E*. |
| Hasegawa, *Girard translation and logical predicates*, JFP 10(1), 2000, [DOI](https://doi.org/10.1017/S0956796899003615), §§2–3 and Thm. 5.6 p. 86 | VERIFIED_SOURCE. Source STLC is arrow-only with βη; target uses linear arrow/! and its βη plus let-! commuting equations. `(σ→τ)°=!σ°⊸τ°`; fullness at `Γ°;∅⊢σ°` gives equality to a translated source term. Our boundary has a native linear p input, and our ambient grammar/equality contains classical dual/cotensor and nonlinear hom/product/U. No matching theorem is obtained by renaming this translation. |
| Heijltjes–Straßburger, *Proof nets and semi-star-autonomous categories*, published-version author PDF, MSCS 26(5), 2016, Def. 5.8/Thm. 5.10 p. 19; Hughes, *Simple free star-autonomous categories and full coherence*, [text](https://arxiv.org/pdf/math/0506521), §4/Thms. 2–3 | VERIFIED_SOURCE for these statements. HS's freeness requires a ∂-strict ssa target and an ssa functor with virtual-unit transformation; use published Thm. 5.10, not manuscript Thm. 5.21. Hughes quotients correct linkings by unit rewiring and gives a free star-autonomous category. Neither theorem has B's nonlinear operations/modalities. These pure comparisons are not dependencies of the attempted witness or singleton source observation. |

Reproducible source identifiers: Shulman LNL PDF SHA-256 `253d5e39a3eb0c3410a93c8443d3109721d75c80f5ea9f823c6b305e2c8b240e`; envelopes `a91e80c76cf0b211bcf4ad80c4208808c277a9847d1bf8566025ea05e3a8e668`; Hasegawa full `6635175212b0501a2ddb8c3e1bc379edab644a0d7b40a94885de42b27a2307d0`; Girard `4ea0d32679758fb67a4933ea62f81bc52dc37a880188a1d92675414e4407749f`; VGH `1ff20d34d6ee16b9722d3c05fc0f13f440780e4840bfde9512589ec8d3a51320`; Hughes `be814e88bc80ffe1af9dace01c5d903e56aefbd3f0cf5b68011b1a2f1770a698`. HS's inspected author PDF is the version archived in the supplied `heijltjes-site/pdf/2016-heijltjes-strassburger.pdf`, whose checksum was independently recomputed as `f26b991401baf30a72d6da0c7724b4e4766a0b9150d2c674f3426be03264d3fe`; the theorem numbering was checked against its actual text.

## 7. Strongest opposing argument, dependencies and stopping point

The strongest opposing argument is that ordinary classical multiplicative exponential proof normalization should recover only the atomic axiom at `p;p`: no !-boundary exists to support a persistent promotion box, and unit/modal detours ought to cancel. Our copied closed-name attempt illustrates that expectation with actual E* equalities. Nevertheless, proving it for **every** B-representative requires a calculus/comparison with exactly the native nonlinear hom/U grammar and full ambient congruence, or a complete recovery argument. None is established here. Invoking normalization in a neighboring syntax without that comparison would silently change the problem.

| Dependency | Status and role |
|---|---|
| Frozen D*, full E*, p↦p, empty proof ledger | Stipulated contract; preserved throughout |
| Singleton atomic source class | Informal direct two-leaf linking classification, supported by independently inspected VGH source equality |
| Closed-name bijection and typed detour cancellation | Informal consequences of specified universal β/η; no global reduction or equality decision assumption |
| FinSet/finite-vector-space whole-doctrine soundness | Informal structural/model argument plus inspected Shulman Prop. 3.15; not a fullness certificate |
| A definable separated closed r, or another t | **Missing:** arbitrary nonidentity model values are insufficient |
| Compact trace's missing interfaces / feedback | Exact failed construction step; no proof of impossibility claimed |
| Report 022 N≅T₀ candidate and unit-extension identification | Not assumed or needed; retain their pending independent-verification status |
| Finite-schema extraction | Separate frozen SC obligation; not settled by this test |
| Exact published mixed conservativity theorem | Not obtained from inspected statements; no novelty/open-literature claim |

The stopping condition is the explicitly isolated construction/equality obstacle in §5 and its equality-stable closed-name formulation in §2. There is no certified negative witness, no positive atomic classification, and no mechanical artifact. Failed attempts do not prove the atomic proposition or full SC. A future separated definable r would refute this frozen SC; this report leaves that question unresolved. Its scope does not address all pure boundaries, dependent/cyclic systems, arbitrary foundations, or impossibility of every finite proof core.
