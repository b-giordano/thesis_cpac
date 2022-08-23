## Global evaluation
* MWE-based: P=90/182=0.4945 R=90/108=0.8333 F=0.6207
* Tok-based: P=192/299=0.6421 R=192/217=0.8848 F=0.7442

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=108/108=100% pred=138/182=76%
* COLL: MWE-based: P=88/138=0.6377 R=88/108=0.8148 F=0.7154
* COLL: Tok-based: P=181/249=0.7269 R=181/217=0.8341 F=0.7768
* <unlabeled>: MWE-proportion: gold=0/108=0% pred=44/182=24%
* <unlabeled>: MWE-based: P=0/44=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/50=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=15/108=14% pred=84/182=46%
* Continuous: MWE-based: P=14/84=0.1667 R=14/15=0.9333 F=0.2828
* Discontinuous: MWE-proportion: gold=93/108=86% pred=98/182=54%
* Discontinuous: MWE-based: P=76/98=0.7755 R=76/93=0.8172 F=0.7958

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=108/108=100% pred=117/182=64%
* Multi-token: MWE-based: P=90/117=0.7692 R=90/108=0.8333 F=0.8000
* Single-token: MWE-proportion: gold=0/108=0% pred=65/182=36%
* Single-token: MWE-based: P=0/65=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=108/108=100% pred=94/182=52%
* Seen-in-train: MWE-based: P=90/94=0.9574 R=90/108=0.8333 F=0.8911
* Unseen-in-train: MWE-proportion: gold=0/108=0% pred=88/182=48%
* Unseen-in-train: MWE-based: P=0/88=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/108=0% pred=4/94=4%
* Variant-of-train: MWE-based: P=0/4=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=108/108=100% pred=90/94=96%
* Identical-to-train: MWE-based: P=90/90=1.0000 R=90/108=0.8333 F=0.9091

