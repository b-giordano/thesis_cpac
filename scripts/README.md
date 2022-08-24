## Scripts

### Python scripts
This folder contains the main Python scripts used during the project:
* Creation of `conll` files from plain text, then into `cupt` files (prefix `0X_`),
* Extraction and classification of annotations, as well as identification of unique patterns (prefix `1X_`),
* Creation of regular expressions from lists of collocation patterns for the manual corpus curation (prefix `2X_`),
* Projection of annotations according to alignment files (prefix `3X_`).

Evaluation work and `cupt` validation were done with PARSEME's scripts.
Many menial tasks were done with really short and simple programs. Those are not included here.

### ZAP (Java projection tool)
The subfolder `./java_zap` consists of the two Java classes needed to do the annotation projection (to generate alignment files). The two of them need to be in the ZAP framework:
* `Language.java`: simple edited enum to be able to use the Arabic translation table. This class needs to replace that of ZAP's original framework.
* `CpacGetAlignments.java`: the class to generate the alignments files. Can be inserted in `zap/src/main/java/zalando.analytics/annotation.transfer` in ZAP's original framework.

Moreover, to be able to project English annotations onto an Arabic file, a translation table is needed. The one we created and used is hosted [here](https://seafile.unistra.fr/f/27f8add9bd0d4b30aee7/?dl=1). 
The archive must be unzipped and the `arabic-hmm.dict` file must be placed in `zap/src/main/resources` in ZAP's original framework.
