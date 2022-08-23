## Global evaluation
* MWE-based: P=77/133=0.5789 R=77/1173=0.0656 F=0.1179
* Tok-based: P=158/266=0.5940 R=158/2453=0.0644 F=0.1162

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1173/1173=100% pred=133/133=100%
* COLL: MWE-based: P=77/133=0.5789 R=77/1173=0.0656 F=0.1179
* COLL: Tok-based: P=158/266=0.5940 R=158/2453=0.0644 F=0.1162

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=429/1173=37% pred=62/133=47%
* Continuous: MWE-based: P=41/62=0.6613 R=41/429=0.0956 F=0.1670
* Discontinuous: MWE-proportion: gold=744/1173=63% pred=71/133=53%
* Discontinuous: MWE-based: P=36/71=0.5070 R=36/744=0.0484 F=0.0883

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1173/1173=100% pred=133/133=100%
* Multi-token: MWE-based: P=77/133=0.5789 R=77/1173=0.0656 F=0.1179
* Single-token: MWE-proportion: gold=0/1173=0% pred=0/133=0%
* Single-token: MWE-based: P=0/0=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1113/1173=95% pred=133/133=100%
* Seen-in-train: MWE-based: P=77/133=0.5789 R=77/1113=0.0692 F=0.1236
* Unseen-in-train: MWE-proportion: gold=60/1173=5% pred=0/133=0%
* Unseen-in-train: MWE-based: P=0/0=0.0000 R=0/60=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=779/1113=70% pred=114/133=86%
* Variant-of-train: MWE-based: P=62/114=0.5439 R=62/779=0.0796 F=0.1389
* Identical-to-train: MWE-proportion: gold=334/1113=30% pred=19/133=14%
* Identical-to-train: MWE-based: P=15/19=0.7895 R=15/334=0.0449 F=0.0850

