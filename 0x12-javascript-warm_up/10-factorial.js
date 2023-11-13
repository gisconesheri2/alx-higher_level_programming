#!/usr/bin/node

const process = require('process');

const numProvided = Number(process.argv[2]);

function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(numProvided));
