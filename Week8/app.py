from langgraph.graph import StateGraph, END

from state import AgentState
from tools import calculator, keyword_extractor
from logger import log_step
from metrics import metrics


# ----------------------------
# Planner Node
# ----------------------------
def planner_node(state: AgentState):
    log_step("Planner Node")
    state["trajectory"].append("Planner")
    metrics.start_task()
    return state


# ----------------------------
# Router Node
# ----------------------------
def router_node(state: AgentState):
    log_step("Router Node")
    state["trajectory"].append("Router")

    query = state["query"].lower()

    if "calculate" in query or any(op in query for op in ["+", "-", "*", "/"]):
        state["intent"] = "calculator"

    elif "keyword" in query or "extract" in query:
        state["intent"] = "keywords"

    else:
        state["intent"] = "general"

    return state


# ----------------------------
# Calculator Node
# ----------------------------
def calculator_node(state: AgentState):
    log_step("Calculator Node")
    state["trajectory"].append("Calculator")
    metrics.tool_called()

    expression = state["query"].replace("calculate", "").strip()

    for _ in range(3):
        try:
            state["tool_output"] = calculator(expression)
            return state
        except Exception:
            state["retries"] += 1

    state["tool_output"] = "Calculation failed."
    return state


# ----------------------------
# Keyword Node
# ----------------------------
def keyword_node(state: AgentState):
    log_step("Keyword Node")
    state["trajectory"].append("Keyword")
    metrics.tool_called()

    text = (
        state["query"]
        .replace("extract", "")
        .replace("keywords", "")
        .replace("keyword", "")
        .strip()
    )

    state["tool_output"] = keyword_extractor(text)

    return state


# ----------------------------
# General Node
# ----------------------------
def general_node(state: AgentState):
    log_step("General Node")
    state["trajectory"].append("General")

    state["tool_output"] = (
        "Hello! I can:\n"
        "- Calculate mathematical expressions\n"
        "- Extract keywords from text"
    )

    return state


# ----------------------------
# Response Node
# ----------------------------
def responder_node(state: AgentState):
    log_step("Responder Node")
    state["trajectory"].append("Responder")

    state["final_response"] = state["tool_output"]

    metrics.complete_task()

    return state


# ----------------------------
# Conditional Routing
# ----------------------------
def route(state: AgentState):
    return state["intent"]


# ----------------------------
# Build Graph
# ----------------------------
builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("router", router_node)
builder.add_node("calculator", calculator_node)
builder.add_node("keywords", keyword_node)
builder.add_node("general", general_node)
builder.add_node("responder", responder_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "router")

builder.add_conditional_edges(
    "router",
    route,
    {
        "calculator": "calculator",
        "keywords": "keywords",
        "general": "general",
    },
)

builder.add_edge("calculator", "responder")
builder.add_edge("keywords", "responder")
builder.add_edge("general", "responder")
builder.add_edge("responder", END)

graph = builder.compile()


# ----------------------------
# Main Program
# ----------------------------
if __name__ == "__main__":

    print("=" * 50)
    print("      Agentic AI Pipeline")
    print("=" * 50)
    print("Type 'exit' to quit.")

    while True:

        query = input("\nEnter your query: ")

        if query.lower() == "exit":
            break

        state = {
            "query": query,
            "intent": "",
            "tool_output": "",
            "final_response": "",
            "trajectory": [],
            "retries": 0,
        }

        result = graph.invoke(state)

        print("\nResponse:")
        print(result["final_response"])

        print("\nTrajectory:")
        print(" -> ".join(result["trajectory"]))

        metrics.report()