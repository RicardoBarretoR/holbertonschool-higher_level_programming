#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) { console.log(err); return; }

  const tasks = JSON.parse(body);
  const tasksCompleted = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (tasksCompleted[task.userId] === undefined) {
        tasksCompleted[task.userId] = 1;
      } else {
        tasksCompleted[task.userId] += 1;
      }
    }
  });

  console.log(tasksCompleted);
});
