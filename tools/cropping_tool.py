from io import BytesIO
from urllib.parse import urlparse
from PIL import Image
from langchain.tools import tool
from google.cloud import storage

import os
import subprocess
import requests

class CroppingTool():
    @tool("Crops an image to the specified dimensions.")
    def crop_image(public_url, new_width, new_height):
        """
        Crops an image to the specified dimensions.
        """
        bucket_name = 'blogger-crew-images'

        filename = CroppingTool().get_filename_from_url(public_url)
        modified_filename = CroppingTool().modify_filename(filename, new_width, new_height)
        folder_path = 'cropped'        

        # Open the image from the URL
        response = requests.get(public_url)
        img = Image.open(BytesIO(response.content))
        # save image to temporary file
        img.save('output_files/temp.jpg')

        # Call smartcrop-cli using npx
        result = subprocess.run(['npx', 'smartcrop-cli', '--width', str(new_width), '--height', str(new_height), 'output_files/temp.jpg', 'output_files/cropped.jpg'], capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode != 0:
            print('Error:', result.stderr)
        else:
            print('Image cropped successfully')

        # Read the cropped image back into a BytesIO buffer
        with open('output_files/cropped.jpg', 'rb') as f:
            img_data = f.read()
        
            # Construct the destination blob name with the folder path
            destination_blob_name = f"{folder_path}/{modified_filename}"

            # Upload the cropped image to the bucket
            cropped_public_url = CroppingTool().upload_to_gcs(bucket_name, destination_blob_name, img_data)

            print(f"cropped_public_url: {cropped_public_url}")

            return cropped_public_url

    @staticmethod
    def upload_to_gcs(bucket_name, blob_name, image_data):
        storage_client = storage.Client.from_service_account_json('blogger-crew-google-drive-api.json')
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(image_data)
        return blob.public_url

    @staticmethod
    def modify_filename(filename, width, height):
        name, extension = os.path.splitext(filename)
        if not extension:
            extension = 'jpg'
        else:
            extension = extension[1:]  # remove the leading dot
        modified_filename = f"{name}-{width}x{height}.{extension}"
        return modified_filename

    @staticmethod
    def get_filename_from_url(public_url):
        parsed_url = urlparse(public_url)
        path_parts = parsed_url.path.split('/')
        filename = path_parts[-1]
        return filename
