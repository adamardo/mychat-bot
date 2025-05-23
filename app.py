import streamlit as st
from openai import OpenAI

# ✅ Replace with your real API key
client = OpenAI(api_key="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")  # Use your actual API key here

# 🌍 Page title
st.markdown("<h1 style='text-align: center; color: green;'>🌍 New World AI Guide</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Helping every profession understand and use AI — in English and Hausa.</p>", unsafe_allow_html=True)
st.write("---")

# 🧑‍🎓 Profession dropdown with emojis
profession_emojis = {
    "Farmer": "👨🏾‍🌾",
    "Tailor": "🧵",
    "Akara Seller": "🍽️",
    "Shoemaker": "👞",
    "Taxi Driver": "🚕",
    "Custom Input": "📝"
}

selected_profession = st.selectbox("Choose your profession:", list(profession_emojis.keys()))
emoji = profession_emojis.get(selected_profession, "")

# 🌐 Language selection buttons
col1, col2 = st.columns(2)
with col1:
    english = st.button("Get Advice in English")
with col2:
    hausa = st.button("Nemi Shawara da Hausa")

# 💬 Optional: Ask your own question
st.write("---")
question = st.text_input("Do you want to ask something specific? (Optional)")
if question:
    st.info(f"🔎 You asked: {question}")
    st.warning("💡 Free question answering will be added in a future upgrade.")

# 🔧 AI advice engine using new OpenAI SDK
def get_ai_advice_from_openai(profession, language):
    prompt = f"Give a simple and practical explanation of how AI can help someone who works as a {profession}. Use {language} language. Be clear and friendly."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that explains how artificial intelligence can help different jobs. Respond clearly and politely."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"

# 🚀 Displaying response
if english and selected_profession:
    st.subheader(f"{emoji} AI Advice for {selected_profession}")
    response = get_ai_advice_from_openai(selected_profession, "English")
    st.success(response)

if hausa and selected_profession:
    st.subheader(f"{emoji} Shawarar AI ga {selected_profession}")
    response = get_ai_advice_from_openai(selected_profession, "Hausa")
    st.success(response)
