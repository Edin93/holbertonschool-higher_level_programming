#!/usr/bin/node

const n = process.argv[2];
function factorial (n) {
  if (n > 1) {
    return n * factorial(n - 1);
  } else if (n === 1) {
    return 1;
  }
}

if (!n || !(typeof (n))) {
  console.log('%d', 1);
} else {
  console.log('%d', factorial(n));
}
