from fastapi import FastAPI
from server.routers import students


app = FastAPI()


@app.get("/", tags=["Root"])
def read_root():
    return {"status": "up"}

app.include_router(
    students.router,
    prefix=students.PREFIX,
    tags=students.TAGES
)
