# BatchPromptRunner — simulates sending multiple prompts to an LLM concurrently (a simplified version of what you'd build in a real RAG or chatbot batch-processing system)

# class BatchPromptRunner:
#     def __init__(self, delay_per_prompt: int = 1):
#         # store the simulated delay
#         ...

#     async def _call_llm(self, prompt: str) -> str:
#         # simulate an LLM call: await sleep, then return f"Response to: {prompt}"
#         ...

#     async def run_batch(self, prompts: list[str]) -> list[str]:
#         # use asyncio.gather to call _call_llm for ALL prompts concurrently
#         # return the list of results, in the same order as input prompts
#         ...


import asyncio


class BatchPromptRunner:
    def __init__(self, delay_per_prompt: int = 1):
        self.delay_per_prompt = delay_per_prompt

    async def _call_llm(self, prompt: str) -> str:
        await asyncio.sleep(self.delay_per_prompt)
        return f"Response to: {prompt}"

    async def run_batch(self, prompts: list[str]) -> list[str]:
        tasks = [self._call_llm(prompt) for prompt in prompts]
        results = await asyncio.gather(*tasks)
        return results


runner = BatchPromptRunner(5)
output = asyncio.run(runner.run_batch(["Prompt 1", "Prompt 2", "Prompt 3"]))
print(output)
