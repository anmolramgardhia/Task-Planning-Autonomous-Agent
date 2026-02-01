"""
Evaluator module for Task-Planning Autonomous Agent

Responsible for measuring progress and updating evaluation metrics.
"""


class Evaluator:
    def __init__(self, state: dict):
        self.state = state

    def evaluate_progress(self):
        tasks = self.state.get("tasks", [])
        completed = sum(1 for t in tasks if t["status"] == "completed")
        total = len(tasks)

        self.state["progress"]["tasks_completed"] = completed
        self.state["progress"]["tasks_pending"] = total - completed
        self.state["progress"]["completion_rate"] = (
            completed / total if total > 0 else 0.0
        )

        return {
            "completed": completed,
            "total": total,
            "completion_rate": self.state["progress"]["completion_rate"]
        }
