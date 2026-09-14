const mainSection = document.getElementById("main-section");
const formSection = document.getElementById("form-section");
const bookmarkListSection = document.getElementById("bookmark-list-section");

const categoryDropdown = document.getElementById("category-dropdown");
const categoryNameElements = document.querySelectorAll(".category-name");

const nameInput = document.getElementById("name");
const urlInput = document.getElementById("url");
const categoryList = document.getElementById("category-list");

const viewCategoryBtn = document.getElementById("view-category-button");
const addBookmarkBtn = document.getElementById("add-bookmark-button");
const closeFormBtn = document.getElementById("close-form-button");
const addBookmarkFormBtn = document.getElementById("add-bookmark-button-form");
const closeListBtn = document.getElementById("close-list-button");
const deleteBookmarkBtn = document.getElementById("delete-bookmark-button");

const getBookmarks = () => {
  try {
    const rawData = localStorage.getItem("bookmarks");
    if (!rawData) return [];
    
    const parsed = JSON.parse(rawData);
    if (!Array.isArray(parsed)) return [];

    const isValid = parsed.every(
      (item) =>
        item &&
        typeof item === "object" &&
        typeof item.name === "string" &&
        typeof item.category === "string" &&
        typeof item.url === "string"
    );

    return isValid ? parsed : [];
  } catch (e) {
    return [];
  }
};

const displayOrCloseForm = () => {
  mainSection.classList.toggle("hidden");
  formSection.classList.toggle("hidden");
};

const displayOrHideCategory = () => {
  mainSection.classList.toggle("hidden");
  bookmarkListSection.classList.toggle("hidden");
};

const updateSelectedCategoryText = () => {
  const selectedText = categoryDropdown.value;
  categoryNameElements.forEach((el) => {
    el.innerText = selectedText;
  });
};

addBookmarkBtn.addEventListener("click", () => {
  updateSelectedCategoryText();
  displayOrCloseForm();
});

closeFormBtn.addEventListener("click", () => {
  displayOrCloseForm();
});

addBookmarkFormBtn.addEventListener("click", () => {
  const name = nameInput.value;
  const url = urlInput.value;
  const category = categoryDropdown.value;

  const currentBookmarks = getBookmarks();
  const newBookmark = { name, category, url };
  currentBookmarks.push(newBookmark);

  localStorage.setItem("bookmarks", JSON.stringify(currentBookmarks));

  nameInput.value = "";
  urlInput.value = "";

  displayOrCloseForm();
});

const renderCategoryList = () => {
  const selectedCategory = categoryDropdown.value;
  const bookmarks = getBookmarks();
  const filteredBookmarks = bookmarks.filter(
    (b) => b.category === selectedCategory
  );

  categoryList.innerHTML = "";

  if (filteredBookmarks.length === 0) {
    const p = document.createElement("p");
    p.innerText = "No Bookmarks Found";
    categoryList.appendChild(p);
  } else {
    filteredBookmarks.forEach((bookmark) => {
      const container = document.createElement("div");

      const radio = document.createElement("input");
      radio.type = "radio";
      radio.id = bookmark.name;
      radio.value = bookmark.name;
      radio.name = "bookmark-item";

      const label = document.createElement("label");
      label.setAttribute("for", bookmark.name);

      const anchor = document.createElement("a");
      anchor.href = bookmark.url;
      anchor.innerText = bookmark.name;
      anchor.target = "_blank";

      label.appendChild(anchor);
      container.appendChild(radio);
      container.appendChild(label);

      categoryList.appendChild(container);
    });
  }
};

viewCategoryBtn.addEventListener("click", () => {
  updateSelectedCategoryText();
  renderCategoryList();
  displayOrHideCategory();
});

closeListBtn.addEventListener("click", () => {
  displayOrHideCategory();
});

deleteBookmarkBtn.addEventListener("click", () => {
  const selectedRadio = categoryList.querySelector(
    'input[name="bookmark-item"]:checked'
  );

  if (!selectedRadio) return;

  const selectedBookmarkName = selectedRadio.value;
  const selectedCategory = categoryDropdown.value;

  const bookmarks = getBookmarks();
  
  const targetIndex = bookmarks.findIndex(
    (b) => b.name === selectedBookmarkName && b.category === selectedCategory
  );

  if (targetIndex !== -1) {
    bookmarks.splice(targetIndex, 1);
    localStorage.setItem("bookmarks", JSON.stringify(bookmarks));
  }

  renderCategoryList();
});