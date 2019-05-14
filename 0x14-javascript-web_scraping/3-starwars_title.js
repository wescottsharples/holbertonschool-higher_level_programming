#!/usr/bin/node
const request = require('request');
url = 'http://swapi.co/api/films' + process.argv[2]
fs.readFile(url, function (err, r, body) {
    if (err) {
        console.log(err);
    } else {
        body = JSON.parse(body);
        console.log(body['title']);
    }
});