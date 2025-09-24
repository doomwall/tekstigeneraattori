# Toteutusdokumentti

## Ohjelman rakenne

Ohjelma toteuttaa trie-tietorakenteen, johon talletetaan Markovin asteen mukaan sanoja tai kirjaimia n-grammeina. Ensin ohjelma alustaa trie-tietorakenteen käyttäen sille annettua materiaalia. Tällä hetkellä ohjelmaan on talletettuna muutamia eri kirjoja, joita voi käyttää materiaalina. Puuhun tallennetaan Markovin asteen mittaisia ketjuja eli n-grammeja, jotka sisältävät materiaalista poimitut arvot. Kun trie on alustettu, niin ohjelmalle voidaan syöttää yksittäisiä arvoja ja trie puusta haetaan todennäköisiä seuraajia kyseiselle arvolle. 

Trie-tietorakenne on tämän ohjelman keskiössä. Se perustuu solmuihin, joihin on talletettu tieto mahdollisista seuraavista arvoista ja arvon frekvenssi lähdemateriaalissa. Lisäksi solmu sisältää tiedon siitä onko kyseessä esimerkiksi lauseen viimeinen sana tai sanan viimeinen kirjain. Kun halutaan ennakoida tulevia arvoja, niin ohjelma ottaa Markovin asteen n-1 verran arvoja ja käyttää niitä ennakoimiseen. Tämä parantaa ohjelman tarkkuutta ja tuloksena lauseissa on jonkinlaista järkeä ja rakennetta. Ennakoidessa ohjelma palauttaa mahdolliset seuraavat arvot ja niiden frekvenssit. Tämän jälkeen niistä arvotaan frekvenssin mukaisesti seuraava arvo. Frekvenssi vaikuttaa siihen kuinka todennäköisesti kyseinen arvo valitaan seuraavaksi arvoksi. 


## Aikavaativuus

Trie-tietorakenne itsessään on aikavaativuudeltaan O(n) kaikilla keskeisillä operaatioilla. Tiedon syöttäminen on aikavaativuudeltaan O(n x m), missä n on materiaalin määrä ja m on Markovin aste. Trie-puuhun talletettavat arvot käydään läpi "liukuikkunalla", jonka koko on m (esim. lause "Minä menen kauppaan" talletetaan ikkunoilla ["minä", "menen"] ja ["menen", "kauppaan"], kun m = 2). 

Sanojen ennakoiminen trie-puusta on myös O(n x m), missä n on generoitavien sanojen määrä ja m on Markovin aste - 1. Arvojen ennakoimisessa käytetään m verran arvoja seuraavan arvon löytämiseen. 

Hakutoiminto itsessään käy läpi m sanaa trie-puussa, joten sen aikavaativuus on O(m).