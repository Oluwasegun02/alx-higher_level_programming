# Javascript - Objects, Scopes and Closures

In this second ALX JavaScript project the language - scope, closures I practiced working with objects and ES6-style classes.

Documention
https://developer.mozilla.org/en-US/docs/Web/JavaScript/

1-rectangle:

In Node.js, every file is considered as a module and can be treated as a separate unit of functionality that can be reused in other parts of the application. To make a class or a function available to other parts of the application, you need to export it as a module.

In this code, the Rectangle class is being defined with a constructor that takes two arguments, w and h, which represent the width and height of the rectangle, respectively. The this.width and this.height properties are then set to these values.

To make this class available as a module, it is being assigned to module.exports. This means that other parts of the application can import this module and use the Rectangle class to create new rectangle objects. For example, if this code is saved in a file called rectangle.js, you could use the Rectangle class in another file like this: