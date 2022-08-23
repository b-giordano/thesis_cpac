## Global evaluation
* MWE-based: P=2417/2829=0.8544 R=2417/2875=0.8407 F=0.8475
* Tok-based: P=5086/5830=0.8724 R=5086/5952=0.8545 F=0.8634

## Per-category evaluation (partition of Global)
* COLL: MWE-proportion: gold=2875/2875=100% pred=2829/2829=100%
* COLL: MWE-based: P=2417/2829=0.8544 R=2417/2875=0.8407 F=0.8475
* COLL: Tok-based: P=5086/5830=0.8724 R=5086/5952=0.8545 F=0.8634

## MWE continuity (partition of Global)
* Continuous: MWE-proportion: gold=380/2875=13% pred=305/2829=11%
* Continuous: MWE-based: P=303/305=0.9934 R=303/380=0.7974 F=0.8847
* Discontinuous: MWE-proportion: gold=2495/2875=87% pred=2524/2829=89%
* Discontinuous: MWE-based: P=2114/2524=0.8376 R=2114/2495=0.8473 F=0.8424

## Number of tokens (partition of Global)
* Multi-token: MWE-proportion: gold=2875/2875=100% pred=2829/2829=100%
* Multi-token: MWE-based: P=2417/2829=0.8544 R=2417/2875=0.8407 F=0.8475
* Single-token: MWE-proportion: gold=0/2875=0% pred=0/2829=0%
* Single-token: MWE-based: P=0/0=0.0000 R=0/0=0.0000 F=0.0000

## Whether seen in train (partition of Global)
* Seen-in-train: MWE-proportion: gold=2417/2875=84% pred=2824/2829=100%
* Seen-in-train: MWE-based: P=2415/2824=0.8552 R=2415/2417=0.9992 F=0.9216
* Unseen-in-train: MWE-proportion: gold=458/2875=16% pred=5/2829=0%
* Unseen-in-train: MWE-based: P=2/5=0.4000 R=2/458=0.0044 F=0.0086

## Whether identical to train (partition of Seen-in-train)
* Variant-of-train: MWE-proportion: gold=1861/2417=77% pred=2266/2824=80%
* Variant-of-train: MWE-based: P=1859/2266=0.8204 R=1859/1861=0.9989 F=0.9009
* Identical-to-train: MWE-proportion: gold=556/2417=23% pred=558/2824=20%
* Identical-to-train: MWE-based: P=556/558=0.9964 R=556/556=1.0000 F=0.9982

