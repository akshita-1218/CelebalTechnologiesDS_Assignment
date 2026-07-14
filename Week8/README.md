# Agentic AI Pipeline using LangGraph

## Overview

This project demonstrates a simple **Agentic AI Pipeline** built using **LangGraph** and Python.

The agent processes user queries through a stateful workflow and routes them to appropriate tools using conditional logic.

---

## Features

- Stateful Directed Graph
- Planner Node
- Router Node
- Calculator Tool
- Keyword Extraction Tool
- General Response
- Conditional Routing
- Retry Loop
- Logging
- Task Metrics
- Trajectory Evaluation

---

## Project Structure

```
Week8/
│── app.py
│── state.py
│── tools.py
│── logger.py
│── metrics.py
│── requirements.txt
│── README.md
│── agent.log
```

---

## Agent Workflow

```
             User Query
                  │
                  ▼
            Planner Node
                  │
                  ▼
             Router Node
          ┌───────┼────────┐
          │       │        │
          ▼       ▼        ▼
 Calculator  Keyword   General
    Node       Node      Node
          └───────┼────────┘
                  ▼
          Responder Node
                  │
                  ▼
             Final Output
```

---

## Concepts Demonstrated

### 1. Stateful Directed Graph

The agent maintains a shared state throughout execution using LangGraph.

### 2. Nodes & Edges

Each processing step is represented as a node connected through graph edges.

### 3. Conditional Routing

The router analyzes user intent and selects the correct tool.

### 4. Retry Loop

The calculator node retries failed operations before returning an error.

### 5. Single-Agent Architecture

A single agent performs multiple roles:

- Planner
- Router
- Tool Executor
- Responder

### 6. Tool Usage

Two tools are implemented:

- Calculator
- Keyword Extractor

### 7. Error Handling

Retry logic and exception handling improve robustness.

### 8. Trajectory Evaluation

Each visited node is logged in `agent.log`.

### 9. Metrics

The project tracks:

- Total Tasks
- Completed Tasks
- Tool Calls
- Completion Rate

---

## Example Usage

### Calculator

Input

```
calculate 20+10
```

Output

```
Answer: 30
```

---

### Keyword Extraction

Input

```
extract keywords from Artificial Intelligence is transforming healthcare
```

Output

```
Artificial, Intelligence, healthcare, transforming
```

---

### General Query

Input

```
hello
```

Output

```
Hello! I can:
- Calculate mathematical expressions
- Extract keywords from text
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python app.py
```

---

## Author

Akshita Sharma