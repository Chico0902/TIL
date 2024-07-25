const fs = require('fs')
const input = fs.readFileSync.toString('15829.txt').trim().split('\n')


const L = Number(input[0]);
const arr = input[1].split('')
const new_arr = [];

for (let i = 0; i < arr.length; i++) {
    new_arr.push(arr[i].charCodeAt(0) - 96);
}

let ans = 0;
for (let i = 0; i < L; i++) {
    ans += new_arr[i] * (31 ** i);
}

console.log(ans % 1234567891);
