# iais-test

Sample Usage
------------

$ python disambiguator.py --help
usage: disambiguator.py [-h] [--jsonstring JSONSTRING] [--jsonfile JSONFILE]

Calls the OKBQA disambiguator web service

optional arguments:
  -h, --help            show this help message and exit
  --jsonstring JSONSTRING
                        The input json string
  --jsonfile JSONFILE   Path of the file containing the json input as string



$ python disambiguator.py --jsonfile input.json 


$ python disambiguator.py --jsonstring '{"query": "SELECT ?v4 WHERE { ?v4 ?v2 ?v6 ; ?v7 ?v3 . } ", "slots": [{"p": "is", "s": "v7", "o": "<http://lodqa.org/vocabulary/sort_of>"}, {"p": "is", "s": "v3", "o": "rdf:Class"}, {"p": "verbalization", "s": "v3", "o": "rivers"},{"p": "is", "s": "v2", "o": "rdf:Property"}, {"p": "verbalization", "s": "v2", "o": "flow"},{"p": "is", "s": "v6", "o": "rdf:Resource|rdfs:Literal"}, {"p": "verbalization", "s": "v6", "o": "Seoul"}], "score": "1.0", "question": "Which rivers flow through Seoul"}'


