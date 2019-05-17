#!/usr/bin/node
let request = require('request');
let taskcount = {};
let user;
request.get(process.argv[2], function (err, request, body) {
  if (err) {
    console.log(err);
  }
  if (request.statusCode === 200) {
    for (user of JSON.parse(body)) {
      if (user.completed === true) {
        if (taskcount[user.userId] === undefined) {
          taskcount[user.userId] = 0;
        }
        taskcount[user.userId]++;
      }
    }
  }
  console.log(taskcount);
});
