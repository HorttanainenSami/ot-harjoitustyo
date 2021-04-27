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
