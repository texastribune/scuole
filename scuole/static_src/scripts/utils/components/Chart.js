import { Component, h } from 'preact';
import { extent, max } from 'd3-array';
import { area } from 'd3-shape';
import { scaleLinear } from 'd3-scale';

import Axis from './Axis';

export default class Chart extends Component {
  constructor() {
    super();

    this.state = {
      containerWidth: null,
    };
  }

  componentDidMount() {
    this.setState({
      containerWidth: this.base.parentNode.clientWidth,
    });
  }

  render(
    { data, title, xField, yField, yField2, yField3, yMax, margins: _margins },
    { containerWidth }
  ) {
    if (!containerWidth) return;

    const width = containerWidth - 20;
    const height = width * 0.625;

    const margins = Object.assign(
      {},
      { top: 20, right: 20, bottom: 20, left: 20 },
      _margins
    );

    const innerWidth = width - margins.left - margins.right;
    const innerHeight = height - margins.top - margins.bottom;

    const xExtent = extent(data, d => d[xField]);

    const x = scaleLinear().rangeRound([0, innerWidth]).domain(xExtent).nice();

    const y = scaleLinear()
      .rangeRound([innerHeight, 0])
      .domain([0, yMax || max(data, d => d[yField])])
      .nice();

    const areaGenerator = area()
      .x(d => x(d[xField]))
      .y0(y(0))
      .y1(d => y(d[yField]));

    const areaGenerator2 = area()
      .x(d => x(d[xField]))
      .y0(y(0))
      .y1(d => y(d[yField2]));

    const areaGenerator3 = area()
      .x(d => x(d[xField]))
      .y0(y(0))
      .y1(d => y(d[yField3]));

    return (
      <svg width={width} height={height}>
        <g transform={`translate(${margins.left},${margins.top})`}>
          <rect width={innerWidth} height={innerHeight} fill="#eee" />
          <path
            class="line line--one"
            stroke="#08b4ac"
            fill="#08b4ac"
            stroke-width="1"
            d={areaGenerator(data)}
          />
          <path
            class="line line--two"
            stroke="#04524f"
            fill="#04524f"
            stroke-width="1"
            d={areaGenerator2(data)}
          />
          <path
            class="line line--three"
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
              const str = d.toString();

              if (d === xExtent[0]) return str;

              return `'${str.slice(2)}`;
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
