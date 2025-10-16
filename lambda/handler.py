import json
import os
import logging
from datetime import datetime, timezone

import sqlalchemy as sa

from auth import get_ebay_app_token
from fetch import fetch_all

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def _make_engine():
    url = os.environ["DATABASE_URL"].replace("postgres://", "postgresql://")
    return sa.create_engine(url, pool_pre_ping=True, future=True)

def lambda_handler(event, context):
    # Use envs to push access eBay API. 
    token = get_ebay_app_token()
    api_token = token.get("access_token")

    # Get the items from scraping (*define fetch_all first)
    items = fetch_all(api_token)
    count = len(items)

    # Check connection to DB
    engine = _make_engine()
    ok = False
    with engine.connect() as conn:
        res = conn.execute(sa.text("SELECT 1")).scalar_one()
        ok = (res == 1)

    body = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fetched": count,
        "db_connect_ok": ok,
        "note": "SQL - (in progress); no data written yet.",
    }
    logger.info("Run summary: %s", body)

    return {
        "statusCode": 200,
        "body": json.dumps(body),
    }
