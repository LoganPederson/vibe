function vibe() {
  # Capture the user's question from the current buffer
  local question="$BUFFER"

  # Optional: clear the current input line before running anything
  BUFFER=""

  # Run your Python script with the question
  local cmd=$(source ~/programming/vibe/env/bin/activate &&
              python ~/programming/vibe/vibe-cli.py "$question" &&
              deactivate)

  # Replace the prompt with the generated command
  LBUFFER+="$cmd"
}

# Register as a ZLE widget
zle -N vibe

# Bind pluss (+) 
bindkey '+' vibe
