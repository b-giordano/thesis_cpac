## Global evaluation
* MWE-based: P=970/1221=0.7944 R=970/1333=0.7277 F=0.7596
* Tok-based: P=1968/2442=0.8059 R=1968/2687=0.7324 F=0.7674

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1333/1333=100% pred=1221/1221=100%
* COLL: MWE-based: P=970/1221=0.7944 R=970/1333=0.7277 F=0.7596
* COLL: Tok-based: P=1968/2442=0.8059 R=1968/2687=0.7324 F=0.7674

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=311/1333=23% pred=246/1221=20%
* Continuous: MWE-based: P=217/246=0.8821 R=217/311=0.6977 F=0.7792
* Discontinuous: MWE-proportion: gold=1022/1333=77% pred=975/1221=80%
* Discontinuous: MWE-based: P=753/975=0.7723 R=753/1022=0.7368 F=0.7541

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1333/1333=100% pred=1221/1221=100%
* Multi-token: MWE-based: P=970/1221=0.7944 R=970/1333=0.7277 F=0.7596
* Single-token: MWE-proportion: gold=0/1333=0% pred=0/1221=0%
* Single-token: MWE-based: P=0/0=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1314/1333=99% pred=1218/1221=100%
* Seen-in-train: MWE-based: P=970/1218=0.7964 R=970/1314=0.7382 F=0.7662
* Unseen-in-train: MWE-proportion: gold=19/1333=1% pred=3/1221=0%
* Unseen-in-train: MWE-based: P=0/3=0.0000 R=0/19=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=827/1314=63% pred=807/1218=66%
* Variant-of-train: MWE-based: P=587/807=0.7274 R=587/827=0.7098 F=0.7185
* Identical-to-train: MWE-proportion: gold=487/1314=37% pred=411/1218=34%
* Identical-to-train: MWE-based: P=383/411=0.9319 R=383/487=0.7864 F=0.8530

