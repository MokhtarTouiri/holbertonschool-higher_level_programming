#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } fs.writeFile(process.argv[3], body, 'utf8', (err) => {
    if (err) console.log(err);
  });
});
