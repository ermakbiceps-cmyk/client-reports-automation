import os
import requests


def get_direct_stats(token, client_login=None):

    url = "https://api.direct.yandex.com/json/v5/reports"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept-Language": "ru",
        "Content-Type": "application/json"
    }

    body = {
        "params": {
            "SelectionCriteria": {},
            "FieldNames": [
                "Date",
                "Impressions",
                "Clicks",
                "Ctr",
                "Cost"
            ],
            "ReportName": "Weekly Report",
            "ReportType": "CUSTOM_REPORT",
            "DateRangeType": "LAST_7_DAYS",
            "Format": "TSV",
            "IncludeVAT": "YES",
            "IncludeDiscount": "YES"
        }
    }

    if client_login:
        headers["Client-Login"] = client_login

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    return response.text
