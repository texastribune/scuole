import { Component, h } from 'preact';

import Chart from './Chart';
import ResponsiveContainer from './ResponsiveContainer';

function BlankChart({ width }) {
  width -= 20;
  const height = width * 0.625;

  return (
    <div class="blank-chart" style={{ width, height }}>
      <p>No data</p>
    </div>
  );
}

export default class ChartGrid extends Component {
  render({ chartData = [] }) {
    const yMax = Math.max(
      ...[].concat(
        ...chartData.map(({ data }) => data.map(d => d.percent_graduated))
      )
    );

    return (
      <div class="chart-grid">
        {chartData.map((c, i) => {
          return (
            c.data.length !== 0 &&
            <div class="chart-container">
              <h3 class="page-section-subheader-cohort">
                {c.title}
              </h3>
              <ResponsiveContainer>
                <Chart
                  data={c.data}
                  xField="year"
                  yField="percent_graduated"
                  yField2="percent_enrolled_higher_education"
                  yField3="percent_completed_higher_education"
                  yMax={yMax}
                  margins={{ left: 40 }}
                />
              </ResponsiveContainer>
            </div>
          );
        })}
      </div>
    );
  }
}
