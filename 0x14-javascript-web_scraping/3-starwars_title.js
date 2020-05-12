#!/usr/bin/node

const request = require('request');

if (process.argv.length === 3) {
  const filmId = process.argv[2];
  const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  request.get(url).on('response', function (response) {
    console.log(response.title);
  });
}
