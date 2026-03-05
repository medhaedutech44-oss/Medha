from fastapi import FastAPI


from app.dashboard.routes import router as dashboard_router


app = FastAPI()

app.include_router(dashboard_router)