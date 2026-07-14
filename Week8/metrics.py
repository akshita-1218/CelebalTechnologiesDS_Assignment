class Metrics:
    """
    Tracks agent performance metrics.
    """

    def __init__(self):
        self.total_tasks = 0
        self.completed_tasks = 0
        self.tool_calls = 0

    def start_task(self):
        self.total_tasks += 1

    def complete_task(self):
        self.completed_tasks += 1

    def tool_called(self):
        self.tool_calls += 1

    def report(self):
        completion_rate = (
            (self.completed_tasks / self.total_tasks) * 100
            if self.total_tasks > 0
            else 0
        )

        print("\n========== AGENT METRICS ==========")
        print(f"Total Tasks      : {self.total_tasks}")
        print(f"Completed Tasks  : {self.completed_tasks}")
        print(f"Completion Rate  : {completion_rate:.2f}%")
        print(f"Tool Calls       : {self.tool_calls}")
        print("===================================\n")


# Global metrics object
metrics = Metrics()