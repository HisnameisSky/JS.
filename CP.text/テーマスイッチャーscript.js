
//テーマスイッチャー

// 【HTML】
// <button id="btn" aria-expanded="false">開閉ボタン</button>
// <ul id="menu" hidden>...</ul>

const btn = document.getElementById("btn");
const menu = document.getElementById("menu");

btn.addEventListener("click", () => {
  // aria-expanded が "true" かどうかで状態を判定
  const isOpen = btn.getAttribute("aria-expanded") === "true";

  // 状態を反転させる（開いていれば閉じる、閉じていれば開く）
  btn.setAttribute("aria-expanded", !isOpen);
  menu.toggleAttribute("hidden", isOpen);
});

//

const themeNames = ["light", "dark", "blue"]; // 定義したテーマ一覧

function changeTheme(newTheme) {
  // 1. 古いテーマクラスをすべて除去する
  themeNames.forEach(name => document.body.classList.remove(`theme-${name}`));

  // 2. 新しいテーマクラスを1つだけ追加する
  document.body.classList.add(`theme-${newTheme}`);
}

//

const dataList = [
  { name: "light", message: "明るいモードです" },
  { name: "dark", message: "暗いモードです" }
];

dataList.forEach(item => {
  // ID（#theme-light など）を動的に指定して要素を取得
  const el = document.getElementById(`theme-${item.name}`);
  
  if (el) {
    el.addEventListener("click", () => {
      // 該当するメッセージを画面に出力
      document.getElementById("status").textContent = item.message;
    });
  }
});

//
