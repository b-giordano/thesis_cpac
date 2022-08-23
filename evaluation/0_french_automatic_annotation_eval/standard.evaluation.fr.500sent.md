## Global evaluation
* MWE-based: P=34/38=0.8947 R=34/46=0.7391 F=0.8095
* Tok-based: P=71/79=0.8987 R=71/95=0.7474 F=0.8161

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=46/46=100% pred=38/38=100%
* COLL: MWE-based: P=34/38=0.8947 R=34/46=0.7391 F=0.8095
* COLL: Tok-based: P=71/79=0.8987 R=71/95=0.7474 F=0.8161

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=6/46=13% pred=5/38=13%
* Continuous: MWE-based: P=5/5=1.0000 R=5/6=0.8333 F=0.9091
* Discontinuous: MWE-proportion: gold=40/46=87% pred=33/38=87%
* Discontinuous: MWE-based: P=29/33=0.8788 R=29/40=0.7250 F=0.7945

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=46/46=100% pred=38/38=100%
* Multi-token: MWE-based: P=34/38=0.8947 R=34/46=0.7391 F=0.8095
* Single-token: MWE-proportion: gold=0/46=0% pred=0/38=0%
* Single-token: MWE-based: P=0/0=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=34/46=74% pred=38/38=100%
* Seen-in-train: MWE-based: P=34/38=0.8947 R=34/34=1.0000 F=0.9444
* Unseen-in-train: MWE-proportion: gold=12/46=26% pred=0/38=0%
* Unseen-in-train: MWE-based: P=0/0=0.0000 R=0/12=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=26/34=76% pred=30/38=79%
* Variant-of-train: MWE-based: P=26/30=0.8667 R=26/26=1.0000 F=0.9286
* Identical-to-train: MWE-proportion: gold=8/34=24% pred=8/38=21%
* Identical-to-train: MWE-based: P=8/8=1.0000 R=8/8=1.0000 F=1.0000

