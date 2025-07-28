# This script will interact with 
# the running ollama server at 
# http://localhost:7869


import requests
import optparse
import json


# CLI options and arguments
parser = optparse.OptionParser()
help="LLM Query for zsh terminal syntax"

(options, args) = parser.parse_args()
USER_QUERY=args[0] # TODO: add check for args, safe exit or retry mechanism




def generate_output_command(userinput:str) -> str:
    #TODO: add HTTP code handling as needed (what do you do if 400? or 404? or 500?)
    #TODO: strip output of triple quotes if using llama3
    URL="http://localhost:7869"
    DATA={
        "model": "llama3:8b",
        "prompt": f"""You are VibeCLI, a helpful and precise assistant for command-line users.

        Task: You will be given a string from the user who would like returned
        a shell command matching their description, generate the correct shell command to accomplish the task. 
        Provide the command first, then give a brief explanation of each part of the command.
   
        Format your response like this:
        Command:
        <the full command>

        Explanation (don't include this line, I am just labelling the below content):
        <brief explanation of the command and its flags, one line per part, commented out as the user will be running your returned command.>
        
       
        Example User Request:
        "list all file in the directory tmp"

        Example Command You Respond With:
        ls -lah /tmp

        Example Explanation You might provide, commented out:
        ls: list directory contents
        -l: use a long listing format
        -a: include hidden files
        -h: human-readable file sizes
        /tmp: target the /tmp directory

        Request:
        {USER_QUERY}""",
        "stream": False
    }
 
    r = requests.post(
        url=f"{URL}/api/generate",
        data=json.dumps(DATA),
        headers={"content-type":"application/json"},
        allow_redirects=True,
        )
    # http code checking goes here
    if r.status_code == 200:
        response = r.json()["response"]
        response = clean_response_string(response)
        print(response,end='')
        return response 

    
    else:
        # What should we do I wonder, in event of error? exit code to indicate it
        print(f"Ollama HTTP Status Code: {r.status_code}")
        exit(1)


def clean_response_string(response_string:str) -> str:
    '''
    Often the response string tends to include these    
    '''
    # strip new line characters
    response_string = response_string.strip()
    # replace backtick blocks
    response_string = response_string.replace("```","")
    # replace triple single quote blocks
    response_string = response_string.replace("'''","")
    # replace 'Command:' like starting phrases
    response_string = response_string.replace("Command:","")
    # replace 'Explanation:'
    cleaned_response = response_string.replace("Explanation:","")
    return cleaned_response

def check_for_sudo(cleaned_response:str) -> str:
    #TODO: implement better safeguards 
    if 'sudo' in cleaned_response.lower():
        cleaned_response+="""
        #WARNING: Prompt contains sudo, this command could cause system damage.
        """ 
    return cleaned_response

if __name__ == "__main__":
    output_command = generate_output_command(USER_QUERY)
    








