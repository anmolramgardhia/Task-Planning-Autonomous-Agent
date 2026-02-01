"""
Memory module for Task-Planning Autonomous Agent

Responsible for loading, saving, and updating agent state.
"""

import json
from pathlib import Path


class Memory:
    def __init__(self, state_path: str):
        self.state_path = Path(state_path)
        self.state = None

    def load(self):
        print("[Memory] Loading state...")
        with open(self.state_path, "r") as f:
            self.state = json.load(f)
        return self.state

    def save(self):
        print("[Memory] Saving state...")
        with open(self.state_path, "w") as f:
            json.dump(self.state, f, indent=2)

    def increment_run_count(self):
        if "agent_runtime" not in self.state:
            self.state["agent_runtime"] = {"run_count": 0}

        self.state["agent_runtime"]["run_count"] += 1

        print(
            f"[Memory] Run count updated to {self.state['agent_runtime']['run_count']}"
        )
