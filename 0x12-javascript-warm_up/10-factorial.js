#!/usr/bin/node
//prints a factorial

function factorial(n) {
    if (isNaN(n) || n == 1){
        return 1;
    } else {
        return n * (n - 1);
    }
}

console.log(factorial(parseInt(process.argv[2])));