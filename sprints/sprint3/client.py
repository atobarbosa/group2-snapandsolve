# client.py
import sys
import os
from agent_controller import AgentController

def main():
    # 1. Check CLI arguments
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]

    # 2. Verify file exists locally
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)

    # 3. Initialize the Agent Controller
    agent = AgentController()

    # 4. Run the Pipeline
    print("\n" + "="*50)
    print("🎓 SNAP & SOLVE: AI TUTOR INITIALIZED")
    print("="*50)
    
    final_output = agent.process_request(image_path)
    
    print("\n" + "="*50)
    print("📝 FINAL TUTOR RESPONSE:")
    print("="*50)
    print(final_output)
    print("="*50 + "\n")

if __name__ == "__main__":
    main()