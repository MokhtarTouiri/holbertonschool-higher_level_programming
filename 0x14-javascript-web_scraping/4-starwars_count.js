#!/usr/bin/node
const process = require('process');
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) 
  const json = JSON.parse(body);
  let i = 0;
  for (let a = 0; json.res[a]; a++) {
    for (let b = 0; json.res[b].characters[b]; b++) {
      if (json.res[a].characters[b].includes('/api/people/18/')) {
           i++; 
        }
    }
  }
  console.log(i);
});
