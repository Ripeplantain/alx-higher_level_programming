#!/usr/bin/node
// Print the status code of a get request

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error){
    console.error('Error: ', error);
  }
  console.log('code: ', response && response.statusCode);
});
