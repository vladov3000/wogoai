
// load dependencies
const express = require('express'),
  logger = require('morgan'),
  path = require('path');
 
var app = express();

app.use(logger('dev'));
app.use(express.static(path.join(__dirname, 'build')));

app.get('/', function (req, res, next) {
  try {
    res.sendFile(path.join(__dirname, 'build', 'index.html'));
  } catch (e) {
    next(e);
  }
})

app.listen(process.env.PORT || 3000, function () {
  console.log('Listening on http://localhost:' + (process.env.PORT || 3000));
})
