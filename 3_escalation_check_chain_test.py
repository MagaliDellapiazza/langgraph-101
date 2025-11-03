from chains.escalation_check import ESCALATION_CHECK_CHAIN

escalation_criteria = """There is currently water damage
or potential water damage reported"""

message = """Several cracks in the foundation have
been identified along with water leaks"""

response = ESCALATION_CHECK_CHAIN.invoke(
    {"message": message, "escalation_criteria": escalation_criteria}
)
print(response)


message = "The wheel chair ramps are too steep"

response = ESCALATION_CHECK_CHAIN.invoke(
    {"message": message, "escalation_criteria": escalation_criteria}
)
print(response)