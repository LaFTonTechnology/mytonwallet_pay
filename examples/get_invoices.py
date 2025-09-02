from mytonwallet_pay import MTWPay
from mytonwallet_pay.types.Invoice import Invoice


async def main() -> None:
    mtw_pay = MTWPay(token="TOKEN", project_id=0)

    invoices: list[Invoice] = await mtw_pay.get_invoices(limit=100)
    print(invoices)  # 100 последних счётов

    invoice: Invoice = await mtw_pay.get_invoice(id=1000)
    print(invoice)  # Счёт ID с 1000


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
