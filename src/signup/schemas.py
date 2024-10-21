from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import date


class UserSignup(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, regex=r'^\w+$',
                          description="Username must be alphanumeric and 3-50 characters long.")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100,
                          description="Password must be at least 8 characters long.")
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    dob: date = Field(..., description="Date of birth in YYYY-MM-DD format.")
    phone_number: str = Field(..., regex=r'^\+?\d{10,15}$',
                              description="Phone number must be 10 to 15 digits long and can include an optional '+' prefix.")

    @field_validator('password')
    def validate_password_strength(cls, password):
        if not any(c.islower() for c in password):
            raise ValueError('Password must contain at least one lowercase letter.')
        if not any(c.isupper() for c in password):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not any(c.isdigit() for c in password):
            raise ValueError('Password must contain at least one digit.')
        return password

    @field_validator('dob')
    def validate_dob(cls, dob):
        # Ensure the user is at least 18 years old
        from datetime import date
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise ValueError('User must be at least 18 years old.')
        return dob
