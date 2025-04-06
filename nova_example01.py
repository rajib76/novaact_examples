from getpass import getpass

from dotenv import load_dotenv

load_dotenv()

from nova_act import NovaAct

with NovaAct(starting_page="https://docs.smith.langchain.com/pricing/faq") as nova:
    act = nova.act("Please browse this page and return me the information on how billing works for langsmith",max_steps=100)

response = act.response
print("------Response--------")
print(response)
print("----------------------")

print("------Parsed Response--------")
parsed_response = act.parsed_response
print(parsed_response)
print("----------------------")

print("------metadata--------")
metadata = act.metadata
print("----------------------")

print("------prompt--------")
print(metadata.prompt)
print("----------------------")



