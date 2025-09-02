import datetime
from typing import Optional, Union
from pydantic import BaseModel, field_validator
from mytonwallet_pay.types.InvoiceStatus import InvoiceStatus


class Invoice(BaseModel):
    createdAt: datetime.datetime | str
    id: Optional[int]
    projectId: Optional[int]
    amount: Optional[int]
    coin: Optional[str]
    amountUsd: Optional[str]
    validUntil: Optional[Union[datetime.datetime, str]]
    description: Optional[str]
    status: Optional[Union[InvoiceStatus, str]] = None
    invoiceLink: Optional[str] = None
    paidByAddress:  Optional[str] = None
    txId:  Optional[str] = None

    @field_validator("createdAt", "validUntil", mode="before")
    @classmethod
    def parse_datetime(cls, v):
        """Преобразование строки в datetime object"""
        if isinstance(v, str):
            return datetime.datetime.fromisoformat(v)
        return v
