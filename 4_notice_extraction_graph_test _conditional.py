from graphs.notice_extraction_conditional import NOTICE_EXTRACTION_GRAPH
from example_emails import EMAILS

photos_directory = "photos/"

image_data = NOTICE_EXTRACTION_GRAPH.get_graph().draw_mermaid_png() # State graph visualization
with open(f"{photos_directory}/conditional_notice_extraction_graph.png", mode="wb") as f:
    f.write(image_data)

initial_state = {
    "notice_message": EMAILS[0],
    "notice_email_extract": None,
    "escalation_text_criteria": """There's a risk of fire or
    water damage at the site""",
    "escalation_dollar_criteria": 100_000,
    "requires_escalation": False,
    "escalation_emails": ["brog@abc.com", "bigceo@company.com"],
}

final_state = NOTICE_EXTRACTION_GRAPH.invoke(initial_state)

print(f' Extracted Email: {final_state["notice_email_extract"]}')
print("---"*20)
print(f' Requires Escalation: {final_state["requires_escalation"]}')