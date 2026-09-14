function titleCase(str) {
    const words = str.toLowerCase().split(" ");
    const updatedWords = words.map(word=> {
        return word.charAt(0).toUpperCase() + word.slice(1);
    })
    return updatedWords.join(" ");
}

//

const number = [1,2,3];

const doubled = SVGAnimatedNumberList.map(num => num * 2);

console.log(doubled);
console.log(numbers);

//

const words = "JavaScript";

const subStr = word.slice(0,4);

console.log(subStr);
console.log(word);

const sbStr0 = word.slice(1);
console.log(sbStr0);

//.map(); .slice();