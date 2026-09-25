from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Literal
from typing_extensions import Annotated
import operator
import time

class State(TypedDict):
    application :str
    comments: Annotated[list[str] ,operator.add]
    retry_count:int
    approved :bool

def application(state:State):
    time.sleep(1)
    return{
        "comments":["A :application looks fine"],
        "retry_count" :state["retry_count"] + 1

    }

def process(state:State):
    time.sleep(1)
    return{
        "comments":["B :application can proceed further to next process"]
    }

def final_approval(state:State):
    time.sleep(1)
    return{
        "comments":["c: sucessfully Approved"],
        "approved":True
    }

def conditional_access_process(state:State)->Literal["reapply the application" ,"go to finalised platform"]:
    time.sleep(2)
    if state["retry_count"]>= 4:
        return "go to finalised platform"
    return "reapply the application"

graph = StateGraph(State)

graph.add_node("App", application)
graph.add_node("2nd_stage" ,process)
graph.add_node("final_approval_stage" ,final_approval)

graph.add_edge(START ,"App")
graph.add_edge("App" , "2nd_stage")
#graph.add_edge("2nd_stage" ,"final_approval_stage")
graph.add_conditional_edges(
    "2nd_stage",
    conditional_access_process,
    {
        "reapply the application" : "App",
        "go to finalised platform" :"final_approval_stage"
    }

)
graph.add_edge("final_approval_stage" ,END)
compiled_graph =graph.compile ()

if __name__ == "__main__":
    query = input ("enter your application name ")
    response = compiled_graph.invoke({
      "application" :query,
      "comments" : [],
      "retry_count" :0,
      "approved" :False

 })
    print(response)