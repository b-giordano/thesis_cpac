## Global evaluation
* MWE-based: P=887/4818=0.1841 R=887/5342=0.1660 F=0.1746
* Tok-based: P=2984/7291=0.4093 R=2984/11224=0.2659 F=0.3223

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=5342/5342=100% pred=3102/4818=64%
* COLL: MWE-based: P=797/3102=0.2569 R=797/5342=0.1492 F=0.1888
* COLL: Tok-based: P=2270/5242=0.4330 R=2270/11224=0.2022 F=0.2757
* <unlabeled>: MWE-proportion: gold=0/5342=0% pred=1717/4818=36%
* <unlabeled>: MWE-based: P=0/1717=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/2050=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=2035/5342=38% pred=3425/4818=71%
* Continuous: MWE-based: P=281/3425=0.0820 R=281/2035=0.1381 F=0.1029
* Discontinuous: MWE-proportion: gold=3307/5342=62% pred=1393/4818=29%
* Discontinuous: MWE-based: P=606/1393=0.4350 R=606/3307=0.1832 F=0.2579

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=5342/5342=100% pred=2473/4818=51%
* Multi-token: MWE-based: P=887/2473=0.3587 R=887/5342=0.1660 F=0.2270
* Single-token: MWE-proportion: gold=0/5342=0% pred=2345/4818=49%
* Single-token: MWE-based: P=0/2345=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=5342/5342=100% pred=1041/4818=22%
* Seen-in-train: MWE-based: P=867/1041=0.8329 R=867/5342=0.1623 F=0.2717
* Unseen-in-train: MWE-proportion: gold=0/5342=0% pred=3777/4818=78%
* Unseen-in-train: MWE-based: P=0/3777=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/5342=0% pred=88/1041=8%
* Variant-of-train: MWE-based: P=0/88=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=5342/5342=100% pred=953/1041=92%
* Identical-to-train: MWE-based: P=867/953=0.9098 R=867/5342=0.1623 F=0.2755

