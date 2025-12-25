from fastapi import APIRouter

from order_app.infrastructure.web.fastapi.routes.user.register import (
    RegisterUserResponse,
    register_user,
)

router = APIRouter()

router.add_api_route(
    "/register",
    methods=["POST"],
    endpoint=register_user,
    response_model=RegisterUserResponse,
    status_code=201,
)
