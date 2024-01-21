import uvicorn
from fastapi import FastAPI
from api_v1 import router as menu_router
from src.settings import settings


app = FastAPI()
app.include_router(router=menu_router, prefix=settings.API_V1_PREFIX)


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
