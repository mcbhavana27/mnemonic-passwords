# German Mnemonic Passwords

Generate easy-to-type passwords with Python 3. 

Inspired by this project: http://edoceo.com/utilitas/mnemonic-password-generator

## Quick start

```
make passwords 
```

### Prerrequesites

  - Gnu Make
  - Python 3.6 
  - Requirements as per `requirements.txt`

### Components


```
 python3.6 ./passwords.py --passwords=5 --length=4 --wordlist=list.txt
```

Writes 5 passwords, each made by concatenating 4 random words from `list.txt` (one word per line) with `-`.



```
 python3.6 ./makelist.py --filename list.txt --inputfile wortliste.txt
```

Reads wortliste.txt, converts it to lower-case, changes umlauts to non-umlaut transcriptions (ä -> ae etc), 
remove accents, makes it contain unique words, writes to list.txt



## Where to get german word lists

    - http://www1.ids-mannheim.de/kl/projekte/methoden/derewo.html 
    - https://github.com/davidak/wortliste/blob/master/wortliste-generieren.sh
