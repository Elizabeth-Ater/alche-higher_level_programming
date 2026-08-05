#!/usr/bin/node

const fs = require('fs');

const path = process.argv[2];

try {
  const data = fs.readFileSync(path, 'utf8');
  console.log(data);
} catch (error) {
  console.log(error);
}
