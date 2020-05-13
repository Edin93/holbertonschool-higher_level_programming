#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/`;
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    for (let j = 0; j < results.length; j++) {
      // console.log(results[j]);
      if (results[j].episode_id === parseInt(filmId)) {
	for (let i = 0; i < results[j].characters.length; i++) {
	  request(results[j].characters[i], function (err, res, body) {
            if (err) {
              console.log(err);
            } else {
              console.log(JSON.parse(body).name);
            }
	  });
	}
      }
    }
  }
});
