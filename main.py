import os

from crewai import Crew, Process
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from agents import AIStoryBookAgents
from tasks import AIStoryBookTasks
from dotenv import load_dotenv

load_dotenv()

# Initialize the agents and tasks
agents = AIStoryBookAgents()
tasks = AIStoryBookTasks()

llama3 = {"llm": ChatGroq(model="llama3-70b-8192"), "rpm": 30}

gpt4 = {"llm": ChatOpenAI(model="gpt-4-turbo"), "rpm": 10000}

claude3 = {"llm": ChatAnthropic(model="claude-3-opus-20240229"), "rpm": 1000}

gemini = {"llm": ChatGoogleGenerativeAI(model="gemini-pro"), "rpm": 2}

creative_director = agents.creative_director()
writer = agents.sci_fi_writer()
# writer = agents.fantasy_writer()
editor = agents.editor()
# visual_artist = agents.illustrator()
visual_artist = agents.photographer()
web_developer = agents.web_developer()
researcher = agents.researcher()

develop_creative_brief = tasks.develop_creative_brief(
    creative_director
)
write_story = tasks.write_story(
    writer,
    [develop_creative_brief]
)
edit_story = tasks.edit_story(
    editor, [write_story]
)
source_image = tasks.source_image(visual_artist, [edit_story])
crop_images = tasks.crop_images(visual_artist, [source_image])
convert_to_json = tasks.convert_to_json(web_developer, [edit_story, crop_images])

crew = Crew(
    agents=[creative_director, writer, editor, visual_artist, web_developer, researcher],
    tasks=[
        develop_creative_brief,
        write_story,
        edit_story,
        source_image,
        crop_images,
        convert_to_json
    ],
    process=Process.hierarchical,
    verbose=2,
    manager_llm=gpt4["llm"],
    max_rpm=gpt4["rpm"],
    output_log_file=True,
)

# clear the output_files directory
directory = "output_files"
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted.")

if os.path.exists("logs.txt"):
    os.remove("logs.txt")
    print("logs.txt has been deleted.")

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)

exit()
