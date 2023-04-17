# Interactive Ideophone Lexicon (Demo)

A database structure and pipeline for building interactive, online lexicons of ideophones, that can be enriched with multimedia and experimental data from psycholinguistic research. This demo uses Japanese as an example. The database is structured with the ideal of having one Github repository per language, with the possibility to then curate and aggregate data from several languages using software provided in IdeoNet (similar to projects like [Lexibank](https://github.com/lexibank/pylexibank)). The database structure is based on and conforms to [CLDF formats](https://github.com/cldf/cldf). 

## Aims

* Make scientific research results more accessible and valuable to the communities to whom the languages belong. 
* Make research results from multiple authors findable in a central location, so that future research can build on past findings, while also identifying new theoretical questions and documentary research gaps.
* Provide a resource for language learners that addresses some of the challenges of communicating the rich, complex, multisensory meanings of ideophones through diverse multimedia, as well as interactive tools for visualising and exploring lexical structure. 

## Database structure

TSV files at the top level of the database form the core structure. The folder `lexicon` contains the html files for the online, interactive version of the database, while the file `GLOTTOCODE_index.html` (named with the glottocode for the language) provides the main webpage through which to access the webpages in the `lexicon` folder.

The interactive web version of the database is built by running the `build_lexicon.py` script, which uses the files in the `templates` folder as templates to control the visual layout and appearance of the website pages, and fills them with data contained in the .tsv files that form the core of the database.  

Additional folders can be added containing experimental data which can be integrated and visualised in the web version of the database by modifying `build_lexicon.py` and the files in the `templates` folder. The R files in each folder contain the code to compile (and if needed, analyse) the experimental data from various sources, and produce TSV files which contain summaries of the experimental results. Some examples are given with **guessing accuracies** (`guesses`), **iconicity ratings** (`iconicity_ratings`) and **sensory modality norms** (`sensory_ratings`). Other types of data that could enrich the lexicon include **measures of structural markedness** (e.g. phonotactic predictability scores for pronunciations), and **measures of semantic relatedness** between lexemes (e.g. results from pile sorting tasks). For instance, it would be good if the `paradigms.tsv` file could eventually be generated directly from the results of experimental studies (rather than being based on the intuitions of the lexicographer). 

```bash
├── language.tsv
├── lexemes.tsv
├── pronunciations.tsv
├── usages.tsv
├── examples.tsv
├── exemplars.tsv
├── paradigms.tsv
├── cognates.tsv
├── etymologies.tsv
├── metalanguage.tsv
├── build_lexicon.py
├── build_index.py
├── templates
│   ├── index.html
│   ├── lexemes.html
├── lexicon
│   ├── english
│   │   ├── indexes  
│   │        ├── domain_index.html
│   │   ├── lexemeID.html  
│   │   ├── lexemeID.html  
│   │   ├── lexemeID.html  
│   ├── orthography
│       ├── indexes  
│       ├── lexemeID.html  
│       ├── lexemeID.html  
│       ├── lexemeID.html  
├── guesses
│   ├── guesses.tsv
│   ├── source.R
├── iconicity_ratings
│   ├── iconicity_ratings.tsv
│   ├── source.R
├── sensory_ratings
│   ├── sensory_ratings.tsv
│   ├── source.R
├── sources
│   ├── sensory_ratings.tsv
│   ├── guesses.tsv
│   ├── examples.tsv
│   ├── exemplars.tsv
│   ├── usages.tsv
├── GLOTTOCODE_index.html
├── README.md
└── .gitignore
```

### languages

|column     |function|
|-----------|--------|
|fields     |specify if this is the language of the 'lexemes' or a 'lingua franca'
|language   |the preferred name of the language
|glottocode |glottocode for the language
|orthography|the language name in the native orthography 

### lexemes.tsv

The master file. Columns marked with an * must be filled in for every entry.

|column     |function                                              |
|-----------|------------------------------------------------------|
|lexemeID*  |permanent identifier for the lexeme                   |
|lexeme*    |preferred spelling of the lexeme (for lexical entries)|
|orthography|standard spelling in native orthography               |

### pronunciations.tsv

|column     |function                                              |
|-----------|------------------------------------------------------|
|lexemeID*  |refers to ID in lexemes.tsv
|ipa*       |ipa transcription
|orthography|representation in native orthography                  
|media      |reference to media demonstrating the pronunciation (in media.tsv)       

### usages.tsv

|column         |function                                              |
|---------------|------------------------------------------------------|
|lexemeID*      |refers to ID in lexemes.tsv
|usageID*       |permanent ID for this usage of the lexeme
|gloss          |short english gloss    
|gloss-ortho    |short gloss in native orthography
|gloss-lf       |short gloss in the lingua franca
|definition     |more elaborated definition in the language of the source                    
|def-eng        |translation of the definition in English (or another metalanguage) 
|definition-lf  |definition in the lingua franca
|date           |date of first attestation of this usage
|source         |source of the definition (cross-referenced to sources.tsv)
|source-lf      |source of the definition in the lingua franca
|source-date    |source of date (cross-referenced to sources.tsv)

### examples.tsv

|column         |function                                              |
|---------------|------------------------------------------------------|
|paradigmID*    |refers to ID in lexemes.tsv
|usageID*       |refers to usage ID in usages


### sources.tsv

|column         |function                                              |
|---------------|------------------------------------------------------|
|source         |source name (in other data files)                     |
|source-eng     |english translation of source name (where applicable)
|type           |type of source. One of 'example', 'example-media', 'example-trans' 'exemplar', 'definition', 'date'


