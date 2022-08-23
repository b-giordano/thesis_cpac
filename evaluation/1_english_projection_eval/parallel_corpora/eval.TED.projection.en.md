## Global evaluation
* MWE-based: P=388/717=0.5411 R=388/745=0.5208 F=0.5308
* Tok-based: P=831/1205=0.6896 R=831/1502=0.5533 F=0.6140

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=745/745=100% pred=555/717=77%
* COLL: MWE-based: P=381/555=0.6865 R=381/745=0.5114 F=0.5862
* COLL: Tok-based: P=781/1023=0.7634 R=781/1502=0.5200 F=0.6186
* <unlabeled>: MWE-proportion: gold=0/745=0% pred=162/717=23%
* <unlabeled>: MWE-based: P=0/162=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/182=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=105/745=14% pred=282/717=39%
* Continuous: MWE-based: P=38/282=0.1348 R=38/105=0.3619 F=0.1964
* Discontinuous: MWE-proportion: gold=640/745=86% pred=435/717=61%
* Discontinuous: MWE-based: P=350/435=0.8046 R=350/640=0.5469 F=0.6512

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=745/745=100% pred=488/717=68%
* Multi-token: MWE-based: P=388/488=0.7951 R=388/745=0.5208 F=0.6294
* Single-token: MWE-proportion: gold=0/745=0% pred=229/717=32%
* Single-token: MWE-based: P=0/229=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=745/745=100% pred=406/717=57%
* Seen-in-train: MWE-based: P=388/406=0.9557 R=388/745=0.5208 F=0.6742
* Unseen-in-train: MWE-proportion: gold=0/745=0% pred=311/717=43%
* Unseen-in-train: MWE-based: P=0/311=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/745=0% pred=15/406=4%
* Variant-of-train: MWE-based: P=0/15=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=745/745=100% pred=391/406=96%
* Identical-to-train: MWE-based: P=388/391=0.9923 R=388/745=0.5208 F=0.6831

