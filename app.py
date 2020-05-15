# Core Pkg
from fastapi import FastAPI
import uvicorn
import json
import csv
import pandas as pd

# Init
app = FastAPI(debug=True)

people = []
with open('people.csv','rU') as f: 
    reader = csv.DictReader(f)
    for row in reader:
        people.append(row)

#Output a Json file with Birth Month as Keys and Names as values
@app.get('/people')
async def get_people():
	df=pd.DataFrame(people)	
	dict1=dict(df.groupby("month").apply(lambda x:x['name'].to_json(orient="records")))
	return json.dumps(dict1)

#Output names that have the corresponding user-inputed birth month
@app.get('/people/{month}')
async def get_person(month):
	person = [person for person in people if person["month"] == month]
	return {"people":person}

if __name__ == '__main__':
	uvicorn.run(app, host="127.0.0.1",port="8000")
