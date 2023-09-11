from aiogram.dispatcher.filters.state import State, StatesGroup

class Add_product_states(StatesGroup):
    product_name = State()
    product_size = State()
    product_img = State()
    product_price = State()
    product_count = State()

class Delete(StatesGroup):
    product_id = State()