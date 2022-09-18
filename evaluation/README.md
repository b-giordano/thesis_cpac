## Evaluation

This folder contains all the relevant evaluation files for our work.  
All these files were generated thanks to the [PARSEME's evaluation script](https://gitlab.com/parseme/sharedtask-data/-/tree/master/1.1/bin).

There are 4 subfolders:
* `0_french_automatic_annotation_eval`: contains the evaluation files for the initial French automatic annotation phase (a standard one on 500 randomly extracted and subtracted sentences from the training corpus and another one on the fully corrected French parallel corpus, both full and per subcorpus). Below are the results for the standard evaluation:  

| Precision | Recall | F-score |
|-----------|--------|---------|
| 0.89      | 0.74   | 0.81    |

* `1_english_projection_eval`: contains the evaluation files for the annotation projection phase from French to English (a standard one on 500 randomly extracted sentences and another one on the fully corrected English parallel corpus, both full and per subcorpus). Below are the results for the standard evaluation:  

| Base  | Precision | Recall | F-score |
|-------|-----------|--------|---------|
| MWE   | 0.49      | 0.83   | 0.62    |
| Token | 0.64      | 0.88   | 0.74    |

* `2_arabic_projection_eval`: contains the evaluation files for the annotation projection phase from English to Arabic (a standard one on 500 randomly extracted sentences and another one on the fully corrected Arabic parallel corpus, both full and per subcorpus). There are files for the simple projection (EN > AR) and the double projection (EN+FR > AR), however results are extremely close. Below are the results for the standard evaluation:

| Type   | Base  | Precision | Recall | F-score |
|--------|-------|-----------|--------|---------|
| Simple | MWE   | 0.21      | 0.40   | 0.27    |
| Simple | Token | 0.46      | 0.64   | 0.53    |
| Double | MWE   | 0.21      | 0.40   | 0.27    |
| Double | Token | 0.46      | 0.64   | 0.53    |

* `3_final_varide_eval`: contains the evaluation files for the final VarIDE automatic annotation. For each language, each annotated parallel corpus was split 80/20 (train/test). Below are the results for each language:

| Language | Precision | Recall | F-score |
|----------|-----------|--------|---------|
| FR       | 0.82      | 0.94   | 0.86    |
| EN       | 0.79      | 0.73   | 0.76    |
| AR       | 0.58      | 0.07   | 0.12    |
