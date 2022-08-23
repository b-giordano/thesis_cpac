## Global evaluation
* MWE-based: P=849/2458=0.3454 R=849/2277=0.3729 F=0.3586
* Tok-based: P=1979/3596=0.5503 R=1979/4594=0.4308 F=0.4833

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=2277/2277=100% pred=1749/2458=71%
* COLL: MWE-based: P=819/1749=0.4683 R=819/2277=0.3597 F=0.4069
* COLL: Tok-based: P=1773/2816=0.6296 R=1773/4594=0.3859 F=0.4785
* <unlabeled>: MWE-proportion: gold=0/2277=0% pred=713/2458=29%
* <unlabeled>: MWE-based: P=0/713=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/784=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=604/2277=27% pred=1590/2458=65%
* Continuous: MWE-based: P=225/1590=0.1415 R=225/604=0.3725 F=0.2051
* Discontinuous: MWE-proportion: gold=1673/2277=73% pred=868/2458=35%
* Discontinuous: MWE-based: P=624/868=0.7189 R=624/1673=0.3730 F=0.4911

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=2276/2277=100% pred=1132/2458=46%
* Multi-token: MWE-based: P=848/1132=0.7491 R=848/2276=0.3726 F=0.4977
* Single-token: MWE-proportion: gold=1/2277=0% pred=1326/2458=54%
* Single-token: MWE-based: P=1/1326=0.0008 R=1/1=1.0000 F=0.0015

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=2277/2277=100% pred=882/2458=36%
* Seen-in-train: MWE-based: P=849/882=0.9626 R=849/2277=0.3729 F=0.5375
* Unseen-in-train: MWE-proportion: gold=0/2277=0% pred=1576/2458=64%
* Unseen-in-train: MWE-based: P=0/1576=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/2277=0% pred=30/882=3%
* Variant-of-train: MWE-based: P=0/30=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=2277/2277=100% pred=852/882=97%
* Identical-to-train: MWE-based: P=849/852=0.9965 R=849/2277=0.3729 F=0.5427

