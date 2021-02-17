#!/usr/bin/node
for (let x = 0; x < process.argv[2]; x++) {
  console.log('C is fun');
}
if (process.argv[2] === 0 || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
}
