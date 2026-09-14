function initStack() {
  return {
    collection: []
  };
}

function push(stack, item) {
  stack.collection.push(item);
}

function pop(stack) {
  return stack.collection.pop();
}

function peek(stack) {
  if (stack.collection.length === 0) {
    return undefined;
  }
  return stack.collection[stack.collection.length - 1];
}

function isEmpty(stack) {
  return stack.collection.length === 0;
}

function clear(stack) {
  stack.collection = [];
}