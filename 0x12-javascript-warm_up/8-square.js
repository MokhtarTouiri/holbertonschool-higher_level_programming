#!/usr/bin/node
const size = parseInt(process.argv[2]);
for (let y = 0; y < size; y++) {
for (let z = 0; z < size; z++) {
    let i = '';
    i += 'X';
  }
  console.log(i);
    i = '';
}
if (process.argv[2] === 0 || isNaN(process.argv[2])) {
  console.log('Missing size');
}
