import httpx
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from src.api.v1.geo_dadata import router as geo_dadata_router

app = FastAPI(
    title="DaData api worker",
    description="Проект для получения данных с DaData и представления их в виде HTML документов",
    version="0.0.1",
    docs_url="/swagger_api",
)

app.include_router(
    geo_dadata_router,
    tags=["Geo data"],
)


@app.exception_handler(httpx.HTTPStatusError)
async def exception_handler(_: Request, exc: httpx.HTTPStatusError) -> ORJSONResponse:
    return ORJSONResponse(
        content=f"Detail: {str(exc)}",
        status_code=exc.response.status_code,
    )
