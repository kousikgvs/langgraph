# LangGraph Human-in-the-Loop Example

This folder contains a simple Human-in-the-Loop, or HITL, example using LangGraph.

Human-in-the-Loop means the graph does not fully finish by itself. It pauses at an important step, asks a human to review something, and then continues after the human gives feedback.

## What the notebook does

The notebook builds a small review workflow:

1. The user enters a topic.
2. The LLM writes a first draft about that topic.
3. The graph pauses and shows the draft to the human.
4. The human types feedback for the draft.
5. The graph resumes and asks the LLM to improve the draft using that feedback.
6. The final improved answer is printed.

This is useful when you want a human to approve, edit, or guide the model before the workflow continues.

## Main files

`9_Langgraph_hitl.ipynb` is the notebook with the full HITL example.

The notebook uses:

- `StateGraph` to create the workflow.
- `interrupt()` to pause the graph for human review.
- `Command(resume=...)` to continue the graph after feedback is entered.
- `InMemorySaver` to save the graph state while it is paused.
- `ChatGroq` as the LLM.

## Graph state

The graph uses this state:

```python
class ReviewState(TypedDict):
	topic: str
	draft: str
	human_feedback: str
	final_answer: str
```

Each field has a simple job:

- `topic`: the topic entered by the user.
- `draft`: the first answer written by the LLM.
- `human_feedback`: the feedback typed by the human.
- `final_answer`: the improved answer after the human feedback is used.

## Graph nodes

The notebook has three graph nodes:

- `write_draft`: creates the first draft.
- `get_human_feedback`: pauses the graph and waits for human feedback.
- `revise_with_feedback`: creates the final answer using the draft and feedback.

The flow is:

```text
START -> write_draft -> get_human_feedback -> revise_with_feedback -> END
```

## How the pause works

The pause happens here:

```python
feedback = interrupt(
	{
		"draft": state["draft"],
		"question": "Review this draft. What should be changed before finalizing it?",
	}
)
```

When LangGraph reaches this line, it stops and returns the draft to the user.

Then the notebook asks:

```text
Enter your feedback for the draft:
```

After the user types feedback, the graph resumes with:

```python
Command(resume=human_feedback)
```

That feedback becomes part of the graph state and is used by the final node.

## How to run

Open `9_Langgraph_hitl.ipynb` and run the cells from top to bottom.

When asked for a topic, enter something like:

```text
why sleep is important for learning
```

After the first draft is shown, enter feedback like:

```text
Make it shorter and include one practical tip.
```

The notebook will then print the final answer after applying your feedback.

## Important note

The checkpoint saver is `InMemorySaver`, so the paused state is only stored in memory while the Python process is running. If the kernel restarts, the saved state is lost.
