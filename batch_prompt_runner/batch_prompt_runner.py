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


# Add error handling: if a prompt is an empty string "", _call_llm should raise a ValueError("Empty prompt not allowed")
# instead of calling sleep.
# In run_batch, use asyncio.gather(*tasks, return_exceptions=True) so one failing prompt doesn't crash the whole batch.
# Print results, showing successful responses normally and printing "Error: {e}" for any prompt that failed.

import asyncio


class BatchPromptRunner:
    def __init__(self, delay_per_prompt: int = 1):
        self.delay_per_prompt = delay_per_prompt

    async def _call_llm(self, prompt: str) -> str:
        if prompt == "":
            raise ValueError("Empty prompt not allowed")
        await asyncio.sleep(self.delay_per_prompt)
        return f"Response to: {prompt}"

    async def run_batch(self, prompts: list[str]) -> list[str]:
        tasks = [self._call_llm(prompt) for prompt in prompts]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results


runner = BatchPromptRunner(5)
outputs = asyncio.run(runner.run_batch(["Prompt 1", "", "Prompt 2", "", "Prompt 3"]))
print(outputs)
for output in outputs:
    if isinstance(output, Exception):
        print(f"Error: {output}")
    else:
        print(output)
