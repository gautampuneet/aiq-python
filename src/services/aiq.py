import json
import secrets
import uuid

import numpy as np
import cv2

from src.schemas.response import Response
from src.models.images import ImagesModel
from src.database import Database


class ResizeImageService:

    def __init__(self, image_data_df=None):
        self.image_data_df = image_data_df
        self.collection = Database().get_collection("images")

    @staticmethod
    def resize_image(row):
        image = np.array([int(pixel) for pixel in row[1:]]).reshape((200, 1))  # Assuming data loaded from row
        resized_image = cv2.resize(image, (150, 1), interpolation=cv2.INTER_AREA)
        return resized_image

    def save_image_csv_file(self):
        # Discard empty rows
        image_data_df = self.image_data_df.dropna()

        # Apply resizing to each row (image)
        new_width = 150
        resized_images = []

        for index, row in image_data_df.iterrows():
            depth = row[0]
            # Assuming pixel values are in columns from 1 to 200
            pixels = row[1:201].values.reshape((1, 200))  # Assuming row represents a flat array of pixel values

            # Reshape pixel values into an image and resize
            image = pixels.reshape((1, 200)).astype(np.uint8)
            resized_image = cv2.resize(image, (new_width, 1))

            # Flatten and append the resized image back to the list
            resized_images.append({"depth": depth, "image": list(resized_image.flatten())})

        # Save the resized image into the database
        file_id = self.save_resized_data_into_db(resized_images)
        return Response(data={"message": "Successfully saved the resized images into the database.",
                              "data": {
                                  "file_id": file_id
                              }
                              }, status_code=201)

    @staticmethod
    def generate_random_hex_color():
        """
        Generate a random hex color code.

        Returns:
        - random_hex_color: A string representing a random hex color code.
        """
        random_hex_color = "#{:06x}".format(secrets.randbelow(0xFFFFFF))
        return random_hex_color

    def save_resized_data_into_db(self, resized_images):
        # Save the resized image into the database
        file_id = str(uuid.uuid4())
        for row in resized_images:
            image_instance = ImagesModel(
                depth=row['depth'],
                pixels=row['image'],
                file_id=file_id,
                color=self.generate_random_hex_color()
            )
            self.collection.insert_one(image_instance.dict(by_alias=True))
        return file_id

    def get_first_record(self):
        data = self.collection.find_one()
        data['_id'] = str(data['_id'])
        return data

    def get_frames_between_depths(self, depth_min, depth_max, file_id):
        # Get the images between the given depths
        images = self.collection.find({"depth": {"$gte": depth_min, "$lte": depth_max}, "file_id": file_id})

        # Convert the images into a list
        images_list = []
        for image in images:
            image['_id'] = str(image['_id'])
            images_list.append(image)

        # Return the list of images
        return Response(data={"message": "Successfully retrieved the images between the given depths.",
                              "data": images_list}, status_code=200)

