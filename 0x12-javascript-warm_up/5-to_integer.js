#!/usr/bin/node
let integer;
let conv = 'Not a number';
if (process.argv.length > 2) {
  integer = parseInt(process.argv[2]);
  if (!isNaN(integer)) {
    conv = 'My number: ' + String(integer);
  }
}
console.log(conv);
