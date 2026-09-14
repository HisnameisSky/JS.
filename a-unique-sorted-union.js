function uniteUnique(...arrays) {
    const flatArray = arrays.flat();
    return [...new Set(flatArray)];
}