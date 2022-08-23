## Global evaluation
* MWE-based: P=169/1344=0.1257 R=169/1238=0.1365 F=0.1309
* Tok-based: P=664/1805=0.3679 R=664/2585=0.2569 F=0.3025

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1238/1238=100% pred=782/1344=58%
* COLL: MWE-based: P=155/782=0.1982 R=155/1238=0.1252 F=0.1535
* COLL: Tok-based: P=478/1195=0.4000 R=478/2585=0.1849 F=0.2529
* <unlabeled>: MWE-proportion: gold=0/1238=0% pred=562/1344=42%
* <unlabeled>: MWE-based: P=0/562=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/610=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=513/1238=41% pred=1097/1344=82%
* Continuous: MWE-based: P=68/1097=0.0620 R=68/513=0.1326 F=0.0845
* Discontinuous: MWE-proportion: gold=725/1238=59% pred=247/1344=18%
* Discontinuous: MWE-based: P=101/247=0.4089 R=101/725=0.1393 F=0.2078

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1238/1238=100% pred=460/1344=34%
* Multi-token: MWE-based: P=169/460=0.3674 R=169/1238=0.1365 F=0.1991
* Single-token: MWE-proportion: gold=0/1238=0% pred=884/1344=66%
* Single-token: MWE-based: P=0/884=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1238/1238=100% pred=197/1344=15%
* Seen-in-train: MWE-based: P=168/197=0.8528 R=168/1238=0.1357 F=0.2341
* Unseen-in-train: MWE-proportion: gold=0/1238=0% pred=1147/1344=85%
* Unseen-in-train: MWE-based: P=0/1147=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/1238=0% pred=17/197=9%
* Variant-of-train: MWE-based: P=0/17=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=1238/1238=100% pred=180/197=91%
* Identical-to-train: MWE-based: P=168/180=0.9333 R=168/1238=0.1357 F=0.2370

