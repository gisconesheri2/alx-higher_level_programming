#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  const completedTasks = {};
  const todoTasks = JSON.parse(body);
  if (!error && response.statusCode === 200) {
    for (const task of todoTasks) {
      if (task.completed === true) {
        if (task.userId in completedTasks) {
          completedTasks[task.userId] = completedTasks[task.userId] + 1;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
