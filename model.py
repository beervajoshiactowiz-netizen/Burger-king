from pydantic import BaseModel, HttpUrl,field_validator
from typing import Optional
import re

class Outlet(BaseModel):
    Outletname: str
    OutletAddress:   str
    OutletCity: str
    OutletState: str
    landmark:str
    Phone: int
    timings:  str
    pincode: int
    MapUrl:   str
    OutletUrl: str

    @field_validator("Outletname", "OutletAddress")
    @classmethod
    def must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Field must not be empty")
        return v.strip()

    @field_validator("Phone", mode="before")
    @classmethod
    def parse_phone(cls, v):
        digits = re.sub(r"^\+?91", "", str(v).strip())
        if not re.fullmatch(r"\d{10}", digits):
            raise ValueError(f"Invalid phone number: '{v}'")
        return int(digits)

    @field_validator("pincode",mode="before")
    @classmethod
    def pincode_int(cls,v):
        return int(v)

    @field_validator("MapUrl","OutletUrl")
    @classmethod
    def url_check(cls,v):
        if v.startswith("http"):
            return v
        else:
            print("Invalid Url")