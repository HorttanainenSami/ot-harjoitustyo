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
**HUOM: jos käyttäjätunnuksesi ei ole uniikki, tai käyttäjätunnuksesi/salasanasi on alle 3 merkkiä pitkä tulee seuraavan kaltainen varoitus***

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
Avaa jokin luoduistasi resepteistä painamalla sitä. 

![image](https://user-images.githubusercontent.com/67758940/117996808-220b0a00-b34b-11eb-8fe3-399a3e115c22.png)

Paina sivun yläpalkissa olevaa 'Modify' joka avaa reseptin muokkaus sivun. 
![image](https://user-images.githubusercontent.com/67758940/117996909-39e28e00-b34b-11eb-80c7-b093da33be76.png)

Muokkaa reseptiä

![image](https://user-images.githubusercontent.com/67758940/117997241-7a420c00-b34b-11eb-9346-ed12f474fa2e.png)

ja paina sivun alakulmasta 'save'

![image](https://user-images.githubusercontent.com/67758940/117997706-e02e9380-b34b-11eb-977c-e1319921dfaf.png)

Nyt huomataan että resepti on päivittynyt

## Reseptin poistaminen
Avaa resepti jonka haluat poistaa tietokannasta

![image](https://user-images.githubusercontent.com/67758940/117997897-123ff580-b34c-11eb-8e6e-738414f7c16e.png)

Paina yläkulmassa olevasta 'Delete' näppäimestä

![image](https://user-images.githubusercontent.com/67758940/117997935-1bc95d80-b34c-11eb-9d39-a3a1341d2aff.png)

Paina 'Yes' sivulle aukeavasta popupista

![image](https://user-images.githubusercontent.com/67758940/117998103-40253a00-b34c-11eb-9a17-c6ac408818eb.png)

Nyt resepti on poistettu tietokannasta

## Ulos kirjautuminen
Paina ```recipes view``` näkymän ```Log out```- näppäintä
