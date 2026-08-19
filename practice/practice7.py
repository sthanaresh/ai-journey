# Write an async function fetch_prompt_response(prompt: str, delay: int) -> str
# that simulates calling an LLM API — it should await asyncio.sleep(delay) then
# return f"Response to: {prompt}". Then write a main() that uses asyncio.gather
# to call it for 3 different prompts concurrently, each with a different delay
# (e.g. 1, 2, 3 seconds), and prints all 3 results.


import asyncio


async def fetch_prompt_response(prompt: str, delay: int) -> str:
    print(f"Sending Prompt: {prompt}")
    await asyncio.sleep(delay)
    return f"Response to: {prompt}"


async def main():
    results = await asyncio.gather(
        fetch_prompt_response("What is AI?", 1),
        fetch_prompt_response("What is API?", 2),
        fetch_prompt_response("What is vector database?", 3),
    )

    print("\nResults:")
    for result in results:
        print(result)


asyncio.run(main())
