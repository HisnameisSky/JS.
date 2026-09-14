const footballTeam = {
  team: "Argentina",
  year: 1986,
  headCoach: "Carlos Bilardo",
  players: [
    {
      name: "Sergio Batista",
      position: "midfielder",
      isCaptain: false,
    },
    {
      name: "Diego Maradona",
      position: "midfielder",
      isCaptain: true, 
    },
    {
      name: "Jorge Valdano",
      position: "forward",
      isCaptain: false,
    },
    {
      name: "José Luis Brown",
      position: "defender",
      isCaptain: false,
    },
    {
      name: "Nery Pumpido",
      position: "goalkeeper",
      isCaptain: false,
    },
  ],
};

const teamSpan = document.getElementById("team");
const yearSpan = document.getElementById("year");
const headCoachSpan = document.getElementById("head-coach");
const playerCardsContainer = document.getElementById("player-cards");
const playersDropdown = document.getElementById("players");

teamSpan.textContent = footballTeam.team;
yearSpan.textContent = footballTeam.year;
headCoachSpan.textContent = footballTeam.headCoach;

const setPlayerCards = (arr = []) => {
  playerCardsContainer.innerHTML = arr
    .map(({ name, position, isCaptain }) => {
      return `
        <div class="player-card">
          <h2>${isCaptain ? "(Captain) " : ""}${name}</h2>
          <p>Position: ${position}</p>
        </div>
      `;
    })
    .join("");
};

setPlayerCards(footballTeam.players);

playersDropdown.addEventListener("change", (e) => {
  const selectedValue = e.target.value;

  if (selectedValue === "all") {
    setPlayerCards(footballTeam.players);
  } else {
    const filteredPlayers = footballTeam.players.filter(
      (player) => player.position === selectedValue
    );
    setPlayerCards(filteredPlayers);
  }
});