# flake8: noqa

import logging
from datetime import datetime

import pytz
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.routing import APIRoute
from src.common.constants import Configuration
from src.routers.base_v1 import base_router_v1
from src.routers.aiq_v1 import aiq_router_v1

logger = logging.getLogger(__name__)


# Initialize FastAPI
aiq_app = FastAPI(
    title="AIQ REST API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    swagger_ui_parameters={"displayRequestDuration": True}
)


aiq_app.include_router(base_router_v1)
aiq_app.include_router(aiq_router_v1)


# Initialized API endpoints
endpoints = []
for route in aiq_app.routes:
    if isinstance(route, APIRoute):
        endpoints.append(f"{','.join(route.methods)} - {route.name}: {route.path}")
logger.info("List of api", extra={"props": {"endpoint": endpoints}})

APPLICATION_STARTUP_TIME_IN_UTC = None


@aiq_app.on_event("startup")
def startup_event():
    global APPLICATION_STARTUP_TIME_IN_UTC
    APPLICATION_STARTUP_TIME_IN_UTC = datetime.now(pytz.utc)


# Redirect root to health
@aiq_app.get("/", tags=["base"], include_in_schema=False)
async def main_route():
    return RedirectResponse(url="/v1/health", status_code=301)


if __name__ == "__main__":
    import uvicorn

    logger.info("Running Decode locally...")
    uvicorn.run(
        app="main:aiq_app",
        host="0.0.0.0",
        port=Configuration.PORT,
        log_level=Configuration.LOG_LEVEL.lower(),
        reload=True,
    )
