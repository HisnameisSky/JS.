function findElement(arr,func) {
    for (let i =0; i< arr.length; i++) {
        if (func(arr[i])) {
            return arr[i];
        }
    }
    return undefined;
}

//

function findElement1(arr, func) {
    return arr.find(func);
}

//

function isEven(num) {
    return num % 2 === 0;
}
fundElement([1,3,8], isEven);

findElement([1,3,8], num => num % 2 ===0);