## Global evaluation
* MWE-based: P=376/2833=0.1327 R=376/1985=0.1894 F=0.1561
* Tok-based: P=1374/4100=0.3351 R=1374/4128=0.3328 F=0.3340

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1985/1985=100% pred=1811/2833=64%
* COLL: MWE-based: P=322/1811=0.1778 R=322/1985=0.1622 F=0.1697
* COLL: Tok-based: P=1000/2865=0.3490 R=1000/4128=0.2422 F=0.2860
* <unlabeled>: MWE-proportion: gold=0/1985=0% pred=1024/2833=36%
* <unlabeled>: MWE-based: P=0/1024=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/1237=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=586/1985=30% pred=2125/2833=75%
* Continuous: MWE-based: P=93/2125=0.0438 R=93/586=0.1587 F=0.0686
* Discontinuous: MWE-proportion: gold=1399/1985=70% pred=708/2833=25%
* Discontinuous: MWE-based: P=283/708=0.3997 R=283/1399=0.2023 F=0.2686

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1985/1985=100% pred=1241/2833=44%
* Multi-token: MWE-based: P=376/1241=0.3030 R=376/1985=0.1894 F=0.2331
* Single-token: MWE-proportion: gold=0/1985=0% pred=1592/2833=56%
* Single-token: MWE-based: P=0/1592=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1985/1985=100% pred=403/2833=14%
* Seen-in-train: MWE-based: P=363/403=0.9007 R=363/1985=0.1829 F=0.3040
* Unseen-in-train: MWE-proportion: gold=0/1985=0% pred=2430/2833=86%
* Unseen-in-train: MWE-based: P=0/2430=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/1985=0% pred=21/403=5%
* Variant-of-train: MWE-based: P=0/21=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=1985/1985=100% pred=382/403=95%
* Identical-to-train: MWE-based: P=363/382=0.9503 R=363/1985=0.1829 F=0.3067

