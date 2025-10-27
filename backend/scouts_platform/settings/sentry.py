"""
Sentry initialization for Django project.

Reads configuration from environment variables:
- SENTRY_DSN
- SENTRY_ENVIRONMENT (default: development)
- SENTRY_TRACES_SAMPLE_RATE (default: 0.0)
- SENTRY_PROFILES_SAMPLE_RATE (default: 0.0)

This module is safe to import even when DSN is missing; initialization will be skipped.
"""

from __future__ import annotations

import os
from typing import Optional


def init_sentry() -> None:
    try:
        import sentry_sdk
        from sentry_sdk.integrations.django import DjangoIntegration
        from sentry_sdk.integrations.logging import LoggingIntegration
    except Exception:
        # sentry-sdk not installed; nothing to do
        return

    dsn: Optional[str] = os.getenv("SENTRY_DSN")
    if not dsn:
        return

    # Capture breadcrumbs from logging and send errors as events
    logging_integration = LoggingIntegration(
        level=None,  # capture breadcrumbs for all levels
        event_level=None,  # Sentry will capture Django exceptions by default
    )

    sentry_sdk.init(
        dsn=dsn,
        integrations=[DjangoIntegration(), logging_integration],
        traces_sample_rate=float(os.getenv("SENTRY_TRACES_SAMPLE_RATE", "0.0")),
        profiles_sample_rate=float(os.getenv("SENTRY_PROFILES_SAMPLE_RATE", "0.0")),
        environment=os.getenv("SENTRY_ENVIRONMENT", "development"),
        send_default_pii=False,
    )
