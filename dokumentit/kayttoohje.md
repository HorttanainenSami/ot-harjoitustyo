# Käyttöohje

## Konfigurointi
Tietokannan nimen voi muuttaa halutessaan tiedostosta ```.env```
```
DATABASE_FILENAME=database.sqlite
```

## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä tulee ohjelman riippuvuuden asentaa komennolla
``` poetry install```
jonka jälkeen tietokannan alustus tapahtuu
```poetry run invoke build```
Nyt ohjelma voidaan käynnistää projektin juurihakemistosta komennolla
```poetry run invoke start```


## Uuden käyttäjän luominen
Ohjelman käynnistyessä ohjelma avaa kirjautumis ikkunan:

![image](https://user-images.githubusercontent.com/67758940/117035221-b999a880-ad0c-11eb-9ec9-98b2a4583a8f.png)

Koska olet todennäköisesti juuri alustanut tietokannat, tulee ensin luoda käyttäjä tietokantaan.

Paina 'Register new user' - painiketta ja siirryt 'Register view' näkymään.

![image](https://user-images.githubusercontent.com/67758940/117035534-185f2200-ad0d-11eb-9bc4-a25236c2662d.png)

Kirjoita haluamasi käyttäjätunnus ja paina 'Register and login' -painiketta
**HUOM: jos käyttäjätunnuksesi ei ole uniikki, tai käyttäjätunnuksesi/salasanasi on alle 3 merkkiä pitkä tulee seuraavan varoitus***

![image](https://user-images.githubusercontent.com/67758940/117035794-6bd17000-ad0d-11eb-82ca-c9cdc8870473.png)

Kun olet luonut käyttäjän onnistuneesti, ohjaa sovellus sinut kirjautumis sivulle.


## Kirjautuminen
Kirjaudu edellä tehdyllä käyttäjällä:

![image](https://user-images.githubusercontent.com/67758940/117036013-a63b0d00-ad0d-11eb-8eb8-d43f3f9c6fe4.png)

jonka jälkeen sinut uudelleen ohjataan ```Recipes view``` näkymälle.

![image](https://user-images.githubusercontent.com/67758940/117036100-c10d8180-ad0d-11eb-8b30-6f09ed1df6d6.png)


## Reseptin luominen
Paina ```Recipes view``` näkymästä ```Create new recipe``` - näppäintä jolloin sinut siirretään ```Create recipe view``` näkymään. Tässä voit luoda uuden reseptin täyttämällä lomakkeen. Uusia ainesosia voit lisätä/poistaa painamalla 'ingredients:' osion + - tai - -näppäintä

![image](https://user-images.githubusercontent.com/67758940/117036676-5ad52e80-ad0e-11eb-9f54-567c3d997102.png)

Tallenna resepti painamalla alakulmasta ```Save```-näppäintä, jolloin resepti talletetaan tietokantaan.

![image](https://user-images.githubusercontent.com/67758940/117036786-79d3c080-ad0e-11eb-89b4-38afba95a1c5.png)


## Reseptin muokkaaminen

## Reseptin poistaminen

## Ulos kirjautuminen
Paina ```recipes view``` näkymän ```Log out```- näppäintä
