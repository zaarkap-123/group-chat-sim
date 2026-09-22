import os
import streamlit as st
from google import genai
from google.genai import types

# Page setup
st.set_page_config(
    page_title="The Group Chat Simulator", 
    page_icon="📱", 
    layout="centered"
)

st.title("📱 The Group Chat Simulator")
st.caption("Forum Theatre Interactive Tool — Type audience responses to see if they stop the bullying!")

# Retrieve API key from Streamlit Secrets or Environment Variable
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ GEMINI_API_KEY not found! Please add it in Streamlit Advanced Settings under Secrets.")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Initial chat state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "avatar": "👤", "content": "**Jake:** Did you guys see her private story screenshot? 💀"},
        {"role": "assistant", "avatar": "👤", "content": "**Liam:** Fr how does she even post stuff like that... making a meme of it right now 😭"}
    ]

# Display current chat log
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message.get("avatar")):
        st.markdown(message["content"])

# Audience input
user_input = st.chat_input("Type audience strategy here...")

if user_input:
    # 1. Display audience response in the chat UI
    st.session_state.messages.append({"role": "user", "avatar": "🙋", "content": f"**Audience Intervention:** {user_input}"})
    with st.chat_message("user", avatar="🙋"):
        st.markdown(f"**Audience Intervention:** {user_input}")

    # 2. Instruct the AI how to evaluate the intervention
    system_instruction = """
    You are simulating a WhatsApp group chat of 14-year-old teens (Jake and Liam). 
    They were previously dogpiling on a classmate's screenshot.
    
    EVALUATION RULES:
    1. IF the intervention effectively defuses the situation (e.g., calls out the behavior maturely, redirects to urgent homework/topics, or uses humor to neutralize tension):
       - Have Jake and Liam back down, agree, or shift focus completely.
       - The bullying MUST stop.
    
    2. IF the intervention is weak, joins in, or aggressively attacks the group:
       - Have Jake and Liam push back or double down (e.g., "Who asked you?", "Why so serious?").
    
    Format output strictly as 1-2 short, realistic group chat messages with character names bolded (e.g., **Jake:** ...).
    """

    # 3. Call Gemini API
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Audience input: {user_input}",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
            )
        )
        bot_reply = response.text

        # Append and display the group's reaction
        st.session_state.messages.append({"role": "assistant", "avatar": "💬", "content": bot_reply})
        with st.chat_message("assistant", avatar="💬"):
            st.markdown(bot_reply)

    except Exception as e:
        st.error(f"Error generating response: {e}")
      
