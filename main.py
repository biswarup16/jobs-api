from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --------------------------------------------------
# CORS
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# CORS
# --------------------------------------------------

@app.get("/")
def home():
    soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
    return soup.prettify()


@app.get("/jobs/{skill}")
def search_job(skill: str):
    url = "https://indeed12.p.rapidapi.com/jobs/search"

    querystring = {
        "query": f"{skill}",
        "location": "india",
        "page_id": "2",
        "locality": "in",
        "fromage": "3",
    }

    headers = {
        "X-RapidAPI-Key": "b27c3f14cbmsh8169570c0edccb8p1df44cjsnacf7b4e85524",
        "X-RapidAPI-Host": "indeed12.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    return JSONResponse(content=response.json())


@app.get("/job-detail/{job_id}")
def job_detail(job_id: str):
    url = "https://indeed12.p.rapidapi.com/job/693fb532641904d1"


    querystring = {"locality": "in"}

    headers = {
        "X-RapidAPI-Key": "b27c3f14cbmsh8169570c0edccb8p1df44cjsnacf7b4e85524",
        "X-RapidAPI-Host": "indeed12.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

    return JSONResponse(content=response.json())
