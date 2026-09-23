import random
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="WhatsApp - Group Chat",
    page_icon="💬",
    layout="centered"
)

# 2. Custom CSS to style Streamlit like WhatsApp
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #ECE5DD;
    }
    
    /* Hide standard Streamlit header/footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* WhatsApp Header Banner */
    .whatsapp-header {
        background-color: #075E54;
        color: white;
        padding: 15px;
        border-radius: 8px 8px 0 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        display: flex;
        align-items: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    .whatsapp-header h3 {
        margin: 0;
        color: white !important;
        font-size: 18px;
    }
    
    .whatsapp-header p {
        margin: 0;
        color: #e0e0e0;
        font-size: 12px;
    }

    /* Style Chat Input Box */
    .stChatInputContainer {
        border-radius: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. WhatsApp Header UI
st.markdown("""
    <div class="whatsapp-header">
        <div>
            <h3>📱 Year 9 Main Group Chat 💬</h3>
            <p>Jake, Liam, You, and 12 others</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# 4. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "avatar": "👤", "content": "**Jake:** Did you guys see her private story screenshot? 💀"},
        {"role": "assistant", "avatar": "👤", "content": "**Liam:** Fr how does she even post stuff like that... making a meme of it right now 😭"}
    ]

# 5. Display Existing Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message.get("avatar")):
        st.markdown(message["content"])

# 6. Response Logic
def evaluate_intervention(text):
    text_lower = text.lower()
    
    # 1. Topic Hijack / Distraction (VERY EFFECTIVE)
    if any(word in text_lower for word in ["chem", "homework", "grade", "test", "mr", "teacher", "class", "due", "math", "science"]):
        responses = [
            "**Jake:** Wait really? 💀 Is that actually due tomorrow?\n\n**Liam:** Nah leave that, did anyone actually finish Q4?",
            "**Jake:** Hold up, is the teacher checking that today?\n\n**Liam:** Wait fr? Send me the answers if you have them.",
            "**Jake:** Wait what grade is that worth again?\n\n**Liam:** Yeah alright, moving past this—someone send the review sheet."
        ]
        return random.choice(responses)
    
    # 2. Setting Boundaries / Calling Out (EFFECTIVE)
    elif any(word in text_lower for word in ["mean", "stop", "toxic", "harsh", "leave", "delete", "chill", "enough", "uncool"]):
        responses = [
            "**Jake:** Alright chill, it was just banter...\n\n**Liam:** Yeah fine, deleting the meme.",
            "**Jake:** Wow alright, taking it pretty serious.\n\n**Liam:** Fine, dropping it. Wasn't that deep anyway.",
            "**Jake:** Okay okay, no need to make it a whole thing.\n\n**Liam:** Yeah whatever, moving on."
        ]
        return random.choice(responses)
    
    # 3. Humor / Deflection (EFFECTIVE)
    elif any(word in text_lower for word in ["lol", "joke", "funny", "random", "bro", "lmao", "weird"]):
        responses = [
            "**Liam:** Haha alright, moving on.\n\n**Jake:** Anyone wanna play games later instead?",
            "**Liam:** Lol fair enough.\n\n**Jake:** Yeah anyway, who's online tonight?",
            "**Liam:** 😂 Alright that was random.\n\n**Jake:** Fr, let's just drop it."
        ]
        return random.choice(responses)
        
    # 4. Aggressive Pushback (BACKFIRES)
    elif any(word in text_lower for word in ["shut up", "loser", "hate", "mad", "annoying"]):
        responses = [
            "**Jake:** Oh look, someone's mad 😂\n\n**Liam:** Cry about it lol. Making another meme now 💀",
            "**Jake:** Why are you getting so aggressive?\n\n**Liam:** Fr, nobody was talking to you anyway 💀"
        ]
        return random.choice(responses)

    # 5. Weak / Generic / Unclear Tactic (INEFFECTIVE)
    else:
        responses = [
            "**Jake:** Who invited you to the chat? 😂\n\n**Liam:** Imagine being this serious. Bro thinks they're the main character 💀",
            "**Jake:** Did anyone ask? 💀\n\n**Liam:** Fr why are you being so dramatic right now",
            "**Jake:** Okay... and?\n\n**Liam:** Bro typed a whole paragraph for nothing 😂"
        ]
        return random.choice(responses)

# 7. Audience Input Area
user_input = st.chat_input("Type audience strategy here...")

if user_input:
    st.session_state.messages.append({"role": "user", "avatar": "🙋", "content": f"**Audience Intervention:** {user_input}"})
    bot_reply = evaluate_intervention(user_input)
    st.session_state.messages.append({"role": "assistant", "avatar": "💬", "content": bot_reply})
    st.rerun()

