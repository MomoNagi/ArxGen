from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from arxgen.tools.arxiv_tool import ArxivSearchTool
import os

@CrewBase
class ArxGenCrew:
    """Crew to research and analyse arxiv papers based on a query"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self) -> None:
        model_name = os.getenv("OLLAMA_MODEL", "phi3:latest")
        self.llm_config = f"ollama/{model_name}"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[ArxivSearchTool()],
            llm=self.llm_config,
            base_url="http://localhost:11434",
            verbose=True,
            allow_delegation=False
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["analyst"],
            llm=self.llm_config,
            base_url="http://localhost:11434",
            verbose=True,
            allow_delegation=False
        )

    @task
    def retrieval_task(self) -> Task:
        return Task(
            config=self.tasks_config["retrieval_task"],
            agent=self.researcher()
        )

    @task
    def extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config["extraction_task"],
            agent=self.analyst(),
            context=[self.retrieval_task()],
            output_file="src/arxgen/outputs/report.md"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )