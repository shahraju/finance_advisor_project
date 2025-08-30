\# Finance Advisor Project



This project is a simple finance advisor tool using a machine learning model.



\## Features

\- Train and save Gradient Boosting model

\- REST API built with FastAPI

\- `/predict` endpoint to get stock price predictions



\## How to Run

1\. Create and activate virtual environment (already done with `finance\_env`).

2\. Install dependencies:

&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt



uvicorn app\_fastapi:app --reload --port 8000



http://127.0.0.1:8000/docs

