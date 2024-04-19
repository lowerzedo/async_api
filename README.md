# Project Title

Async server to communicate with WB APIs. It fetches data from /sales and /orders endpoints, saves them in Postrgres DB in AWS, creates report in Excel and finally sends it as a message in Telegram using tg bot.

## Getting Started

Since i didn't have access to WB API Keys, i had to improvise and created a dummy data refering to the WB documentation. It did the job and i was able to simulate whole process flow from A to Z.

### Prerequisites

In order for this code to work, you will need to:

- install dependecies that are listed in requirements.txt
- create .env file and add enviromental variables
  - more specifically:
    - DB_URL = "db_uri_here"
    - TELEGRAM_TOKEN='tg_token_here'
    - WB_API_KEY = "wildberries_api_key_here"

### Execution

Once all above mentioned are completed, you have two options to execute the code:

- with container
  docker build -t asyn_api .
  docker run -p 4000:80 asyn_api

- with python app/main.py
  activate virtualenv: source venv/bin/activate
  run: python app/main.py
