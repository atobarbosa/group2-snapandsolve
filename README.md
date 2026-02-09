# 📸 Snap & Solve: The AI-Powered Visual Homework Tutor

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Running-green?logo=fastapi)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.5-orange?logo=google)
![PyTorch](https://img.shields.io/badge/PyTorch-ResNet18-red?logo=pytorch)

**Snap & Solve** is a single-agent AI system designed to help students understand their homework, not just copy answers. By combining local computer vision (to filter relevant content) with cloud-based Generative AI (to explain concepts), it provides a privacy-focused, cost-effective tutoring experience.

---

## 🚀 Key Features

* **🔒 Local Guardrails:** Uses a quantized **PyTorch ResNet18** model locally to verify if an image is "Academic Material" (Document/Paper) before sending it to the cloud.
* **👁️ Optical Character Recognition:** Integrated **EasyOCR** engine to extract handwritten or printed text from images.
* **🧠 One-Shot Tutoring:** Powered by **Google Gemini 2.5 Flash-Lite**, acting as a "Tutor Agent" that solves problems step-by-step.
* **⚡ Lightweight Architecture:** Runs entirely on standard hardware (CPU-optimized) without requiring Admin privileges.

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Agent Controller** | Python 3.12 | The main logic orchestrating the tools. |
| **Vision Model** | PyTorch (ResNet18) | Local image classification (The "Guardrail"). |
| **Backend API** | FastAPI | Hosts the vision model for the agent to call. |
| **OCR Engine** | EasyOCR | Extracts text from validated images. |
| **Reasoning** | Google Gen AI SDK | Generates educational explanations. |
| **Package Manager** | `uv` | Fast Python package management (No Admin needed). |

---

## 📂 Project Structure

```text
snap-and-solve/
├── server.py                # FastAPI Server (Hosts the PyTorch Model)
├── client.py                # CLI Entry point for the User
├── agent_controller.py      # Main Agent Logic (Connects OCR + Server + Gemini)
├── resnet18_quantized.pt    # Pre-trained local model file
├── requirements.txt         # Dependency list
├── .env                     # API Keys (Not committed to Git)
└── README.md                # Project Documentation
