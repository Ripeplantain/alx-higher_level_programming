#!/usr/bin/node
//print first arguement passed to it

if (process.argv[2] == undefined){
    console.log('No arguement');
} else {
    console.log(process.argv[2]);
}