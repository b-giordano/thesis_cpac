## Global evaluation
* MWE-based: P=84/409=0.2054 R=84/211=0.3981 F=0.2710
* Tok-based: P=282/618=0.4563 R=282/440=0.6409 F=0.5331

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=211/211=100% pred=261/409=64%
* COLL: MWE-based: P=75/261=0.2874 R=75/211=0.3555 F=0.3178
* COLL: Tok-based: P=211/440=0.4795 R=211/440=0.4795 F=0.4795
* <unlabeled>: MWE-proportion: gold=0/211=0% pred=148/409=36%
* <unlabeled>: MWE-based: P=0/148=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/178=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=92/211=44% pred=294/409=72%
* Continuous: MWE-based: P=27/294=0.0918 R=27/92=0.2935 F=0.1399
* Discontinuous: MWE-proportion: gold=119/211=56% pred=115/409=28%
* Discontinuous: MWE-based: P=57/115=0.4957 R=57/119=0.4790 F=0.4872

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=211/211=100% pred=204/409=50%
* Multi-token: MWE-based: P=84/204=0.4118 R=84/211=0.3981 F=0.4048
* Single-token: MWE-proportion: gold=0/211=0% pred=205/409=50%
* Single-token: MWE-based: P=0/205=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=211/211=100% pred=94/409=23%
* Seen-in-train: MWE-based: P=84/94=0.8936 R=84/211=0.3981 F=0.5508
* Unseen-in-train: MWE-proportion: gold=0/211=0% pred=315/409=77%
* Unseen-in-train: MWE-based: P=0/315=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/211=0% pred=8/94=9%
* Variant-of-train: MWE-based: P=0/8=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=211/211=100% pred=86/94=91%
* Identical-to-train: MWE-based: P=84/86=0.9767 R=84/211=0.3981 F=0.5657

