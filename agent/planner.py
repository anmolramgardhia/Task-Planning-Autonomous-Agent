"""
Planner module for Task-Planning Autonomous Agent

Responsible for selecting and updating tasks based on simple rules.
"""

from asyncio import tasks
import time


class Planner:
    def __init__(self, state: dict):
        self.state = state

    def complete_next_task(self):
        tasks = self.state.get("tasks", [])

        pending_tasks = [t for t in tasks if t["status"] == "pending"]

        if not pending_tasks:
            return None

    # Select highest-priority task
        task_to_complete = max(
            pending_tasks, key=lambda t: t.get("priority", 0)
    )

        task_to_complete["status"] = "completed"
        task_to_complete["completion_date"] = time.strftime("%Y-%m-%d")

        return task_to_complete

