## Annotated Parallel Corpora

### Contents
This folder contains 3 ZIP archives:
* `annotation.gold.fr.zip`: contains the full French annotated corpus,
* `projection.gold.ar.zip`: contains the full Arabic annotated corpus,
* `projection.gold.en.zip`: contains the full English annotated corpus.

Our parallel corpus is also multi-genre. Each corpus (>100k sentences) contains sentences from 4 different parallel corpora:
* [GlobalVoices v2018q4](https://opus.nlpl.eu/GlobalVoices.php),
* [TED2020](https://opus.nlpl.eu/TED2020.php),
* [United Nations Parallel Corpus](https://conferences.unite.un.org/uncorpus),
* [WikiMatrix v1](https://opus.nlpl.eu/WikiMatrix.php).

### Quick description of the `cupt` format
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

### Statistics of the corpora
#### Number of tokens, sentences and annotations per language  

| Language | FR        | EN        | AR     |
|----------|-----------|-----------|-------|
| Tokens       | 3,358,017 | 2,920,239 | 2,904,790 |
| Sentences       | 105,731 | 105,731   | 105,731 |
| Annotations       | 7,211     | 5,976     | 5,342 |

#### Number of annotations per subcorpus per language

| Subcorpus      | FR    | EN    | AR    |
|----------------|-------|-------|-------|
| GlobalVoices   | 1,721 | 1,508 | 1,238 |
| TED            | 768   | 745   | 510   |
| United Nations | 2,875 | 2,277 | 1,985 |
| WikiMatrix     | 1,847 | 1,446 | 1,609 |

#### Most frequent collocations per subcorpus per language

| Subcorpus      | FR                                                                        | EN                                                                  | AR                                                       |
|----------------|---------------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------|
| GlobalVoices   | histoire,raconter (82)<br/>attention,attirer (70)<br/>jouer,rôle (68)     | story,tell (84)<br/>play,role (76)<br/>ask,question (37)            | دور،لعب (54)<br/>تحدّث،لعة (29)<br/>روى،قصّة (26)        |
| TED            | poser,question (99)<br/>histoire,raconter (79)<br/>problème,résoudre (66) | story,tell (89)<br/>ask,question (72)<br/>decision,make (58)        | مشكلة،واجه (29)<br/>سؤال،طرح (28)<br/>طريقة،وجد (21)     |
| United Nations | mesure,prendre (421)<br/>jouer,rôle (245)<br/>adopter,résolution (118)    | assistance,provide (211)<br/>play,role (159)<br/>measure,take (130) | قدّم،مساعدة (164)<br/>بذل،جهد (139)<br/>اتّخذ،قرار (100) |
| WikiMatrix     | jouer,rôle (111)<br/>prix,recevoir (79)<br/>occuper,poste (45)            | play,role (87)<br/>publish,work (31)<br/>book,publish (31)          | شغل،منصب (104)<br/>دور،لعب (99)<br/>حصل،على،جائزة (64)   |
| Full corpus    | mesure,prendre (485)<br/>jouer,rôle (448)<br/>décision,prendre (209)      | play,role (342)<br/>assistance,provide (236)<br/>story,tell (182)   | دور،لعب (203)<br/>قدّم،مساعدة (188)<br/>بذل،جهد (173)    |

