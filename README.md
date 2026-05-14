

# Organizational Intelligence System
https://github.com/user-attachments/assets/3acded88-b844-43dc-9d1e-16716c8673ee


https://company-brain-kappa.vercel.app/

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
- Groq
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
