from aiogram import Dispatcher

from loader import dp
# from .is_admin import AdminFilter
from .is_admin import AdminFilterGroup

if __name__ == "filters":
    #dp.filters_factory.bind(is_admin)
    dp.filters_factory.bind(AdminFilterGroup)
