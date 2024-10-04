#!/usr/bin/node
// Import the 'fs' (File System) module
const fs = require('fs');

// Get command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the content to the specified file
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error("An error occurred:", err); // Print the error if any occurs
  } else {
    console.log("File written successfully!");
  }
});

