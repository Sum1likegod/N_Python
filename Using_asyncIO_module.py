import asyncio as ay


async def funct():
    print("this is the trial for the async module")


async def main():
    # await funct()
    taski = ay.create_task(funct())


ay.run(main())
