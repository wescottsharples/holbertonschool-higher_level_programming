#!/usr/bin/node

const num = process.argv[2];
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < parseInt(num); i++) {
    console.log('C is fun');
  }
}
