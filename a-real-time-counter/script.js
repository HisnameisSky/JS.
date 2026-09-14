const textInput = document.getElementById("text-input");
const charCount = document.getElementById("char-count");

textInput.addEventListener("input", () => {
  if (textInput.value.length > 50) {
    textInput.value = textInput.value.slice(0, 50);
  }

  const length = textInput.value.length;
  charCount.textContent = `Character Count: ${length}/50`;

  if (length === 50) {
    charCount.classList.add("red");
  } else {
    charCount.classList.remove("red");
  }
});