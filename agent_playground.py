import os

from crewai import Crew
from agents import AIStoryBookAgents
from tasks import AIStoryBookTasks
from dotenv import load_dotenv

load_dotenv()

agents = AIStoryBookAgents()
tasks = AIStoryBookTasks()

seo_specialist = agents.seo_specialist()
writer = agents.fantasy_writer()
editor = agents.editor()
researcher = agents.researcher()
web_developer = agents.web_developer()
creative_director = agents.creative_director()
art_director = agents.art_director()
social_media_manager = agents.social_media_manager()

review_seo_brief = tasks.review_seo_brief(writer)
review_creative_brief = tasks.review_creative_brief(writer)
write_story = tasks.write_story(writer, [review_seo_brief, review_creative_brief])
convert_to_html = tasks.convert_to_html(web_developer)
generate_prompt_from_story = tasks.generate_prompt_from_story(writer)
develop_social_media_plan = tasks.develop_social_media_plan(social_media_manager)

crew = Crew(
    agents=[web_developer],
    tasks=[convert_to_html],
    verbose=True,
    output_log_file=True,
)

# clear the output_files directory
# directory = "output_files"
# for filename in os.listdir(directory):
#     file_path = os.path.join(directory, filename)
#     # do not delete the seo_brief.md file or the creative_brief.md file
#     if "seo_brief" in file_path or "creative_brief" in file_path:
#         continue
#     if os.path.isfile(file_path):
#         os.remove(file_path)
#         print(f"{file_path} has been deleted.")

if os.path.exists("logs.txt"):
    os.remove("logs.txt")
    print("logs.txt has been deleted.")

results = crew.kickoff()

print("Crew Work Results:")
print(results)

exit()
