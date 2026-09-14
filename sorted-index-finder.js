function getIndexToIns(arr, num) {
    arr.sort((a,b)=> a-b);

    const index = arr.findIndex(element=>element >= num);

    return index === -1 ? arr.length: index;
}

//

function gcd(a,b){
    while (b !== 0) {
        const temp = b;
        b=a%b;
        a=temp;
    }
    return a;
}

function lcm(a,b){
    if(a===0 || b === 0) return 0;
    return Math.abs(a/ gcd(a,b)) * b;
}

function ldmArray(numbers){
    return numbers.reduce((acc,curr)=> lcm(acc,curr),1);
}

console.log(lcmArray([12,18,24]));

//
const bigNum1 = 9007199254740991n; // リテラル
const bigNum2 = BigInt("9007199254740992");

const num = bigNum1 + bigNum2;

console.log(5n / 2n);

//

function gcdBigInt(a,b){
    if(a=== 0n || b === 0n) return 0n;
    return (a / gcdBigInt(a,b)*b);
}

const range50 = Array.from({ length: 50 }, (_, i) => BigInt(i + 1));
const result = range50.reduce((acc, curr) => lcmBigInt(acc, curr), 1n);

console.log(result.toString());