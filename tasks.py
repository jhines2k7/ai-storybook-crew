from crewai import Task
from crewai_tools import FileReadTool

import textwrap


class AIStoryBookTasks:
    def develop_creative_brief(self, agent):
        return Task(
            description=textwrap.dedent(
                """
                Develop a creative brief for a short fantasy story for male readers between the 
                ages of 41 and 56 as if it were written by Tyler Durden from the movie Fight Club.
                The story should be between 1500 and 2000 words. An example creative brief can be found in the 
                creative_brief_example.md file.
                """
            ),
            expected_output=textwrap.dedent(
                """
                A creative brief that outlines the project’s background, story premise, objectives, 
                desired audience reactions, and specific requirements such as tone and style and any 
                additional guidelines.
                """
            ),
            agent=agent,
            output_file="output_files/creative_brief.md",
            tools=[
                FileReadTool(file_path="creative_brief_example.md"),
            ],
        )

    def write_story(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                Write a short story based on the guidelines and requirements outlined in the creative brief.

                Consider consulting or collaborating with the researcher at various stages of the writing process:

                1. **Concept Development:** When developing the initial concept for a story, especially if it involves complex scientific or technological elements, consulting a researcher can provide valuable insights and ensure accuracy in portraying scientific concepts.

                2. **World-Building:** For creating believable and immersive fictional worlds, collaborating with experts in fields such as astronomy, physics, biology, or engineering can help ensure consistency and plausibility in the depiction of futuristic technologies, environments, or societies.

                3. **Fact-Checking:** During the writing process, it's essential to fact-check scientific details to maintain credibility. Consulting with a researcher can help verify the accuracy of scientific concepts, terminology, and principles used in the story.

                4. **Problem-Solving:** If the narrative encounters scientific or technical challenges that require creative solutions, collaborating with a researcher can provide valuable perspectives and help brainstorm realistic and innovative resolutions.
                """
            ),
            context=context,
            agent=agent,
            expected_output=textwrap.dedent(
                """
                    A concise yet compelling narrative that engages the reader from beginning to end. It should feature well-developed 
                    characters, a clear setting, and a plot that unfolds naturally within the constraints of the short form.
                    The story should have a fully developed plot which typically follows a structured format such as exposition, 
                    rising action, climax, falling action, and resolution. The story should evoke emotion, provoke thought, and 
                    entertain the reader, leaving a lasting impact despite its brevity.
                """
            ),
            output_file="output_files/story_draft.txt",
            tools=[
                FileReadTool(file_path="output_files/creative_brief.md"),
            ],
        )

    def edit_story(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                Refine the narrative, characters, and prose to enhance clarity, coherence, and emotional impact while 
                maintaining the author's voice and vision. Delicately balance constructive critique, language refinement, 
                and structural adjustments to ensure the story engages and resonates with the reader.
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                A polished, cohesive narrative that captivates the reader from beginning to end. It should showcase strong 
                character development, a well-paced plot, and compelling prose, ultimately leaving a lasting impression and 
                eliciting an emotional response from the audience.
                """
            ),
            output_file="output_files/final_draft.txt",
            tools=[FileReadTool(file_path="output_files/story_draft.txt")]
        )

    def convert_to_json(self, agent, context):        
        return Task(
            description=textwrap.dedent(
                """
                1. Convert the markdown from the final draft into html using h3 and p tags. 
                2. Reformat the html so that it is on one line and be sure to properly escape any double quotes. 
                3. Create a json file that will be used as data for the api that delivers the story to our readers.                 
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                Example Output:
                {
                    "title": <Story Title>,
                    "storyNum": "00",
                    "author": <Author Name>,
                    "story": <Story Content>,
                    "images": [
                        "https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_1]", 
                        "https://storage.googleapis.com/[BUCKET_NAME]/[FILE_"NAME_2]",
                        "https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_3]"]
                }
                """
            ),
            output_file="output_files/story.json",
            tools=[
                FileReadTool(file_path="output_files/final_draft.txt"),
                FileReadTool(file_path="output_files/cropped_image_urls.txt"),
            ]
        )

    def source_image(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                Visually interpret the narrative to enhance and complement the text. Read the story to 
                fully understand its themes, characters, and settings. Conceptualizes ideas that capture 
                key moments or emotions from the text. Consult with the author or editor to ensure alignment 
                with the story's tone. The final artwork provides a visual entry point that deepens the 
                reader's connection to the story. Provide at least 3 different images to choose from. The 
                images will be dislayed with a vertical orientation. Keep that in mind when composing your images.
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """A line separated list of image URLs for the story.
                Example Output:
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_1]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_3]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_4]            
                """
            ),
            output_file="output_files/image_urls.txt"
        )

    def crop_images(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                    You will be given a list of image URLs in a text 
                    file. Crop each image to a width of 
                    450px and a height of 1100px. 
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """A line separated list of image URLs for the blog post.
                Example Output:
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_1]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_2]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_3]
                    https://storage.googleapis.com/[BUCKET_NAME]/[FILE_NAME_4]            
            """
            ),
            tools=[FileReadTool(file_path="output_files/image_urls.txt")],
            output_file="output_files/cropped_image_urls.txt"
        )
