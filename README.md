# Parallel Corpora & Annotation of Collocations
## Master's Thesis, University of Strasbourg
### Supervisors: 
* Amalia Todirascu (University of Strasbourg) 
* Frédéric Imbert (Aix-Marseille University)

#### Abstract

Multiword expressions (MWEs) are pervasive in language. Their heterogeneous nature makes them especially difficult to identify with Natural Language Processing (NLP) tools and techniques. Even though numerous methodologies have been considered over the years, automatic MWE identification is still challenging nowadays. Among the several MWE categories (idioms, compounds, named entities…), collocations are defined as recurrent arbitrary word combinations appearing more often than chance. Unfortunately, the number of resources annotated for collocations, even more so in multilingual parallel corpora, is incredibly scarce. This thesis presents a methodology for the semi-automatic annotation of verb-noun collocations in a multi-genre corpus in French, as well as a methodology for projecting these same annotations onto two parallel corpora in English and Arabic.

__Keywords__: natural language processing, collocations, multiword expressions, annotation, parallel corpora

#### Contents

In this GitHub repository, one can find:
* the fully annotated parallel corpora in `./annotated_parallel_corpora`,
* the annotation guidelines in `./annotation_guidelines`,
* the evaluation of our work (automatic annotation and automatic projection) in `./evaluation`,
* the manuscript for the Master's thesis in `./manuscript` (as well as the slides used during its defense),
* some scripts developped during the project in `./scripts`,
* and the training corpus used for the French automatic annotation with VarIDE in `./train_corpus`.

