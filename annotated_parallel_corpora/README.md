## Annotated Parallel Corpora

This folder contains 3 ZIP archives:
* `annotation.gold.fr.zip`: contains the full French annotated corpus,
* `projection.gold.ar.zip`: contains the full Arabic annotated corpus,
* `projection.gold.en.zip`: contains the full English annotated corpus.

Our parallel corpus is also multi-genre. Each corpus (>100k sentences) contains  
sentences from 4 different parallel corpora:
* [GlobalVoices v2018q4](https://opus.nlpl.eu/GlobalVoices.php),
* [TED2020](https://opus.nlpl.eu/TED2020.php),
* [United Nations Parallel Corpus](https://conferences.unite.un.org/uncorpus),
* [WikiMatrix v1](https://opus.nlpl.eu/WikiMatrix.php).

All corpora are in the `cupt` format, an extended CoNLL format used by [PARSEME](https://typo.uni-konstanz.de/parseme/).  
Below is a sentence in the `cupt` format. The main difference with a standard CoNLL file is the 11th column `PARSEME:MWE`. Our annotations (`X:COLL`) go in this column.

```
# global.columns = ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC PARSEME:MWE
# source_sent_id = WM/WM.tri.fr::1
# text = La découverte de ces similitudes offre l'espoir d'avancées thérapeutiques qui pourraient améliorer simultanément de nombreuses maladies,.
1	La	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	_	_	*
2	découverte	découverte	NOUN	_	Gender=Fem|Number=Sing	6	nsubj	_	_	*
3	de	de	ADP	_	_	5	case	_	_	*
4	ces	ce	DET	_	Number=Plur|PronType=Dem	5	det	_	_	*
5	similitudes	similitude	NOUN	_	Gender=Fem|Number=Plur	2	nmod	_	_	*
6	offre	offrir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_	*
7	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	8	det	_	_	*
8	espoir	espoir	NOUN	_	Gender=Masc|Number=Sing	6	obj	_	_	*
9	d'	de	ADP	_	_	10	case	_	_	*
10	avancées	avancée	NOUN	_	Gender=Fem|Number=Plur	8	nmod	_	_	*
11	thérapeutiques	thérapeutique	ADJ	_	Gender=Fem|Number=Plur	10	amod	_	_	*
12	qui	qui	PRON	_	PronType=Rel	13	nsubj	_	_	*
13	pourraient	pouvoir	VERB	_	Mood=Cnd|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	10	acl:relcl	_	_	*
14	améliorer	améliorer	VERB	_	VerbForm=Inf	13	xcomp	_	_	*
15	simultanément	simultanément	ADV	_	_	14	advmod	_	_	*
16	de	un	DET	_	Definite=Ind|Number=Plur|PronType=Art	18	det	_	_	*
17	nombreuses	nombreux	ADJ	_	Gender=Fem|Number=Plur	18	amod	_	_	*
18	maladies	maladie	NOUN	_	Gender=Fem|Number=Plur	14	obj	_	_	*
19	,	,	PUNCT	_	_	6	punct	_	_	*
20	.	.	PUNCT	_	_	6	punct	_	_	*
```
