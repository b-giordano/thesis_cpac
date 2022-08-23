## Global evaluation
* MWE-based: P=928/6571=0.1412 R=928/5342=0.1737 F=0.1558
* Tok-based: P=3372/9259=0.3642 R=3372/11224=0.3004 F=0.3292

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=5342/5342=100% pred=3986/6571=61%
* COLL: MWE-based: P=834/3986=0.2092 R=834/5342=0.1561 F=0.1788
* COLL: Tok-based: P=2505/6299=0.3977 R=2505/11224=0.2232 F=0.2859
* <unlabeled>: MWE-proportion: gold=0/5342=0% pred=2589/6571=39%
* <unlabeled>: MWE-based: P=0/2589=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/2964=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=2035/5342=38% pred=5036/6571=77%
* Continuous: MWE-based: P=294/5036=0.0584 R=294/2035=0.1445 F=0.0832
* Discontinuous: MWE-proportion: gold=3307/5342=62% pred=1535/6571=23%
* Discontinuous: MWE-based: P=634/1535=0.4130 R=634/3307=0.1917 F=0.2619

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=5342/5342=100% pred=2655/6571=40%
* Multi-token: MWE-based: P=928/2655=0.3495 R=928/5342=0.1737 F=0.2321
* Single-token: MWE-proportion: gold=0/5342=0% pred=3916/6571=60%
* Single-token: MWE-based: P=0/3916=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=5342/5342=100% pred=1082/6571=16%
* Seen-in-train: MWE-based: P=906/1082=0.8373 R=906/5342=0.1696 F=0.2821
* Unseen-in-train: MWE-proportion: gold=0/5342=0% pred=5489/6571=84%
* Unseen-in-train: MWE-based: P=0/5489=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/5342=0% pred=92/1082=9%
* Variant-of-train: MWE-based: P=0/92=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=5342/5342=100% pred=990/1082=91%
* Identical-to-train: MWE-based: P=906/990=0.9152 R=906/5342=0.1696 F=0.2862

