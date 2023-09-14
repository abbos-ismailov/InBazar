from typing import Union
import aiogram
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config



class Db_connection:
    def __init__(self) -> None:
        self.pool : Union[Pool, None] = None
    
    async def create(self):
        self.pool = await asyncpg.create_pool(
            user = config.DB_USER,
            password = config.DB_PASS,
            host = config.DB_HOST,
            database = config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False,
                      ):

        async with self.pool.acquire() as connection:
            connection: Connection
            
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
        return result

    async def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL UNIQUE,
        full_name VARCHAR(255) NULL,
        telephone VARCHAR(255) NULL,
        username VARCHAR(255) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_purchases(self):
        sql = """
        CREATE TABLE IF NOT EXISTS purchases (
        user_tg_id INT NOT NULL,
        product_id INT NOT NULL,
        product_url VARCHAR(950) NOT NULL,
        product_size VARCHAR(20) NOT NULL,
        product_name VARCHAR(250) NOT NULL,
        product_count INT NOT NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod ### Shunga tushunish kerak
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, telegram_id, full_name, telephone, username):
        sql = """
        INSERT INTO Users(telegram_id, full_name, telephone, username) VALUES($1, $2, $3, $4) returning *
        """
        return await self.execute(sql, telegram_id, full_name, telephone, username, fetchrow=True)
    
    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def get_one_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parametrs = self.format_args(sql, parametrs=kwargs)
        return await self.execute(sql, *parametrs, fetchrow=True)
    
    ### CLOTHES tablesi kodlari
    ### MAHSULOT qo'shish
    async def add_product(self, product_name, product_size, product_count, product_price, product_url):
        sql = """
        INSERT INTO clothes(product_name, product_size, product_count, product_price, product_url) VALUES($1, $2, $3, $4, $5) returning *
        """
        return await self.execute(sql, product_name, product_size, product_count, product_price, product_url, fetchrow=True)
    
    ### DELETE PRODUCT FUNCTION
    async def delete_product(self, telegram_id):
        await self.execute("DELETE FROM clothes WHERE product_url=$1", telegram_id, execute=True)
    
    ### Mahsulot name siga qarab chiqarish
    async def select_product(self, pr_name):
        sql = "SELECT * FROM clothes WHERE product_name=$1"
        return await self.execute(sql, pr_name, fetch=True)
    
    async def select_product_clothes(self, pr_id):
        sql = "SELECT * FROM clothes WHERE product_id=$1"
        return await self.execute(sql, pr_id, fetchrow=True)

    async def get_one_clothes(self, pr_id):
        sql = "SELECT * FROM clothes WHERE product_id=$1"
        return await self.execute(sql, pr_id, fetchrow=True)

    async def update_clothes_count(self, product_count, product_id):
        sql = "UPDATE clothes SET product_count=$1 WHERE product_id=$2"
        return await self.execute(sql, product_count, product_id, execute=True)
    
    ### PURCHASES tablesi kodlari -------------------------------------------------
    ### mahsulotni korzinkaga qoshyapmiz
    async def add_to_korzinka(self, user_tg_id, product_id, product_url, product_size, product_name, product_count):
        sql = """ 
        INSERT INTO purchases(user_tg_id, product_id, product_url, product_size, product_name, product_count) VALUES($1, $2, $3, $4, $5, $6) returning *
        """
        return await self.execute(sql, user_tg_id, product_id, product_url, product_size, product_name, product_count, fetchrow=True)

    async def update_purchases_count(self, product_count, product_id, user_tg_id):
        sql = "UPDATE purchases SET product_count=$1 WHERE product_id=$2 AND user_tg_id=$3"
        return await self.execute(sql, product_count, product_id, user_tg_id, execute=True)
    
    async def get_from_purchases(self, **kwargs): ### id siga qarab oldik
        sql = """
        SELECT * FROM purchases WHERE 
        """
        sql, parametrs = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parametrs, fetchrow=True)
    
    ### Sotib olingan mahsulotlarni foydalanuvchiga korsatyapmiz
    async def show_purchases(self, user_tg_id):
            sql = "SELECT * FROM purchases WHERE user_tg_id=$1"
            return await self.execute(sql, user_tg_id, fetch=True)
    
    async def get_one_purchases(self, pr_id, user_tg_id):
        sql = "SELECT * FROM purchases WHERE product_id=$1 AND user_tg_id=$2"
        return await self.execute(sql, pr_id, user_tg_id, fetchrow=True)
    
    ### count = 0 bolganini ochirib tashladik
    async def delete_product_from_korzinka(self, pr_id, user_tg_id):
        await self.execute("DELETE FROM purchases WHERE product_id=$1 AND user_tg_id=$2", pr_id, user_tg_id, execute=True)