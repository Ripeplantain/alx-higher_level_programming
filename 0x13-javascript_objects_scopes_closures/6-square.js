#!/usr/bin/node
// Class square represents a square
const ParentSquare = require('./5-square');
module.exports = class Square extends ParentSquare {
  CharPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
