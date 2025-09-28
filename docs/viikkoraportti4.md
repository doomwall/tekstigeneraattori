# Viikkoraportti 4

Tällä viikolla sairastuin flunssaan ja sen seurauksena ohjelma ei paljoa edennyt. Vein ohjelman dokumentaatiota eteenpäin ja keskityin tekemään siitä vertaisarviointi kelpoisen. Ohjelman pitäisi olla toimiva ja testattavissa. Testeihin lisäsin testin, joka mittaa ohjelman suorituskykyä. Se laskee paljonko menee aikaa, kun trie-tietorakenteeseen syötetään englannin kielinen Kalevala Markovin asteella kolme, ja kauanko menee aikaa ennustaa sanoja kyseisestä puusta. Lisäksi lisätty lähdemateriaalin käyttöoikeustiedot. 

Löysin ohjelmasta ison puutteen, johon en ole vielä keksinyt järkevää ratkaisua. Jos ohjelma ei löydä seuraavaa ennustettavaa arvoa, niin se arpoo sanan trie-puun juuresta, ja jatkaa tällä eteenpäin. Tämä on kuitenkin ongelma, jos Markovin aste on enemmän kuin 1. Silloin sanojen ketju on sattumanvaraisia sanoja, ja kun edellisiä sanoja käytetään ennustamaan seuraavia sanoja, niin ketjut ovat rikkonaisia, eikä niitä löydy enää juuresta. Tähän ja vertaisarviointien tuloksiin aion keskittyä ensi viikolla. 

Käytetty aika: 6h