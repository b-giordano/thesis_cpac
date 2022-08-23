## Global evaluation
* MWE-based: P=1504/1770=0.8497 R=1504/1847=0.8143 F=0.8316
* Tok-based: P=3105/3630=0.8554 R=3105/3777=0.8221 F=0.8384

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1847/1847=100% pred=1770/1770=100%
* COLL: MWE-based: P=1504/1770=0.8497 R=1504/1847=0.8143 F=0.8316
* COLL: Tok-based: P=3105/3630=0.8554 R=3105/3777=0.8221 F=0.8384

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=139/1847=8% pred=106/1770=6%
* Continuous: MWE-based: P=103/106=0.9717 R=103/139=0.7410 F=0.8408
* Discontinuous: MWE-proportion: gold=1708/1847=92% pred=1664/1770=94%
* Discontinuous: MWE-based: P=1401/1664=0.8419 R=1401/1708=0.8203 F=0.8310

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1847/1847=100% pred=1770/1770=100%
* Multi-token: MWE-based: P=1504/1770=0.8497 R=1504/1847=0.8143 F=0.8316
* Single-token: MWE-proportion: gold=0/1847=0% pred=0/1770=0%
* Single-token: MWE-based: P=0/0=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1503/1847=81% pred=1761/1770=99%
* Seen-in-train: MWE-based: P=1499/1761=0.8512 R=1499/1503=0.9973 F=0.9185
* Unseen-in-train: MWE-proportion: gold=344/1847=19% pred=9/1770=1%
* Unseen-in-train: MWE-based: P=5/9=0.5556 R=5/344=0.0145 F=0.0283

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=1266/1503=84% pred=1523/1761=86%
* Variant-of-train: MWE-based: P=1262/1523=0.8286 R=1262/1266=0.9968 F=0.9050
* Identical-to-train: MWE-proportion: gold=237/1503=16% pred=238/1761=14%
* Identical-to-train: MWE-based: P=237/238=0.9958 R=237/237=1.0000 F=0.9979

