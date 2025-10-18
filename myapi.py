from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel 
from datetime import datetime, timezone
import requests

app = FastAPI(title = "My Profile API Server")



# Define timestamp model
class Item(BaseModel):
    name: str
    timestamp: datetime

# Define User model
class userData(BaseModel):
    email: str
    name: str
    stack: str

# Define profile model
class Profile(BaseModel):
    status: str
    user: userData
    timestamp: datetime
    fact: str

# myProfile =  {
#         "status": "success",
#         "email": "adejinmiseyi@gmail.com",
#         "name": "Oluwaseyi Adejinmi",
#         "stack": "Backend - Python/FastAPI"
#     }








@app.get("/me", status_code=status.HTTP_200_OK)
async def getProfile():

    # Get the current time in UTC - ISO 8601 format
    now_utc = datetime.now(timezone.utc)

     # The Cat fact api call
    # def cat_fact_api():
    url = "https://catfact.ninja/fact"
    response = requests.get(url, headers={"Content-Type": "application/json"},
                            )
    if response.status_code == 200:
        data = response.json()
        catFact = data['fact']
        print("fact:", catFact)
    else:
        raise HTTPException(status_code=404, detail="No cat facts available")
            
    
    # Get User bio information 
    user_data = userData ( 
        email = "adejinmiseyi@gmail.com",
        name = "Oluwaseyi Adejinmi",
        stack = "Backend - Python/FastAPI"
        )
    
    my_profile = Profile (
         status = "success",
         user =  user_data,
         timestamp = now_utc,
         fact = catFact
         
    )
   
    
    # user =  {
    #     "status": myProfile["status"],
    #     "email": myProfile["email"],
    #     "name": myProfile["name"],
    #     "stack": myProfile["stack"],
    # }

    # "timestamp":  datetime.now(timezone.utc),
    # "fact": catFact

    return my_profile
       


'''

{
    "status": "success",
    
    "user": {
        "email"
        "name"
        "stack"
    }

    "timestamp":
    "fact"
}


'''