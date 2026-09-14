function smallestCommons(arr){
    const min = Math.min(arr[0], arr[1]);
    const max = Math.max(arr[0], arr[1]);

    const gcd = (a,b) => (b === 0 ? a : gcd(b,a % b));

    const lcm = (a,b,) => (a*b) / gcd(a,b);

    let multiple = min;
    for(let i= min + 1; i <= max; i++) {
        multiple = lcm(multiple, i)
    }
    return multiple;
}