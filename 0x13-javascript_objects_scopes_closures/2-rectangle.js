#!/usr/bin/node
// Class rectangle defines a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !h || !w) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
};
