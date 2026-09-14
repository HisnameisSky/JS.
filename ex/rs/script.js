async function convertIngredient(){
    const sendData={
        ingredient: "flour",
        quantity:2,
        unit:"cup"
    };

    const response = await fetch("https://example.com/api/convert",{
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(sendData)
    });

    const result=await response.json();
    document.getElementById("result").textContent= `${result.ingredient}: ${result.convertedQuantity} gram`;
};