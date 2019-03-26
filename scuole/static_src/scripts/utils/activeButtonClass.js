import classie from 'desandro-classie';
import forEach from 'lodash.foreach';

export default (elementList, activeElement, activeClass, inactiveClass) => {
  forEach(elementList, function(el) {
    if (el === activeElement) {
      classie.remove(el, inactiveClass);
      classie.add(el, activeClass);
    } else {
      classie.remove(el, activeClass);
      classie.add(el, inactiveClass);
    }
  });
};
