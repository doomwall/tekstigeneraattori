# Määrittelydokumentti

Tämä on määrittelydokumentti Helsingin yliopiston aineopintojen harjoitustyötä varten. Aiheena Algoritmit ja tekoäly. 

## Aihe - Harjoitustyö: Kielimalli Markovin ketjuilla ja Trie-tietorakenteella

Tarkoituksena on luoda ohjelma, jolle voidaan syöttää harjoitusdatana tekstimateriaalia ja tallettaa se trie-tietorakenteeseen. Tämän jälkeen käyttäjä voi syöttää ohjelmalle sanan tai sanoja ja ohjelma ennustaa miten sana/lause jatkuu eteenpäin. Ohjelma on tarkoitus toteuttaa käyttämällä Markovin ketjua. Ohjelma lukee trie-tietorakenteesta edelliseen n-1 sanaan liittyvät sanat ja niiden todennäköisyydet. Tämän mukaan ohjelma ennakoi mikä on seuraava sana. Tarkoituksena on käyttää mielivaltaista määrää Markovin ketjun asteita (n-gram), eli ohjelmaa pystyy konfiguroimaan kuinka pitkälle trie-puuhun ohjelma lukee ennen kuin se päättää mikä on seuraava sana. Ohjelman käyttö tapahtuu komentorivillä. Koska ohjelman suorittamiseen tarvitaan harjoitusdataa, ohjelmaa alustaessa sitä koulutetaan jollain kolmannen osapuolen materiaalilla. 

Harjoitustyön ydin on toimiva ja tehokas Markov ketju, jota pystytään kouluttamaan ja joka pystyy ennustamaan suhteellisen järkeviä lauserakenteita. Haluan erityisesti tutustua siihen, mikä on sovelluksen toimivuus eri asteilla. 

## Ohjelmointikielet

Ohjelmointikieleksi valitsin Pythonin. Uskon sen soveltuvan sovelluksen toteutukseen hyvin ja minulla on siitä eniten kokemusta.
Vertaisarviointia varten osaan myös JavaScriptiä.

## Aikavaativuus

Trie-tietorakenteen eri operaatiot ovat aikavaativuudeltaan O(n), missä n on Markovin aste. Datan määrä voi kuitenkin olla erittäin suuri, ja vaikka n olisi pieni, muistin vaatimus n-grammien tallentamiseksi voi kasvaa merkittävästi.

## Lisätiedot

Opinto-ohjelma on tietojenkäsittelytieteen kandidaatti.

## Lähteet

* [Trie-tietorakenne - Wikipedia](https://en.wikipedia.org/wiki/Trie)  <br/>
* [Markovin ketju - Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)
