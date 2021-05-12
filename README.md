# Ohjelmistotekniikka harjoitustyö

tehnyt **Sami Horttanainen**
*aloitettu 17.03.2021*

## ReseptiApp

## Python-versio
Sovelluksen toiminta on kehitetty ja todettu toimivaksi vähintään Python-versiolla ```3.6.0 ```
## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/dokumentit/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/dokumentit/tyoaikakirjanpito.md)
- [Arkkitehtuurikuvaus](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/dokumentit/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/dokumentit/kayttoohje.md)
- [Testidokumentti](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/dokumentit/testausdokumentti.md)

## Release
- [Viikko5](https://github.com/HorttanainenSami/ot-harjoitustyo/releases/tag/viikko_5)
- [viikko6](https://github.com/HorttanainenSami/ot-harjoitustyo/releases/tag/viikko6)
- [Viikko7](https://github.com/HorttanainenSami/ot-harjoitustyo/releases/tag/viiikko7)
## Asennus
1. Asenna riippuvuudet komennolla:
 ```poetry install```
2. suorita alustustoimentpiteet:
```poetry run invoke build```
3. Käynnistä sovellus komennolla:
```poetry run invoke start```

## Komentorivitoiminnot
### Ohjelman suorittaminen
Ohjelman pystyy suorittamaan komennolla:
```poetry run invoke start```
### Testaus
Testit suoritetaan komennolla:
```poetry run invoke test```
### Testikattavuus
```poetry run invoke coverage-report```
### Pylint
```poetry run invoke lint```
