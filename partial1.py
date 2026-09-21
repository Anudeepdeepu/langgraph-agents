from langgraph.graph import StateGraph, START, END
from typing import TypedDict


# 1. Define what our State should contain
class State(TypedDict):
    fin_dept: bool
    lib_dept: bool
    sports_dept: bool
    student_id: str


# 2. Financial department node
def financial_department_check(state: State):
    return {
        "fin_dept": True
    }


# 3. Library department node
def library_department_check(state: State):
    return {
        "lib_dept": True
    }


# 4. Sports department node
def sports_department_check(state: State):
    return {
        "sports_dept": True
    }


# 5. Create the graph
graph = StateGraph(State)


# 6. Add nodes
graph.add_node("fin", financial_department_check)
graph.add_node("lib", library_department_check)
graph.add_node("sports", sports_department_check)


# 7. Connect nodes sequentially
graph.add_edge(START, "fin")
graph.add_edge("fin", "lib")
graph.add_edge("lib", "sports")
graph.add_edge("sports", END)


# 8. Compile the graph
compiled_graph = graph.compile()


# 9. Run the graph
if __name__ == "__main__":

    result = compiled_graph.invoke({
        "student_id": "10013",
        "fin_dept": False,
        "lib_dept": False,
        "sports_dept": False
    })

    print(result)