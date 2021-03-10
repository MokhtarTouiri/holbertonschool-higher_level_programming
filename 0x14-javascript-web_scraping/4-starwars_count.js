#!/usr/bin/node
const request = require('request');
const process = require('process');

request(process.argv[2], function (error, response, body) {
    let x = 0;
    if (error) {
      console.log(error);
    }
    const jsn = JSON.parse(body);
    for (let i = 0; jsn.results[i] !== undefined; i++) {
      if (jsn.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        x++;
      }
    }
    console.log(c);
  });
  