#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
