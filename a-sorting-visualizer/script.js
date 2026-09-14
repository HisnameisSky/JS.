const generateElement = () => Math.floor(Math.random() * 100) + 1;

const generateArray = () => {
  const arr = [];
  for (let i = 0; i < 5; i++) {
    arr.push(generateElement());
  }
  return arr;
};

const generateContainer = () => document.createElement("div");

const fillArrContainer = (element, arr) => {
  element.innerHTML = "";
  arr.forEach((num) => {
    const span = document.createElement("span");
    span.textContent = num;
    element.appendChild(span);
  });
};

const isOrdered = (a, b) => a <= b;

const swapElements = (arr, index) => {
  if (!isOrdered(arr[index], arr[index + 1])) {
    const temp = arr[index];
    arr[index] = arr[index + 1];
    arr[index + 1] = temp;
  }
};

const highlightCurrentEls = (element, index) => {
  const children = element.children;
  if (children[index]) {
    children[index].style.border = "2px dashed red";
  }
  if (children[index + 1]) {
    children[index + 1].style.border = "2px dashed red";
  }
};

const arrayContainer = document.getElementById("array-container");
const startingArrayDiv = document.getElementById("starting-array");
const generateBtn = document.getElementById("generate-btn");
const sortBtn = document.getElementById("sort-btn");

let currentArray = [];

generateBtn.addEventListener("click", () => {
  arrayContainer.innerHTML = "";
  arrayContainer.appendChild(startingArrayDiv);

  currentArray = generateArray();
  fillArrContainer(startingArrayDiv, currentArray);
});

sortBtn.addEventListener("click", () => {
  if (currentArray.length === 0) return;

  arrayContainer.innerHTML = "";
  arrayContainer.appendChild(startingArrayDiv);

  let arr = [...currentArray];
  
  fillArrContainer(startingArrayDiv, arr);
  highlightCurrentEls(startingArrayDiv, 0);


  let swapped = true;
  while (swapped) {
    swapped = false;
    for (let i = 0; i < arr.length - 1; i++) {
      if (!isOrdered(arr[i], arr[i + 1])) {
        swapElements(arr, i);
        swapped = true;
      }

      const stepContainer = generateContainer();
      fillArrContainer(stepContainer, arr);
      highlightCurrentEls(stepContainer, i);
      arrayContainer.appendChild(stepContainer);
    }
  }
});



//alt

const generateBtn = document.getElementById("generate-btn");
const sortBtn = document.getElementById("sort-btn");

// Set Display of Sort Button to None
sortBtn.style.display = 'none';

function generateElement() {
  return Math.floor(Math.random() * 100) + 1;
}

function generateArray() {
  return Array(5).fill(0).map((_) => generateElement());
}

function generateContainer() {
  return document.createElement("div");
}

function fillArrContainer(element, arr) {
  element.innerHTML = "";
  for (const arrEl of arr) {
    element.innerHTML += `<span>${arrEl}</span>`;
  }
}

function isOrdered(num1, num2) {
  return num1 <= num2;
}

function swapElements(arr,idx) {
  if (!isOrdered(arr[idx],arr[idx+1])) {
    [arr[idx],arr[idx+1]] = [arr[idx+1],arr[idx]];
  }
}

function highlightCurrentEls(element, idx) {
  
    element.children[idx].style.border = "2px dashed red";
  element.children[idx + 1].style.border = "2px dashed red";
  
  
}

generateBtn.addEventListener("click", () => {
  const startingArray = document.getElementById("starting-array");
  const arrayContainer = document.getElementById("array-container");

  if (startingArray.textContent || arrayContainer.textContent) {
    startingArray.innerHTML = "";
    arrayContainer.innerHTML = "";
    arrayContainer.appendChild(startingArray);
  }

  let array = generateArray();
  fillArrContainer(startingArray, array);
  sortBtn.style.display = 'block';
});

sortBtn.addEventListener("click", () => {
  const startingArray = document.getElementById("starting-array");
  const arrayContainer = document.getElementById("array-container");
  let spanArray = Array.from(startingArray.children);
  let array = spanArray.map((span) => parseInt(span.textContent));

  if (startingArray.textContent || arrayContainer.textContent) {
    startingArray.innerHTML = "";
    arrayContainer.innerHTML = "";
  }

    fillArrContainer(startingArray, array);
    highlightCurrentEls(startingArray, 0);
    arrayContainer.appendChild(startingArray);

let swapped = true;
let steps = 0;
while (swapped) {
  swapped = false;
  for (let idx = 0; idx < array.length - 1;idx++) {
    const stepContainer = generateContainer();
	if (steps != 0) {
		fillArrContainer(stepContainer, array);
		highlightCurrentEls(stepContainer,idx);
		arrayContainer.appendChild(stepContainer);
	}
    
    if (!isOrdered(array[idx],array[idx+1])) {
      swapElements(array,idx);
      swapped = true;
    }
	steps++;
	
  }
} 


const finalDivContainer = generateContainer();
fillArrContainer(finalDivContainer, array);
arrayContainer.appendChild(finalDivContainer);
  
  sortBtn.style.display = 'none';
});