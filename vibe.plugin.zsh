#
#
VIBE_PYTHON="${VIBE_PYTHON:-python3}"
VIBE_SCRIPT="${VIBE_SCRIPT:-$HOME/.oh-my-zsh/custom/plugins/vibecli/vibe.py}"
#
#
function vibe() {
  # Capture the user's request from the current buffer
  local request="$BUFFER"
  # Clear the buffer 

  # Run your Python script with the request
local cmd=$("$VIBE_PYTHON" "$VIBE_SCRIPT" "$request" 2>/dev/null)

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
