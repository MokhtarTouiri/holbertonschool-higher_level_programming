#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  let a = 0;
  if (error) {
    console.log(error);
  }
  const js = JSON.parse(body);
  for (let b = 0; js.results[b] !== undefined; b++) {
    if (js.results[b].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      a++;
    }
  }
  console.log(a);
});
