# Arkkitehtuurikuvaus
## Rakenne
Koodin pakkausrakenne on seuraava:

![image](https://user-images.githubusercontent.com/67758940/115427008-baf5ac00-a209-11eb-8fc6-f46a9d6c6d9a.png)

Pakkaus UI sisältää käyttöliittymän, Services sovelluslogiikan ja repositories sisältää pysyväistallennuksen koodin. Sovelluslogiikka toimii kaikkien pakkauksien yhdistäjänä.

## Käyttöliittymä
Käyttölittymä sisältää 6 erillistä näkymää:
- Kirjautuminen
- Rekistöröityminen
- Reseptit
- Uuden reseptin luominen
- Reseptin katsominen
- Respetin päivittäminen

Jokainen näistä on luotu omana luokkanaan jotka näkyvät vain yksi kerrallaan. Näkymien näkymisen hoitaa [UI](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/ui/ui.py)-luokka.

## Sovelluslogiikka
Toiminnallisista kokonaisuuksista vastaa [RecipeService](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/services/recipe_service.py)-Luokka. Luokka tarjoaa käyttöliittymän toiminnoille omat metodit, kuten:
- handle_login(username, password)
- handle_logout()
- create_user(username, password)
- create_recipe(recipe_name, ingredients, instructions)
- ...

Sovelluslogiikka toimii myös käyttöliittymän ja pysyväistallennukseen tarkoitettujen _repositories_ pakkauksen välikätenä, tallettaen ja hakien tietoa tietokannasta. 

```RecipeService``` pääsee käsiksi ```RecipeRepository```:yn ja ```UserRepository```:yn joiden avulla sovelluslogiikka pääsee käsiksi tietokantaan tallennettuihin käyttäjiin ja resepteihin. 

## Tietojen pysyväistallennus
Tiedostot [recipe_repository](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/repositories/recipes_repository.py) ja [users_repository](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/repositories/users_repository.py) huolehtivat tietokannan kanssa kommunikoinnista ja tallettavat tiedostot _sqlite_ tietokantaan.

## Päätoiminnallisuus
### Käyttäjän kirjautuminen
Kun kirjautumis lomakkeeseen kirjoitetaan käyttäjätunnus ja salasana, ja painetaan 'Login', etenee sovellus seuraavasti:

![image](https://user-images.githubusercontent.com/67758940/117028580-83f1c100-ad06-11eb-9517-cbe5f904c846.png)

Painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan [```RecipeService```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/services/recipe_service.py#L55) metodia [```handle_login()```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/f4e1f121bff317be0e7826529b05152227e3a96c/src/services/recipe_service.py#L30) joka tarkistaa voidaanko käyttäjä kirjata sisälle. ```handle_login()``` metodi taas kutsuu [```UserRepository```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/repositories/users_repository.py):n [```get_user()```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/010087bb07d603f2868919fed3b760eb3d93d416/src/repositories/users_repository.py#L27) -metodia joka palauttaa käyttäjätunnusta vastaavan käyttäjän jos sellainen löytyy.

```RecipeService``` tarkistaa onko salasana oikein ja palauttaa True jos salasana ja tietokannassa oleva salasana täsmäävät. Seuraavaksi [```UI```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/ui/ui.py) suorittaa [```_show_recipes_view()```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/010087bb07d603f2868919fed3b760eb3d93d416/src/ui/ui.py#L32)- metodin joka muuttaa käyttöliittymän näkymän [```RecipesView```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/010087bb07d603f2868919fed3b760eb3d93d416/src/ui/recipes_view.py#L3)- ikkunaan. Uusi ikkuna taas hakee käyttäjän tallennetut reseptit seuraavanlaisesti: ```get_all_recipes()``` -metodi kutsuu sovelluslogiikan ```RecipesService``` metodia ```get_all_recipes()``` joka palauttaa ```RecipesRepository```:n avulla käyttäjän tekemät reseptit. ```RecipesView``` renderöi nämä reseptit näkyviin.

### Käyttäjän luominen

![image](https://user-images.githubusercontent.com/67758940/117031366-2dd24d00-ad09-11eb-9d25-0234a44895d8.png)

Painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan [```RecipeService```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/services/recipe_service.py) metodia [```create_user()```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/010087bb07d603f2868919fed3b760eb3d93d416/src/services/recipe_service.py#L55) joka palauttaa 'username':a vastaavan käyttäjän tai None. Jos käyttäjää ei ole tietokannassa luodaan käyttäjä kutsumalla ```UserRepository```:n metodia ```insert_user()```. jos käyttäjän luominen on onnistunut ```UI``` suorittaa tällöin ```_show_login_view()``` metodin joka renderöi ```LoginView``` - näkymän. Jos käyttäjän luominen epäonnistuu renderöi ```UI```näkymään virheviestin.

### Ulos kirjautuminen

![image](https://user-images.githubusercontent.com/67758940/117971957-33481c80-b333-11eb-8800-11229f1392c4.png)

Painikkeen 'Log out' tapahtumankäsittelijä kutsuu sovelluslogiikan ```RecipeService``` metodia [handle_logout()](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/010087bb07d603f2868919fed3b760eb3d93d416/src/services/recipe_service.py#L47) joka poistaa kijrautuneen käyttäjän tiedot sovelluslogiikan muistista. ```RecipesView``` kutsuu tiedoston ```ui``` metodia ```handle_login()``` joka renderöi ```LoginView``` näkymän.

### Reseptin luominen

![image](https://user-images.githubusercontent.com/67758940/117974099-d9952180-b335-11eb-935d-321dd3f50ce3.png)


### Reseptin poistaminen

### Reseptin muokkaaminen

