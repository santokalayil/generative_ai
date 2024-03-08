from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Crew, Task, Process
from langchain.tools import DuckDuckGoSearchRun

import prep as _
from generative_ai.env_variables import get_variable
from generative_ai.llms import mistralai, gemini

# llm = ChatGoogleGenerativeAI(
#     model="gemini-pro",
#     verbose=True,
#     temperature=0.5,
#     google_api_key=get_variable("GEMINI_API_KEY"),
# )
# llm = gemini.get()

llm = mistralai.get(temperature=0.5, max_tokens=10000)

# create searches
search_tool = DuckDuckGoSearchRun()

# defining agents
email_auther = Agent(
    role="Professional Email Author",
    goal="Craft concise and engaging emails",
    backstory="Experienced in writing impactful marketing emails.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[search_tool],
)

# marketing strategist
marketing_strategist = Agent(
    role="Marketing Strategist",
    goal="Lead the team in creating effective cold emails",
    backstory="A seasoned Chief Marketing Officer with a keep eye for standout marketing content",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)
content_specialist = Agent(
    role="Content Specialist",
    goal="Critique and refine email content",
    backstory="A professional copywriter with a wealth of experience in persuasive writing",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

# defining tasks
email_task = Task(
    description="""1. Generate two distinct variations of a cold email promoting a video.
    2. Evaluate the written emails for their effectiveness and engagement.
    3. Scrutinize the emails for grammatical correctness
    4. Adjust the emails to align with best practices for cold outreach.
    4. Revice the emails based on all feedback, creating two final versions.
    """,
    expected_output="Two verisons of email in markdown format",
    agent=marketing_strategist,
)

# creating single crew
email_crew = Crew(
    agents=[email_auther, marketing_strategist, content_specialist],
    tasks=[email_task],
    verbose=True,
    process=Process.sequential,
)


# execution flow
print("Crew: working on email task")
email_output = email_crew.kickoff()
print(100 * "=")
print(email_output)
