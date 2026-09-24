from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Literal
#from typing_extensions import Annotated

class State(TypedDict):
    query :str
    response:str

def process_question(state :State)-> Literal["finance" ,"sports", "admin"]:
    if  'fee' in state["query"]:
        return "finance"
    elif 'sports' in state["query"] or 'game' in state["query"]:
        return "sports"
    else :
        return "admin"

def fin_response(state:State):
    return {"response" : "pay your fee"}

def admin_response(state:State):
    return{"response" :"come again another day "}

def sports_response(state:State):
    return{"response" :"the pt sir is gud at games"}

graph = StateGraph(State)

graph .add_node("fin" ,fin_response)
graph .add_node("adm", admin_response )
graph .add_node("sport", sports_response)

graph.add_conditional_edges(
    START,
    process_question, #DECISION
    {
        "finance" : "fin",
        "sports" : "sport",
        "admin" : "adm"
    }
)

graph.add_edge("fin" ,END)
graph.add_edge("adm" ,END)
graph.add_edge("sport",END)

compiled_graph = graph.compile()


if __name__ == "__main__":
    query = input("enter your question")
    response = compiled_graph.invoke({
        "query": query
    })
    print(response)