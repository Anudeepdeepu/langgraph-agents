from langgraph.graph import StateGraph,START,END
from typing import TypedDict
from typing_extensions import Annotated
import operator

#reducer
def my_choice(existing,new):
    return new


class State(TypedDict):
    message: Annotated[list[str],operator.add]
    #message:Annotated[list[str] ,my_choice]
    student:str

def message_from_friend(state :State):
    return{"message" : ["you will win"]}


def message_from_enemy(state: State):
    return{"message" :["you will not succeed"]}

graph = StateGraph(State)
graph.add_node("friend" , message_from_friend)
graph.add_node("enemy" , message_from_enemy)

graph.add_edge(START ,"friend")
graph.add_edge(START ,"enemy")

graph.add_edge("friend" ,END)
graph.add_edge("enemy" ,END)

compiled_graph = graph.compile()


if __name__ == "__main__":
    result = compiled_graph.invoke(State(student="anupam"))
    print(result)

"""

fan-out means one point in the graph branches out to multiple nodes,
 allowing those nodes to execute in parallel when the framework/runtime supports parallel execution.
                 ┌──→ Finance ──┐
                 │              │
START ── FAN OUT ┼──→ Library ──┼──→ ...
                 │              │
                 └──→ Sports ───┘

                 
 

"""

