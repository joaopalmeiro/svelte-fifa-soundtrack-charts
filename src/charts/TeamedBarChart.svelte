<script>
  // Based on: https://svelte.dev/examples#bar-chart
  // More info:
  // - https://github.com/d3/d3-axis
  // - https://github.com/d3/d3-scale
  import { from } from 'arquero';
  import { scaleLinear } from 'd3-scale';
  import { filter, maxBy, partialRight, uniqBy } from 'lodash';

  export let data;

  let width = 500;
  let height = 200;
  const padding = { top: 20, right: 15, bottom: 20, left: 25 };

  const xAccessor = (d) => d.LIST;
  const yearAccessor = (d) => d.GAME;
  const yAccessor = (d) => d.count;

  const uniqX = partialRight(uniqBy, xAccessor);
  // const uniqYear = partialRight(uniqBy, yearAccessor);

  // console.log(data);
  const dataToPlot = from(data).groupby('GAME', 'LIST').count().objects();
  // console.log(dataToPlot);

  const xTicks = uniqX(data).map(xAccessor);
  // const annotations = uniqYear(data).map(yearAccessor);
  const yMax = yAccessor(maxBy(dataToPlot, yAccessor));
  // console.log(annotations);
  // console.log(xTicks, xTicks.length);
  // console.log(yMax);

  $: innerWidth = width - (padding.left + padding.right);
  $: barWidth = innerWidth / xTicks.length;

  $: xScale = scaleLinear()
    .domain([0, xTicks.length])
    .range([padding.left, width - padding.right]);

  $: yScale = scaleLinear()
    .domain([0, yMax])
    .range([height - padding.bottom, padding.top]);
</script>

<h2>Teamed bar chart</h2>
<div class="chart" bind:clientWidth={width} bind:clientHeight={height}>
  <svg xmlns="http://www.w3.org/2000/svg">
    <!-- <rect width="100%" height="100%" fill="crimson" /> -->

    <!-- Y-axis -->
    <g class="axis y-axis">
      {#each yScale.ticks(5) as tick}
        <g class="tick tick-{tick}" transform="translate(0, {yScale(tick)})">
          <line x2="100%" />
          <text y="-5">{tick}{tick === yMax ? ' songs' : ''}</text>
        </g>
      {/each}
    </g>

    <!-- X-axis -->
    <g class="axis x-axis">
      {#each xTicks as tick, i}
        <g class="tick" transform="translate({xScale(i)}, {height})">
          <text x={barWidth / 2} y="-5">{tick}</text>
        </g>
      {/each}
    </g>

    <!-- Bars -->
    <g class="bars" transform="translate({barWidth / 6}, 0)">
      {#each dataToPlot as datum}
        <rect
          x={xScale(xAccessor(datum) === xTicks[0] ? 0 : 1)}
          y={yScale(yAccessor(datum))}
          width={barWidth / 2}
          height={yScale(0) - yScale(yAccessor(datum))}
          fill={xAccessor(datum) === xTicks[0] ? '#333333' : '#9A9285'}
          opacity={yearAccessor(datum) === 'FIFA 21' ? '1' : 0.25}
          transform={yearAccessor(datum) === 'FIFA 21'
            ? `translate(${barWidth / 6}, 0)`
            : `translate(0, 0)`}
        />
      {/each}
    </g>

    <!-- Annotations -->
    <g>
      {#each filter(dataToPlot, ['LIST', xTicks[0]]) as datum}
        <line
          x1={yearAccessor(datum) === 'FIFA 20'
            ? barWidth / (6 * 2) + barWidth / 6 + padding.left
            : barWidth / 2 + barWidth / (6 * 2) + padding.left}
          y1={yScale(yAccessor(datum))}
          x2={yearAccessor(datum) === 'FIFA 20'
            ? barWidth / (6 * 2) + barWidth / 6 + padding.left
            : barWidth / 2 + barWidth / (6 * 2) + padding.left}
          y2={yScale(yAccessor(datum)) - 20}
          stroke="#333333"
          stroke-width="0.5px"
          stroke-opacity={yearAccessor(datum) === 'FIFA 21' ? '1' : 0.25}
        />

        <text
          x={yearAccessor(datum) === 'FIFA 20'
            ? barWidth / (6 * 2) + barWidth / 6 + padding.left
            : barWidth / 2 + barWidth / (6 * 2) + padding.left}
          y={yScale(yAccessor(datum)) - 23}
          text-anchor="middle"
          class="tick"
          fill="#333333"
          opacity={yearAccessor(datum) === 'FIFA 21' ? '1' : 0.25}
        >
          {yearAccessor(datum)}
        </text>
      {/each}
    </g>
  </svg>
</div>

<style>
  /* .chart {
    width: 100%;
    max-width: 500px;
    margin: 0 auto;
  } */

  svg {
    width: 100%;
    height: 200px;
  }

  h2 {
    font-family: Helvetica, Arial, sans-serif;
    margin-bottom: 1rem;
    color: #1c1917;
  }

  .tick {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 0.725rem;
    font-weight: 200;
  }

  .tick line {
    stroke: #e2e2e2;
    stroke-dasharray: 2;
  }

  .tick text {
    fill: #ccc;
    text-anchor: start;
  }

  .tick.tick-0 line {
    stroke-dasharray: 0;
  }

  .x-axis .tick text {
    text-anchor: middle;
  }

  .bars rect {
    stroke: none;
  }
</style>
