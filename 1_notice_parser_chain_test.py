from chains.notice_extraction import NOTICE_PARSER_CHAIN
import example_emails
import os

response = NOTICE_PARSER_CHAIN.invoke({"message": example_emails.EMAILS[0]})
print(response)