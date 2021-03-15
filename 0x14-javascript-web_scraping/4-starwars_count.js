#!/usr/bin/node
const process = require('process');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (error) { throw error; }
  const json = JSON.parse(body);
  let z = 0;
  for (let i = 0; json.results[i]; i++) {
    for (let y = 0; json.results[i].characters[y]; y++) {
      if (json.results[i].characters[y].includes('/api/people/18/')) { z++; }
    }
  }
  console.log(z);
});
