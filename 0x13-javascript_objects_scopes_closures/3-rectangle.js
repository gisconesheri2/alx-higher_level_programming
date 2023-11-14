#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let hc = 0; hc < this.height; hc++) {
      let row = '';
      for (let wc = 0; wc < this.width; wc++) {
        row = row + 'X';
      }
      console.log(row);
    }
  }
};
