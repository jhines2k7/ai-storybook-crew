from crewai import Task
from crewai_tools import FileReadTool, DirectoryReadTool

import textwrap

class AIStoryBookTasks:
    def develop_creative_brief(self, agent, description):
        return Task(
            description=textwrap.dedent(
                description
            ),
            expected_output=textwrap.dedent(
                """
                Please ensure it includes:
                1. Project Overview: A brief description of what the project is and why it is being undertaken.
                2. Clear Objectives: What we are aiming to achieve with this campaign.
                3. Target Audience Insight: Who we are targeting, including any demographic and psychographic details.
                4. Key Messages: The core messages that should be communicated in the copy and visuals.
                5. Tone and Style Guidelines: How these messages should be delivered to align with our brand.
                6. List of Deliverables: Specific outputs we need from the copywriter and design team.

                A creative brief that outlines the project’s background, story premise, objectives, 
                desired audience reactions, and specific requirements such as tone and style and any 
                additional guidelines.
                """
            ),
            agent=agent,
            output_file="output_files/creative_brief.md",
        )

    def review_creative_brief(self, agent):
        return Task(
            description=textwrap.dedent(
                """
                Review the creative brief to make sure you understand the project's background, objectives,
                target audience, key messages, and tone. If you have any questions or need clarification,
                please reach out to the creative director for further guidance.
                """
            ),
            agent=agent,
            expected_output=textwrap.dedent(
                """
                An affirmation that you have reviewed the creative brief and are ready to proceed with your next task.
                """
            ),
            tools=[
                FileReadTool(file_path="output_files/creative_brief.md")
            ]
        )

    def write_ad_copy(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """                
                I'm looking for something that resonates emotionally, aligns with our tone, and drives engagement. 
                Please include any specific calls to action, promotional details, or key messages from the creative 
                brief. You'll be given a creative brief and seo brief. Feel free to work with the researcher to get 
                any necessary information or insights. Expect to receive one or more rounds of revisions.                 
                """
            ),
            context=context,
            agent=agent,
            expected_output=textwrap.dedent(
                """
                Ad copy with the following characteristics:
                
                1. Content Structure: The copy should have a clear and logical structure, typically including an introduction, 
                main body (divided into sections or headings for clarity), and a conclusion. This structure should effectively convey 
                the points highlighted in the brief.
                2. Engaging and Relevant Content: The writing should be engaging, well-researched, and relevant to the intended audience. 
                It should incorporate any specific points, keywords, or calls to action as specified in the brief.
                3. SEO Elements: The copy should incorporate relevant keywords, meta tags, and possibly links, 
                ensuring the copy is optimized for search engines.

                After revisions, the final version of the copy should be polished, error-free, and ready to publish.
                """
            ),
            async_execution=True,
            output_file="output_files/ad_copy.txt",
            tools=[
                FileReadTool(file_path="output_files/seo_brief.md")
            ]
        )

    def write_social_media_posts(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                Refer to the social media plan and creative brief to write engaging and compelling social media copy for the 
                upcoming product launch campaign. Feel free to collaborate with the social media manager, 
                creatvie director and editor for this task. The copy should be tailored to different platforms and 
                audiences, reflecting the brand's tone and voice while incorporating key messages and calls 
                to action from the creative brief. Collaborate with the creative team to ensure consistency 
                across all marketing materials.
                """
            ),
            context=context,
            agent=agent,
            expected_output=textwrap.dedent(
                """
                A set of social media posts tailored for different platforms (e.g., Facebook, Twitter, Instagram) 
                and audiences. The copy should be engaging, informative, and aligned with the brand's tone and voice. 
                It should incorporate key messages, calls to action, and relevant hashtags to maximize reach and engagement.
                """
            ),
            output_file="output_files/social_media_copy.md",
            async_execution=True,
            tools=[
                FileReadTool(file_path="output_files/creative_brief.md"),
                FileReadTool(file_path="output_files/social_media_plan.md")
            ]
        )

    def write_story(self, agent, context=None):
        return Task(
            description=textwrap.dedent(
                """
                Write a short story between 5000 and 6000 words based on the creative brief and the seo brief in the output_files directory.
                It should feature well-developed characters, a clear setting, and a fully developed plot that unfolds naturally within the constraints of 
                the short form. Work with the editor to refine the narrative of the story. There is no need to edit the creative brief
                or the seo brief. It is up to you to decide how to incorporate the information from the briefs into the story. Be creative and
                have fun with it. The creative brief and seo brief are there to guide you, not restrict you.
                Break the story into sections or chapters to make it easier to read and digest.
                It should also incorporate elements of the seo brief to ensure alignment with the campaign's messaging and objectives.
                The story should evoke emotion, provoke thought, and entertain the reader, leaving a lasting impact despite its brevity.
                Be sure to follow the recommendations in the seo brief to optimize the story for search engines paying close attention to 
                the suggested keyword density and header tags. Each primary keyword must appear at least once in the story.
                Consider consulting or collaborating with the researcher, seo specialist, or editor at the various stages of the writing process:

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
                A concise yet compelling narrative that engages the reader from beginning to end. The story should be in markdown with appropriate headings and 
                formatting to enhance readability.
                """
            ),
            output_file="output_files/story.md",           
            llm_config={
                "temperature": 0.9,  # High creativity
                "top_p": 0.9,  # Nucleus sampling
                "frequency_penalty": 0.5,  # Reduce repetition
                "presence_penalty": 0.6,  # Encourage new topics
            },
        )

    def convert_to_html(self, agent, context=None):        
        return Task(
            description=textwrap.dedent(
                """
                Convert the contents of the story markdown file into an HTML fragment. Be sure to escape any double quotes.
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                An html fragment on a single line.
                """
            ),
            tools=[
                FileReadTool(file_path="output_files/story.md")
            ],
            output_file="output_files/story.html"
        )

    def source_image(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                Read the story to fully understand its themes, characters, and settings to capture 
                key moments or emotions from the text. Collaborate with the writer and creative director 
                to ensure alignment with the story's tone and to provide a visual entry point that deepens the 
                reader's connection to the story. Provide at least 3 different images to choose from. The 
                images will be dislayed with a vertical orientation. Keep that in mind when composing your images.
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                A line separated list of the image URLs returned from the image generation tool.
                Example Output:
                    https://storage.googleapis.com/blogger-crew-images/Journey_to_Mount_Gaiyara.jpg
                    https://storage.googleapis.com/blogger-crew-images/Awakening_at_the_Peak.jpg
                    https://storage.googleapis.com/blogger-crew-images/adventure_forest.jpg

                Do not make any changes to public urls returned from the image generation tool when you add them to the output file.
                """
            ),
            output_file="output_files/image_urls.txt",
        )

    def crop_images(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                You will be given a list of image URLs in a text 
                file.

                1. Crop each image to a width of 450px and a height of 1100px  
                2. Crop each image to a width of 600px and a height of 200px
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                A line separated list of image URLs returned from the cropping tool
                Example Output:
                    https://storage.googleapis.com/blogger-crew-images/cropped/Ancient_City_of_Tenria-450x1100.jpg
                    https://storage.googleapis.com/blogger-crew-images/cropped/Ancient_City_of_Tenria-600x200.jpg
                    https://storage.googleapis.com/blogger-crew-images/cropped/Awakening_at_the_Peak-450x1100.jpg
                    https://storage.googleapis.com/blogger-crew-images/cropped/Awakening_at_the_Peak-600x200.jpg

                Do not make any changes to public urls returned from the cropping tool when you add them to the output file.
                """
            ),
            output_file="output_files/cropped_image_urls.txt",
            tools=[
                FileReadTool(file_path="output_files/image_urls.txt")
            ]
        )

    def create_seo_brief(self, agent, context):
        return Task(
            description=textwrap.dedent(
                """
                Start by affirming that you understand the project's background, objectives, target audience, key messages, and tone 
                from the creative brief.
                You'll be given a list of keywords in a text file called keywords.txt.
                Create an SEO brief for an upcoming product launch campaign, outlining the targeted keywords from the keywords.txt file, 
                content recommendations, and backlink strategies to ensure maximum visibility and engagement on search engines.
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                An SEO content brief which includes:
                    Target Keywords: Specific primary and secondary keywords that the content should rank for. 
                    Keyword Density: Recommendations on how frequently keywords should appear in the content.
                    SEO Title: The suggested title that includes the primary keyword.
                    Meta Description: A pre-written meta description that includes primary keywords and is designed to encourage clicks.
                    Header Tags: Guidance on structuring content with SEO-friendly header tags (H1, H2, H3, etc.).
                    URL Suggestions: Advice on creating SEO-friendly URLs.
                    Image Alt Text: Descriptions for images to include as alt text.
                    External Linking: Recommendations for linking to external authoritative sources.
                    Content Length: Specification on the minimum word count based on the competitiveness of the keywords and the depth of the topic.
                    Audience and Intent: Insights into the target audience and the search intent behind the primary keywords.

                Please list at least 4 external links to include in the external linking section of your SEO brief.
                """
            ),
            output_file="output_files/seo_brief.md",
            tools=[
                FileReadTool(file_path="seo/keywords.txt"),
            ],
        )

    def review_seo_brief(self, agent):
        return Task(
            description=textwrap.dedent(
                """
                Review the SEO brief to ensure you understand the targeted keywords, content recommendations, and backlink strategies. 
                If you have any questions or need clarification, please reach out to the SEO specialist for further guidance.
                """
            ),
            agent=agent,
            expected_output=textwrap.dedent(
                """
                An affirmation that you have reviewed the SEO brief and are ready to proceed with your next task.
                """
            ),
            tools=[
                FileReadTool(file_path="output_files/seo_brief.md")
            ]
        )

    def develop_social_media_plan(self, agent, context=None):
        return Task(
            # Plan the promotion of content on X, Instagram, and Facebook. Collaborate with the creative team to ensure consistency across platforms.
            description=textwrap.dedent(
                """
                Plan the promotion of content on X, Instagram, and Facebook.
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                A markdown-formatted social media promotion plan, including platform-specific post content and hashtags.
                Example Output:
                    ## Social Media Promotion Plan\\n\\n
                    **X:**\\n
                    - Tweet 1: {Tweet content} #hashtag1 #hashtag2\\n
                    - Tweet 2: {Tweet content} #hashtag1 #hashtag3\\n\\n
                    **Facebook:**\\n
                    - Post 1: {Facebook post content}\\n
                    - Post 2: {Facebook post content}\\n\\n
                    **Instagram:**\\n
                    - Post 1: {Instagram post content}\\n
                    - Post 2: {Instagram post content}\\n\\n
                """
            ),
            async_execution=False,
            output_file="output_files/social_media_plan.md",
            tools=[FileReadTool(file_path="output_files/creative_brief.md")]
        )

    
    def generate_prompt_from_ad_copy(self, agent, context=None):
        return Task(
            description=textwrap.dedent(
                """
                Read the ad copy to fully understand the product, target audience, and key messages. Collaborate with the copywriter and creative director 
                to ensure alignment with the campaign's objectives and tone. Use the information in the creative brief to generate a prompt that captures the essence 
                of the ad copy and encourages the reader to take action. The choice of style is up to you.
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                A prompt that captures the essence of the ad copy and encourages the reader to take action.
                """
            ),
            output_file="output_files/midjourney_ad_copy_prompt.txt",
            tools=[
                FileReadTool(file_path="output_files/ad_copy.txt"),
                FileReadTool(file_path="output_files/creative_brief.md"),
                FileReadTool(file_path="midjourney_docs.md")
            ],
            llm_config={
                "temperature": 0.9,  # High creativity
                "top_p": 0.9,  # Nucleus sampling
                "frequency_penalty": 0.5,  # Reduce repetition
                "presence_penalty": 0.6,  # Encourage new topics
            }
        )
    def generate_prompt_from_story(self, agent, context=None, aspect_ratio="9:22"):
        return Task(
            description=textwrap.dedent(
                f"""
                Read the story to fully understand its themes, characters, and settings to capture
                key moments or emotions from the text. Collaborate with the writer and creative director
                to ensure alignment with the story's tone and to provide a visual entry point that deepens the
                reader's connection to the story. Use the information in the midjourney_docs.md file to
                generate a midjourney prompt that captures the essence of the story and engages the reader's curiosity.
                The choice of style is up to you.
                Refer to the information in the midjourney-docs.md file to generate a prompt that captures the essence of this 
                story. Be sure to use the appropriate parameters necessary to achieve the desired effects. Use only parameters
                listed in the documentation, do not invent new parameters. 
                Use version 6 unless otherwise specified and use an aspect ratio of {aspect_ratio}.         
                """
            ),
            agent=agent,
            context=context,
            expected_output=textwrap.dedent(
                """
                A midjourney prompt that captures the essence of the story and engages the reader's curiosity
                """
            ),
            output_file="output_files/midjourney_story_prompt.txt",
            tools=[FileReadTool(file_path="output_files/story.md")],
        )
