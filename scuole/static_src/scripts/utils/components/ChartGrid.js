import { Component, h } from 'preact';

import Chart from './Chart';

export default class ChartGrid extends Component {
  componentDidMount() {
    console.log(this.base.parentNode.clientWidth);
  }

  render({ chartData = [] }) {
    const yMax = Math.max(
      ...[].concat(
        ...chartData.map(({ data }) => data.map(d => d.percent_graduated))
      )
    );

    return (
      <div class="chart-grid">
        {chartData.map((c, i) =>
          <div class="chart-container">
            <h3 class="page-section-subheader-cohort">
              {c.title}
            </h3>
            <Chart
              data={c.data}
              xField="year"
              yField="percent_graduated"
              yField2="percent_enrolled_higher_education"
              yField3="percent_completed_higher_education"
              yMax={yMax}
              margins={{ left: 40 }}
            />
          </div>
        )}
      </div>
    );
  }
}
