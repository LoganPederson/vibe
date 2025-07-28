#
#
#
#
#
function vibe() {
  # Capture the user's request from the current buffer
  local request="$BUFFER"
  # Clear the buffer 

  # Run your Python script with the request
local cmd=$("$HOME/programming/vibe/env/bin/python" ~/programming/vibe/vibe.py "$request" 2>/dev/null)

  # Replace the prompt with the generated command
  BUFFER=""
  cursor=0
  zle reset-prompt
  BUFFER="$cmd"
}

function clear_line(){
  BUFFER=""
  cursor=0
  zle reset-prompt
}


# Register as a ZLE widget
zle -N vibe

# Bind pluss (+) 
bindkey '+' vibe
