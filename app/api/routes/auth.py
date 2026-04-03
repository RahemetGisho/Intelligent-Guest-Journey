from fastapi import APIRouter, HTTPException, Depends, Header

router = APIRouter()

FAKE_TOKENS = {"admin-token": "admin", "guest-token": "guest"}

def get_current_user(x_token: str = Header(...)):
    if x_token not in FAKE_TOKENS:
        raise HTTPException(status_code=401, detail="Invalid token")
    return FAKE_TOKENS[x_token]

@router.get("/me")
def read_me(user: str = Depends(get_current_user)):
    return {"role": user}