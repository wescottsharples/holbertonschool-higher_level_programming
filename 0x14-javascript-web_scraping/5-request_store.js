#!/usr/bin/node
let request = require('request');
const fs = require('fs');
request.get(process.argv[2], function (err, r, body) {
  if (err) {
    console.log(err);
  } else if (r.statusCode === 200) {
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
