## Global evaluation
* MWE-based: P=573/1414=0.4052 R=573/1508=0.3800 F=0.3922
* Tok-based: P=1240/2224=0.5576 R=1240/3037=0.4083 F=0.4714

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1508/1508=100% pred=1006/1414=71%
* COLL: MWE-based: P=547/1006=0.5437 R=547/1508=0.3627 F=0.4352
* COLL: Tok-based: P=1132/1761=0.6428 R=1132/3037=0.3727 F=0.4719
* <unlabeled>: MWE-proportion: gold=0/1508=0% pred=409/1414=29%
* <unlabeled>: MWE-based: P=0/409=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/464=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=360/1508=24% pred=785/1414=56%
* Continuous: MWE-based: P=143/785=0.1822 R=143/360=0.3972 F=0.2498
* Discontinuous: MWE-proportion: gold=1148/1508=76% pred=629/1414=44%
* Discontinuous: MWE-based: P=430/629=0.6836 R=430/1148=0.3746 F=0.4840

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1508/1508=100% pred=809/1414=57%
* Multi-token: MWE-based: P=573/809=0.7083 R=573/1508=0.3800 F=0.4946
* Single-token: MWE-proportion: gold=0/1508=0% pred=605/1414=43%
* Single-token: MWE-based: P=0/605=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1508/1508=100% pred=602/1414=43%
* Seen-in-train: MWE-based: P=573/602=0.9518 R=573/1508=0.3800 F=0.5431
* Unseen-in-train: MWE-proportion: gold=0/1508=0% pred=812/1414=57%
* Unseen-in-train: MWE-based: P=0/812=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/1508=0% pred=29/602=5%
* Variant-of-train: MWE-based: P=0/29=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=1508/1508=100% pred=573/602=95%
* Identical-to-train: MWE-based: P=573/573=1.0000 R=573/1508=0.3800 F=0.5507

