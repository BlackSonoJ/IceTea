SENSITIVE_HEADERS = {
    "authorization",
    "cookie",
    "x-forwarded-for",
    "referer",
    "user-agent",
}


def remove_headers(headers: dict) -> dict:
    return {
        key: value
        for key, value in headers.items()
        if key.lower() not in SENSITIVE_HEADERS
    }
