#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) { throw err; }
  const js = JSON.parse(body);
  let i = 0;
  for (let a = 0; js.results[a]; a++) {
    for (let b = 0; js.results[a].characters[b]; b++) {
      if (js.results[i].characters[b].includes('/api/people/18/')) { i++; }
    }
  }
  console.log(i);
});
