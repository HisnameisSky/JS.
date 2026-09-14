const questions = [
  {
    category: "Science",
    question: "What is the chemical symbol for Gold?",
    choices: ["Au", "Ag", "Fe"],
    answer: "Au"
  },
  {
    category: "Geography",
    question: "What is the capital of Japan?",
    choices: ["Tokyo", "Kyoto", "Osaka"],
    answer: "Tokyo"
  },
  {
    category: "Math",
    question: "What is 2 + 2?",
    choices: ["3", "4", "5"],
    answer: "4"
  },
  {
    category: "Technology",
    question: "Which programming language is known as the language of the web?",
    choices: ["Python", "JavaScript", "C++"],
    answer: "JavaScript"
  },
  {
    category: "Gaming",
    question: "Who is Mario's brother?",
    choices: ["Luigi", "Wario", "Toad"],
    answer: "Luigi"
  }
];

function getRandomQuestion(questionsArray) {
  const randomIndex = Math.floor(Math.random() * questionsArray.length);
  return questionsArray[randomIndex];
}

function getRandomComputerChoice(choicesArray) {
  const randomIndex = Math.floor(Math.random() * choicesArray.length);
  return choicesArray[randomIndex];
}

function getResults(questionObj, computerChoice) {
  if (computerChoice === questionObj.answer) {
    return "The computer's choice is correct!";
  } else {
    return `The computer's choice is wrong. The correct answer is: ${questionObj.answer}`;
  }
}