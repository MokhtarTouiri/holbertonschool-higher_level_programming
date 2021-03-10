#!/usr/bin/node
const process = require('process');
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) { 
      throw error; 
    }
  const jsn = JSON.parse(body);
  let i = 0;
  for (let a = 0; jsn.results[a]; a++) {
    for (let b = 0; jsn.results[a].characters[b]; b++) {
      if (jsn.results[a].characters[b].includes('/api/people/18/')) {
           i++; 
        }
    }
  }
  console.log(i);
});
