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

agents = AIStoryBookAgents()
tasks = AIStoryBookTasks()

llama3 = {"llm": ChatGroq(model="llama3-70b-8192"), "rpm": 30}

gpt4 = {"llm": ChatOpenAI(model="gpt-4-turbo"), "rpm": 10000}

gpt4o = {"llm": ChatOpenAI(model="gpt-4o"), "rpm": 10000}

claude3 = {"llm": ChatAnthropic(model="claude-3-opus-20240229"), "rpm": 1000}

gemini = {"llm": ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest"), "rpm": 360}

creative_director = agents.creative_director()
# writer = agents.sci_fi_writer()
writer = agents.fantasy_writer()
editor = agents.editor()
web_developer = agents.web_developer()
researcher = agents.researcher()
copywriter = agents.copywriter()
seo_specialist = agents.seo_specialist()
social_media_manager = agents.social_media_manager()

product_name = "Potaroma Cat Toys Flapping Bird"
description = f"""
                We are embarking on an ad campaign for {product_name} targeted at male readers between the ages of 41 and 56. 
                I would like you to take the lead in developing the creative brief for this project. I want this campaign to 
                have a distinctly high fantasy feel, with a focus on action and adventure. The brief should comprehensively 
                outline our objectives, the target audience, the tone, and the key messages. Work with the researcher to gather any 
                necessary insights.
                """
develop_creative_brief = tasks.develop_creative_brief(
    creative_director,
    description
)
review_creative_brief = tasks.review_creative_brief(seo_specialist, [develop_creative_brief])
create_seo_brief = tasks.create_seo_brief(seo_specialist, [review_creative_brief])
develop_social_media_plan = tasks.develop_social_media_plan(
    social_media_manager, 
    [develop_creative_brief, create_seo_brief]
)
write_ad_copy = tasks.write_ad_copy(
    copywriter, [develop_creative_brief, create_seo_brief]
)
write_social_media_posts = tasks.write_social_media_posts(
    copywriter, [develop_social_media_plan, create_seo_brief]
)
write_story = tasks.write_story(
    writer,
    [develop_creative_brief, create_seo_brief, write_ad_copy]
)
# generate_prompt_from_story = tasks.generate_prompt_from_story(
#     art_director, [write_story]
# )
# generate_prompt_from_ad_copy = tasks.generate_prompt_from_ad_copy(
#     art_director, [write_ad_copy]
# )
convert_to_html = tasks.convert_to_html(
    web_developer, [write_story]
)

crew = Crew(
    agents=[
        creative_director,
        seo_specialist,
        copywriter,
        social_media_manager,
        writer,
        editor,
        web_developer,
        researcher,
    ],
    tasks=[
        develop_creative_brief,
        create_seo_brief,
        develop_social_media_plan,
        write_ad_copy,
        write_social_media_posts,
        write_story,
        convert_to_html
    ],
    process=Process.hierarchical,
    verbose=2,
    manager_llm=gpt4o["llm"],
    max_rpm=gpt4o["rpm"],
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
