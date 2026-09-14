function isPalindrome(word) {
  if (!word) return false;
  const cleaned = word.toLowerCase();
  return cleaned === cleaned.split("").reverse().join("");
}

function findPalindromeBreaks(words) {
  if (!words || words.length === 0) return [];
  const breaks = [];
  for (let i = 0; i < words.length; i++) {
    if (!isPalindrome(words[i])) {
      breaks.push(i);
    }
  }
  return breaks;
}

function findRepeatedPhrases(words, phraseLength) {
  if (!words || phraseLength >= words.length || phraseLength <= 0) return [];

  const phrases = []; 
  const maxStart = words.length - phraseLength;

  for (let i = 0; i <= maxStart; i++) {
    const phraseStr = words.slice(i, i + phraseLength).join(" ").toLowerCase();
    phrases.push(phraseStr);
  }

  const counts = {};
  for (const p of phrases) {
    counts[p] = (counts[p] || 0) + 1;
  }

  const repeatedIndices = [];
  for (let i = 0; i < phrases.length; i++) {
    if (counts[phrases[i]] > 1) {
      repeatedIndices.push(i);
    }
  }

  return repeatedIndices;
}

function analyzeTexts(texts, phraseLength) {
  if (!texts || texts.length === 0) return [];

  return texts.map(words => ({
    repeatedPhrases: findRepeatedPhrases(words, phraseLength),
    palindromeBreaks: findPalindromeBreaks(words)
  }));
}

//

function isPalindromeAdvanced(word) {
    if (!word) return false;

    const cleaned = word.toLowerCase().replace(/[^a-z0-9]/g, "");
    return cleaned === cleaned.split("").reverse().join("");
}
console.log(isPalindromeAdvanced("A man, a plan, a canal: Panama")); 

//

function isPalindromeTwoPointers(word) {
    if(!word) return false;
    const cleaned = word.toLowerCase();
    let left = 0;
    let right = cleaned.length -1;

    while (left < right) {
        if (cleaned[left] !== cleaned[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

//

function isPalindromeJapanese(str) {
  let cleaned = str
    .replace(/[っ]/g, "つ")
    .replace(/[ゃ]/g, "や")
    .replace(/[ゅ]/g, "ゆ")
    .replace(/[ょ]/g, "よ");

  return cleaned === cleaned.split("").reverse().join("");
}

console.log(isPalindromeJapanese("しんぶんし")); // true
console.log(isPalindromeJapanese("きしぶしき")); 
