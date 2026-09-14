function destroyer(arr, ...valToRemove) {
    return arr.filter(item => !valToRemove.includes(item));
}

destroyer([1,2,3],2,3);