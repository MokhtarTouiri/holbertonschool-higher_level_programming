#!/usr/bin/node
""" Who was playing in this movie """

const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi.co/api/films/' + movie;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const dict = JSON.parse(body);
  const characters = dict.characters;
  characters.forEach(character => {
    request(character, (error, response, data) => {
      if (error) throw error;
      console.log(JSON.parse(data).name);
    });
  });
});
