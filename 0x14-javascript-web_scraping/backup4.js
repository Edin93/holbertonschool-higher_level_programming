#!/usr/bin/node

const request = require('request');

if (process.argv.length === 3) {
  const url = process.argv[2];
  let count = 0;
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      // console.log(JSON.parse(body));
      const results = JSON.parse(body).results;
      for (let i = 0; i < results.length; i++) {
	const charUrls = results[i].characters;
	for (let j = 0; j < charUrls; j++) {
	  request(charUrls[j], function (error, response, body) {
	    if (error) {
	      console.log(error)
	    } else {
	      console.log(JSON.parse(body));
	    }
	  })
	}
      }
    }
  });
  console.log(count);
}
