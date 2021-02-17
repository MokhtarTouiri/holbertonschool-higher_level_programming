#!/usr/bin/node
function factorial (i) {
  if ((Number.isNaN(i)) || (i < 2)) {
    return 1;
  }
  return i * factorial(i - 1);
}
console.log(factorial(parseInt(process.argv[2])));
