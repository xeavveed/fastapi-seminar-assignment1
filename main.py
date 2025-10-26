import fastapi
from src.dto import CreateUserRequest, UserResponse
from fastapi import Query

app = fastapi.FastAPI()

user_count = 0
user_db = {}


@app.post("/api/users")
def create_user(request: CreateUserRequest) -> UserResponse:
    # Todo
    global user_count
    user_count+=1
    user_db[user_count] = {
        "name": request.name,
        "phone_number": request.phone_number,
        "height": request.height,
        "bio": request.bio,
    }
    return UserResponse(user_id = user_count, name = request.name, phone_number = request.phone_number,
                        height = request.height, bio = request.bio)


@app.get("/api/users/{user_id}")
def get_user(
    # Todo
    user_id: int
) -> UserResponse:
    # Todo
    if user_id not in user_db:
        raise ValueError("해당 id의 유저가 존재하지 않습니다.")
    return UserResponse(user_id = user_id, name = user_db[user_id]["name"], phone_number = user_db[user_id]["phone_number"],
                        height = user_db[user_id]["height"], bio = user_db[user_id]["bio"])


@app.get("/api/users")
def get_users(
    # Todo
    min_height: float = Query(...), max_height: float = Query(...)
) -> list[UserResponse]:
    # Todo
    arr = []
    for k, v in user_db.items():
        if v["height"] >= min_height and v["height"] <= max_height:
            arr.append(UserResponse(user_id = k, name = v["name"], phone_number = v["phone_number"], height = v["height"], bio = v["bio"]))
    return arr
