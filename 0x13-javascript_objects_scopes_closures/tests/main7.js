#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([], 40));
console.log(nbOccurences(['S', 12, 'c', 'S', 'School', 8], 'S'));
