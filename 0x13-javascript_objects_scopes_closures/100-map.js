#!/usr/bin/node
const list = require('./100-data.js');
function multiply (a, b) {
  return a * b;
}
const newList = list.map((x, i) => x * i);
console.log(list);
console.log(newList);
