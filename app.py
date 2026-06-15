import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
st.set_page_config(
    page_title="Jimmy's AI Chatbot",
    page_icon="🤖",
    layout="centered"
)
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
with st.sidebar:
    st.title("settings & info ⚙️")
    st.caption("Customized AI Assistant")
    st.markdown("---")
    st.write("✨ **Quick Shortcuts:**")
    st.info("💡 Try asking: 'Who is Mr. Bakker?' or 'Who is Marcus?' or 'Who is D-Jinming' to trigger custom Easter eggs!")
    st.markdown("---")
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
st.title("Jimmy's AI Chatbot 🤖")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "image" in msg:
            st.image(
                msg["image"],
                caption=msg.get("image_caption", ""),
                use_container_width=True
            )

        if "image2" in msg:
            st.image(
                msg["image2"],
                caption=msg.get("image_caption2", ""),
                use_container_width=True
            )
prompt = st.chat_input("Type your message")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    user_lower = prompt.strip().lower()
    answer = ""
    image_path = None
    image_caption = None
    image_path2 = None
    image_caption2 = None

    if "hello" in user_lower or "hi" in user_lower:
        answer = "Bot: Hello! How can I help you?"
    elif "how are you" in user_lower:
        answer = "Bot: I'm good, thank you! How about you? 😊"
    elif "what is your name" in user_lower:
        answer = "Bot: I'm a simple chatbot. My name is Chat Jimmy T.\nAnd I was created by D-Jinming to have fun conversations with you! 😎"
    elif "what can you do" in user_lower or "what can u do" in user_lower:
        answer = "Bot: I can have a conversation with you and answer some basic questions."
    elif "who is elijah" in user_lower:
        answer = "Bot: Elijah is a person you might know.\nHe is a good friend of D-Jinming and is known for his kindness and handsomeness! ✍️ A figure comparable to Tronald Dump"
        image_path = "ChatGPT Image of Elijah.png"
        image_caption = "His hadsome photos"
    elif "who's d-jinming" in user_lower or "who is d-jinming" in user_lower:
        answer = """Bot: D-Jinming is the creator of this chatbot.
He is a talented programmer and a great friend! 😊
It is said that he is also the king of a so-called Daddy Kingdom! 👑"""
    elif "who is marcus" in user_lower:
        answer = "Bot: Marcus is a person you might know.\nHe is a good friend of D-Jinming and is known for his humor and handsomeness! 👍 A figure comparable to MTR 最牛逼之人"
        image_path = "ChatGPT Image 2026年6月14日 15_43_26.png"
        image_caption = "His cool photos"
    elif "who is bakker" in user_lower or "who is mr. bakker" in user_lower or "who is todd bakker" in user_lower:
        answer = "Bot: Mr. Bakker is a person you really should know.\nHe is an excellent teacher in Abbotsford Christian School and is known for his kindness and wisdom."
        image_path = "720796318_1504124068077286_1102852011225536066_n.png"
        image_caption = "His cool photos"
        image_path2 = "weixi image_20260614183242_14_8.png"
        image_caption2 = "His cool photos while teaching nitrogen lab"
    else:
        try:
            with st.spinner("Thinking..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                answer = response.text
        except Exception as e:
            answer = f"Error communicating with AI: {e}"
    msg_data = {"role": "assistant", "content": answer}
    if image_path:
     msg_data["image"] = image_path
     msg_data["image_caption"] = image_caption

    if image_path2:
     msg_data["image2"] = image_path2
     msg_data["image_caption2"] = image_caption2

    st.session_state.messages.append(msg_data)
    st.rerun()
