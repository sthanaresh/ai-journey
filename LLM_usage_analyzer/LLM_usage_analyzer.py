# Let's build something directly relevant to your target job: an LLM Usage Analyzer — simulates analyzing API
# usage logs (tokens/cost tracking is a real thing every AI Engineer deals with — cost optimization is literally
# Phase 7 of your roadmap).

import pandas as pd


class LLMUsageAnalyzer:
    def __init__(self, logs: pd.DataFrame):
        self.logs = logs

    def total_cost(self) -> float:
        return self.logs["cost_usd"].sum()

    def average_tokens(self) -> float:
        return self.logs["tokens_used"].mean()

    def most_expensive_call(self) -> str:
        # return the "prompt" value with the highest cost_usd
        index_max = self.logs["cost_usd"].idxmax()
        return self.logs.loc[index_max, "prompt"]

    def cost_by_model(self) -> pd.Series:
        # group by "model" column, sum cost_usd per model
        return self.logs.groupby("model")["cost_usd"].sum()


logs = pd.DataFrame(
    {
        "prompt": [
            "Summarize doc",
            "Translate text",
            "Generate code",
            "Answer question",
        ],
        "tokens_used": [450, 200, 890, 310],
        "cost_usd": [0.009, 0.004, 0.018, 0.006],
        "model": ["gpt-4", "gpt-3.5", "gpt-4", "gpt-3.5"],
    }
)

Analyzer = LLMUsageAnalyzer(logs)
print(f"Total Cost:{ Analyzer.total_cost()}")
print(f"Average Tokens:{Analyzer.average_tokens()}")
print(f"Most Expensive Call:{Analyzer.most_expensive_call()}")
print(f"Cost by Model:\n{Analyzer.cost_by_model()}")
