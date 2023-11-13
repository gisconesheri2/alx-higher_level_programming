#!/usr/bin/node

const process = require('process');

const numOcur = Math.floor(Number(process.argv[2]));

if (isNaN(numOcur)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numOcur; i++) {
    let row = '';
    for (let z = 0; z < numOcur; z++) {
      row = row + 'X';
    }
    console.log(row);
  }
}
