function largestOfAll(arr) {
  const results = [];

  for (let i = 0; i < arr.length; i++) {
    let maxNum = arr[i][0];

    for (let j = 1; j < arr[i].length; j++) {
      if (arr[i][j] > maxNum) {
        maxNum = arr[i][j];
      }
    }

    results.push(maxNum);
  }

  return results;
}
//variant 

function largestOfAll(arr) {
    return arr.map(subArr => Math.max(...subArr));
}

//ex

const fruits = ["🍎", "🍌"];
const vegetables = ["🥦", "🥕"];

const foodList = [...fruits, ...vegetables];
console.log(foodList); 

const fullMenu = ["🍞", ...fruits, "🧀", ...vegetables];
console.log(fullMenu);

//

const original = [1,2,3];
let copy = [...original];
copy.push(99);

console.log(original);

console.log(copy);