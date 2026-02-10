from pydantic import BaseModel, EmailStr, Field, field_validator, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=128)

    @classmethod
    @field_validator("username", mode="before")
    def validate_username(cls, value: str) -> str:
        if not value:
            raise ValueError("Username cannot be empty")
        
        if value[0].isdigit():
            raise ValueError("Username cannot start with a digit")
        
        return value.lower()

class UserOut(BaseModel):
    id: int
    email: EmailStr
    username: str
    profile_image: str
    timezone: str
    bio: str
    website: str
    location: str

    model_config = ConfigDict(from_attributes=True)
