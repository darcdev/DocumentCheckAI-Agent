from dataclasses import dataclass

@dataclass(frozen=True)
class Goal:
    """
    A goal is a high-level objective that the agent is trying to achieve.
    """
    priority: int
    name: str
    description: str