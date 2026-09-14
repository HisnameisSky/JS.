function frankenSplice(arr1, arr2, n) {
    const localArray = [...arr2];
    localArray.splice(n,0, ... arr1);
  return localArray;
}