## Global evaluation
* MWE-based: P=60/574=0.1045 R=60/510=0.1176 F=0.1107
* Tok-based: P=242/756=0.3201 R=242/1051=0.2303 F=0.2678

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=510/510=100% pred=289/574=50%
* COLL: MWE-based: P=56/289=0.1938 R=56/510=0.1098 F=0.1402
* COLL: Tok-based: P=161/455=0.3538 R=161/1051=0.1532 F=0.2138
* <unlabeled>: MWE-proportion: gold=0/510=0% pred=286/574=50%
* <unlabeled>: MWE-based: P=0/286=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/302=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=267/510=52% pred=473/574=82%
* Continuous: MWE-based: P=21/473=0.0444 R=21/267=0.0787 F=0.0568
* Discontinuous: MWE-proportion: gold=243/510=48% pred=101/574=18%
* Discontinuous: MWE-based: P=39/101=0.3861 R=39/243=0.1605 F=0.2267

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=510/510=100% pred=180/574=31%
* Multi-token: MWE-based: P=60/180=0.3333 R=60/510=0.1176 F=0.1739
* Single-token: MWE-proportion: gold=0/510=0% pred=394/574=69%
* Single-token: MWE-based: P=0/394=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=510/510=100% pred=75/574=13%
* Seen-in-train: MWE-based: P=57/75=0.7600 R=57/510=0.1118 F=0.1949
* Unseen-in-train: MWE-proportion: gold=0/510=0% pred=499/574=87%
* Unseen-in-train: MWE-based: P=0/499=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/510=0% pred=15/75=20%
* Variant-of-train: MWE-based: P=0/15=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=510/510=100% pred=60/75=80%
* Identical-to-train: MWE-based: P=57/60=0.9500 R=57/510=0.1118 F=0.2000

