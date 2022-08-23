## Global evaluation
* MWE-based: P=364/1953=0.1864 R=364/1985=0.1834 F=0.1849
* Tok-based: P=1191/3107=0.3833 R=1191/4128=0.2885 F=0.3292

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1985/1985=100% pred=1312/1953=67%
* COLL: MWE-based: P=311/1312=0.2370 R=311/1985=0.1567 F=0.1887
* COLL: Tok-based: P=880/2280=0.3860 R=880/4128=0.2132 F=0.2747
* <unlabeled>: MWE-proportion: gold=0/1985=0% pred=641/1953=33%
* <unlabeled>: MWE-based: P=0/641=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/827=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=586/1985=30% pred=1313/1953=67%
* Continuous: MWE-based: P=90/1313=0.0685 R=90/586=0.1536 F=0.0948
* Discontinuous: MWE-proportion: gold=1399/1985=70% pred=640/1953=33%
* Discontinuous: MWE-based: P=274/640=0.4281 R=274/1399=0.1959 F=0.2688

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1985/1985=100% pred=1154/1953=59%
* Multi-token: MWE-based: P=364/1154=0.3154 R=364/1985=0.1834 F=0.2319
* Single-token: MWE-proportion: gold=0/1985=0% pred=799/1953=41%
* Single-token: MWE-based: P=0/799=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1985/1985=100% pred=391/1953=20%
* Seen-in-train: MWE-based: P=351/391=0.8977 R=351/1985=0.1768 F=0.2955
* Unseen-in-train: MWE-proportion: gold=0/1985=0% pred=1562/1953=80%
* Unseen-in-train: MWE-based: P=0/1562=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/1985=0% pred=20/391=5%
* Variant-of-train: MWE-based: P=0/20=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=1985/1985=100% pred=371/391=95%
* Identical-to-train: MWE-based: P=351/371=0.9461 R=351/1985=0.1768 F=0.2980

