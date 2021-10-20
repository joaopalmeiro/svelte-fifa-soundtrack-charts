# svelte-fifa-soundtrack-charts

FIFA soundtrack visualizations built with Svelte.

## Quickstart

> Python

- `pipenv install --python 3.6`.
- `pipenv shell`.

> Svelte

- `npm install`.
- `npm start`.

## References

- [FIFA 20 Soundtrack](https://www.ea.com/news/fifa-20-soundtrack-volta-football?isLocalized=true) page.
- [FIFA 21 Soundtrack](https://www.ea.com/en-gb/games/fifa/fifa-21/soundtrack) page.
- [How to handle environment variables in Python](https://pybit.es/articles/how-to-handle-environment-variables-in-python/) blog post by Bob Belderbos.
- _Teamed_ (or grouped) bar chart:
  - [Lisa Charlotte Muth's tweet](https://twitter.com/lisacmuth/status/1442175586726780929/photo/2).
  - [Wahlergebnisse : Alle Ergebnisse der Bundestagswahl 2021](https://www.zeit.de/politik/deutschland/2021-09/wahlergebnisse-bundestagswahl-2021-wahlkreise-karte-deutschland-live) by ZEIT ONLINE.

## Notes

- [Deta Base](https://docs.deta.sh/docs/base/about):
  - NoSQL database.
  - `pipenv install deta`.
  - The `put` method is the fastest way to store an item in the database.
  - The `put_many` method puts up to 25 items on a single call.
  - `key` parameter: ID. It will be automatically generated if not provided.
  - [HTTP API](https://docs.deta.sh/docs/base/http).
- [HTTPie](https://httpie.io/):
  - `brew install httpie`.
  - `https -v POST https://database.deta.sh/v1/{project_id}/fifa_soundtrack/query X-API-Key:{project_key} Content-Type:application/json query:='[{"GAME": "FIFA 21"}, {"GAME": "FIFA 20"}]'` (more info [here](https://docs.deta.sh/docs/base/http/#query-items)).
  - `param==value` for URL parameters ([source](https://httpie.io/docs#querystring-parameters)).
  - `Name:Value` for HTTP Headers.
  - [Cheatsheet](https://httpie.io/docs#request-items).
