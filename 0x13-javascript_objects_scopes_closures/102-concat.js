#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  fs.writeFile(process.argv[4], '', 'utf8', (err) => {
    if (err) {
      throw err;
    }
  });
  fs.readFile(process.argv[2], (err, data) => {
    if (err) {
      throw err;
    }
    if (Object.keys(data).length !== 0 && data.constructor !== Object) {
      fs.appendFile(process.argv[4], data + '\n', (err) => {
        if (err) {
          throw (err);
        }
      });
    }
  });
  fs.readFile(process.argv[3], (err, data) => {
    if (err) {
      throw err;
    }
    if (Object.keys(data).length !== 0 && data.constructor !== Object) {
      fs.appendFile(process.argv[4], data + '\n', (err) => {
        if (err) {
          throw (err);
        }
      });
    }
  });
}
