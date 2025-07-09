vibe

vibe is a Zsh plugin that helps you generate, learn, and safely execute shell commands using natural language queries and a locally hosted LLM (such as Ollama). Designed to bridge the gap between “what do I want to do?” and “how do I write that command?”, vibe makes your terminal faster, smarter, and more educational.

🚀 Features

🔨 Natural language → shell command translation using a local Ollama model.

📖 Explain what the generated command does.

🧠 Learning mode: practice exercises to help you memorize and apply commands.

🛡️ Safety checks for risky commands (rm -rf /, etc.).

⚙️ Built as an Oh My Zsh plugin for seamless shell integration.

🎛️ Plans for multiplexed output (e.g., explanation and command in split panes).

🔧 Installation

1. Clone the plugin into your custom plugins directory:

git clone git@github-vibe:LoganPederson/vibe.git ~/.oh-my-zsh/custom/plugins/vibe

2. Enable it in your .zshrc:

# Example
plugins=(git ssh-agent fzf-tab vibe)

3. Reload your shell:

source ~/.zshrc

🔌 Requirements

Zsh 5.8+ with Oh My Zsh

Python 3.11+

Running Ollama server (ollama serve)

Optional: tmux or another terminal multiplexer for advanced modes

🛠️ Usage

🔍 Basic Use

Type your natural language query directly into your shell prompt and press the bound key (e.g., Shift + +) to trigger vibe. The contents of your prompt will be passed to the LLM and replaced with the generated command.

Example workflow:

Type your request in your prompt (e.g., list all files larger than 1GB in the /var directory).

Press your configured keybind.

vibe replaces the prompt buffer with the generated command.

You review and manually execute it.

🧠 Learning Mode (Planned)

Learning mode will:

Explain each flag in the generated command.

Give you guided practice writing the command from scratch.

Quiz you on similar command structures.

📅 Roadmap

Phase

Milestone

Target

0.1

Local MVP: natural language → command

Done

0.2

Add inline explanations in split terminal panes

WIP

0.3

Sandbox execution for risky commands

TBD

0.4

Learning mode with quizzes and guided exercises

TBD

0.5

CLI polish, config files, installation script

TBD

1.0

Public release on GitHub / Oh My Zsh registry

TBD

1.1+

Additional LLM backends, advanced sandboxing, extensibility

TBD

⚙️ Example Workflow

# Step 1: Type a request into your shell:
list all open TCP ports

# Step 2: Press your keybind (e.g., Shift + +)

# Step 3: vibe replaces the line with:
lsof -iTCP -sTCP:LISTEN -P -n

# Step 4: You confirm and run the command.

🔐 Security Note

vibe does not automatically run commands.It inserts the generated command into your shell prompt for review and manual execution.

Future versions will detect and sandbox potentially destructive commands.

📂 Project Goals

Help intermediate users level up their shell skills.

Accelerate repetitive or hard-to-remember command usage.

Create an approachable way to learn shell tools and options.

🤝 Contributing

PRs and ideas are welcome! Future plans include adding test coverage, plugin documentation, and support for other shells.

ℹ️ Possible Future CLI Support

We may eventually add a CLI interface to vibe that simply prints the generated command to stdout. This could be paired with a Vim-friendly keybind to yank the previous output lines. For now, focus is on Zsh widget integration where the shell buffer can be directly updated.
