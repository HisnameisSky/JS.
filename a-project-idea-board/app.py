from typing import List, Dict, Any

PROJECT_STATUS: Dict[str, Dict[str, str]] = {
    "PENDING": {"description": "Pending Execution"},
    "SUCCESS": {"description": "Executed Successfully"},
    "FAILURE": {"description": "Execution Failed"}
}


class ProjectIdea:
    def __init__(self, title: str, description: str) -> None:
        self.title: str = title
        self.description: str = description
        self.status: Dict[str, str] = PROJECT_STATUS["PENDING"]

    def update_project_status(self, new_status: Dict[str, str]) -> None:
        self.status = new_status


class ProjectIdeaBoard:
    def __init__(self, title: str) -> None:
        self.title: str = title
        self.ideas: List[ProjectIdea] = []

    def pin(self, idea: ProjectIdea) -> None:
        self.ideas.append(idea)

    def unpin(self, idea: ProjectIdea) -> None:
        if idea in self.ideas:
            self.ideas.remove(idea)

    def count(self) -> int:
        return len(self.ideas)

    def format_to_string(self) -> str:
        s: str = f"{self.title} has {self.count()} idea(s)\n"
        if self.count() == 0:
            return s
        for idea in self.ideas:
            s += f"{idea.title} ({idea.status['description']}) - {idea.description}\n"
        return s


if __name__ == "__main__":
    tech_projects_board = ProjectIdeaBoard("Tech Projects Board")
    
    idea1 = ProjectIdea(
        "Smart Home System",
        "An integrated system to control lighting, temperature, and security devices remotely."
    )
    tech_projects_board.pin(idea1)
    
    print(tech_projects_board.format_to_string(), end="")