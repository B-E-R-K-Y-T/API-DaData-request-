from fastapi import FastAPI

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
