## Global evaluation
* MWE-based: P=59/485=0.1216 R=59/510=0.1157 F=0.1186
* Tok-based: P=233/657=0.3546 R=233/1051=0.2217 F=0.2728

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=510/510=100% pred=253/485=52%
* COLL: MWE-based: P=55/253=0.2174 R=55/510=0.1078 F=0.1442
* COLL: Tok-based: P=157/410=0.3829 R=157/1051=0.1494 F=0.2149
* <unlabeled>: MWE-proportion: gold=0/510=0% pred=233/485=48%
* <unlabeled>: MWE-based: P=0/233=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/248=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=267/510=52% pred=391/485=81%
* Continuous: MWE-based: P=21/391=0.0537 R=21/267=0.0787 F=0.0638
* Discontinuous: MWE-proportion: gold=243/510=48% pred=94/485=19%
* Discontinuous: MWE-based: P=38/94=0.4043 R=38/243=0.1564 F=0.2255

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=510/510=100% pred=172/485=35%
* Multi-token: MWE-based: P=59/172=0.3430 R=59/510=0.1157 F=0.1730
* Single-token: MWE-proportion: gold=0/510=0% pred=313/485=65%
* Single-token: MWE-based: P=0/313=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=510/510=100% pred=74/485=15%
* Seen-in-train: MWE-based: P=56/74=0.7568 R=56/510=0.1098 F=0.1918
* Unseen-in-train: MWE-proportion: gold=0/510=0% pred=411/485=85%
* Unseen-in-train: MWE-based: P=0/411=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/510=0% pred=15/74=20%
* Variant-of-train: MWE-based: P=0/15=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=510/510=100% pred=59/74=80%
* Identical-to-train: MWE-based: P=56/59=0.9492 R=56/510=0.1098 F=0.1968

