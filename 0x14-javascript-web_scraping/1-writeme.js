#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
fs.writeFile(argv[2], argv[3], 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
