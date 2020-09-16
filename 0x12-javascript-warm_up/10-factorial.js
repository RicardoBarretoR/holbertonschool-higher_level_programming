#!/usr/bin/node
function factorialize (n) {
  let t = 1;
  if (isNaN(n)) {
    n = 1;
  }
  for (let i = 1; i <= n; i++) {
    t *= i;
  }
  console.log(t);
}
factorialize(parseInt(process.argv.slice(2)[0]));
