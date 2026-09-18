# Python Experiments

A collection of exploratory Python scripts focused on algorithms, simulations, and data experiments. This repository serves as a personal playground for testing algorithmic logic like Monte Carlo Tree Search (MCTS), spatial/galaxy simulations, and general prototyping.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have **Python 3.10 or higher** installed on your system. You can check your version by running:
```bash
python --version
```

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd python-experiments
   ```

2. **Create a virtual environment:**
   This keeps your project dependencies isolated from your global system.
   ```bash
   # Windows
   python -m venv venv
   
   # macOS/Linux
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   # Windows (Command Prompt)
   venv\Scripts\activate.bat

   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1

   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies:**
   *(If you add external packages later, you can install them here)*
   ```bash
   pip install -r requirements.txt
   ```

---

## 📂 Project Structure

```text
Python Experiments/
├── .gitignore          # Tells Git to ignore the virtual environment and caches
├── README.md           # Project documentation
├── MCTS.py            # Monte Carlo Tree Search implementation
├── galaxy.py          # Galaxy / spatial simulation script
├── fi.py              # Financial / data analysis experiment
├── gr.py              # Graph theory or graphics experiment
└── new.py             # Sandbox file for fresh ideas
```

---

## 🛠️ Running the Scripts

You can run any of the experimental scripts individually from your terminal. Ensure your virtual environment is activated before running them:

```bash
python MCTS.py
python galaxy.py
```

---

## ⚙️ Best Practices Used Here

* **Environment Isolation:** Uses standard `venv` to prevent dependency conflicts.
* **Git Optimized:** A `.gitignore` file is included to ensure the thousands of auto-generated virtual environment files are not tracked or committed to GitHub.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
