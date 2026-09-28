from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_table
from routes.reviews import router as Review_Router


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Startup
    create_table()

    print("Database table created")

    yield

    # Shutdown
    print("Shutting down the app")


app = FastAPI(
    title="Rangmanch Reviews API",
    description="Theatre reviews API for Pune Rangmanch",
    lifespan=lifespan
)


app.include_router(Review_Router)


@app.get("/")
def root():

    return {
        "message": "Welcome to Rangmanch Review API"
    }