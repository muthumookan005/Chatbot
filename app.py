import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="Customer Support",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

    /* ---------- Global ---------- */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
    }

    .main .block-container {
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 6rem;
    }

    /* ---------- Header ---------- */
    .hero {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        padding: 2rem 2.2rem;
        border-radius: 24px;
        color: white;
        margin-bottom: 1.8rem;
        box-shadow: 0 12px 35px rgba(79, 70, 229, 0.20);
    }

    .hero-icon {
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
    }

    .hero-title {
        font-size: 2rem;
        font-weight: 750;
        letter-spacing: -0.5px;
        margin: 0;
    }

    .hero-subtitle {
        font-size: 1rem;
        margin-top: 0.55rem;
        opacity: 0.9;
        line-height: 1.6;
    }

    /* ---------- Suggested Topics ---------- */
    .section-label {
        font-size: 0.85rem;
        font-weight: 650;
        color: #64748b;
        margin-bottom: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .topics {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-bottom: 1.7rem;
    }

    .topic {
        background: rgba(255, 255, 255, 0.85);
        border: 1px solid #e2e8f0;
        padding: 0.55rem 0.9rem;
        border-radius: 999px;
        color: #475569;
        font-size: 0.88rem;
        box-shadow: 0 3px 10px rgba(15, 23, 42, 0.04);
    }

    /* ---------- Chat Area ---------- */
    [data-testid="stChatMessage"] {
        border-radius: 18px;
        padding: 0.35rem 0;
        margin-bottom: 0.7rem;
    }

    [data-testid="stChatMessageContent"] {
        line-height: 1.65;
        font-size: 0.96rem;
    }

    /* ---------- Chat Input ---------- */
    [data-testid="stChatInput"] {
        background: white;
        border-radius: 18px;
    }

    [data-testid="stChatInput"] textarea {
        font-size: 0.95rem;
    }

    /* ---------- Empty State ---------- */
    .empty-state {
        text-align: center;
        padding: 2rem 1rem;
        color: #64748b;
    }

    .empty-icon {
        font-size: 2.4rem;
        margin-bottom: 0.5rem;
    }

    .empty-title {
        font-size: 1.15rem;
        font-weight: 650;
        color: #334155;
        margin-bottom: 0.35rem;
    }

    /* ---------- Footer ---------- */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.78rem;
        margin-top: 2rem;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero">
    <div class="hero-icon">🤖</div>
    <div class="hero-title">Customer Support</div>
    <div class="hero-subtitle">
        Hi! I'm here to help with your orders, payments, delivery,
        returns, and other support questions.
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Suggested topics
# -----------------------------
if not st.session_state.get("messages"):

    st.markdown(
        '<div class="section-label">Popular topics</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="topics">
        <div class="topic">📦 Order status</div>
        <div class="topic">💳 Payment issues</div>
        <div class="topic">🚚 Delivery</div>
        <div class="topic">↩️ Returns</div>
        <div class="topic">🛠️ General support</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="empty-state">
        <div class="empty-icon">💬</div>
        <div class="empty-title">How can I help you?</div>
        <div>
            Type your question below and I'll do my best to help.
        </div>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# Store chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display chat history
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar="🤖" if message["role"] == "assistant" else "👤"
    ):
        st.markdown(message["content"])


# -----------------------------
# Chat input
# -----------------------------
user_text = st.chat_input(
    "Ask about your order, payment, delivery, returns..."
)


if user_text:

    # User message
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_text)

    st.session_state.messages.append({
        "role": "user",
        "content": user_text
    })

    # Assistant response
    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("Thinking..."):
            response = get_response(user_text)

        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })


# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div class="footer">
    Customer Support Assistant • Available 24/7
</div>
""", unsafe_allow_html=True)