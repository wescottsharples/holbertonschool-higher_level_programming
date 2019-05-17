#!/usr/bin/node
exports.converter = function (base) {
  return function conbase (num) {
    return num.toString(base);
  };
  // return conbase(num, base);
};
