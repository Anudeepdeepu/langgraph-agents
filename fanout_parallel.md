                 ┌──→ Finance ──┐
                 │              │
START ── FAN OUT ┼──→ Library ──┼──→ ...
                 │              │
                 └──→ Sports ───┘


fan-out means one point in the graph branches out to multiple nodes, allowing those nodes to execute in parallel when the framework/runtime supports parallel execution.

Fan-out = split into multiple parallel branches.
Fan-in = bring multiple branches back together.