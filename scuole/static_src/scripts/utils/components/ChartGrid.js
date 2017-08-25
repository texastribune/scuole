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
    const genderTitles = [];
    const gender = 'gender';
    const econTitles = [];
    const econ = 'economic status';
    const ethnicityTitles = [];
    const ethnicity = 'ethnicity';

    ////////////  TO DO //////////////
    const year = 2005;

    chartData.map((c, i) => {
      if (c.data.length > 3) {
        genderTitles.push(c.title);
      }
    });

    const yMax = Math.max(
      ...[].concat(
        ...chartData.map(({ data }) => data.map(d => d.percent_graduated))
      )
    );

    return (
      <div class="chart-block">
        {ethnicityTitles.length !== 0 &&
          <div class="legend-block">
            <h3 class="page-section-subheader">
              Class outcomes by ethnicity over time, 1997-{year}
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
          </div>}

        {genderTitles.length !== 0 &&
          <div class="legend-block">
            <h3 class="page-section-subheader">
              Class outcomes by gender over time, 1997-{year}
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
          </div>}

        {econTitles.length !== 0 &&
          <div class="legend-block">
            <h3 class="page-section-subheader">
              Class outcomes by economic status over time, 1997-{year}
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
          </div>}

        <div class="chart-grid">
          {chartData.map((c, i) => {
            return (
              c.data.length > 3 &&
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
      </div>
    );
  }
}
