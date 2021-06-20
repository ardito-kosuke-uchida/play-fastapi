from fastapi import FastAPI, Response, status, Depends

from . import middlewares, routes
from . import dependencies

app = FastAPI(
    title="Play FastAPI",
    description="FastAPI サンプル集",
)

middlewares.setup(app)

for route in routes.routers:
    app.include_router(route)


@app.get("/", include_in_schema=False)
async def root():
    # / はドキュメントにリダイレクト
    return Response(
        status_code=status.HTTP_302_FOUND,
        headers={"Location": "/docs"},
    )
