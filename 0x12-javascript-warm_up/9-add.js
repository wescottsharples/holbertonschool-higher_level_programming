#!/usr/bin/node

const num1 = process.argv[2];
const num2 = process.argv[3];
function add (x, y) {
  return (x + y);
}
console.log(add(parseInt(num1), parseInt(num2)));
