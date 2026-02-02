"""
Planner module for Task-Planning Autonomous Agent

Responsible for selecting and updating tasks based on simple rules.
"""

from asyncio import tasks
import time




class Planner:
    def __init__(self, state: dict , max_tasks_per_run: int):
        self.state = state
        self.max_tasks_per_run = max_tasks_per_run

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
        for task in pending_tasks[:self.max_tasks_per_run]:

            task["status"] = "completed"
            task["completed_at"] = time.time()
            completed.append(task)

        return completed

    



