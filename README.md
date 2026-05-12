# Organizational Intelligence System

An AI-powered organizational memory and reasoning platform that ingests:

- meetings
- Slack discussions
- support tickets
- CRM data

and enables:

- semantic organizational search
- decision intelligence
- root cause analysis
- organizational reasoning

## Tech Stack

- FastAPI
- Gemini
- Sentence Transformers
- Qdrant
- Docker

## Run

### Install

pip install -r requirements.txt

### Start Qdrant

docker run -p 6333:6333 qdrant/qdrant

### Start Backend

uvicorn main:app --reload