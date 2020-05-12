#!/usr/bin/node

let XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

let requestURL = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json';

let request = new XMLHttpRequest();

request.open('GET', requestURL);
request.responseType = 'json';
request.send();
request.onload = function() {
  let res = request.responseText;
  console.log(res);
}
