## Global evaluation
* MWE-based: P=684/792=0.8636 R=684/768=0.8906 F=0.8769
* Tok-based: P=1414/1625=0.8702 R=1414/1577=0.8966 F=0.8832

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=768/768=100% pred=792/792=100%
* COLL: MWE-based: P=684/792=0.8636 R=684/768=0.8906 F=0.8769
* COLL: Tok-based: P=1414/1625=0.8702 R=1414/1577=0.8966 F=0.8832

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=30/768=4% pred=26/792=3%
* Continuous: MWE-based: P=26/26=1.0000 R=26/30=0.8667 F=0.9286
* Discontinuous: MWE-proportion: gold=738/768=96% pred=766/792=97%
* Discontinuous: MWE-based: P=658/766=0.8590 R=658/738=0.8916 F=0.8750

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=768/768=100% pred=792/792=100%
* Multi-token: MWE-based: P=684/792=0.8636 R=684/768=0.8906 F=0.8769
* Single-token: MWE-proportion: gold=0/768=0% pred=0/792=0%
* Single-token: MWE-based: P=0/0=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=683/768=89% pred=791/792=100%
* Seen-in-train: MWE-based: P=683/791=0.8635 R=683/683=1.0000 F=0.9267
* Unseen-in-train: MWE-proportion: gold=85/768=11% pred=1/792=0%
* Unseen-in-train: MWE-based: P=1/1=1.0000 R=1/85=0.0118 F=0.0233

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=579/683=85% pred=686/791=87%
* Variant-of-train: MWE-based: P=579/686=0.8440 R=579/579=1.0000 F=0.9154
* Identical-to-train: MWE-proportion: gold=104/683=15% pred=105/791=13%
* Identical-to-train: MWE-based: P=104/105=0.9905 R=104/104=1.0000 F=0.9952

