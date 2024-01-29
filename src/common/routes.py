class RouteTags:
    OPEN_API = "Open API"
    PROTECTED = "Protected"


class BaseRoutes:
    TAGS = [RouteTags.OPEN_API]
    HEALTH = "/health"


class AIQRoutes:
    TAGS = ["AIQ"]
    BASE_AIQ = "/aiq"
    IMAGES = f"{BASE_AIQ}/images"
