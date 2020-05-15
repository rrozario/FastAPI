# FastAPI

The app.py file has two functions:
1. get_people() returns a json file with people segregated by their birth months as the key.
2. get_person() takes a month as an input and returns the names of all the people with that input as their birthday month

The python file takes people.csv as an input file. 

Running instructions:
In bash - uvicorn app:app --reload
On browser - http://127.0.0.1:8000/docs#/
