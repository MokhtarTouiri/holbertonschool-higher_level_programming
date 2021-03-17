#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) {
  const Any = {};
  const json = JSON.parse(body);
  for (const ex of json) {
    if (ex.completed === true) {
      if (Any[ex.userId]) {
        Any[ex.userId] += 1;
      } else {
        Any[ex.userId] = 1;
      }
    }
  }
  console.log(Any);
});
