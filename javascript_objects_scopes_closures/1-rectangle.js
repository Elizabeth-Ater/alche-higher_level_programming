#!/usr/bin/node

const fs = require('fs');

const path = process.argv[2];
const content = process.argv[3];

try {
  fs.writeFileSync(path, content, 'utf8');
} catch (error) {
  console.log(error);
}
