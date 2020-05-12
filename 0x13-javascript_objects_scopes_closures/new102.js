#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 5) {
  const file1Content = fs.readFileSync(process.argv[2]);
  const file2Content = fs.readFileSync(process.argv[3]);
  fs.writeFileSync(process.argv[4], file1Content + file2Content);
}
