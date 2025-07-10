#
#
#
#
#
function vibe() {
  # Capture the user's request from the current buffer
  local request="$BUFFER"
  clear_line()  
  # Clear the buffer 

  # Add request to the history (so users can up arrow and see what they asked)
  print -s "$BUFFER"


  # Run your Python script with the request
  local cmd=$(source ~/programming/vibe/env/bin/activate &&
              python ~/programming/vibe/vibe.py "$request" &&
              deactivate)

  # Replace the prompt with the generated command
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
