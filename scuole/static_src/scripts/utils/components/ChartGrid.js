import { Component, h } from 'preact';

import Chart from './Chart';
import ResponsiveContainer from './ResponsiveContainer';

function last(array) {
  const length = array == null ? 0 : array.length;
  return length ? array[length - 1] : undefined;
}

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
  render({ title, chartData = [] }) {
    const legendShouldRender = chartData.some((c, i) => {
      if (
        c.data &&
        c.data.some(d => d.percent_graduated) &&
        c.data.length > 3
      ) {
        return true;
      } else {
        return false;
      }
    });

    if (!legendShouldRender) {
      return (
        <div class="chart-block">
          <div class="chart-grid" />
        </div>
      );
    }

    const yMax = Math.max(
      ...[].concat(
        ...chartData.map(({ data }) => data.map(d => d.percent_graduated))
      )
    );
    let year;
    if (chartData[0].data.length == 0) {
      year = last(chartData[1].data).year;
    } else {
      year = last(chartData[0].data).year;
    }
    return (
      <div class="chart-block">
        {legendShouldRender && (
          <div class="legend-block">
            <h3 class="page-section-subheader">
              Class outcomes by {title} over time, 1997-{year}
            </h3>
            <div class="legend">
              <div class="legend__cell">
                <span class="dot dot--graduated" />Graduated from high school
              </div>
              <div class="legend__cell">
                <span class="dot dot--enrolled" />Graduated and enrolled in
                college
              </div>
              <div class="legend__cell">
                <span class="dot dot--completed" />Graduated, enrolled in and
                completed college
              </div>
            </div>
          </div>
        )}

        <div class="chart-grid">
          {legendShouldRender &&
            chartData.map((c, i) => {
              return (
                c.data.length > 3 && (
                  <div class="chart-container">
                    <h3 class="page-section-subheader-cohort">{c.title}</h3>
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
                )
              );
            })}
        </div>
      </div>
    );
  }
}
