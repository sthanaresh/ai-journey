# Synchronous function
import time


def sync_task(name: str, seconds: int) -> str:
    print(f"{name} starting...")
    time.sleep(seconds)
    print(f"{name} done!")
    return f"{name} result"


sync_task("Task A", 2)
sync_task("Task B", 2)

# Asynchronous function
import asyncio


async def async_task(name: str, seconds: int) -> str:
    print(f"{name} starting...")
    await asyncio.sleep(seconds)
    print(f"{name} done!")
    return f"{name} result"


async def main():
    await asyncio.gather(async_task("Task C", 2), async_task("Task D", 2))


asyncio.run(main())
