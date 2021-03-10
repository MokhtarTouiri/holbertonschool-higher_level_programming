#!/usr/bin/node
const request = require('request');
const process = require('process');
request(process.argv[2], function (error, response, body) {
  if (error) throw error;
  console.log('code:', response.statusCode);
});
