const pantry = [
  { sku: "A10", name: "Tomatoes", qty: 4, expires: "2027-01-01", zone: "fridge" },
  { sku: "D43", name: "Pineapples", qty: 2, expires: "2020-01-01", zone: "general" }
];

const rawData = [
  "A10|Tomatoes|5|2027-01-01",
  "B21|Bananas|10|2027-01-01",
  "C32|Eggs|3|2027-01-01|fridge",
  "C32|Eggs|3|2027-01-01",
  "D43|Pineapples|0|2027-01-01",
  "E54|Peppers|-1|2027-01-01|fridge"
];

function parseShipment(rawData) {
  const result = [];
  const seenSkus = new Set(); // 重複チェック用のSet（箱）

  for (const itemStr of rawData) {
    const parts = itemStr.split("|");
    const sku = parts[0];
    const name = parts[1];
    const qty = Number(parts[2]);
    const expires = parts[3];
    const zone = parts[4] || "general"; // 省略時は "general"

    // 重複しているSKUは無視
    if (!seenSkus.has(sku)) {
      seenSkus.add(sku);
      result.push({ sku, name, qty, expires, zone });
    }
  }

  return result;
}

function planRestock(pantry, shipment) {
  const actions = [];
  const pantrySkus = pantry.map(item => item.sku); // パントリーにあるSKU一覧

  for (const item of shipment) {
    let type = "";

    if (item.qty <= 0) {
      type = "discard"; // 数量が0以下の場合は破棄
    } else if (pantrySkus.includes(item.sku)) {
      type = "restock"; // パントリーに存在する場合は補充
    } else {
      type = "donate";  // 存在しない場合は寄付
    }

    actions.push({ type, item });
  }

  return actions;
}

function groupByZone(actions) {
  const grouped = {};

  for (const action of actions) {
    const zone = action.item.zone;
    if (!grouped[zone]) {
      grouped[zone] = [];
    }
    grouped[zone].push(action);
  }

  return grouped;
}

function clonePantry(pantry) {
  return JSON.parse(JSON.stringify(pantry));
}

const parsedShipment = parseShipment(rawData);
const restockPlan = planRestock(pantry, parsedShipment);
const groupedResults = groupByZone(restockPlan);

console.log(groupedResults);

//公式による正解事例⇣

function parseShipment(rawData) {

  
  if (!Array.isArray(rawData)) return [];

  const result = [];
  const seenSKUs = [];

  for (let line of rawData) {

    const parts = line.split("|");

    const sku = parts[0].trim();

    if (seenSKUs.includes(sku)) continue;

    const name = parts[1].trim();
    const qty = Number(parts[2].trim()); 
    const expires = parts[3].trim();
    const zone = ( parts[4] ) ? parts[4].trim() : "general";

    result.push({
      sku: sku,
      name: name,
      qty: qty,
      expires: expires,
      zone: zone
    });

    seenSKUs.push(sku);

  }

  return result;
}

function planRestock(pantry, shipment) {
  const actions = [];

  for (let item of shipment) {

    var exists = false;

    for (let stock of pantry)
    {
      if (stock.sku === item.sku)
      {
        exists = true;
      }
    }

    if (item.qty > 0) {
      if (exists) {
        actions.push({ type: "restock", item: item });
      } else{
        actions.push({ type: "donate", item: item });
      }
    } else {
      actions.push({ type: "discard", item: item });
    }
  }

  return actions;
}

function groupByZone(actions) {

  const byZone = {};

  for (const action of actions) {

    const zone = action.item.zone;

    if (!byZone[zone]) {
      byZone[zone] = [];
    }

    byZone[zone].push(action);
  }

  return byZone;

}

function clonePantry(pantry) {
  const pantryClone = [];

  for (let item of pantry) {
    pantryClone.push({
      sku: item.sku,
      name: item.name,
      qty: item.qty,
      expires: item.expires,
      zone: item.zone
    });
  }

  return pantryClone;
}

const pantry = [
  { sku: "A10", name: "Tomatoes", qty: 4, expires: "2027-01-01", zone: "fridge" },
  { sku: "D43", name: "Pineapples", qty: 2, expires: "2020-01-01", zone: "general" }
];

const rawData = [
  "A10|Tomatoes|5|2027-01-01", 
  "B21|Bananas|10|2027-01-01", 
  "C32|Eggs|3|2027-01-01|fridge", 
  "C32|Eggs|3|2027-01-01", 
  "D43|Pineapples|0|2027-01-01", 
  "E54|Peppers|-1|2027-01-01|fridge" 
];

const shipment = parseShipment(rawData);
const pantryCopy = clonePantry(pantry);
const actions = planRestock(pantryCopy, shipment);
const grouped = groupByZone(actions);

console.log(grouped);
