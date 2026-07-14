import logging

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def log_step(step: str):
    """
    Logs every node visited by the agent.
    """
    print(f"[LOG] {step}")
    logging.info(step)