import asyncio


async def fetch_data(source: str, delay: int) -> str:
    await asyncio.sleep(delay)
    return f"Data from {source}"


async def main():
    result1 = fetch_data("API_A", 2)
    result2 = fetch_data("API_B", 2)

    print(await result1)
    print(await result2)


asyncio.run(main())
