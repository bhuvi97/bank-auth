from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from dependencies.sql_session import get_db
from sqlalchemy import select
from models import User

signup_router = APIRouter(prefix="/signup", tags=["signup"])


@signup_router.get('', status_code=200)
async def signup(async_session: AsyncSession = Depends(get_db)):
    result = await async_session.execute(select(User))  # Fetch all users from the 'users' table
    users = result.scalars().all()  # Convert result to list of User objects
    return users
