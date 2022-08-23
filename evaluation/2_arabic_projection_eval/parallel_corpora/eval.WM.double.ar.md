## Global evaluation
* MWE-based: P=323/1820=0.1775 R=323/1609=0.2007 F=0.1884
* Tok-based: P=1092/2598=0.4203 R=1092/3460=0.3156 F=0.3605

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1609/1609=100% pred=1104/1820=61%
* COLL: MWE-based: P=301/1104=0.2726 R=301/1609=0.1871 F=0.2219
* COLL: Tok-based: P=866/1784=0.4854 R=866/3460=0.2503 F=0.3303
* <unlabeled>: MWE-proportion: gold=0/1609=0% pred=717/1820=39%
* <unlabeled>: MWE-based: P=0/717=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/815=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=669/1609=42% pred=1341/1820=74%
* Continuous: MWE-based: P=112/1341=0.0835 R=112/669=0.1674 F=0.1114
* Discontinuous: MWE-proportion: gold=940/1609=58% pred=479/1820=26%
* Discontinuous: MWE-based: P=211/479=0.4405 R=211/940=0.2245 F=0.2974

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1609/1609=100% pred=774/1820=43%
* Multi-token: MWE-based: P=323/774=0.4173 R=323/1609=0.2007 F=0.2711
* Single-token: MWE-proportion: gold=0/1609=0% pred=1046/1820=57%
* Single-token: MWE-based: P=0/1046=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1609/1609=100% pred=373/1820=20%
* Seen-in-train: MWE-based: P=318/373=0.8525 R=318/1609=0.1976 F=0.3209
* Unseen-in-train: MWE-proportion: gold=0/1609=0% pred=1447/1820=80%
* Unseen-in-train: MWE-based: P=0/1447=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/1609=0% pred=27/373=7%
* Variant-of-train: MWE-based: P=0/27=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=1609/1609=100% pred=346/373=93%
* Identical-to-train: MWE-based: P=318/346=0.9191 R=318/1609=0.1976 F=0.3253

