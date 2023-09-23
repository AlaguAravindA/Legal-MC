"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as palm

import api_key as ak
def MCbot(prompt):
    palm.configure(api_key=ak.key)

    defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
    }
    context = ""
    examples = []
    messages = []
    messages.append(prompt)
    response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
    )
    return(f"{response.last}") # Response of the AI to your most recent request



