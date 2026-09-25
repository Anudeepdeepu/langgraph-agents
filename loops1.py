from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Literal
from typing_extensions import Annotated
import operator
import time

class State(TypedDict):
    show_idcard:str
    comments: Annotated[list[str],operator.add]
    retry_count: int
    approved : bool

def Security_Gate(state:State):
    time.sleep(1)
    return{
        "comments": ["entry is permitted if employee carries id card"],
        #"retry_count": state["retry_count"] + 1
    }

def office_entry_access(state:State):
    time.sleep(1)
    return{
        "comments": ["employee swipes the main door and enters inside campus"],
        "retry_count": state["retry_count"] + 1
    }

def server_entry_access(state:State):
    time.sleep(1)
    return{
        "comments": ["server room access granted"],
        #"approved": True
    }
def switch_access(state:State):
    time.sleep(1)
    return{
        "comments":["switch access granted"],
        "approved" :True
    }

def checkin_process(state:State)-> Literal["reswipe office entry" ,"switch access granted"]:
    time.sleep(3)
    if state["retry_count"]>=3:
        return "switch access granted"
    return "reswipe office entry"

graph = StateGraph(State)

graph.add_node("initial_access", Security_Gate)
graph.add_node("secondary_access", office_entry_access)
graph.add_node("prefinal_access", server_entry_access)
graph.add_node("final_access" ,switch_access)

graph.add_edge(START ,"initial_access")
graph.add_edge("initial_access","secondary_access")
graph.add_edge("secondary_access" ,"prefinal_access")
graph.add_conditional_edges(
    "prefinal_access",
     checkin_process,
    {
        "switch access granted": "final_access",
        "reswipe office entry": "secondary_access"

    }
)
#graph.add_edge("prefinal_access" ,"final_access")
graph.add_edge("final_access", END)

compiled_graph = graph.compile()

if __name__ == "__main__":
    employee_entry = input("kinldy show the idcard to security gaurd at get inside the campus :")
    response = compiled_graph.invoke({
        "show_idcard":employee_entry,
        "comments":[],
        "retry_count":0,
        "approved":False
    })
    #print(response)

    #lets simplify the output
    final_output = {
        "comments":[response["comments"][-1]],
        "retry_count":response["retry_count"],
        "approved":response["approved"]
    }
    print(final_output)

