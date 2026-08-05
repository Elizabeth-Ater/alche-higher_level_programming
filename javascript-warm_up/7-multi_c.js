#!/usr/bin/node

const count = parseInt(process.argv[2], 10);

if (Number.isNaN(count)) {
  console.log('Missing number of occurrences');
}

const lines = [];

for (let i = 0; i < count; i++) {
  lines.push('C is fun');
}

if (lines.length > 0) {
  console.log(lines.join('\n'));
}
