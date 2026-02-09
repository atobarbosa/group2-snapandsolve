# Snap & Solve: The AI-Powered Visual Homework Tutor

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Running-green?logo=fastapi)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.5-orange?logo=google)
![PyTorch](https://img.shields.io/badge/PyTorch-ResNet18-red?logo=pytorch)

**Snap & Solve** is a single-agent AI system designed to help students understand their homework rather than just providing answers. By combining local computer vision (to filter relevant content) with cloud-based Generative AI (to explain concepts), it provides a privacy-focused, cost-effective tutoring experience.

---

## Key Features

* **Local Guardrails:** Uses a quantized **PyTorch ResNet18** model locally to verify if an image is "Academic Material" (Document/Paper) before sending it to the cloud.
* **Optical Character Recognition:** Integrated **EasyOCR** engine to extract handwritten or printed text from images.
* **One-Shot Tutoring:** Powered by **Google Gemini 2.5 Flash-Lite**, acting as a "Tutor Agent" that solves problems step-by-step.
* **Lightweight Architecture:** Runs entirely on standard hardware (CPU-optimized) without requiring Admin privileges.

---

## Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Agent Controller** | Python 3.12 | The main logic orchestrating the tools. |
| **Vision Model** | PyTorch (ResNet18) | Local image classification (The "Guardrail"). |
| **Backend API** | FastAPI | Hosts the vision model for the agent to call. |
| **OCR Engine** | EasyOCR | Extracts text from validated images. |
| **Reasoning** | Google Gen AI SDK | Generates educational explanations. |
| **Package Manager** | `uv` | Fast Python package management (No Admin needed). |

---

## Project Structure

```text
snap-and-solve/
├── server.py                # FastAPI Server (Hosts the PyTorch Model)
├── client.py                # CLI Entry point for the User
├── agent_controller.py      # Main Agent Logic (Connects OCR + Server + Gemini)
├── resnet18_quantized.pt    # Pre-trained local model file
├── requirements.txt         # Dependency list
├── .env                     # API Keys (Not committed to Git)
└── README.md                # Project Documentation

```

---

## Installation & Setup

### Prerequisites

* Python 3.10 or higher.
* [uv](https://github.com/astral-sh/uv) (Recommended for restricted environments) or `pip`.
* A Google Cloud API Key (for Gemini).

### 1. Clone the Repository

```bash
git clone [https://github.com/YourUsername/snap-and-solve.git](https://github.com/YourUsername/snap-and-solve.git)
cd snap-and-solve

```

### 2. Install Dependencies

We use `uv` for fast, isolated installation:

```bash
uv venv
# On Windows:
.venv\Scripts\activate
# Install requirements
uv pip install -r requirements.txt

```

### 3. Configure Environment

Create a `.env` file in the root directory and add your Google API key:

```ini
GOOGLE_API_KEY=your_actual_api_key_here

```

---

## Usage Guide

This system uses a **Client-Server** architecture. You need two terminal windows.

### Terminal 1: Start the Vision Server

This runs the local PyTorch model that filters images.

```bash
python server.py
# Output: Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000)

```

### Terminal 2: Run the Client Agent

Upload an image to get a solution.

```bash
# Syntax: python client.py <path_to_image>

python client.py homework_photo.png

```

---

## Demo Scenario

**Input:** A photo of a math problem ().

**Process Flow:**

1. **Agent** sends photo to `localhost:8000`.
2. **Server** confirms: *"Class: Document (98% Conf)"*.
3. **Agent** runs EasyOCR: *"Detected text: 2x + 5 = 15"*.
4. **Agent** prompts Gemini: *"Explain this math problem."*
5. **Gemini** returns the solution.

**Output:**

```text
> Solution found!

Step 1: Subtract 5 from both sides.
2x = 10

Step 2: Divide by 2.
x = 5

Concept: This is a linear equation. The goal is to isolate the variable x.

```

---

## Contributors

* **[Your Name]** - Lead Developer
* **[Member 2]** - Architecture & Documentation
* **[Member 3]** - Testing & QA

---

## License

This project is for educational purposes under the [MIT License](https://www.google.com/search?q=LICENSE).

```

```
