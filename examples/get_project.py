from mytonwallet_pay import MTWPay
from mytonwallet_pay.types import Project


async def main() -> None:
    mtw_pay = MTWPay(token="TOKEN", project_id=0)

    project: Project = await mtw_pay.get_me()
    print(project)  # Проект


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
