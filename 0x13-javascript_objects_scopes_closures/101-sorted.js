#!/usr/bin/node
const dict = require('./101-data').dict;

function sortByOccurrences (obj) {
  const dict = {};
  for (const key in obj) {
    dict[obj[key]] = [];
  }
  for (const key in obj) {
    dict[obj[key]].push(key);
  }
  return dict;
}

console.log(sortByOccurrences(dict));
