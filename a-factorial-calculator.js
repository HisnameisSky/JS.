const num = 5;

function factorialCalculator(n) {
  let result = 1;
  
  for (let i = 1; i <= n; i++) {
    result = result * i; // result *= i; と書いてもOK
  }
  
  return result;
}

const factorial = factorialCalculator(num);

const resultMsg = `Factorial of ${num} is ${factorial}`;

console.log(resultMsg);
