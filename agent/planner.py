"""
Planner module for Task-Planning Autonomous Agent

Responsible for selecting and updating tasks based on simple rules.
"""

from asyncio import tasks
import time


class Planner:
    def __init__(self, state: dict):
        self.state = state

    MAX_TASKS_PER_RUN = 2


def complete_tasks(self):
    tasks = self.state.get("tasks", [])
    pending_tasks = [t for t in tasks if t["status"] == "pending"]

    if not pending_tasks:
        return []

    # Sort pending tasks by priority (highest first)
    pending_tasks.sort(
        key=lambda t: t.get("priority", 0),
        reverse=True
    )

    completed = []

    for task in pending_tasks[:self.MAX_TASKS_PER_RUN]:
        task["status"] = "completed"
        task["completion_date"] = time.strftime("%Y-%m-%d")
        completed.append(task)

    return completed


