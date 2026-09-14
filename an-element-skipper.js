function dropElements(arr, func) {
    const index = arr.findIndex(func);
    return index === -1 ? [] : arr.slice(index);
}

//while

function fropElements(arr, func) {
    while(arr.length > 0 && !func(arr[0])){
        arr.shift();
    }
    return arr;
}
