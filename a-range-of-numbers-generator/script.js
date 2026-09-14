function rangeOfNumbers(startNum, endNum){
    if(startNum === endNum){
        return[startNum] ;
    } else {
        const numbers = rangeOfNumbers(startNum, endNum -1);
        numbers.push(endNum);
        return numbers;
    }
}

//variant

function rangeOfNumbers(startNum, endNum){
    if(startNum === endNum){
        return [startNum];
    } else {
        return [...rangeOfNumbers(startNum,endNum - 1),endNum];
    }
}