let contacts = [
  {
    firstName: "Akira",
    lastName: "Laine",
    number: "0543236543",
    likes: ["Pizza", "Coding", "Brownie Points"],
  },
  {
    firstName: "Harry",
    lastName: "Potter",
    number: "0994372684",
    likes: ["Hogwarts", "Magic", "Hagrid"],
  },
  {
    firstName: "Sherlock",
    lastName: "Holmes",
    number: "0487345643",
    likes: ["Intriguing Cases", "Violin"],
  },
  {
    firstName: "Kristian",
    lastName: "Vos",
    number: "unknown",
    likes: ["JavaScript", "Gaming", "Foxes"],
  },
];

function lookUpProfile (nameArg, prop) {
  for (let item of contacts) {
    if (item.firstName == nameArg) {
      if (item.hasOwnProperty(prop)) {
        return item[prop];
      } else {
        return "No such property";
      }
    }
  }
  return "No such contact";
}

//variant

function lookUpProfile(name,prop) {
    const person = contacts.find(contact => contact.firstName === name);
    if(!person) {
        return "No such contact";
    }
    if(person.hasOwnProperty(prop)) {
        return person[prop];
    } else {
        return "No such property";
    }
}