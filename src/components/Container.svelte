<script>
  // Based on:
  // - https://illright.github.io/attractions/docs/components/card
  // - https://github.com/illright/attractions/blob/v3.4.0/attractions/card/card.svelte
  // - https://github.com/illright/attractions/blob/v3.4.0/attractions/_variables.scss
  // - https://svelte.dev/docs#Attributes_and_props
  export let outline = false;
</script>

<div class:outline class="container" {...$$restProps}>
  <slot />
</div>

<style>
  .container {
    background-color: white;
    border-radius: 1.25em;
    overflow: hidden;
    padding: 1.5em;
  }

  .container.outline {
    /* More info: warm-gray, 900 (https://windicss.org/utilities/colors.html) */
    border: 1px solid #1c1917;
  }
</style>
