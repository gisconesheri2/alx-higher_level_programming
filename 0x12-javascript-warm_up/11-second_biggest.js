#!/usr/bin/node

const process = require('process');

function compareNum (a, b) {
  return b - a;
}

if (process.argv.length === 2) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('1');
} else {
  const numList = [];
  for (let i = 2; i < process.argv.length; i++) {
    numList.push(Number(process.argv[i]));
  }
  numList.sort(compareNum);
  console.log(numList[1]);
}
