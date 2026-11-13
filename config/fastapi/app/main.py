from fastapi import FastAPI
from app.routes.dynamic_content import router_get_users

app = FastAPI()

app.include_router(router_get users, prefix="/app")

app.include_router(router_get users, prefix="/app")
