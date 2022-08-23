## Global evaluation
* MWE-based: P=296/1256=0.2357 R=296/1609=0.1840 F=0.2066
* Tok-based: P=940/1950=0.4821 R=940/3460=0.2717 F=0.3475

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=1609/1609=100% pred=851/1256=68%
* COLL: MWE-based: P=277/851=0.3255 R=277/1609=0.1722 F=0.2252
* COLL: Tok-based: P=778/1460=0.5329 R=778/3460=0.2249 F=0.3163
* <unlabeled>: MWE-proportion: gold=0/1609=0% pred=405/1256=32%
* <unlabeled>: MWE-based: P=0/405=0.0000 R=0/0=0.0000 F=0.0000
* <unlabeled>: Tok-based: P=0/490=0.0000 R=0/0=0.0000 F=0.0000

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=669/1609=42% pred=837/1256=67%
* Continuous: MWE-based: P=102/837=0.1219 R=102/669=0.1525 F=0.1355
* Discontinuous: MWE-proportion: gold=940/1609=58% pred=419/1256=33%
* Discontinuous: MWE-based: P=194/419=0.4630 R=194/940=0.2064 F=0.2855

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=1609/1609=100% pred=694/1256=55%
* Multi-token: MWE-based: P=296/694=0.4265 R=296/1609=0.1840 F=0.2571
* Single-token: MWE-proportion: gold=0/1609=0% pred=562/1256=45%
* Single-token: MWE-based: P=0/562=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=1609/1609=100% pred=346/1256=28%
* Seen-in-train: MWE-based: P=293/346=0.8468 R=293/1609=0.1821 F=0.2997
* Unseen-in-train: MWE-proportion: gold=0/1609=0% pred=910/1256=72%
* Unseen-in-train: MWE-based: P=0/910=0.0000 R=0/0=0.0000 F=0.0000

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=0/1609=0% pred=25/346=7%
* Variant-of-train: MWE-based: P=0/25=0.0000 R=0/0=0.0000 F=0.0000
* Identical-to-train: MWE-proportion: gold=1609/1609=100% pred=321/346=93%
* Identical-to-train: MWE-based: P=293/321=0.9128 R=293/1609=0.1821 F=0.3036

