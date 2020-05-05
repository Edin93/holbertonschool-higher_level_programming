#!/usr/bin/node

if (!Number(process.argv[2])) {
  console.log('Missing size');
} else {
  let msg = '';
  for (let i = 0; i < process.argv[2]; i++) {
    msg += 'X';
  }
  for (let j = 0; j < process.argv[2]; j++) {
    console.log('%s', msg);
  }
}
