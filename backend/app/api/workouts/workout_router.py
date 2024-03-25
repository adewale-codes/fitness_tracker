# app/api/workouts/workout_router.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/log")
def log_workout():
    pass

@router.get("/history")
def get_workout_history():
    pass
