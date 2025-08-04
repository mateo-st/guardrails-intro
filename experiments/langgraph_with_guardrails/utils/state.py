from langgraph.graph import MessagesState


class AgentState(MessagesState):
    pass


class AgentGuardrailBeforeState(MessagesState):
    about_weather: bool


class AgentGuardrailAfterState(MessagesState):
    is_english: bool
