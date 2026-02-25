from fastapi import FastAPI
from starlette import status

from app.schema.product import ProductSchema

app = FastAPI(title="9_lektion")


@app.get("/")
def root():
    return {"message: Hello World"}


@app.post(path: "/products",status_code =status.HTTP_201_CREATED, response_model=ProductSchema)
def post_product(product:ProductSchema) -> ProductSchema:
    return product