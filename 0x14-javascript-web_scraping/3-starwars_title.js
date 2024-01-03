#!/usr/bin/node

const request = require('request');

request
  .get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log(movie.title);
    }
  });
