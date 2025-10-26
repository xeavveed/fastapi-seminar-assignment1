from pydantic import BaseModel, field_validator
import re

class CreateUserRequest(BaseModel):
    # Todo
    name: str
    phone_number: str
    height: float
    bio: str | None = None
    
    @field_validator("phone_number")
    def validate_phone_number(cls, v):
        pattern = r"^010-\d{4}-\d{4}$"
        if not re.fullmatch(pattern, v):
            raise ValueError("올바른 형식으로 전화번호를 입력하세요.")
        return v

    @field_validator("bio")
    def validate_bio(cls, v):
        if v is not None and len(v) > 500:
            raise ValueError("500자 이내로 bio를 입력하세요.")
        return v

class UserResponse(BaseModel):
    # Todo
    user_id: int
    name: str
    phone_number: str
    height: float
    bio: str | None = None
