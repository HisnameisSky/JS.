function translatePigLatin(str) {
  const vowelRegex = /[aeiou]/;

  if (vowelRegex.test(str[0])) {
    return str + "way";
  }

  if (!vowelRegex.test(str)) {
    return str + "ay";
  }

  const firstVowelIndex = str.search(vowelRegex);

  const consonants = str.slice(0, firstVowelIndex);
  const rest = str.slice(firstVowelIndex);

  return rest + consonants + "ay";
}