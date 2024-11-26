from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from rquestpath.catch_request_data import router as official_request
from testpath.apitest import router as test_request
from testpath.sampletest import router as sample_request

app = FastAPI()

app.include_router(official_request)
app.include_router(test_request)
app.include_router(sample_request)

app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
