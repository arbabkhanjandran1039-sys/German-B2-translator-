import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="German B2 Translator", page_icon="🇩🇪")

st.title("🇩🇪 German B2 AI Translator")
st.write("Kisi bhi zuban ka text likhein, yeh B2 level German mein translate kar dega.")

# Sidebar mein API Key lene ke liye box
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # Text input
    user_input = st.text_area("Apna text yahan likhein:")
    
    if st.button("Translate to B2 German"):
        if user_input:
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"""
                Translate the following text into German at a strict B2 CEFR level.
                Ensure accurate grammar, standard B2 vocabulary, and natural phrasing.
                Provide ONLY the B2 German translation without extra commentary.
                
                Text to translate:
                {user_input}
                """
                
                with st.spinner("Translating..."):
                    response = model.generate_content(prompt)
                    st.success("### German (B2) Translation:")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Pehle kuch text to likhein!")
else:
    st.info("👈 Shuru karne ke liye sidebar mein apni Free Gemini API Key darj karein.")
