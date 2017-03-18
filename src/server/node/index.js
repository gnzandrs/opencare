var express = require('express');
var app = express();

var logger = require('./logger');
app.use(logger);

app.get('/', function (request, response) {
  response.send('Hello World');
});

app.listen(3000, function () {
  console.log('Server running on port 3000 \n');
});
