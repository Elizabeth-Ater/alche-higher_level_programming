#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    films.forEach((film) => {
      const hasWedge = film.characters.some(
        (character) => character.endsWith('/18/')
      );
      if (hasWedge) {
        count += 1;
      }
    });

    console.log(count);
  }
});
