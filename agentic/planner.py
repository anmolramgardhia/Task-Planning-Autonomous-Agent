"""
Planner module for Task-Planning Autonomous Agent

Responsible for selecting and updating tasks based on simple rules.
"""

import time

MAX_TASKS_PER_RUN = 2


class Planner:
    def __init__(self, state: dict):
        self.state = state

    def complete_tasks(self):
        tasks = self.state.get("tasks", [])
        pending_tasks = [t for t in tasks if t["status"] == "pending"]

        if not pending_tasks:
            return []

        pending_tasks.sort(
            key=lambda t: t.get("priority", 0),
            reverse=True
        )

        completed = []

        for task in pending_tasks[:MAX_TASKS_PER_RUN]:
            task["status"] = "completed"
            task["completion_date"] = time.strftime("%Y-%m-%d")
            completed.append(task)

        return completed



