from fastapi import HTTPException
from fastapi.routing import APIRoute



class APIException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)

    def to_dict(self):
        return {"detail": self.detail}

def generate_sitemap(app):
    links = []
    for route in app.routes:
        if isinstance(route, APIRoute):
            path = route.path
            if "/admin" not in path:
                links.append(path)
    return links

