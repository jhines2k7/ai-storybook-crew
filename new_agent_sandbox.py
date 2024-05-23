from crewai import Crew
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from agents import AIStoryBookAgents
from tasks import AIStoryBookTasks
from dotenv import load_dotenv

load_dotenv()

agents = AIStoryBookAgents()
tasks = AIStoryBookTasks()

claude3 = {"llm": ChatAnthropic(model="claude-3-opus-20240229"), "rpm": 1000}

gemini = {"llm": ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest"), "rpm": 360}

art_director = agents.art_director()

generate_prompt_from_story = tasks.generate_prompt_from_story(
    art_director
)
# generate_prompt_from_ad_copy = tasks.generate_prompt_from_ad_copy(
#     art_director
# )

crew = Crew(
    agents=[art_director],
    tasks=[generate_prompt_from_story]
)

results = crew.kickoff()

print("Crew Work Results:")
print(results)

exit()
