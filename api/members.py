import fastapi

router = fastapi.APIRouter(
    prefix='/members',
    tags=['Members']
)

# Getting all members
@router.get("/")
async def read_members():
    return {"members": []}

# Creating a member
@router.post("/")
async def create_member_api():
    return {"members": []}

# Getting a member by ID
@router.get("/:{id}")
async def read_member():
    return {"members": []}

# Updating member
@router.patch("/:{id}")
async def update_member():
    return {"member": []}

# Deleting member
@router.delete("/:{id}")
async def delete_member():
    return {"members": []}

