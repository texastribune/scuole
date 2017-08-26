import { Component, h } from 'preact';

const top = 1;
const right = 2;
const bottom = 3;
const left = 4;
const epsilon = 1e-6;

function translateX(x) {
  return `translate(${x + 0.5},0)`;
}

function translateY(y) {
  return `translate(0,${y + 0.5})`;
}

function number(scale) {
  return function(d) {
    return +scale(d);
  };
}

function center(scale) {
  var offset = Math.max(0, scale.bandwidth() - 1) / 2; // Adjust for 0.5px offset.
  if (scale.round()) offset = Math.round(offset);
  return function(d) {
    return +scale(d) + offset;
  };
}

function identity(x) {
  return x;
}

const orientations = {
  top: 1,
  right: 2,
  bottom: 3,
  left: 4,
};

export default class Axis extends Component {
  render({
    orientation = 'left',
    scale,
    tickArguments = [],
    firstTickFormat,
    tickFormat,
    tickPadding = 3,
    tickSize,
    tickSizeInner = 6,
    tickSizeOuter = 6,
    tickValues,
    ...props
  }) {
    const orient = orientations[orientation];

    // if (tickSize) {
    //   tickSizeInner = tickSizeOuter = tickSize;
    // }

    const k = orient === top || orient === left ? -1 : 1;
    const x = orient === left || orient === right ? 'x' : 'y';
    const transform =
      orient === top || orient === bottom ? translateX : translateY;

    const values =
      tickValues == null
        ? scale.ticks ? scale.ticks.apply(scale, tickArguments) : scale.domain()
        : tickValues;
    const format =
      tickFormat == null
        ? scale.tickFormat
          ? scale.tickFormat.apply(scale, tickArguments)
          : identity
        : tickFormat;
    const spacing = Math.max(tickSizeInner, 0) + tickPadding;
    const range = scale.range();
    const range0 = +range[0] + 0.5;
    const range1 = +range[range.length - 1] + 0.5;
    const position = (scale.bandwidth ? center : number)(scale.copy());

    const lineProps = {
      [`${x}2`]: k * tickSizeInner,
    };

    const textProps = {
      [x]: k * spacing,
      dy: orient === top ? '0em' : orient === bottom ? '0.71em' : '0.32em',
    };

    return (
      <g
        fill="none"
        font-size={10}
        font-family="sans-serif"
        text-anchor={
          orient === right ? 'start' : orient === left ? 'end' : 'middle'
        }
        {...props}
      >
        <path
          class="domain"
          stroke="#000"
          d={
            orient === left || orient == right
              ? 'M' +
                k * tickSizeOuter +
                ',' +
                range0 +
                'H0.5V' +
                range1 +
                'H' +
                k * tickSizeOuter
              : 'M' +
                range0 +
                ',' +
                k * tickSizeOuter +
                'V0.5H' +
                range1 +
                'V' +
                k * tickSizeOuter
          }
        />
        {values.map((d, i) =>
          <g class="tick" transform={transform(position(d))} key={i}>
            <line stroke="#000" {...lineProps} />
            <text fill="#000" {...textProps}>
              {format(d, i)}
            </text>
          </g>
        )}
      </g>
    );
  }
}
