from datetime import datetime

from fastapi import APIRouter

from src.common.routes import BaseRoutes
from src.common.constants import Configuration
from src.schemas.response import Response


base_router_v1 = APIRouter(prefix="/v1", tags=BaseRoutes.TAGS)


@base_router_v1.get(BaseRoutes.HEALTH, response_model=Response)
async def check_health_handler():
    return Response(
        status_code=200,
        data={
            "status": "Hello from Decode!",
            "current_time": datetime.now(),
            "version": Configuration.APP_VERSION,
        }
    )
