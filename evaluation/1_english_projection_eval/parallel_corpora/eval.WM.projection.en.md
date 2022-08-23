## Global evaluation
* MWE-based: P=675/1612=0.4187 R=675/1446=0.4668 F=0.4415
* Tok-based: P=1482/2532=0.5853 R=1482/2912=0.5089 F=0.5445

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1446/1446=100% pred=1148/1612=71%
* COLL: MWE-based: P=656/1148=0.5714 R=656/1446=0.4537 F=0.5058
* COLL: Tok-based: P=1371/2036=0.6734 R=1371/2912=0.4708 F=0.5542
* <unlabeled>: MWE-proportion: gold=0/1446=0% pred=466/1612=29%
* <unlabeled>: MWE-based: P=0/466=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/498=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=251/1446=17% pred=816/1612=51%
* Continuous: MWE-based: P=93/816=0.1140 R=93/251=0.3705 F=0.1743
* Discontinuous: MWE-proportion: gold=1195/1446=83% pred=796/1612=49%
* Discontinuous: MWE-based: P=582/796=0.7312 R=582/1195=0.4870 F=0.5846

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1446/1446=100% pred=919/1612=57%
* Multi-token: MWE-based: P=675/919=0.7345 R=675/1446=0.4668 F=0.5708
* Single-token: MWE-proportion: gold=0/1446=0% pred=693/1612=43%
* Single-token: MWE-based: P=0/693=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1446/1446=100% pred=692/1612=43%
* Seen-in-train: MWE-based: P=675/692=0.9754 R=675/1446=0.4668 F=0.6314
* Unseen-in-train: MWE-proportion: gold=0/1446=0% pred=920/1612=57%
* Unseen-in-train: MWE-based: P=0/920=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/1446=0% pred=17/692=2%
* Variant-of-train: MWE-based: P=0/17=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=1446/1446=100% pred=675/692=98%
* Identical-to-train: MWE-based: P=675/675=1.0000 R=675/1446=0.4668 F=0.6365

