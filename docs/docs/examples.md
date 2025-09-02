# Usage Examples
Готовые примеры использования <b>mtwpay</b> с асинхронным клиентом.

### Инициализация
```python
from mytonwallet_pay import MTWPay

mtw_pay = MTWPay(token="YOUR_API_TOKEN", project_id=0)
```
<br><br>


### Создание счёта ```create_invoice```
```python
from datetime import datetime, timedelta
from mytonwallet_pay.types import Invoice

async def main() -> None:
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
```

### Получение счетов ```get_invoices``` и ```get_invoice```
```python
from mytonwallet_pay.types import Invoice

async def main() -> None:
    invoices: list[Invoice] = await mtw_pay.get_invoices(limit=100)
    print(invoices)  # 100 последних счётов

    invoice: Invoice = await mtw_pay.get_invoice(id=1000)
    print(invoice)  # Счёт ID с 1000

```


### Получение информации о проекта ```get_project```
```python
from mytonwallet_pay.types import Project

async def main() -> None:
    project: Project = await mtw_pay.get_me()
    print(project)  # Проект
```
