import pandas as pd

logs = pd.DataFrame(
    {
        "model": ["gpt-4", "gpt-3.5", "gpt-4", "claude-3"],
        "cost_usd": [0.02, 0.01, 0.015, 0.008],
    }
)


def get_model_cost(logs: pd.DataFrame, model_name: str) -> float:
    result = logs[logs["model"] == model_name]["cost_usd"].sum()
    return result


print(get_model_cost(logs, "gpt-4"))
