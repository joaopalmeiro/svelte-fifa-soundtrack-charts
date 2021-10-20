<script>
  import Container from './components/Container.svelte';
  // More info:
  // - https://sveltesociety.dev/recipes/component-recipes/using-fetch-to-consume-apis
  // - https://svelte.dev/tutorial/await-blocks
  // - https://svelte.dev/docs#await
  // - https://developer.mozilla.org/en-US/docs/Web/API/fetch
  // - https://dmitripavlutin.com/javascript-fetch-async-await/
  // - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify
  // - https://www.browserstack.com/guide/how-to-perform-network-throttling-in-chrome
  // - https://javascript.info/async-await
  // - https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#uploading_json_data
  const { SNOWPACK_PUBLIC_PROJECT_ID, SNOWPACK_PUBLIC_PROJECT_KEY } = __SNOWPACK_ENV__;

  async function getData() {
    // More info:
    // - https://docs.deta.sh/docs/base/http/#general--auth
    // - https://docs.deta.sh/docs/base/http/#query-items
    const url = `https://database.deta.sh/v1/${SNOWPACK_PUBLIC_PROJECT_ID}/fifa_soundtrack/query`;
    const method = 'POST';
    const headers = {
      'Content-Type': 'application/json',
      'X-API-Key': SNOWPACK_PUBLIC_PROJECT_KEY,
    };
    const jsonPayload = {
      query: [{ GAME: 'FIFA 21' }, { GAME: 'FIFA 20' }],
    };
    const body = JSON.stringify(jsonPayload);

    const res = await fetch(url, { method, headers, body });

    if (!res.ok) {
      const message = `An error has occured: ${res.status} ${res.statusText}`;
      throw new Error(message);
    }

    const data = await res.json();
    return data;
  }

  const promise = getData();
  // console.log(promise);
</script>

{#await promise}
  <p>Loading data...</p>
{:then data}
  <!-- <pre>{JSON.stringify(data, null, 2)}</pre> -->
  <Container outline>card content</Container>
{:catch error}
  <p style="color: crimson">{error.message}</p>
{/await}
