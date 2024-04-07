from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional



class check_api_post(BaseModel):
    message:str
    full_name:str
    location:Optional[str] = None

app = FastAPI()


valuesToBeStored = {
    "class":"data Science",
    "Student_name":"suraj",
    "id":1
    }



@app.get('/')
def get_home_page():
    return JSONResponse(content={"message":"hello world"})



@app.get('/post_comment/{id}')
def take_comment(id:int):

    """
    Takes message and return something
    """

    try:
        if valuesToBeStored[id] == id:
            takesClass,student_name = valuesToBeStored['class'],valuesToBeStored['Student_name']
        
        return {"class":takesClass,"Name":student_name}

    except Exception as err:
        return err

@app.post('/post_comment')
def take_comment(paramter:check_api_post)->str:

    """
    Takes message and return something
    """

    try:
        return JSONResponse(content={"message":paramter.message,"values":paramter.location})

    except Exception as err:
        return err
        print("error")