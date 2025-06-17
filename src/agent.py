class Agent:
    def __init__(self, goals: List[Goal], agent_language: AgentLanguage, action_registry : ActionRegistry, generate_response : Callable[[Prompt], str], environment : Environment):
        """
        Initialize the agent with its core GAME Components
        """
        self.goals = goals
        self.generate_response = generate_response
        self.actions = action_registry,
        self.environment = environment,
        self.agent_language = agent_language
