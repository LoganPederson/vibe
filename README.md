# vibe

**vibe** is a Zsh plugin that transforms natural language into shell commands using a locally hosted LLM like Ollama. It helps you work faster, learn more efficiently, and remove the friction of remembering obscure syntax.

> “command to show logs of the ollama named docker container”  
> ⤷ becomes: `docker logs -f ollama`  
> ⤷ plus inline explanation of each flag.

---

## 🚀 Features

- 🧠 Natural language → shell command translation
- 💬 Inline explanation of each command and flag
- ✍️ Editable buffer before executing anything
- ⚙️ Configurable backend (e.g., model URL, Python path)
- 🔌 Lightweight Oh My Zsh plugin, no autoloads or wrappers

---

## 📸 Example

**You type:**
```shell
command to show logs of the ollama named docker container
```

**Then press your bound key (e.g., `Ctrl+X V`)**

**vibe replaces the line with:**
```shell
docker logs -f ollama
# docker: interacts with Docker containers
# logs: shows the logs for a specific container
# -f: follows the log output as it is updated
# ollama: specifies the name of the container to show logs for
```

---

## 🛠️ Installation

1. Clone into your Oh My Zsh custom plugins directory:

```bash
git clone https://github.com/yourusername/vibe.git ~/.oh-my-zsh/custom/plugins/vibe
```

2. Enable the plugin in your `.zshrc`:

```zsh
plugins=(git vibe)
```

3. Reload your shell:

```bash
source ~/.zshrc
```

---

## ⚙️ Configuration (optional)

You can customize the Python path, script location, and Ollama backend via environment variables:

| Variable         | Default                           | Description                             |
|------------------|-----------------------------------|-----------------------------------------|
| `VIBE_PYTHON`     | `python3`                         | Python executable to run `vibe.py`      |
| `VIBE_SCRIPT`     | Path to included `vibe.py`        | Script that sends the prompt to Ollama  |
| `OLLAMA_URL`      | `http://localhost:7869`           | Ollama server URL                       |
| `OLLAMA_MODEL`    | `llama3:8b`                       | Model to use for command generation     |

Set these in your `.zshrc` if needed:
```zsh
export OLLAMA_MODEL="mistral:instruct"
export VIBE_PYTHON="$HOME/.venvs/vibe/bin/python"
```

---

## 🔎 How It Works

- Captures your current Zsh prompt buffer
- Sends it to your locally hosted Ollama LLM
- Receives a shell command and inline explanation
- Replaces the prompt buffer for manual review and execution

---

## 🔐 Safety

vibe **does not execute anything automatically.**  
The generated command appears in your prompt — you run it when ready.

---

## 🤝 Contributing

Pull requests are welcome! Whether it’s:
- Adding new LLM models or backends
- Improving parsing or formatting
- Enhancing documentation

…let’s build a better terminal experience together.

---

## 📁 Project Goals

- Make terminals more approachable through natural language
- Help users actually learn the commands they run
- Stay fast, local, and privacy-respecting

---

## 🧪 Future Ideas

_(Not a roadmap — just things we’re thinking about)_

- Multiplexed output (e.g. command + explanation in split panes)
- Interactive learning mode
- Clipboard copy or direct Vim integration
