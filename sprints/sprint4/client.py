# client.py
import sys
import os
from agent_controller import AgentController

def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)

    agent = AgentController()

    print("\n" + "="*50)
    print("🎓 SNAP & SOLVE: AI TUTOR INITIALIZED")
    print("="*50)
    
    # 1. Initial Analysis
    initial_response = agent.start_interaction(image_path)
    print(f"\n🤖 TUTOR:\n{initial_response}\n")

    # If guardrail failed, exit immediately
    if "[STOP]" in initial_response:
        sys.exit(0)

    # 2. Interactive Chat Loop
    print("-" * 50)
    print("Type your answer below (or type 'exit' to quit)")
    print("-" * 50)

    while True:
        try:
            user_input = input("\n🧑 YOU: ")
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\n👋 Session ended. Good luck with your studies!")
                break
            
            if not user_input.strip():
                continue

            print("🤖 TUTOR is thinking...")
            ai_reply = agent.continue_chat(user_input)
            print(f"\n🤖 TUTOR:\n{ai_reply}")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()