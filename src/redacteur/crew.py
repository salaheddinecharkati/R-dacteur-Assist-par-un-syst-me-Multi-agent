from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool,ScrapeWebsiteTool,FileWriterTool
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Redacteur():
    """Redacteur crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def WebSite_Searcher(self) -> Agent:
        return Agent(
            config=self.agents_config['WebSite_Searcher'], # type: ignore[index]
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def WebSite_Scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['WebSite_Scraper'], # type: ignore[index]
            tools=[ScrapeWebsiteTool()],
            verbose=True
        )
    
    @agent
    @agent
    def Pdf_comparer(self) -> Agent:
        return Agent(
            config=self.agents_config['Pdf_comparer'],  # correspond à agents.yaml
            tools=[
                    FileReadTool(),
                KnowledgePDFSource(pdf_path="knowledge/Energiesrenouvelables.pdf")],
            verbose=True
    )

    
    @agent
    def summarizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer_agent'], # type: ignore[index]
            tools=[FileWriterTool()],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def Search_task(self) -> Task:
        return Task(
            config=self.tasks_config['Search_task'], # type: ignore[index]
        )

    @task
    def Scraping_task(self) -> Task:
        return Task(
            config=self.tasks_config['Scraping_task'], # type: ignore[index]
        )
    @task
    def Pdf_compare_task(self) -> Task:
        return Task(
            config=self.tasks_config['Pdf_compare_task'],
        )
    @task
    def Summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['Summary_task'], # type: ignore[index]
            output_file='report.json'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Redacteur crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
