# Testausdokumentti
Sovellus on testattu yksikkö ja integraatiotesteillä unitestillä ja manuaalisesti käyttöohjeita noudattaen. Testeille luodaan testienaikainen tietokanta tiedostossa ```.env.test``` jollon testit eivät sekoita tuotannossa olevaa tietokantaa.

## Integraatiotestaus

### Sovelluslogiikka
Sovelluslogiikka ```RecipesService``` on testattu integraatiotestein ja metodit joita on testattu on todettu toimiviksi. Sovelluslogiikkaa testaava luokka on [```TestRecipeService```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/tests/recipe_service_test.py). ```TestRecipeService``` alustaa tietokannan ja tallettaa tietokannan tauluun ```user``` käyttäjän 'testi' salasanalla 'asd'. Tätä käyttäjää käytetään testien aikana integraatiotestien testaamiseksi.

**Haarautumiskattavuus 89%**
## Yksikkötestaus
### Repository -luokat
```UserRepository``` luokan testaus on suoritettu yksikkötesteillä jota testataan luokalla [```TestUserRepository```](https://github.com/HorttanainenSami/ot-harjoitustyo/blob/master/src/tests/repositories/user_repository_test.py). Luokka alustaa tietokannan ennen testien tekemistä.

**Haarautumiskattavuus 100%**

```RecipeRepository``` luokan testaus perustuu sovelluslogiikan integraatiotestaukseen.

**Haarautumiskattavuus 72%**

## Testikattavuus
**Testien haarautumiskattavuus on 86%**
![image](https://user-images.githubusercontent.com/67758940/118014307-bb421c80-b35b-11eb-97b2-bb0122f4b574.png)

# Järjestelmätestaus
Testaukset on tehty käyttöohjeiden mukaisesti Linux käyttöliittymällä.
## Toiminnallisuudet
Kaikki käyttöohjeiden metodit on testattu manuaalisesti
## parantamisen varaa
Testauksessa on parantamisenvaraa ainakin testikattavuuden kannalta. Myös virheilmoitukset voisivat olla parempia.
