# ui.py
import gradio as gr
from agent_controller import AgentController

# 1. Initialize our existing Agent
print("Initializing Agent Controller for UI...")
agent = AgentController()

# 2. Define the UI Logic Functions
def start_tutor(image_path, history):
    """Triggered when the user uploads an image and clicks Start."""
    if not image_path:
        history.append({"role": "assistant", "content": "⚠️ Please upload an image first."})
        return history, gr.update(interactive=False)
    
    initial_response = agent.start_interaction(image_path)
    history.append({"role": "assistant", "content": initial_response})
    
    is_interactive = "[STOP]" not in initial_response
    return history, gr.update(interactive=is_interactive)

def chat_with_tutor(user_message, history):
    """Triggered when the user types a reply."""
    if not user_message.strip():
        return history, ""
    
    # Append user message and a temporary thinking state
    history.append({"role": "user", "content": user_message})
    history.append({"role": "assistant", "content": "⏳ Tutor is thinking..."})
    yield history, ""
    
    # Get the real reply from Gemini
    ai_reply = agent.continue_chat(user_message)
    
    # Replace the "thinking" state with the actual reply
    history[-1]["content"] = ai_reply
    yield history, ""

# 3. Build the Graphical Interface
# Removed the 'theme' argument to silence the Gradio 6.0 warning
with gr.Blocks() as app:
    gr.Markdown("# 📸 Snap & Solve: AI Visual Homework Tutor")
    gr.Markdown("Upload a picture of your homework, and our AI will guide you through it step-by-step!")
    
    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(type="filepath", label="1. Upload Homework Image")
            start_btn = gr.Button("2. Start Tutor Analysis", variant="primary")
        
        with gr.Column(scale=2):
            # Removed 'type="messages"' to fix the crash. Your version defaults to it automatically!
            chatbot = gr.Chatbot(
                label="Tutor Chat", 
                height=400,
                latex_delimiters=[
                    {"left": "$$", "right": "$$", "display": True},
                    {"left": "$", "right": "$", "display": False}
                ]
            )
            
            with gr.Row():
                chat_input = gr.Textbox(
                    placeholder="Type your answer here...", 
                    label="Your Reply", 
                    interactive=False, 
                    scale=4
                )
                send_btn = gr.Button("Send", interactive=False, scale=1)

    # 4. Wire the buttons
    start_btn.click(
        fn=start_tutor,
        inputs=[image_input, chatbot],
        outputs=[chatbot, chat_input]
    ).then(
        fn=lambda: gr.update(interactive=True),
        outputs=[send_btn]
    )

    chat_input.submit(
        fn=chat_with_tutor,
        inputs=[chat_input, chatbot],
        outputs=[chatbot, chat_input]
    )
    send_btn.click(
        fn=chat_with_tutor,
        inputs=[chat_input, chatbot],
        outputs=[chatbot, chat_input]
    )

# 5. Run the app
if __name__ == "__main__":
    print("Starting UI...")
    app.launch(server_name="127.0.0.1", server_port=7860)