#!/usr/bin/node
const argts = process.argv.slice(2);
if (argts.length < 2) {
  console.log(0);
} else {
  console.log(argts.sort().reverse()[1]);
}
