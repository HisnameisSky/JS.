function diffArray(arr1, arr2) {
    const diff1 = arr1.filter(item => !arr2.includes(item));
    const diff2 = arr2.filter(item => !arr1.includes(item));
    return diff1.concat(diff2);
}