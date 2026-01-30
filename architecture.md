# Architecture: Task-Planning Autonomous Agent

## 1. Overview

This document describes the architecture of the Task-Planning Autonomous Agent.  
The system is designed as a **single, semi-autonomous, stateful agent** that operates through a continuous decision-making loop.

The architecture emphasizes:
- Clear separation of concerns
- Persistent state management
- Hybrid decision-making (rule-based + ML-assisted)
- Explainability and modularity

---

## 2. High-Level Architecture

The agent operates using a control loop composed of five stages:


Each iteration of the loop represents one decision cycle of the agent.

---

## 3. Core Components

### 3.1 Agent Controller (`agent.py`)
**Responsibility:**
- Orchestrates the full agent loop
- Coordinates interactions between modules
- Controls execution flow

The Agent Controller does not contain business logic.  
It delegates responsibility to specialized components.

---

### 3.2 Planner (`planner.py`)
**Responsibility:**
- Generates task plans from goals
- Updates existing plans based on feedback
- Prioritizes tasks using predicted difficulty

The planner uses both deterministic rules and ML outputs.

---

### 3.3 Evaluator (`evaluator.py`)
**Responsibility:**
- Measures user progress
- Scores task completion
- Detects stagnation or overload

Evaluation results directly influence future planning decisions.

---

### 3.4 Memory / State Manager (`memory.py`)
**Responsibility:**
- Stores agent state persistently
- Loads state on restart
- Acts as the single source of truth

State includes goals, tasks, completion history, and feedback.

---

### 3.5 Machine Learning Model (`ml_model.py`)
**Responsibility:**
- Predicts task difficulty
- Assists task prioritization

The ML model does not make autonomous decisions.  
It provides guidance to the planner.

---

## 4. State Management

The agent maintains a persistent state containing:
- User goal
- Planned tasks
- Completed tasks
- User feedback
- Performance metrics

State is updated after every loop iteration and saved to disk.

---

## 5. Decision-Making Strategy

The agent uses a **hybrid decision-making approach**:
- Rule-based logic ensures predictable behavior
- ML predictions introduce adaptability

This approach balances reliability with learning capability.

---

## 6. Autonomy Model

The agent is **semi-autonomous**:
- Users provide goals and feedback manually
- The agent autonomously plans, evaluates, and adapts

Human input remains part of the decision loop by design.

---

## 7. Constraints

- Single-agent system
- CPU-only execution
- Classical machine learning only
- Local execution without cloud dependencies

---

## 8. Future Extensions (Out of Scope)

- Multi-agent collaboration
- Reinforcement learning optimization
- LLM-based planning
- Real-time execution environments

