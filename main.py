import os
from fastapi import FastAPI
from psycopg2 import connect

conn = connect(
    host=os.getenv("POSTGRES_HOST"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT")
)

cur = conn.cursor()

app = FastAPI()


@app.get("/create")
async def root(name: str):
    table = """create table if not exists sample(
        id serial primary key,
        name varchar(255)
    );"""
    cur.execute(table)
    conn.commit()
    query = """insert into sample(name) values (%s)"""
    cur.execute(query, (name,))
    conn.commit()
    return {"name": name}


@app.get("/")
async def root():
    query = """select * from sample limit 400"""
    cur.execute(query)
    datas = cur.fetchall()
    result = {data[0]: data[1] for data in datas}
    return result


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}