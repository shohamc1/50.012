from typing import Optional

from fastapi import HTTPException
from fastapi.param_functions import Header
from starlette.responses import FileResponse

from main import app

# return image/jpg instead of plaintext/json
@app.get("/yee/")
def yee():
    return FileResponse("media/yee.jpg", media_type="image/jpg")


@app.get("/secure/")
def secure_hello(super_secure: Optional[str] = Header(None)):
    if super_secure == "yee":
        return FileResponse("media/yee.jpg", media_type="image/jpg")
    else:
        raise HTTPException(
            status_code=401, detail="You are not authorized for the yee :("
        )
