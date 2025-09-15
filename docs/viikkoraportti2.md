# Viikkoraportti 2

Tällä viikolla keskityin trie-rakenteen toteuttamiseen ja Markovin ketjun toteutukseen siinä. Ohjelmaan on lisätty pieni käyttöliittymä ja githubiin asennus- ja käynnistysohjeet. Trie-puu rakentuu solmuista, joihin on tallennettu tieto sanasta/merkistä ja sen frekvenssistä. Ohjelma lukee tällä hetkellä automaattisesti englannin kielisen Kalevalan, kun sen käynnistää ja sille antaa Markovin asteen. Tällä hetkellä ohjelma osaa lukea vain lauseita, ei vielä pelkästään merkkejä. Ohjelma toimii, kun sille antaa Markovin asteen, jonkin sanan mikä löytyy lähde aineistosta (esim. "I" tai "beer") ja montako sanaa haluat ohjelman tuottavan.

Opin Trie-rakenteesta ja Markovin ketjusta ja sen toteutuksesta python koodilla. Minua on yllättänyt algoritmin nopeus. Ollut kiva nähdä miten nopeasti ohjelma pystyy lukemaan suhteellisen isoa määrää tietoa.

Vielä minulle on epäselvää miten lopetan lauseet ja miten määrittelen aloitus sanat lauseille. Nodelle on määritelty arvo isTerminal, eli onko Node lauseen lopetus. Tätä ei kuitenkaan vielä käytetä ohjelman suorituksessa. Tätä lähden selvittämään ensi viikolla. Lisäksi haluan ohjelmalle lisää luettavaa dataa ja muuntaa ohjelman myös muotoon, että se osaa lukea sanoista merkit, eikä lauseista sanoja. 

Käytetty aika: 15h


Tekoälyä käytetty Trie-tietorakenteen ymmärtämiseen, mutta tekoälyä ei ole käytetty koodin luomiseen. 

