#!/usr/bin/node

const process = require('process');

const numOne = Math.floor(Number(process.argv[2]));
const numTwo = Math.floor(Number(process.argv[3]));

function add (a, b) {
  return a + b;
}

console.log(add(numOne, numTwo));
