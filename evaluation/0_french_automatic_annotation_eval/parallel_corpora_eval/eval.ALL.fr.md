## Global evaluation
* MWE-based: P=5947/6968=0.8535 R=5947/7211=0.8247 F=0.8388
* Tok-based: P=12396/14330=0.8650 R=12396/14843=0.8351 F=0.8498

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=7211/7211=100% pred=6968/6968=100%
* COLL: MWE-based: P=5947/6968=0.8535 R=5947/7211=0.8247 F=0.8388
* COLL: Tok-based: P=12396/14330=0.8650 R=12396/14843=0.8351 F=0.8498

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=749/7211=10% pred=586/6968=8%
* Continuous: MWE-based: P=578/586=0.9863 R=578/749=0.7717 F=0.8659
* Discontinuous: MWE-proportion: gold=6462/7211=90% pred=6382/6968=92%
* Discontinuous: MWE-based: P=5369/6382=0.8413 R=5369/6462=0.8309 F=0.8360

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=7211/7211=100% pred=6968/6968=100%
* Multi-token: MWE-based: P=5947/6968=0.8535 R=5947/7211=0.8247 F=0.8388
* Single-token: MWE-proportion: gold=0/7211=0% pred=0/6968=0%
* Single-token: MWE-based: P=0/0=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=5948/7211=82% pred=6951/6968=100%
* Seen-in-train: MWE-based: P=5937/6951=0.8541 R=5937/5948=0.9982 F=0.9205
* Unseen-in-train: MWE-proportion: gold=1263/7211=18% pred=17/6968=0%
* Unseen-in-train: MWE-based: P=10/17=0.5882 R=10/1263=0.0079 F=0.0156

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=4822/5948=81% pred=5814/6951=84%
* Variant-of-train: MWE-based: P=4812/5814=0.8277 R=4812/4822=0.9979 F=0.9049
* Identical-to-train: MWE-proportion: gold=1126/5948=19% pred=1137/6951=16%
* Identical-to-train: MWE-based: P=1125/1137=0.9894 R=1125/1126=0.9991 F=0.9943

