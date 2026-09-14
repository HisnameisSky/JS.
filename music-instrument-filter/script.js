const instrumentsArr = [
  { category: "woodwinds", instrument: "Flute", price: 500 },
  { category: "woodwinds", instrument: "Clarinet", price: 200 },
  { category: "woodwinds", instrument: "Oboe", price: 4000 },
  { category: "brass", instrument: "Trumpet", price: 200 },
  { category: "brass", instrument: "Trombone", price: 300 },
  { category: "brass", instrument: "French Horn", price: 4300 },
  { category: "percussion", instrument: "Drum Set", price: 500 },
  { category: "percussion", instrument: "Xylophone", price: 3000 },
  { category: "percussion", instrument: "Cymbals", price: 200 },
  { category: "percussion", instrument: "Marimba", price: 3000 }
];

const selectContainer = document.querySelector("select");
const productsContainer = document.querySelector(".products-container");

function instrumentCards(instrumentCategory) {
  const instruments =
    instrumentCategory === "all"
      ? instrumentsArr
      : instrumentsArr.filter(
          ({ category }) => category === instrumentCategory
        );

  return instruments
    .map(({ instrument, price }) => {
      return `
          <div class="card">
            <h2>${instrument}</h2>
            <p>$${price}</p>
          </div>
        `;
    }).join('');
}

selectContainer.addEventListener("change", () => {
  productsContainer.innerHTML = instrumentCards(selectContainer.value);
});

/*
// 画面全体の背景とテキストを「夜モード」に一瞬で描き変える魔法
document.body.style.transition = "all 0.8s";
document.body.style.backgroundColor = "#1a1a2e";
document.body.style.color = "#e94560";
document.body.innerHTML += `<h1 style="position:fixed;top:40%;left:30%;font-size:3rem;z-index:9999;background:white;padding:20px;border-radius:10px;box-shadow:0 10px 25px rgba(0,0,0,0.5);">🎨 JSの魔法で画面をレイヤージャック！</h1>`;
*/