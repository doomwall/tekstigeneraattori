# tekstigeneraattori
Aineopintojen harjoitustyö: Algoritmit ja tekoäly - Tekstigeneraattori

Käyttää Trie-tietorakennetta ja Markovin ketjua generoidakseen tulevia sanoja tai merkkejä annetulle inputille. Ohjelmassa on kolme eri lähdemateriaalia:
- "Books" kouluttaa ohjelman kirjoilla Moby Dick, Liisa Ihmemaassa, Ylpeys ja ennakkoluulo ja Frankenstein
- "Kalevala" kouluttaa ohjelman englannin kielisellä Kalevalalla
- "Dog names" käyttää listaa koirien nimistä

Lähdemateriaalin valinnan jälkeen ohjelma kysyy käyttäjältä Markovin asteen (suosittelen käyttämään joko 3 tai 4) ja pyytää englanninkielisen sanan, josta sanoja lähdetään generoimaan. Koirien nimien kanssa käytetään yhtä kirjainta. Isompien Markovin asteiden käyttäminen voi hidastaa ohjelman toimintaa huomattavasti, eikä se ole muutenkaan suositeltavaa. Mitä isompi Markovin aste on, niin sitä todennäköisemmin ohjelma alkaa vain toistamaan lähdemateriaalia sana sanalta. Siksi on järkevämpää käyttää asteita 3 tai 4. 

Tämä projekti käyttää tekstiaineistoa Project Gutenbergistä (https://www.gutenberg.org), joka tarjoaa julkisen domainin kirjallisuutta.

# Asentaminen

Lataa ohjelma laitteellesi käyttämällä toimintoa ja siirry ohjelman kansioon: 
```
git clone git@github.com:doomwall/tekstigeneraattori.git tekstigeneraattori
cd tekstigeneraattori
```

Asenna tarvittavat paketit komennolla: 
```
poetry install --no-root
```

Käynnistä virtual environment venv:
```
poetry shell
```

Ohjelma käynnistyy komennolla:
```
python src/main.py
```

Testit voi ajaa venvin sisällä komennoilla:
```
poetry run task tests
poetry run task coverage
```
