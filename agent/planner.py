"""
Planner module for Task-Planning Autonomous Agent

Responsible for selecting and updating tasks based on simple rules.
"""

import time


class Planner:
    def __init__(self, state: dict):
        self.state = state

    def complete_next_task(self):
        tasks = self.state.get("tasks", [])

        for task in tasks:
            if task["status"] == "pending":
                task["status"] = "completed"
                task["completion_date"] = time.strftime("%Y-%m-%d")
                return task

        return None
