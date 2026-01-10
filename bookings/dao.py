from ..dao.base import BaseDAO
from ..database import async_session_maker
from sqlalchemy import select
from .models import Bookings


class BookingDAO(BaseDAO):
    model = Bookings