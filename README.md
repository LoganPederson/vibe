# vibecli

**vibecli** is a terminal-first AI-powered assistant that transforms natural language into executable shell commands. Inspired by the need for faster problem-solving and hands-on learning, vibecli bridges the gap between remembering syntax and getting the job done. It helps users learn shell commands over time through guided practice and explanations.

## 🚀 Goals

- Translate user requests into shell commands using a locally-hosted LLM (initially via Ollama)
- Provide explainable output to help users understand what each command does
- Enable a "learning mode" where users practice applying commands and flags
- Sandbox risky commands and encourage safe experimentation

## 🔧 Features (Planned)

- 🔨 Natural language to command-line translation
- 📖 Explain the generated command in a pop-up or split terminal window
- 🧠 Learning mode with guided exercises and challenges
- 🛡️ Safety layer to detect destructive commands (e.g., `rm -rf /`)
- ⚙️ Configurable LLM backend (initially supporting Ollama)

## 🔌 Requirements

- Python 3.11+
- Ollama server running locally (`ollama serve`)
- Terminal emulator with support for multiplexing (e.g., tmux, or eventually vibecli's own wrapper)

## 🚧 Roadmap

| Phase | Milestone                                                      | Target Release |
|------|------------------------------------------------------------------|----------------|
| 0.1  | Local MVP: Prompt → Ollama → Shell command output                | Week 1         |
| 0.2  | Add explanation window / terminal split                          | Week 2         |
| 0.3  | Sandbox evaluation of risky commands                             | Week 3         |
| 0.4  | Learning mode w/ quizzes and practice                            | Week 4-5       |
| 0.5  | CLI polish, config files, installation script                    | Week 6         |
| 1.0  | Public release on GitHub / PyPI                                  | TBD            |
| 1.1+ | Support for other LLM providers, advanced sandboxing, extensions | TBD            |

## 🔍 Example Usage

```bash
#~>vibe "check journalctl for errors related to nvidia or docker"
#~(output)>journalctl
