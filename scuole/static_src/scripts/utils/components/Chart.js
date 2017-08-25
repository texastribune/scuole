import { Component, h } from 'preact';
import { extent, max } from 'd3-array';
import { area, line } from 'd3-shape';
import { scaleLinear } from 'd3-scale';

import Axis from './Axis';

export default class Chart extends Component {
  render({
    data,
    width: containerWidth,
    ratio = 0.625,
    title,
    xField,
    yField,
    yField2,
    yField3,
    yMax,
    margins: _margins,
  }) {
    const width = containerWidth - 20;
    const height = width * ratio;

    const margins = Object.assign(
      {},
      { top: 20, right: 20, bottom: 20, left: 20 },
      _margins
    );

    const innerWidth = width - margins.left - margins.right;
    const innerHeight = height - margins.top - margins.bottom;

    data = data.sort((a, b) => a.year - b.year);

    const xExtent = extent(data, d => d[xField]);

    const x = scaleLinear().rangeRound([0, innerWidth]).domain(xExtent).nice();

    const y = scaleLinear()
      .rangeRound([innerHeight, 0])
      .domain([0, yMax || max(data, d => d[yField])])
      .nice();

    const lineGenerator = line()
      .defined(d => d[yField])
      .x(d => x(d[xField]))
      .y(d => y(d[yField]));

    const areaGenerator = area()
      .defined(lineGenerator.defined())
      .x(lineGenerator.x())
      .y0(y(0))
      .y1(lineGenerator.y());

    const lineGenerator2 = line()
      .defined(d => d[yField2])
      .x(d => x(d[xField]))
      .y(d => y(d[yField2]));

    const areaGenerator2 = area()
      .defined(lineGenerator2.defined())
      .x(lineGenerator2.x())
      .y0(y(0))
      .y1(lineGenerator2.y());

    const lineGenerator3 = line()
      .defined(d => d[yField3])
      .x(d => x(d[xField]))
      .y(d => y(d[yField3]));

    const areaGenerator3 = area()
      .defined(lineGenerator3.defined())
      .x(lineGenerator3.x())
      .y0(y(0))
      .y1(lineGenerator3.y());

    return (
      <svg width={width} height={height}>
        <g transform={`translate(${margins.left},${margins.top})`}>
          <rect width={innerWidth} height={innerHeight} fill="#eee" />
          <path
            class="area area--one"
            stroke="#08b4ac"
            fill="#08b4ac"
            stroke-width="1"
            d={areaGenerator(data)}
          />
          <path
            class="area area--two"
            stroke="#04524f"
            fill="#04524f"
            stroke-width="1"
            d={areaGenerator2(data)}
          />
          <path
            class="area area--three"
            stroke="#04524f"
            fill="#04524f"
            stroke-width="1"
            d={areaGenerator3(data)}
          />
          <Axis
            scale={x}
            orientation="bottom"
            transform={`translate(0,${innerHeight})`}
            class="axis axis--x"
            tickArguments={[4]}
            tickFormat={(d, i) => {
              if (i === 0) return d.toString();

              return `'${d.toString().slice(2)}`;
            }}
          />
          <Axis
            scale={y}
            class="axis axis--y"
            tickSizeInner={-innerWidth}
            tickArguments={[4]}
            tickFormat={d => {
              if (d === 0) return '';
              return `${Math.round(d * 100)}%`;
            }}
          />
        </g>
      </svg>
    );
  }
}
