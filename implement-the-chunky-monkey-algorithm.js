function chunkArrayInGroups(arr, size) {
  const result = [];
  
  for (let i = 0; i < arr.length; i += size) {
    result.push(arr.slice(i, i + size));
  }
  
  return result;
}

//variant

function chunkArrayInGroups(arr, size) {
    const result = [];
    while (arr.length > 0) {
        result.push(arr.splice(0,size));
    }
    return result;
}