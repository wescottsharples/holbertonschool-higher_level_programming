#!/usr/bin/node

const numArr = process.argv.slice(2);
function findSecondBiggest (array) {
  if (array.length < 2) {
    return (0);
  } else {
    array.sort((x, y) => x - y);
    array.reverse();
    return (array[1]);
  }
}
console.log(findSecondBiggest(numArr));
