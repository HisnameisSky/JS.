function sequence() {
  const fibonacci = [0, 1];

  return function getFibonacci(n) {
    if (n < 0) return undefined;

    while (fibonacci.length <= n) {
      const len = fibonacci.length;
      fibonacci.push(fibonacci[len - 1] + fibonacci[len - 2]);
    }

    return fibonacci[n];
  };
}

const fibonacci = sequence();

//alt

function fibonacci(n) {
    const sequence = [0, 1];
    
    if (n === 0) return 0;
    if (n === 1) return 1;
    
    for (let i = 2; i <= n; i++) {
        const nextNum = sequence[i-2] + sequence[i-1];
        sequence.push(nextNum);
    }
    
    return sequence[n];
}