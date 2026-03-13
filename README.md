# Snap & Solve: The AI-Powered Visual Homework Tutor

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Running-green?logo=fastapi)
![Gemini](https://img.shields.io/badge/AI-Gemini%203.1_Flash_Lite-orange?logo=google)
![PyTorch](https://img.shields.io/badge/PyTorch-CUDA_GPU-red?logo=pytorch)
![Gradio](https://img.shields.io/badge/UI-Gradio_5-lightgrey?logo=gradio)

**Snap & Solve** is a single-agent AI system designed to help students understand their homework rather than just providing answers. By combining local computer vision (to filter relevant content) with cloud-based Generative AI (to explain concepts), it provides a privacy-focused, cost-effective, and interactive tutoring experience.

---

## Contributors

* **AJ Timothy O. Barbosa** = atobarbosa
* **Juan Miguel C. Ocampo** = JuanMiguelOcampo
* **John David M. Villota** = jdvillota

---

## Key Features

* **Interactive AI Tutor:** Powered by **Google Gemini 3.1 Flash-Lite**, acting as a conversational agent that remembers chat history and guides students step-by-step instead of just giving the final answer.
* **Modern Web UI:** Features a clean, browser-based chat interface built with **Gradio 5** for easy image uploading and interacting.
* **Local Vision Guardrails:** Uses a **PyTorch ResNet18** model locally to verify if an image is "Academic Material" (papers, documents, or digital screens) before sending it to the cloud, saving API costs and preventing misuse.
* **GPU-Accelerated OCR:** Integrated **EasyOCR** engine utilizing Nvidia CUDA to instantly extract complex handwritten or printed math text from images.

---

## Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **User Interface** | Gradio 5 | Interactive web-based chat frontend. |
| **Agent Controller** | Python 3.11 | The main logic orchestrating the pipeline. |
| **Vision Model** | PyTorch (ResNet18) | Local image classification (The "Guardrail"). |
| **Backend API** | FastAPI | Hosts the vision model for the agent to call. |
| **OCR Engine** | EasyOCR (CUDA) | GPU-accelerated text extraction. |
| **Reasoning** | Google Gen AI SDK | Gemini 3.1 for educational explanations. |
| **Package Manager** | `uv` | Fast Python package management. |

---

## Project Structure

```text
snap-and-solve/
├── server.py              # FastAPI Server (Hosts the PyTorch Guardrail)
├── ui.py                  # Gradio Web Interface (Entry Point)
├── agent_controller.py    # Main Agent Logic (Connects UI + Server + Tools)
├── ocr_tool.py            # EasyOCR wrapper optimized for math extraction
├── gemini_tool.py         # Google GenAI wrapper with Chat Session memory
├── client.py              # Legacy CLI Entry point (Backup)
├── requirements.txt       # Dependency list
├── .env                   # API Keys (Not committed to Git)
└── README.md              # Project Documentation

```

---

## Installation & Setup

### Prerequisites

* **Python 3.11** (Required for PyTorch CUDA compatibility).
* [uv](https://github.com/astral-sh/uv) (Recommended for lightning-fast installation).
* A Google Cloud API Key (for Gemini).
* *(Optional but recommended)* An Nvidia GPU for accelerated OCR.

### 1. Clone the Repository

```bash
git clone [https://github.com/YourUsername/snap-and-solve.git](https://github.com/YourUsername/snap-and-solve.git)
cd snap-and-solve

```

### 2. Install Dependencies

We use `uv` to build the environment and install the GPU-enabled PyTorch:

```bash
# 1. Create a Python 3.11 virtual environment
uv venv --python 3.11 .venv

# 2. Activate it (Windows)
.venv\Scripts\activate

# 3. Install PyTorch with CUDA 12.1 support
uv pip install torch torchvision --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)

# 4. Install remaining dependencies
uv pip install fastapi uvicorn python-multipart easyocr google-genai python-dotenv requests gradio

```

### 3. Configure Environment

Create a `.env` file in the root directory and add your Google API key:

```ini
GOOGLE_API_KEY=your_actual_api_key_here

```

---

## Usage Guide

This system uses a **Client-Server** architecture. You need two terminal windows running simultaneously.

### Terminal 1: Start the Vision Server

This runs the local PyTorch model that filters out non-academic images.

```bash
python server.py
# Wait for Output: Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000)

```

### Terminal 2: Launch the Web UI

This initializes the Agent and opens the frontend.

```bash
python ui.py
# Output: Running on local URL:  [http://127.0.0.1:7860](http://127.0.0.1:7860)

```

*Ctrl+Click the local URL to open the app in your browser!*

---

## Demo Scenario

**Input:** A user uploads a screenshot of a math problem: `8 ÷ 2 (2 + 2) = ?`

**Process Flow:**

1. **UI** passes the image to the `AgentController`.
2. **Agent** sends photo to local FastAPI server.
3. **Server** confirms: *"Class: Digital Screen (Valid Academic Document)"*.
4. **Agent** runs GPU EasyOCR: *"Detected text: 8 ÷ 2 (2 + 2) = ?"*.
5. **Agent** initializes a chat session with Gemini 3.1 Flash-Lite.

**Output (In the Web UI):**

```text
🤖 Tutor: Hello there! I see you uploaded an order of operations problem. 
Let's break this down step-by-step!

1. Identify operations within parentheses.
Why? The order of operations (PEMDAS/BODMAS) tells us to group those numbers first.

Can you tell me what you get when you solve the part inside the parentheses (2 + 2)?

🧑 You: 4

🤖 Tutor: Excellent! Now the equation looks like this: 8 ÷ 2 * 4. 
What do you think the next step is?

```

---

## License

This project is for educational purposes under the [MIT License](https://www.google.com/search?q=LICENSE).

