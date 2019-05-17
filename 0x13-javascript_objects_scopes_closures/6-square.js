#!/usr/bin/node
const SquareOld = require('./5-square');
class Square extends SquareOld {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
