from typing import TypedDict, List


class AgentState(TypedDict):
    """
    Shared state that flows through every node
    in the LangGraph pipeline.
    """

    query: str
    intent: str
    tool_output: str
    final_response: str

    trajectory: List[str]

    retries: int