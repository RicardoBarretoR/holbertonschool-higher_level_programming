#!/usr/bin/node
const integer = parseInt(process.argv.slice(2)[0]);
if (!isNaN(integer)) {
  for (let iter = 0; iter < integer; iter++) {
    console.log('x'.repeat(integer));
  }
} else {
    console.log('Missing size');
}
