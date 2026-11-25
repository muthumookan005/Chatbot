
import streamlit as st
from datetime import datetime
from chatbot import get_response

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Customer Support AI",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =====================================
# SESSION STATE
# =====================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None


# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #F5F0FF,
        #EDE9FE,
        #F8F5FF
    );
}

.main .block-container {
    max-width: 750px;
    padding-top: 2rem;
    padding-bottom: 6rem;
}

/* Header Card */

.hero {
    background: linear-gradient(
        135deg,
        #4B0082,
        #8000FF
    );
    padding: 30px 20px;
    border-radius: 24px;
    text-align: center;
    color: white;
    box-shadow: 0 12px 35px rgba(75, 0, 130, 0.2);
}

.hero-title {
    color: white;
    font-size: 30px;
    font-weight: 750;
    text-align: center;
}

.hero-subtitle {
    color: #E9D5FF;
    font-size: 15px;
    text-align: center;
    line-height: 1.7;
}

.status {
    color: white;
    font-size: 13px;
    text-align: center;
}

/* Popular Topics */

.section-title {
    text-align: center;
    color: #6B21A8;
    font-size: 14px;
    font-weight: 750;
    letter-spacing: 1.5px;
}

/* Topic Buttons */

div.stButton > button {
    background: #EDE0FF;
    color: #5B21B6;
    border: 1px solid #D8B4FE;
    border-radius: 30px;
    padding: 12px;
    font-weight: 650;
    transition: 0.3s;
}

div.stButton > button:hover {
    background: #6B21A8;
    color: white;
    border-color: #6B21A8;
}

/* Clear Chat Button */

div[data-testid="stHorizontalBlock"] div.stButton > button {
    white-space: nowrap;
}

/* Chat Messages */

div[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 8px 0 !important;
}

div[data-testid="stChatMessageContent"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    line-height: 1.7;
    font-size: 15px;
}

/* Chat Input */

div[data-testid="stChatInput"] {
    background: white;
    border: 2px solid #C084FC;
    border-radius: 20px;
    box-shadow: 0 5px 18px rgba(107, 33, 168, 0.08);
}

div[data-testid="stChatInput"] textarea {
    font-size: 15px;
}

/* Footer */

.footer {
    color: #8B5CF6;
    text-align: center;
    font-size: 12px;
}

/* Mobile Responsive */

@media screen and (max-width: 600px) {
    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero-title {
        font-size: 24px;
    }
}

</style>
""", unsafe_allow_html=True)


# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="hero">
    <div class="hero-title">
        🤖 Customer Support AI
    </div>
    <div class="hero-subtitle">
        Your intelligent support assistant.<br>
        Ask anything about orders, payments,
        delivery, returns and more.
    </div>
    <br>
    <div class="status">
        🟢 Online • Available 24/7
    </div>
</div>
""", unsafe_allow_html=True)


# =====================================
# CHAT HEADER + CLEAR BUTTON
# =====================================

st.write("")

col1, col2 = st.columns(
    [3, 1],
    vertical_alignment="center",
    gap="medium"
)

with col1:
    st.markdown("### 💬 Chat with us")

with col2:
    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True,
        key="clear_chat"
    ):
        st.session_state.messages = []
        st.session_state.pending_prompt = None
        st.rerun()

st.write("")


# =====================================
# POPULAR TOPICS
# =====================================

if not st.session_state.messages:

    st.markdown(
        "<h4 style='text-align:center; color:#6B21A8;'>"
        "POPULAR TOPICS</h4>",
        unsafe_allow_html=True
    )

    questions = [
        "📦 Order status",
        "💳 Payment issues",
        "🚚 Delivery",
        "↩️ Returns",
        "🛠️ General support"
    ]

    for i in range(0, len(questions), 2):

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                questions[i],
                use_container_width=True,
                key=f"topic_{i}"
            ):
                st.session_state.pending_prompt = questions[i]
                st.rerun()

        if i + 1 < len(questions):
            with col2:
                if st.button(
                    questions[i + 1],
                    use_container_width=True,
                    key=f"topic_{i+1}"
                ):
                    st.session_state.pending_prompt = questions[i + 1]
                    st.rerun()

    # Welcome Message

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<h2 style='text-align:center; color:#5B21B6;'>"
        "💬 How can I help you?</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; color:#7C3AED;'>"
        "Type your question below and I'll do my best to help."
        "<br>We're always happy to assist you!</p>",
        unsafe_allow_html=True
    )


# =====================================
# DISPLAY CHAT HISTORY
# =====================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar="🤖" if message["role"] == "assistant" else "👤"
    ):

        st.markdown(message["content"])

        if "time" in message:
            st.caption(message["time"])


# =====================================
# CHAT INPUT
# =====================================

user_text = st.chat_input(
    "✍️ Type your message here..."
)


# Handle topic button selection

if st.session_state.pending_prompt:

    user_text = st.session_state.pending_prompt
    st.session_state.pending_prompt = None


# =====================================
# GENERATE CHATBOT RESPONSE
# =====================================

if user_text:

    st.session_state.messages.append({
        "role": "user",
        "content": user_text,
        "time": datetime.now().strftime("%I:%M %p")
    })

    try:
        with st.spinner("🤖 Assistant is typing..."):
            response = get_response(user_text)

        if not isinstance(response, str):
            response = str(response)

    except Exception as e:
        response = (
            "Sorry, something went wrong. "
            "Please try again later."
        )
        print("Chatbot Error:", e)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": datetime.now().strftime("%I:%M %p")
    })

    st.rerun()


# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.markdown(
    "<p style='text-align:center; color:#8B5CF6;'>"
    "🔒 Secure Customer Support Assistant"
    "<br><br>"
    "Powered by AI • Available 24/7"
    "</p>",
    unsafe_allow_html=True
)
