from fastapi import FastAPI
from fastapi_pagination import add_pagination

import routes

app = FastAPI()
app.include_router(routes.router)

add_pagination(app)




