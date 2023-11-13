#!/usr/bin/node

const process = require('process');
let total = 0;

for (let x in process.argv) {
  x = x + '';
  total++;
}

if (total === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
