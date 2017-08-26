import { Component, h } from 'preact';

export default class Dimensions extends Component {
  constructor() {
    super();

    this.state = {
      containerHeight: null,
      containerWidth: null,
    };
  }

  render({}, { containerWidth, containerHeight }) {}
}
