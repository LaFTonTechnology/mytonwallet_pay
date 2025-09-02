from datetime import datetime, timedelta
from mytonwallet_pay import MTWPay
from mytonwallet_pay.types import Invoice


async def main() -> None:
    mtw_pay = MTWPay(token="TOKEN", project_id=0)

    inv_ton: Invoice = await mtw_pay.create_invoice(
        amount=1000000000,
        coin="TON",
        validUntil=datetime.now()+timedelta(minutes=5),
        description="order-12345"
    )
    print(inv_ton.invoiceLink)  # Счёт на 1 TON

    inv_usdt: Invoice = await mtw_pay.create_invoice(
        amount=1000000,
        coin="TON",
        validUntil=datetime.now()+timedelta(minutes=5),
        description="order-12345"
    )
    print(inv_usdt.invoiceLink)  # Счёт на 1 USDT


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
