from enum import Enum

from fastapi import FastAPI

# class ModelName (str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

app = FastAPI()

# @app.get("/models/{model_name}")
# async def get_model (model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the iamges"}
#     return {"model_name": model_name, "message": "Have some residuals"}

# @app.get("/")
# async def root():
#     return("message": "Hello World")

# # @app.get("/items/")
# # async def items():
# #     return("Hello Items")

# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, skip: int, limit: int, q: str | None = None):
#     if q:
#         return {"skip": skip, "limit": limit, "q": q}
#     return {"skip": skip, "limit": limit}

@app.get("/users/{users_id}")
async def read_id(users_id: int):
    return{"users id": users_id}

@app.get("/users/{user_id}/items/")
async def read_user_item(
    user_id: int, skip: int, limit: int):
    return{"user id": user_id, "skip": skip, "limit": limit}
