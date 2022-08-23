## Global evaluation
* MWE-based: P=168/1124=0.1495 R=168/1238=0.1357 F=0.1423
* Tok-based: P=620/1577=0.3932 R=620/2585=0.2398 F=0.2979

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1238/1238=100% pred=686/1124=61%
* COLL: MWE-based: P=154/686=0.2245 R=154/1238=0.1244 F=0.1601
* COLL: Tok-based: P=455/1092=0.4167 R=455/2585=0.1760 F=0.2475
* <unlabeled>: MWE-proportion: gold=0/1238=0% pred=438/1124=39%
* <unlabeled>: MWE-based: P=0/438=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/485=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=513/1238=41% pred=884/1124=79%
* Continuous: MWE-based: P=68/884=0.0769 R=68/513=0.1326 F=0.0974
* Discontinuous: MWE-proportion: gold=725/1238=59% pred=240/1124=21%
* Discontinuous: MWE-based: P=100/240=0.4167 R=100/725=0.1379 F=0.2073

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1238/1238=100% pred=453/1124=40%
* Multi-token: MWE-based: P=168/453=0.3709 R=168/1238=0.1357 F=0.1987
* Single-token: MWE-proportion: gold=0/1238=0% pred=671/1124=60%
* Single-token: MWE-based: P=0/671=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1238/1238=100% pred=196/1124=17%
* Seen-in-train: MWE-based: P=167/196=0.8520 R=167/1238=0.1349 F=0.2329
* Unseen-in-train: MWE-proportion: gold=0/1238=0% pred=928/1124=83%
* Unseen-in-train: MWE-based: P=0/928=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/1238=0% pred=17/196=9%
* Variant-of-train: MWE-based: P=0/17=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=1238/1238=100% pred=179/196=91%
* Identical-to-train: MWE-based: P=167/179=0.9330 R=167/1238=0.1349 F=0.2357

