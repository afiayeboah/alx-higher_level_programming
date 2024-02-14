#!/usr/bin/node

const { readFileSync, writeFile } = require('fs');
const { argv } = require('process');

const getContent = (file) => readFileSync(file, 'utf8');

const file1Content = getContent(argv[2]);
const file2Content = getContent(argv[3]);
const concatenatedContent = file1Content + '' + file2Content;

writeFile(argv[4], concatenatedContent, 'utf8', (err) => {
  if (err) throw err;
});
