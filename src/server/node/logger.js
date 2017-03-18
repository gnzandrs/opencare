module.exports = function (request, response, next) {
  var startTime  = +new Date();
  var stream = process.stdout;
  var url = request.url;
  var method = request.method;

  response.on('finish', function () {
    var durationTime = +new Date() - startTime;
    var message = method + ' to ' + url + '\ntook ' + durationTime + ' ms \n\n';
    stream.write(message);
  });

  next();
}
