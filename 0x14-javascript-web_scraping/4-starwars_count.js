#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/movies' + process.argv[2];
request(url, function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    let movies = JSON.parse(body).results;
    for (let m in movies) {
      let characters = movies[m].characters;
      for (let c in characters) {
        if (characters[c].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
    body = JSON.parse(body);
    console.log(body.title);
  }
});
