import json
import markdown

from crewai_tools import BaseTool

from langchain.tools import tool

class BundleTool(BaseTool):
    name: str = "Bundle Tool"
    description: str = "Takes no input and combines the results from multiple files into a single JSON object."

    def _run(self) -> str:
        with open("output_files/story.md", "r") as file:
            md_text = file.read()
            html = markdown.markdown(md_text)

        with open("output_files/cropped_image_urls.txt", "r") as file:
            cropped_images_urls = file.read().splitlines()

        bundle = {
            "story": html,
            "images": cropped_images_urls
        }

        results = json.dumps(bundle)
        print(results)
        
        return results
