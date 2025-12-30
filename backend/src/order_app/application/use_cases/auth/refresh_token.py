from dataclasses import dataclass

from jwt import InvalidTokenError
from order_app.application.common.result import Error, Result
from order_app.application.ports.auth_token_service import AuthTokenService
from order_app.application.repositories.auth.refresh_token_repository import (
    RefreshTokenRepository,
)
from order_app.domain.exceptions.token_errors import (
    RefreshTokenNotFoundError,
    TokenExpiredError,
)


@dataclass
class RefreshTokenRequestDto:
    refresh_token: str


@dataclass
class RefreshTokenResponseDto:
    access_token: str
    refresh_token: str


@dataclass
class RefreshTokenUseCase:
    jwt_service: AuthTokenService
    refresh_token_repository: RefreshTokenRepository

    def execute(
        self, request: RefreshTokenRequestDto
    ) -> Result[RefreshTokenResponseDto]:
        try:
            self.jwt_service.verify_token(request.refresh_token)
        except InvalidTokenError:
            return Result.error(Error.domain("Invalid refresh token"))
        except TokenExpiredError:
            return Result.error(Error.domain("Refresh token expired"))

        try:
            old_refresh_token = self.refresh_token_repository.get_by_token(
                request.refresh_token
            )
        except RefreshTokenNotFoundError:
            return Result.error(Error.domain("Refresh token not found"))

        if not old_refresh_token.is_valid():
            return Result.error(Error.domain("Refresh token expired"))

        return self.refresh_token_repository.revoke_token(old_refresh_token.id)
