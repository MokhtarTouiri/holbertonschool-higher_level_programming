#!/usr/bin/node
let c = 0;
module.exports.logMe = function (item) {
  console.log(`${c}: ${item}`);
  c++;
};
