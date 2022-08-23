## Global evaluation
* MWE-based: P=84/405=0.2074 R=84/211=0.3981 F=0.2727
* Tok-based: P=280/609=0.4598 R=280/440=0.6364 F=0.5338

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=211/211=100% pred=261/405=64%
* COLL: MWE-based: P=75/261=0.2874 R=75/211=0.3555 F=0.3178
* COLL: Tok-based: P=211/439=0.4806 R=211/440=0.4795 F=0.4801
* <unlabeled>: MWE-proportion: gold=0/211=0% pred=144/405=36%
* <unlabeled>: MWE-based: P=0/144=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/170=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=92/211=44% pred=290/405=72%
* Continuous: MWE-based: P=27/290=0.0931 R=27/92=0.2935 F=0.1414
* Discontinuous: MWE-proportion: gold=119/211=56% pred=115/405=28%
* Discontinuous: MWE-based: P=57/115=0.4957 R=57/119=0.4790 F=0.4872

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=211/211=100% pred=204/405=50%
* Multi-token: MWE-based: P=84/204=0.4118 R=84/211=0.3981 F=0.4048
* Single-token: MWE-proportion: gold=0/211=0% pred=201/405=50%
* Single-token: MWE-based: P=0/201=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=211/211=100% pred=94/405=23%
* Seen-in-train: MWE-based: P=84/94=0.8936 R=84/211=0.3981 F=0.5508
* Unseen-in-train: MWE-proportion: gold=0/211=0% pred=311/405=77%
* Unseen-in-train: MWE-based: P=0/311=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/211=0% pred=8/94=9%
* Variant-of-train: MWE-based: P=0/8=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=211/211=100% pred=86/94=91%
* Identical-to-train: MWE-based: P=84/86=0.9767 R=84/211=0.3981 F=0.5657

