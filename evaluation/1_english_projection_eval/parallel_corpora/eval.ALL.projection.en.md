## Global evaluation
* MWE-based: P=2485/6201=0.4007 R=2485/5976=0.4158 F=0.4081
* Tok-based: P=5532/9557=0.5788 R=5532/12045=0.4593 F=0.5122

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=5976/5976=100% pred=4458/6201=72%
* COLL: MWE-based: P=2403/4458=0.5390 R=2403/5976=0.4021 F=0.4606
* COLL: Tok-based: P=5057/7636=0.6623 R=5057/12045=0.4198 F=0.5139
* <unlabeled>: MWE-proportion: gold=0/5976=0% pred=1750/6201=28%
* <unlabeled>: MWE-based: P=0/1750=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/1928=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=1320/5976=22% pred=3473/6201=56%
* Continuous: MWE-based: P=499/3473=0.1437 R=499/1320=0.3780 F=0.2082
* Discontinuous: MWE-proportion: gold=4656/5976=78% pred=2728/6201=44%
* Discontinuous: MWE-based: P=1986/2728=0.7280 R=1986/4656=0.4265 F=0.5379

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=5975/5976=100% pred=3348/6201=54%
* Multi-token: MWE-based: P=2484/3348=0.7419 R=2484/5975=0.4157 F=0.5329
* Single-token: MWE-proportion: gold=1/5976=0% pred=2853/6201=46%
* Single-token: MWE-based: P=1/2853=0.0004 R=1/1=1.0000 F=0.0007

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=5976/5976=100% pred=2586/6201=42%
* Seen-in-train: MWE-based: P=2485/2586=0.9609 R=2485/5976=0.4158 F=0.5805
* Unseen-in-train: MWE-proportion: gold=0/5976=0% pred=3615/6201=58%
* Unseen-in-train: MWE-based: P=0/3615=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/5976=0% pred=93/2586=4%
* Variant-of-train: MWE-based: P=0/93=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=5976/5976=100% pred=2493/2586=96%
* Identical-to-train: MWE-based: P=2485/2493=0.9968 R=2485/5976=0.4158 F=0.5868

