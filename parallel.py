from langgraph.graph import StateGraph,START,END
from typing import TypedDict

class State(TypedDict):
    message :str
    student :str

def message_from_friend(state:State):
    return{"message" : "you will win"}

def message_from_enemy(state:State):
    return {"message" : "you will not succeed"}

graph = StateGraph(State)
graph.add_node("friend", message_from_friend)
graph.add_node("enemy" ,message_from_enemy)

graph.add_edge(START ,"friend")
graph.add_edge(START ,"enemy")

graph.add_edge("friend" ,END)
graph.add_edge("enemy" ,END)

compiled_graph = graph.compile()

if __name__ == "__main__":
    result = compiled_graph.invoke(State(student="anupam"))
    print(result)

"""
error 

  File "F:\agents\langraph-agents\.venv\Lib\site-packages\langgraph\channels\last_value.py", line 64, in update
    raise InvalidUpdateError(msg)
langgraph.errors.InvalidUpdateError: At key 'message': Can receive only one value per step. Use an Annotated key to handle multiple values.
For troubleshooting, visit: https://docs.langchain.com/oss/python/langgraph/errors/INVALID_CONCURRENT_GRAPH_UPDATE

now lets understand one important aspect when parallel node executions happen updating 
the same fields in the state,the conflict arises.langgraph cannot make a choice thats what above error says 
as we gave similiar keys names in parallel execution

in parallel1.py we resolve this by implementing annotations /reducer

"""

