function countdown(n){
    if(n<1){
        return [];
    } else {
        const countArray = countdown(n-1);
        countArray.unshift(n);
        return countArray;
    }
}

//variant

function countdown(n){
    if(n<1){
        return [];
    } else {
        return [n, ...countdown(n-1)];
    }
}