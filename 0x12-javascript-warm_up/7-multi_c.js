#!/usr/bin/node

const process = require('process');

const numOcur = Math.floor(Number(process.argv[2]));

if (isNaN(numOcur)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < numOcur; i++) {
    console.log('C is fun');
  }
}
