#!/usr/bin/node
//print according to arguments

if (process.argv.length === 2){
    console.log("No arguement");
} else if (process.argv.length === 3){
    console.log('Arguement found');
} else {
    console.log('Arguements found');
}