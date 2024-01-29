from fastapi import File
from pydantic import BaseModel


class UploadImageCsvFile(BaseModel):

    file = UploadFile = File(...)
