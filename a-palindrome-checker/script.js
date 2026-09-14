const textInput=document.getElementById("text-input");
const checkBtn = document.getElementById("check-btn");
const result=document.getElementById("result");

checkBtn.addEventListener("click",()=>{
    const rawInput = textInput.value;
    if(rawInput===""){
        alert("Please input a value");
        return;
    }

    const cleanInput = rawInput.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
    const reversedInput = cleanInput=cleanInput.split("").reverse().join("");

    if (cleanInput === reversedInput) {
        result.textContent = `${rawInput} is a palindrome`;
    } else {
        result.textContent = `${rawInput} is not a palindrome`;
    }

});


//公式による「正解」

const checkBtn = document.getElementById('check-btn');
const textInput = document.getElementById('text-input');
const result = document.getElementById('result');

const checkPalindrome = (str) => {
  const correction = str.toLowerCase().replace(/[^a-zA-Z0-9]/g, '');
  const reversedStr = correction.split('').reverse().join('');
  return correction === reversedStr;
}

checkBtn.addEventListener('click', (e) => {
  e.preventDefault();
  const text = textInput.value;
  if (!text) {
    alert('Please input a value');
    return;
  }

  const isPalindrome = checkPalindrome(text);
  result.textContent = isPalindrome ? `${text} is a palindrome` : `${text} is not a palindrome`;
  console.log(result.textContent);
  textInput.value = '';
  result.classList.remove('hidden');
})