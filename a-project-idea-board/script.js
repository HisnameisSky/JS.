const projectStatus = {"PENDING": {"description": "Pending Execution"},"SUCCESS":{"description":"Executed Successfully"},"FAILURE":{"description":"Execution Failed"}};

class ProjectIdea {
  constructor(title, description) {
    this.title = title;
    this.description = description;
    this.status = projectStatus.PENDING;
  }

  updateProjectStatus(newStatus) {
    this.status = newStatus;
  }
}

class ProjectIdeaBoard  {
  constructor (title) {   
    this.title = title;
    this.ideas = [];
  }

  pin(idea) {
    this.ideas.push(idea);
  }

  unpin(idea) {
    const idx = this.ideas.indexOf(idea);
    this.ideas.splice(idx,1);
  }

  count() {
    return this.ideas.length;
  }

  formatToString() {
    let str = `${this.title} has ${this.count()} idea(s)\n`;
    if (this.count() == 0) return str;
    for (let idea of this.ideas) {
      str += `${idea.title} (${idea.status.description}) - ${idea.description}\n`;
    }
    return str;
  }
}

const techProjectsBoard = new ProjectIdeaBoard("Tech Projects Board");
techProjectsBoard.pin(new ProjectIdea("Smart Home System","An integrated system to control lighting, temperature, and security devices remotely."));
console.log(techProjectsBoard.formatToString());