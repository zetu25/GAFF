# GAFF
Generateur Automatique de Fotes de Français

Ce projet est dans le cadre de la réalisation d'un générateur de "fotes" de français

## Projets connexes

Dans le répertoire "Papiers" se trouve des papiers de recherches sur l'orthographe français
* *Des corpus d'erreurs pour TRACE*
* *Typologie des modifications dans les révisions de Wikipédia*
* *Comparaison de types d erreurs orthographiques en FLM et FLE*
* *Identifier les erreurs : une typologie des erreurs* & *Typologie erreurs CATACH*
    * A partir du chapitre 6, la fin n'est pas la même
* *Quelle typologie adopter pour l analyse des erreurs orthographiques des apprenants du FLE*

Plus sur ce qui est du Seq2Seq :
* *Sequence to Sequence Learning with Neural Networks*
* *Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation*

Autre :
* *Liste orthographique de base*

## Corpus

Des travaux sur la langue française existe déjà, notamment :

* [Wikipedia Correction and Paraphrase Corpus (WiCoPaCo)]()
    * Corpus extrait de la totalité des sites [Wikimedia Foundation, Inc](https://wikimediafoundation.org/) (Wikipédia, Wikilivres, Wikinews, etc...)

* [Corpus LARA](https://github.com/fauconnier/corpus-LARA)

* [frWac](https://corpora.dipintra.it/public/run.cgi/corp_info?corpname=frwac_full)
    * Le corpus frWaC est un corpus de textes français collectés dans le domaine *.fr* avec l'utilisation de mots de moyenne fréquence du corpus Le Monde Diplomatique et de listes de vocabulaire français de base comme la sémantique. Le corpus se compose de sites Web français d'une taille totale de 1,3 milliard de mots.
    * [autre source](https://www.sketchengine.eu/frwac-french-corpus/)

## Recherche, code & developpement
### Recherches

Les debuts de tests et d'appropriation de Keras se sont fait principalement à l'aide du code en exemple dans la documentation Keras.
Plus précisement la partie qui concerne le [Seq2Ses d'entrainement Keras](https://keras.io/examples/lstm_seq2seq/) et le [Seq2Seq prédictif](https://keras.io/examples/lstm_seq2seq_restore/).
J'ai pu aussi tester la [génération de texte par LSTM](https://keras.io/examples/lstm_text_generation/) en changeant le dataset par du contenue venant du dataset Wikiquote.

### Developpement

#### Prérequis

Avant de pouvoir utiliser certains fichiers, il faut disposer des librairies suivante :
[ ! ] *L'utilisation d'un venv est fortement conseillé*

* Pip
```
sudo apt install python3-pip
```

* LXML
```
pip3 install lxml
```

* Scipy

```
pip3 install numpy scipy matplotlib ipython jupyter pandas sympy nose
```

#### Enumération des fichiers utilitaires

Après avoir navigué dans et utilisé différent corpus, différent fichier de dévellopement ont été développé, notamment :

* **XML strainer**. Permet d'extraire le contenu des balises "modif" dans le corpus v1 ou v2 de WiCoPaCo en un fichier .csv ou .txt. *Si extraction en .txt, alors utilisation possible du corpus_breaker.py à l'issue*

* **Corpus breaker**. Permet de diviser un gros corpus en des "corpus" plus petit. Le corpus en entrée doit être extrait au préalable et dois respecter un format bien spécifique pour être segmenté en fichiers de n lignes souhaités.

## Outils

* [Grammalecte](https://grammalecte.net/)
