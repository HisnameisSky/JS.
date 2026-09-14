const themes = [
  {
    name: "light",
    message: "Light theme activated!"
  },
  {
    name: "dark",
    message: "Dark theme activated!"
  }
];

const themeSwitcherBtn = document.getElementById("theme-switcher-button");
const themeDropdown = document.getElementById("theme-dropdown");
const statusMsg = document.getElementById("status");

themeSwitcherBtn.addEventListener("click", () => {
  const isExpanded = themeSwitcherBtn.getAttribute("aria-expanded") === "true";

  if (isExpanded) {
    themeSwitcherBtn.setAttribute("aria-expanded", "false");
    themeDropdown.setAttribute("hidden", "");
  } else {
    themeSwitcherBtn.setAttribute("aria-expanded", "true");
    themeDropdown.removeAttribute("hidden");
  }
});

themes.forEach((theme) => {
  const themeItem = document.getElementById(`theme-${theme.name}`);
  if (themeItem) {
    themeItem.addEventListener("click", () => {
      themes.forEach((t) => {
        document.body.classList.remove(`theme-${t.name}`);
      });

      document.body.classList.add(`theme-${theme.name}`);
      statusMsg.textContent = theme.message;

      themeSwitcherBtn.setAttribute("aria-expanded", "false");
      themeDropdown.setAttribute("hidden", "");
    });
  }
});