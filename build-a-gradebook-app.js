function getAverage(scores) {
    let sum =0;
    for (let i=0; i<scores.length; i++) {
        sum += scores[i];
    }
    return sum / scores.length;
}

function getGrade(score) {
  if (score === 100) return "A+";
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}

function hasPassingGrade(score) {
    return getGrade(score) !== "F";
}

function studentMsg(totalScores, studentScore) {
    const average = getAverage(totalScores);
    const grade = getGrade(studentScore);
    const passed = hasPassingGrade(studentScore);

    if (passed) {
    return "Class average: " + average + ". Your grade: " + grade + ". You passed the course.";
  } else {
    return "Class average: " + average + ". Your grade: " + grade + ". You failed the course.";
  }
}

//variant

function studentMsg1(totalScores, studentScore) {
    const average = getAverage = getAverage(totalScores);
    const grade = getGrade(studentScore);
    const passed = hasPassingGrade(studentScore);
    
    const status = passed? "passed" : "failed";
    return `Class average: ${average}. Your grade: ${grade}. You ${status} the course.`;
}