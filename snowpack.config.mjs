// More info:
// - https://www.snowpack.dev/reference/configuration
// - https://github.com/snowpackjs/snowpack/blob/main/create-snowpack-app/app-template-svelte/snowpack.config.mjs
// - https://www.snowpack.dev/reference/environment-variables

/** @type {import("snowpack").SnowpackUserConfig } */
export default {
  mount: {
    public: { url: '/', static: true },
    src: '/dist',
  },
  plugins: ['@snowpack/plugin-svelte', '@snowpack/plugin-dotenv'],
  routes: [],
  optimize: {},
  packageOptions: {},
  devOptions: {},
  buildOptions: {},
};
