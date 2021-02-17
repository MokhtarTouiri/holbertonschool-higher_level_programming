#!/usr/bin/node
let i = '';
const s = parseInt(process.argv[2]);
for (let a = 0; a < s; a++) {
for (let b = 0; b < s; b++) {
    i += 'X';
  }
  console.log(i);
  i = '';
}
if (process.argv[2] === 0 || isNaN(process.argv[2])) {
  console.log('Missing size');
}
