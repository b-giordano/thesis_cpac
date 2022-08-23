## Global evaluation
* MWE-based: P=1342/1577=0.8510 R=1342/1721=0.7798 F=0.8138
* Tok-based: P=2791/3245=0.8601 R=2791/3537=0.7891 F=0.8231

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1721/1721=100% pred=1577/1577=100%
* COLL: MWE-based: P=1342/1577=0.8510 R=1342/1721=0.7798 F=0.8138
* COLL: Tok-based: P=2791/3245=0.8601 R=2791/3537=0.7891 F=0.8231

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=200/1721=12% pred=149/1577=9%
* Continuous: MWE-based: P=146/149=0.9799 R=146/200=0.7300 F=0.8367
* Discontinuous: MWE-proportion: gold=1521/1721=88% pred=1428/1577=91%
* Discontinuous: MWE-based: P=1196/1428=0.8375 R=1196/1521=0.7863 F=0.8111

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1721/1721=100% pred=1577/1577=100%
* Multi-token: MWE-based: P=1342/1577=0.8510 R=1342/1721=0.7798 F=0.8138
* Single-token: MWE-proportion: gold=0/1721=0% pred=0/1577=0%
* Single-token: MWE-based: P=0/0=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1345/1721=78% pred=1575/1577=100%
* Seen-in-train: MWE-based: P=1340/1575=0.8508 R=1340/1345=0.9963 F=0.9178
* Unseen-in-train: MWE-proportion: gold=376/1721=22% pred=2/1577=0%
* Unseen-in-train: MWE-based: P=2/2=1.0000 R=2/376=0.0053 F=0.0106

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=1116/1345=83% pred=1339/1575=85%
* Variant-of-train: MWE-based: P=1112/1339=0.8305 R=1112/1116=0.9964 F=0.9059
* Identical-to-train: MWE-proportion: gold=229/1345=17% pred=236/1575=15%
* Identical-to-train: MWE-based: P=228/236=0.9661 R=228/229=0.9956 F=0.9806

