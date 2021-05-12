# Arkkitehtuurikuvaus
## Rakenne

![image](https://user-images.githubusercontent.com/67758940/115427008-baf5ac00-a209-11eb-8fc6-f46a9d6c6d9a.png)

Pakkausrakenne on yllä olevan kaltainen, se sisältää käyttöliittymän (UI), sovelluslogiikan (services) ja paikallistallennuksen (repositories). Sovelluslogiikka toimii kaikkien pakkauksien yhdistäjänä.

## Käyttöliittymä
Käyttölittymä sisältää 6 näkymää joiden näkymisestä huolehtii [UI](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/ui/ui.py)-luokka. UI pitää huolen että vain yksi näkymä renderöidään kerrallaan. UI myös välittää tarpeellisen tiedon toisista näkymistä jokaisen näkymän konstruktoriin.

Käyttöliittymän kaikki näkymä luokat:
- [Kirjautuminen](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/ui/login_view.py)
- [Rekistöröityminen](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/ui/register_view.py)
- [Reseptit](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/ui/recipes_view.py)
- [Uuden reseptin luominen](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/ui/create_recipe_view.py)
- [Reseptin katsominen](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/ui/recipe_view.py)
- [Respetin päivittäminen](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/ui/edit_recipe_view.py)


## Sovelluslogiikka
Sovelluksen toiminnallisuudesta vastaa [RecipeService](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/services/recipe_service.py)-Luokka. Luokka tarjoaa käyttöliittymän toiminnoille omat metodit joilla voidaan siirtyä käyttöliitymien näkymien välillä.

```RecipeService``` pääsee käsiksi ```RecipeRepository```:yn ja ```UserRepository```:yn joiden avulla sovelluslogiikka pystyy keskustelemaan tietokantaan tallennettuihin käyttäjiin ja resepteihin. 

Sovelluslogiikka toimii myös käyttöliittymän ja pysyväistallennukseen tarkoitettujen _repositories_ pakkauksen välikätenä, tarjoen näkymille päässyn tietokannan dataan ja mahdollistaa tietokannassa olevan data muokkaamisen.



## Tietojen pysyväistallennus
Tiedostot [recipe_repository](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/repositories/recipes_repository.py) ja [users_repository](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/repositories/users_repository.py) huolehtivat tietokannan kanssa kommunikoinnista ja tallettavat tiedostot _SQLite_ tietokantaan.

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

Painikkeen 'save' tapahtumankäsittelijä kutsuu sovelluslogiikan```RecipeService```:n metodia [```create_recipe()```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/010087bb07d603f2868919fed3b760eb3d93d416/src/services/recipe_service.py#L86) joka tallettaa reseptin tietokantaan ```RecipeRepository```:n metodilla [insert_recipe](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/0f529c87158c6c046624632ceb6a872c9f7ca439/src/repositories/recipes_repository.py#L37) joka palauttaa ```recipe_id```, eli juuri luodun reseptin id:n. Reseptin luonnin jälkeen ```RecipeService``` käy silmukassa _ingredients_ listan jokaisen alkion ja lisää ne yksitellen tietokannan _ingredient_-tauluun kutsumalla ```RecipesRepository```:n metodia [```add_ingredient```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/0f529c87158c6c046624632ceb6a872c9f7ca439/src/repositories/recipes_repository.py#L64). Reseptin luomisen  ja ainesosien jälkeen ```UI``` kutsuu metodia ```_show_recipes()``` joka renderöi ```RevcipesView```-näkymän näkyviin.

### Reseptin poistaminen

![image](https://user-images.githubusercontent.com/67758940/117976381-64771b80-b338-11eb-9dd1-973b5d284a5b.png)

Painikkeen 'Delete' tapahtumankäsittelijä renderöi ruudulle ```askyesno()``` funktion jonka hyväksyttyä tapahtumankäsittelijä kutsuu sovelluslogiikan ```RecipeService```:n metodia [```delete_recipe```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/0f529c87158c6c046624632ceb6a872c9f7ca439/src/services/recipe_service.py#L162)-metodia joka kutsuu ```RecipeRepository```:n metodia [```remove_recipe```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/0f529c87158c6c046624632ceb6a872c9f7ca439/src/repositories/recipes_repository.py#L98) joka poistaa reseptin ja siihen kuuluvat ainesosat tietokannasta. ```UI``` kutsuu metodia ```_recipes_view()``` joka renderöi ```RecipesView```-näkymän.

### Reseptin muokkaaminen

![image](https://user-images.githubusercontent.com/67758940/117993486-7496f700-b348-11eb-83cf-61c8f356e520.png)

Painikkeen 'Modify' tapahtumankäsittelijä renderöi näkymän ```EditRecipeView``` josta voidaan muokata kyseistä reseptiä.

Painikkeen 'save' tapahtumankäsittelijä kutsuu sovelluslogiikan ```RecipeService``` metodia [```update_recipe```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/0f529c87158c6c046624632ceb6a872c9f7ca439/src/services/recipe_service.py#L114) joka kutsuu ```RecipeRepository```:n metodia ```update_recipe()```. Kyseinen metodi päivittää tietokannassa olevan reseptin nimen ja ohjeet paramtereilla annetuilla muuttujilla. Tämän jälkeen kutsutaan sovelluslogiikan omaa metodia [```ingredients_changed()```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/0f529c87158c6c046624632ceb6a872c9f7ca439/src/services/recipe_service.py#L132) joka lisää/poistaa sen mukaan ainesosia miten ainesosalistaa on muokattu.
```UI``` kutsuu metodia ```_show_recipes_view()``` joka renderöi RecipesView -näkymän

### Reseptin viimeisimmän tekopäivän muokkaaminen

![image](https://user-images.githubusercontent.com/67758940/117994251-128ac180-b349-11eb-9c7e-0c28a42b50e7.png)

Painikkeen 'Produce' tapahtumankäsittelijä kutsuu sovelluslogiikan [```set_recipe_produced()```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/0f529c87158c6c046624632ceb6a872c9f7ca439/src/services/recipe_service.py#L125) metodia. Metodi kutsuu taas ```RecipeRepository```:n metodia [```set_produced()```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/0f529c87158c6c046624632ceb6a872c9f7ca439/src/repositories/recipes_repository.py#L91) joka tallettaa tämänhetkisen ajan tietokantaan.
