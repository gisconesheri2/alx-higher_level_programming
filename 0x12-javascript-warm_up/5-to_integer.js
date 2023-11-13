#!/usr/bin/node

const process = require('process');

let integer = Number(process.argv[2]);

if (integer) {
  integer = Math.floor(integer);
  console.log(`My number: ${integer}`);
} else {
  console.log('Not a number');
}
