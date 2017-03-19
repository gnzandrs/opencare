var express = require('express');
var app = express();
var req = require('request');

var logger = require('./logger');
app.use(logger);

app.get('/', function (request, response) {
  response.send('Api Index');
});

app.get('/person/list', function (request, response) {
  req('http://localhost:8000/person/list', function (error, responseApi, data) {
    if (!error && responseApi.statusCode == 200) {
      response.send(data);
    }
  });
});

app.listen(3000, function () {
  console.log('Server running on port 3000 \n');
});
