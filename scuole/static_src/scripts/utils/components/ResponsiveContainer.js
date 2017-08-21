import { cloneElement, Component, h } from 'preact';

export default class ResponsiveContainer extends Component {
  componentDidMount() {
    this.parentNode = this.base.parentNode;
    this.getSize();
  }

  getSize() {
    this.setState({
      bounds: this.parentNode.getBoundingClientRect(),
    });
  }

  render({ children }, { bounds }) {
    if (!bounds) return null;
    return cloneElement(children[0], bounds);
  }
}
