# This script will interact with 
# the running ollama server at 
# http://localhost:7869


from typing import ParamSpecArgs
import requests
import os
import optparse
import json


# CLI options and arguments
parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="filename",  
help="writ report to FILE", metavar="FILE")  
parser.add_option("-q", "--quiet",  
action="store_false", dest="verbose", default=True,
help="CLI LLM Query for zsh terminal syntax")

(options, args) = parser.parse_args()
USER_QUERY=args[0] # TODO: add check for args, safe exit or retry mechanism




def generate_output_command(userinput:str) -> str:
    #TODO: add HTTP code handling as needed (what do you do if 400? or 404? or 500?)
    #TODO: strip output of triple quotes if using llama3
    URL="http://localhost:7869"
    DATA={
        "model": "llama3:8b",
        "prompt": f"You are VibeCLI, a helpful and precise assistant for command-line users. \n\nInput: What is the correct shell syntax to: {USER_QUERY}\n\nRespond with only the output of the command or the result of the request, no additional commentary. Format clearly. Respond with the output only. Limit to 5 lines maximum. No explanations, examples, or follow-up suggestions.\n\nOutput:",
        "stream": False
    }
 
    r = requests.post(
        url=f"{URL}/api/generate",
        data=json.dumps(DATA),
        headers={"content-type":"application/json"}, #: _HeadersMapping | None = ...,
        allow_redirects=True,
        )
    # http code checking goes here
    if r.status_code == 200:
        response = r.json()["response"]
        response = clean_response_string(response)
        print(response)
        return response 

    
    else:
        # What should we do I wonder, in event of error? exit code to indicate it
        print(f"Ollama HTTP Status Code: {r.status_code}")
        exit(1)


def clean_response_string(response_string:str) -> str:

    # remove backtick blocks
    clean_string = response_string.strip("```")
    return clean_string



if __name__ == "__main__":
    output_command = generate_output_command(USER_QUERY)
    








