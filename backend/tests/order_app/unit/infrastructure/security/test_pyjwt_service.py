from uuid import UUID, uuid4

import jwt
import pytest
from freezegun import freeze_time
from order_app.domain.exceptions.token_errors import (
    InvalidTokenError,
    TokenExpiredError,
)
from order_app.infrastructure.security.pyjwt_service import PyJWTService


@freeze_time("2022-01-01")
def test_generate_token_success():
    secret_key = "test_secrect_key"
    algorithm = "HS256"
    expires_in = 3600
    py_jwt_service = PyJWTService(
        secret_key=secret_key, algorithm=algorithm, expires_in=expires_in
    )

    user_id = str(uuid4())
    role = "CUSTOMER"
    payload = {"sub": user_id, "role": role}

    token = py_jwt_service.generate_token(payload=payload, expires_in=3600)

    decoded_payload = jwt.decode(token, secret_key, algorithms=[algorithm])
    assert isinstance(token, str)
    assert len(token.split(".")) == 3
    assert decoded_payload == {
        **payload,
        "exp": 1640998800,
        "iat": 1640995200,
    }


def test_verify_token_expired():
    secret_key = "test_secrect_key"
    algorithm = "HS256"
    expires_in = 3600
    py_jwt_service = PyJWTService(
        secret_key=secret_key, algorithm=algorithm, expires_in=expires_in
    )

    user_id = str(uuid4())
    role = "CUSTOMER"
    payload = {"sub": user_id, "role": role}
    with freeze_time("2026-01-01 01:00"):
        token = py_jwt_service.generate_token(payload=payload, expires_in=expires_in)

    with freeze_time("2026-01-01 02:00:01"):
        with pytest.raises(TokenExpiredError):
            py_jwt_service.verify_token(token=token)


def test_verify_token_invalid():
    secret_key = "test_secrect_key"
    algorithm = "HS256"
    expires_in = 3600
    py_jwt_service = PyJWTService(
        secret_key=secret_key, algorithm=algorithm, expires_in=expires_in
    )

    user_id = str(uuid4())
    role = "CUSTOMER"
    payload = {"sub": user_id, "role": role}
    with freeze_time("2026-01-01 01:00"):
        valid_token = py_jwt_service.generate_token(
            payload=payload, expires_in=expires_in
        )
    tampered_signature_token = valid_token[:-1] + (
        "a" if valid_token[-1] != "a" else "b"
    )
    with freeze_time("2026-01-01 01:05"):
        with pytest.raises(InvalidTokenError):
            py_jwt_service.verify_token(token=tampered_signature_token)


def test_verify_token_success():
    secret_key = "test_secrect_key"
    algorithm = "HS256"
    expires_in = 3600
    py_jwt_service = PyJWTService(
        secret_key=secret_key, algorithm=algorithm, expires_in=expires_in
    )

    user_id = str(uuid4())
    role = "CUSTOMER"
    payload = {"sub": user_id, "role": role}
    with freeze_time("2026-01-01 01:00"):
        token = py_jwt_service.generate_token(payload=payload, expires_in=3600)

    with freeze_time("2026-01-01 01:00"):
        decoded_payload = py_jwt_service.verify_token(token)
    assert isinstance(token, str)
    assert len(token.split(".")) == 3
    assert decoded_payload == {
        **payload,
        "exp": 1767232800,
        "iat": 1767229200,
    }
