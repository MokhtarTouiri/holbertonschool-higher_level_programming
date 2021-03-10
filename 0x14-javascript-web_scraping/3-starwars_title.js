#!/usr/bin/node
const request = require('request');
const process = require('process');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const jsn = JSON.parse(body);
  console.log(jsn.title);
});
