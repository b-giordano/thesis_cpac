## Global evaluation
* MWE-based: P=1423/1733=0.8211 R=1423/1517=0.9380 F=0.8757
* Tok-based: P=2935/3564=0.8235 R=2935/3122=0.9401 F=0.8780

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1517/1517=100% pred=1733/1733=100%
* COLL: MWE-based: P=1423/1733=0.8211 R=1423/1517=0.9380 F=0.8757
* COLL: Tok-based: P=2935/3564=0.8235 R=2935/3122=0.9401 F=0.8780

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=164/1517=11% pred=146/1733=8%
* Continuous: MWE-based: P=140/146=0.9589 R=140/164=0.8537 F=0.9032
* Discontinuous: MWE-proportion: gold=1353/1517=89% pred=1587/1733=92%
* Discontinuous: MWE-based: P=1283/1587=0.8084 R=1283/1353=0.9483 F=0.8728

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1517/1517=100% pred=1733/1733=100%
* Multi-token: MWE-based: P=1423/1733=0.8211 R=1423/1517=0.9380 F=0.8757
* Single-token: MWE-proportion: gold=0/1517=0% pred=0/1733=0%
* Single-token: MWE-based: P=0/0=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1472/1517=97% pred=1728/1733=100%
* Seen-in-train: MWE-based: P=1421/1728=0.8223 R=1421/1472=0.9654 F=0.8881
* Unseen-in-train: MWE-proportion: gold=45/1517=3% pred=5/1733=0%
* Unseen-in-train: MWE-based: P=2/5=0.4000 R=2/45=0.0444 F=0.0800

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=782/1472=53% pred=1052/1728=61%
* Variant-of-train: MWE-based: P=754/1052=0.7167 R=754/782=0.9642 F=0.8222
* Identical-to-train: MWE-proportion: gold=690/1472=47% pred=676/1728=39%
* Identical-to-train: MWE-based: P=667/676=0.9867 R=667/690=0.9667 F=0.9766

