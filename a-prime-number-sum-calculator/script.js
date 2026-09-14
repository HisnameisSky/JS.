function sumPrimes(num){
    if(num<2){
        return 0;
    }
    function isPrime(n){
        if(n<2)return false;
        for(let i=2; i<=Math.sqrt(n); i++){
            if(n%i===0) return false;
        }
        return true;
    }
    let sum =0;
    for(let i=2; i<=num; i++){
        if(isPrime(i)){
            sum+=i;
        }
    }
    return sum ;
}

console.log(sumPrimes(10));  // 17 (2 + 3 + 5 + 7)
console.log(sumPrimes(5));   // 10 (2 + 3 + 5)
console.log(sumPrimes(2));   // 2
console.log(sumPrimes(0));   // 0
console.log(sumPrimes(977)); // 73156