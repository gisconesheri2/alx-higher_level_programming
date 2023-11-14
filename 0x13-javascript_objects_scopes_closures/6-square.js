#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let hc = 0; hc < this.height; hc++) {
      let row = '';
      for (let wc = 0; wc < this.width; wc++) {
        row = row + c;
      }
      console.log(row);
    }
  }
};
