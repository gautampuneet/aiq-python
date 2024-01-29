import pandas as pd
from io import BytesIO
from fastapi import APIRouter, File, UploadFile


from src.common.routes import AIQRoutes
from src.schemas.response import Response
from src.services.aiq import ResizeImageService

aiq_router_v1 = APIRouter(prefix="/v1", tags=AIQRoutes.TAGS)


@aiq_router_v1.post(AIQRoutes.IMAGES, response_model=Response)
async def upload_image_csv_file(csv_file: UploadFile = File(...)):
    content = csv_file.file.read()

    # Validate the file as CSV
    try:
        image_data_df = pd.read_csv(BytesIO(content))
    except pd.errors.ParserError as e:
        return Response(
            status_code=400,
            data={"error": f"Invalid CSV file. Error: {str(e)}"},
        )

    return ResizeImageService(image_data_df).save_image_csv_file()


@aiq_router_v1.get(AIQRoutes.IMAGES, response_model=Response)
async def get_image_frames(depth_min: float, depth_max: float, file_id: str):
    return ResizeImageService().get_frames_between_depths(depth_min, depth_max, file_id)
