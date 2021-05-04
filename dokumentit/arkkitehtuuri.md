# Arkkitehtuurikuvaus
## Rakenne
Koodin pakkausrakenne on seuraava:
![image](https://user-images.githubusercontent.com/67758940/115427008-baf5ac00-a209-11eb-8fc6-f46a9d6c6d9a.png)

## käyttöliittymä

## Sovelluslogiikka

## Tietojen pysyväistallennus

## Päätoiminnallisuus
### Käyttäjän kirjautuminen
Kun kirjautumis lomakkeeseen kirjoitetaan käyttäjätunnus ja salasana, ja painetaan 'Login', etenee sovellus seuraavasti:
![image](https://user-images.githubusercontent.com/67758940/117028580-83f1c100-ad06-11eb-9517-cbe5f904c846.png)
Painikkeen tapahtumankäsittelijä kutsuu sovelluslogiikan ```RecipeService``` metodia [handle_login()](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/f4e1f121bff317be0e7826529b05152227e3a96c/src/services/recipe_service.py#L30) joka tarkistaa voidaanko käyttäjä kirjata sisälle. handle_login() metodi taas kutsuu ```UserRepository```:n get_user() -metodia joka palauttaa käyttäjätunnusta vastaavan käyttäjän jos sellainen löytyy. ```RecipeService``` tarkistaa onko salasana oikein ja palauttaa True jos salasana ja tietokannassa oleva salasana täsmäävät. Seuraavaksi ```UI``` suorittaa ```_show_recipes_view()```- metodin joka muuttaa käyttöliittymän näkymän ```RecipesView```- ikkunaan. Uusi ikkuna taas hakee käyttäjän tallennetut reseptit seuraavanlaisesti: ```get_all_recipes()``` -metodi kutsuu sovelluslogiikan ```ReciperService``` metodia get_all_recipes() joka palauttaa ```RecipesRepository```:n avulla käyttäjän tekemät reseptit. ```RecipesView``` renderöi nämä reseptit näkyviin.

### Käyttäjän luominen
![image](https://user-images.githubusercontent.com/67758940/117031366-2dd24d00-ad09-11eb-9d25-0234a44895d8.png)
