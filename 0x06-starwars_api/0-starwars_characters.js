#!/usr/bin/node

const request = require('request');

const movieId = (array, a) => {
  if (a === array.length) return;
  request(array[a], (_error, response, body) => {
    if (_error) {
      throw _error;
    } else {
        console.log(JSON.parse(body).name);
        movieId(array, a + 1);
    }
  });
};

request(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (_error, response, body) => {
    if (_error) {
      throw _error;
    } else {
      const charachtersReqBody = JSON.parse(body).characters;
      movieId(charachtersReqBody, 0);
    }
  }
);
