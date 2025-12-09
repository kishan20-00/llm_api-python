# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BatchCancelResponse"]


class BatchCancelResponse(BaseModel):
    """The response schema returned when attempting to cancel a batch job."""

    batch_id: str
    """The batch ID"""

    message: str
    """Cancellation status message"""

    previous_status: str
    """The status before cancellation"""

    status: str
    """The new status of the batch"""

    task_cancellation_attempted: bool
    """Whether task cancellation was attempted"""
