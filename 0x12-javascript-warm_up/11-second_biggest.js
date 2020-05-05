#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('%d', 0);
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  arr.sort((a, b) => b - a);
  console.log('%d', arr[1]);
}
