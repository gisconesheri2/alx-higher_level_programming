#!/usr/bin/node

const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    for (const character of film.characters) {
      request.get(character, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const person = JSON.parse(body);
          console.log(person.name);
        }
      });
    }
  }
});
