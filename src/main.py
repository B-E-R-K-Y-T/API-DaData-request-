from fastapi import FastAPI

app = FastAPI(
    title="DaData api worker",
    description="Проект для получения данных с DaData и представления их в виде HTML документов",
    version="0.0.1",
)
