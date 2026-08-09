#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const result = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (result[todo.userId]) {
          result[todo.userId] += 1;
        } else {
          result[todo.userId] = 1;
        }
      }
    });

    console.log(result);
  }
});
