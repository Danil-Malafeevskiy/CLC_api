from server.api.models.user import UserResponse


class TokenResponse(UserResponse):
    token: str
