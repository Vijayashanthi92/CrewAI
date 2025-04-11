import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process
from crew_ai_tools import SerperDevTool

load_dotenv()



def run_ai_new_crew():
    search_tool=SerperDevTool()


    #Create agents


    researcher = Agent(
        role="Tech news researcher",
        goal="find and analyse latest",
        backstory="You're an AI Technology expert who can identify groundbreaking developments",
        tools=[search_tool],
        verbose=True
    )


    writer= Agent(
        role="Tech content creator",
        goal="Create viral-worthy content"
        backstory="You're a skilled content creator",
        tools=[search_tool],
        verbose=True
)


    research_task=Task(
        Description="Research the most shocking AI Breakthroughs",
        expect_output="A detailed summary of groundbreaking AI Development"
        agent=reseacher
    )
    writing_task=Task(
         Description="create a viral script about AI Breakthroughs",
        expect_output="A cpmpleing 60 secon script"
        agent=writer
    )