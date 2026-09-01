from fastapi import FastAPI

from src.routes.file_route import router


app = FastAPI(
    title="Semantic Search API"
)

app.include_router(router)