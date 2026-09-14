function fearNotLetter(str) {
    for(let i = 0; i < str.length - 1; i++) {
        const currentCode = str.charCodeAt(i);
        const nextCode = str.charCodeAt(i+ 1);

        if(nextCode != currentCode +1) {
            return String.fromCharCode(currentCode +1);
        }
    }
    return undefined;
}

//variant

function fearNotLetter(str) {
    const alphabet = "abcdefghijklmnopqrstuvwxyz";
    const startIndex = alphabet.indexOf(str[0]);

    for (let i=0; i< str.length; i++) {
        if(str[i] !== alphabet[startIndex + i]) {
            return alphabet[startIndex + i];
        }
    }
    return undefined;
}