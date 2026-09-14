const regexPattern = document.getElementById("pattern");
const stringToTest = document.getElementById("test-string");
const testButton = document.getElementById("test-btn");
const testResult = document.getElementById("result");

const caseInsensitiveFlag = document.getElementById("i");
const globalFlag = document.getElementById("g");

function getFlags() {
  let flags = "";
  if (caseInsensitiveFlag.checked) {
    flags += "i";
  }
  if (globalFlag.checked) {
    flags += "g";
  }
  return flags;
}

testButton.addEventListener("click", () => {
  const patternText = regexPattern.value;
  const rawText = stringToTest.innerText || stringToTest.textContent;
  const flags = getFlags();

  if (!patternText) {
    testResult.textContent = "no match";
    return;
  }

  try {
    const regex = new RegExp(patternText, flags);
    const matches = rawText.match(regex);

    if (matches && matches.length > 0) {
      const highlightedText = rawText.replace(
        regex,
        (match) => `<span class="highlight">${match}</span>`
      );
      stringToTest.innerHTML = highlightedText;

      testResult.textContent = matches.join(", ");
    } else {
      testResult.textContent = "no match";
    }
  } catch (error) {
    testResult.textContent = "no match";
  }
});