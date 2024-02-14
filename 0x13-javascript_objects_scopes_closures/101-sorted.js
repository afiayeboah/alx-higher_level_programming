#!/usr/bin/node
const data = require('./101-data').dict;
const keys = Object.keys(data);
const values = Object.values(data);
let matchedKeys;
const result = {};

for (let i = 0; i < values.length; i++) {
  result[JSON.stringify(values[i])] = [];
  matchedKeys = keys.filter(key => data[key] === values[i]);
  matchedKeys.forEach(item => result[JSON.stringify(values[i])].push(item));
}

console.log(result);
