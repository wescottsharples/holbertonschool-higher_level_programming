#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/films' + process.argv[2];
request(url, function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    let body = JSON.parse(body);
    console.log(body.title);
  }
});
