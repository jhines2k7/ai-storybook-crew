import json
import markdown


def bundle_crew_results():
    with open("output_files/story.md", "r") as file:
        md_text = file.read()
        html = markdown.markdown(md_text)

    with open("output_files/cropped_image_urls.txt", "r") as file:
        cropped_images_urls = file.read().splitlines()

    # create a dictionary with the html and the cropped images urls
    bundle = {
        "html": html,
        "images": cropped_images_urls
    }

    # convert the dictionary to json string
    return json.dumps(bundle)

results = bundle_crew_results()
print(results)