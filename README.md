# BibTex -lähdehallintatyökalu 
[![GHA workflow badge](https://github.com/Metanjarki/LATEX-LAHTEET/workflows/CI/badge.svg)](https://github.com/Metanjarki/LATEX-LAHTEET/actions)
[![codecov](https://codecov.io/gh/Metanjarki/LATEX-LAHTEET/graph/badge.svg?token=LWVYAAM3LO)](https://codecov.io/gh/Metanjarki/LATEX-LAHTEET)

Sovelluksen tarkoitus on helpottaa BibTex-lähdeviittausten hallintaa.

## Ominaisuuksia

Sovellukseen voi lisätä lähteitä muodoissa kirja, artikkeli ja artikkeli konferenssijulkaisussa. Sovelluksesta voi myös ladata lähteet typistettynä.

## Backlog
Nykyisen backlogin voi nähdä [täältä](https://docs.google.com/spreadsheets/d/1M5kKUjORXVepBhWVwGJPqX7DncR86aFn1dlTe7wg358/edit?usp=sharing)

## Asennus
Asenna projektin riippuvuudet ajamalla komennon `poetry install`. Tämän jälkeen laita projektin juureen `.env` -niminen tiedosto, joka sisältää ainakin seuraavat tiedot.

```
DATABASE_URL=Postgres-tietokannan osoite
TEST_ENV=true
SECRET_KEY=jokin satunnainen merkkijono
```

Varmista että Postgres-tietokantasi on toiminnassa. Alusta sovelluksen skeema ajamalla komennon `python3 src/db_helper.py`. 

Tämän jälkeen aktivoi python-virtuaaliympäristö komennolla `poetry shell`. Tämän jälkeen projektin ajaminen onnistuu komennolla `python3 src/index.py`.

## Hyödyllistä tietää

Mikäli tarkastelet tietokantaa `psql` -ohjelmalla, projektin käyttämään skeemaan pääsee käsiksi ajamalla ensin kyselyn `SET search_path TO lahteet;`.

## Resursseja

- [Tietoa bibtex-lähdetyypeistä ja mitä kenttiä ne pitää sisällään](https://www.openoffice.org/bibliographic/bibtex-defs.html)
- [Github releasien teko](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

## Definition of done
- User storyille tulee määritellä hyväksymiskriteerit, jotka on testattavissa Robot-frameworkilla
- Toteutetulla koodilla on riittävä testikattavuus
- Asiakas pääsee näkemään koodin ja testien tilanteen CI-palvelusta
- Koodin dokumentaatio on riittävä ja ajantasainen
- Koodin ylläpidettävyyden tulee olla mahdollisimman hyvä
  - järkevä nimeäminen
  - selkeä ja perusteltu arkkitehtuuri
  - yhtenäinen koodityyli

