"""
Agent Controller for Task-Planning Autonomous Agent

This file defines the main agent loop and coordinates
state loading, execution steps, and persistence.
"""

from agent import planner
from agent.planner import Planner
from asyncio import tasks
import json
import time
from pathlib import Path


class Agent:
    def __init__(self, state_path: str):
        self.state_path = Path(state_path)
        self.state = None

    # -----------------------------
    # State Management
    # -----------------------------
    def load_state(self):
        print("[Agent] Loading state...")
        with open(self.state_path, "r") as f:
            self.state = json.load(f)

    def save_state(self):
        print("[Agent] Saving state...")
        with open(self.state_path, "w") as f:
            json.dump(self.state, f, indent=2)

    def update_state(self):
        print("[Agent] Updating state")

        if "agent_runtime" not in self.state:
            self.state["agent_runtime"] = {"run_count": 0}

        self.state["agent_runtime"]["run_count"] += 1

        print(
        f"[Agent] Run count updated to {self.state['agent_runtime']['run_count']}"
    )


    # -----------------------------
    # Agent Loop Steps (STUBS)
    # -----------------------------
    def observe(self):
        print("[Agent] Observing current state")

    def plan(self):
        print("[Agent] Planning tasks")

    def act(self):
        print("[Agent] Acting on plan")

        planner = Planner(self.state)
        completed_task = planner.complete_next_task()

        if completed_task:
         print(f"[Agent] Completed task: {completed_task['title']}")
        else:
         print("[Agent] No pending tasks to complete")

         

    def evaluate(self):
        print("[Agent] Evaluating progress")

        tasks = self.state.get("tasks", [])
        completed = sum(1 for t in tasks if t["status"] == "completed")
        total = len(tasks)
        self.state["progress"]["tasks_completed"] = completed
        self.state["progress"]["tasks_pending"] = total - completed
        self.state["progress"]["completion_rate"] = (
            completed / total if total > 0 else 0.0
        )
        print(
        f"[Agent] Progress: {completed}/{total} tasks completed"
    )

        



    # -----------------------------
    # Main Loop
    # -----------------------------
    def run(self, iterations: int = 1):
        self.load_state()

        for step in range(iterations):
            print(f"\n[Agent] --- Iteration {step + 1} ---")
            self.observe()
            self.plan()
            self.act()
            self.evaluate()
            self.update_state()
            time.sleep(1)

        self.save_state()


if __name__ == "__main__":
    agent = Agent(state_path="state_schema.json")
    agent.run(iterations=1)
