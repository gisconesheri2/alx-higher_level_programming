#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    let count = 0;
    const films = JSON.parse(body);
    for (const movie of films.results) {
      for (const character of movie.characters) {
        if (character.includes('/18/')) {
          count = count + 1;
        }
      }
    }
    console.log(count);
  }
});
