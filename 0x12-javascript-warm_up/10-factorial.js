#!/usr/bin/node

const num = process.argv[2];
function factorial (x) {
  if (isNaN(x) || x === 0) {
    return (1);
  }
  return (x * factorial(x - 1));
}
console.log(factorial(parseInt(num)));
