import traceback
from core.action import Action
import time
from typing import Any

class Environment:
    """
    Environment is the class that represents the environment in which the agent operates.
    It is responsible for executing actions and returning the result.
    """
    def execute_action(self, action : Action, args : dict) -> dict:
        try:
            result = self.action.execute(**args)
        except Exception as e:
            return {
                "tool_executed" : False,
                "error" : str(e),
                "traceback" : traceback.format_exc()
            }
    
    def format_result(self, result  : Any) -> dict:
        return {
            "tool_executed" : True,
            "result" : result
            timestamp : time.strftime("%Y-%m-%d %H:%M:%Sz")
        }