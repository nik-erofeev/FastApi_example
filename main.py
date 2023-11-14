import uvicorn
from fastapi import FastAPI

from routers.items import router as items_router
from routers.users import router as users_router
from routers.tokens import router as tokens_router

app = FastAPI()

# core.Base.metadata.create_all(bind=engine)  # create table

app.include_router(router=items_router, prefix="/items")

app.include_router(router=users_router, prefix="/users")

app.include_router(router=tokens_router, prefix="/tokens")


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
