function repeatStringNumTimes(str, num) {
  if (num <= 0) {
    return "";
  }

  let result = "";

  for (let i = 0; i < num; i++) {
    result += str; 
  }

  return result;
}

//variant

function repeatStringNumTimes(str,num) {
    let result = "";
    while(num > 0) {
        result += str;
        num--;
    }
    return result;
}

//variant 2

function repeatStringNumTimes(str,num) {
    if (num <= 0) {
        return "";
    }
    return str + repeatStringNumTimes(str,num -1)
}

//for {start; goal; skip};