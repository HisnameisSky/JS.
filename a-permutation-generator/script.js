function permuteString(str, prefix = "", result = []) {
  if (str.length === 0) {
    if (!result.includes(prefix)) {
      result.push(prefix);
    }
    return result;
  }

  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    const remaining = str.slice(0, i) + str.slice(i + 1);
    permuteString(remaining, prefix + char, result);
  }

  return result;
}