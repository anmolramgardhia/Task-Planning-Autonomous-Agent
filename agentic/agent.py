"""
Agent Controller for Task-Planning Autonomous Agent

This file defines the main agent loop and coordinates
state loading, execution steps, and persistence.
"""
from .memory import Memory
from unittest import result
from agent import evaluator
from .evaluator import Evaluator
from agent import planner
from .planner import Planner
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

    def average_difficulty(self):
        feedback = self.state.get("feedback", [])
        if not feedback:
            return 0

        return sum(
        f["self_reported_difficulty"] for f in feedback
    ) / len(feedback)


    def is_overloaded(self):
        pending = self.state["progress"]["tasks_pending"]
        avg_difficulty = self.average_difficulty()

        return pending > 5 or avg_difficulty >= 4

    
    def record_feedback(self, difficulty: int, comment: str = ""):
        feedback_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "comment": comment,
        "self_reported_difficulty": difficulty
    }

        self.state.setdefault("feedback", []).append(feedback_entry)



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
        completed_tasks = planner.complete_tasks()

        if completed_tasks:
            for task in completed_tasks:
                print(f"[Agent] Completed task: {task['title']}")

        # Simulated user feedback (temporary)
            self.record_feedback(
            difficulty=4,
            comment="Task felt challenging"
        )
        else:
            print("[Agent] No pending tasks to complete")




    def evaluate(self):
        print("[Agent] Evaluating progress")

        evaluator = Evaluator(self.state)
        result = evaluator.evaluate_progress()

        print(
         f"[Agent] Progress: {result['completed']}/{result['total']} tasks completed"
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
            if self.is_overloaded():
                print("[Agent] Overloaded — skipping task execution")
            else:
                self.act()

            self.evaluate()
            self.update_state()
            time.sleep(1)

        self.save_state()


if __name__ == "__main__":
    agent = Agent(state_path="state_schema.json")
    agent.run(iterations=1)