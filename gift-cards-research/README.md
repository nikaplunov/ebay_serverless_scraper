# Lambda & DB Connector - *Based on my gift cards research 

> Here you find the AWS Lambda function and database connectivity only.  
> **SQL — (in progress):** schema/migrations will be added later.

## What’s here?
- Minimal Lambda that:
  1. Requests an eBay OAuth app token (client credentials).
  2. Calls a placeholder `fetch_all()`. Default=provide demo result. Overall, require you to specify the category for scraping and determine the parameters of interest. 
  3. Verifies DB connectivity with `SELECT 1`. 

## Environment Variables
- `DATABASE_URL` — e.g. `postgresql://USER:PASSWORD@HOST:5432/DBNAME`
- `CLIENT_ID`, `CLIENT_SECRET` — eBay app credentials
- `EBAY_SCOPES` — default: `https://api.ebay.com/oauth/api_scope`

## Quickstart (Local)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r lambda/requirements.txt
cp .env.example .env
