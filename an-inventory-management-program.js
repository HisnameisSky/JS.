const inventory = [];

function findProductIndex(productName) {
  const nameLower = productName.toLowerCase();
  for (let i = 0; i < inventory.length; i++) {
    if (inventory[i].name.toLowerCase() === nameLower) {
      return i;
    }
  }
  return -1;
}

function addProduct(product) {
  const nameLower = product.name.toLowerCase();
  const index = findProductIndex(nameLower);

  if (index !== -1) {
    inventory[index].quantity += product.quantity;
    console.log(`${nameLower} quantity updated`);
  } else {
    inventory.push({
      name: nameLower,
      quantity: product.quantity
    });
    console.log(`${nameLower} added to inventory`);
  }
}

function removeProduct(productName, quantity) {
  const nameLower = productName.toLowerCase();
  const index = findProductIndex(nameLower);

  if (index === -1) {
    console.log(`${nameLower} not found`);
    return;
  }

  const currentQuantity = inventory[index].quantity;

  if (quantity > currentQuantity) {
    console.log(`Not enough ${nameLower} available, remaining pieces: ${currentQuantity}`);
  } else {
    inventory[index].quantity -= quantity;
    const remainingQuantity = inventory[index].quantity;

    if (remainingQuantity === 0) {
      inventory.splice(index, 1);
    }

    console.log(`Remaining ${nameLower} pieces: ${remainingQuantity}`);
  }
}

//合格判定の実例？？なぜだおるか・・

let inventory=[];

function findProductIndex(productName){
 return inventory.findIndex(productIndex=>productIndex.name.toLowerCase() === productName.toLowerCase())
}
console.log(findProductIndex('flUr'));

function addProduct(productObject){
  productObject.name = productObject.name.toLowerCase()
  const index = findProductIndex(productObject.name);
    if(index !== -1) {
    inventory[index].quantity += productObject.quantity;
      console.log(`${productObject.name} quantity updated`)}
      else {inventory.push(productObject)
      console.log(`${productObject.name} added to inventory`)}
}

addProduct({name:'flur', quantity:9})

function removeProduct(name,quantity){
 // console.log(inventory)
   name = name.toLowerCase();
  const index = findProductIndex(name)
  //console.log(index)
  if(index === -1){  
      console.log(`${name} not found`)
      return
  } if(inventory[index].quantity < quantity) {
    inventory[index].remove
     console.log(`Not enough ${name} available, remaining pieces: ${inventory[index].quantity}`)
  }else if(inventory[index].quantity === quantity){
    inventory.splice(index,1)
          console.log(`${name} not found`)

  }
  else{
  inventory[index].quantity -= quantity;
  console.log(`Remaining ${name} pieces: ${inventory[index].quantity}`)
  }
  }
removeProduct('fluor',9)