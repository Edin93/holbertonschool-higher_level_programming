#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    for (let j = 0; j < results.length; j++) {
      // console.log(results[j]);
      if (results[j].url === `${url}${filmId}/`) {
	console.log(results[j].characters);
	console.log('-----------------------');
	let characters = results[j].characters.sort(function (a, b) {
	  // let na = a.slice(0, -1).lastIndexOf('/');
	  // na = a.slice(na + 1, -1);
	  let na = a.slice(a.slice(0, -1).lastIndexOf('/') + 1, -1);
	  let nb = b.slice(b.slice(0, -1).lastIndexOf('/') + 1, -1);
	  return (parseInt(na) - parseInt(nb));
	});
	console.log(characters);
	for (let i = 0; i < characters.length; i++) {
          request(characters[i], function (err, res, body) {
            if (err) {
              console.log(err);
            } else {
	      // console.log(JSON.parse(body).url);
              // console.log(JSON.parse(body).name);
            }
          });
        }
      }
    }
  }
});
