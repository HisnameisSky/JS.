// getWeather 関数 (constは不可)
async function getWeather(city) {
  try {
    const response = await fetch(`https://weather-proxy.freecodecamp.rocks/api/city/${city}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.log(error);
  }
}

async function showWeather(city) {
  if (!city) return;

  const data = await getWeather(city);

  if (!data) {
    alert("Something went wrong, please try again later");
    return;
  }

  const iconElem = document.getElementById("weather-icon");
  const mainTempElem = document.getElementById("main-temperature");
  const feelsLikeElem = document.getElementById("feels-like");
  const humidityElem = document.getElementById("humidity");
  const windElem = document.getElementById("wind");
  const windGustElem = document.getElementById("wind-gust");
  const weatherMainElem = document.getElementById("weather-main");
  const locationElem = document.getElementById("location");

  iconElem.src = data.weather?.[0]?.icon ?? "N/A";
  mainTempElem.textContent = data.main?.temp ?? "N/A";
  feelsLikeElem.textContent = data.main?.feels_like ?? "N/A";
  humidityElem.textContent = data.main?.humidity ?? "N/A";
  windElem.textContent = data.wind?.speed ?? "N/A";
  windGustElem.textContent = data.wind?.gust ?? "N/A";
  weatherMainElem.textContent = data.weather?.[0]?.main ?? "N/A";
  locationElem.textContent = data.name ?? "N/A";
}

const getWeatherBtn = document.getElementById("get-weather-btn");
const citySelect = document.getElementById("city-select");

getWeatherBtn.addEventListener("click", () => {
  const selectedCity = citySelect.value;
  if (selectedCity) {
    showWeather(selectedCity);
  }
});