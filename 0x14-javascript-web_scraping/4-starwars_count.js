#!/usr/bin/node
const process = require('process');

request(process.argv[2], function (error, response, body) {
    let x = 0;
    if (error) {
      console.log(error);
    }
    const js = JSON.parse(body);
    for (let i = 0; js.results[i] !== undefined; i++) {
      if (js.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        x++;
      }
    }
    console.log(x);
  });
