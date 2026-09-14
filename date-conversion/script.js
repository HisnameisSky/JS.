const currentDate = new Date();

const currentDateFormat = `Current Date and Time: ${currentDate}`;

console.log(currentDateFormat);

function formatDateMMDDYYYY(date) {
  const month = date.getMonth() + 1; // 月は 0 から始まるため +1
  const day = date.getDate();
  const year = date.getFullYear();
  return `Formatted Date (MM/DD/YYYY): ${month}/${day}/${year}`;
}

function formatDateLong(date) {
  const formattedDate = date.toLocaleDateString("en-US", {
    month: "long",
    day: "numeric",
    year: "numeric"
  });
  return `Formatted Date (Month Day, Year): ${formattedDate}`;
}