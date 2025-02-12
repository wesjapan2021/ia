import streamlit as st
import ollama

# configuracion de interfaz de streamlit
st.title('WES')

# Cuadro de texto para prompt
user_input = st.text_area("Ingresa tu pregunta:", " ")

if st.button("Enviar"):
    if user_input.strip():
        with st.empty():
            full_response = ""
            for chunk in ollama.chat(
                model="deepseek-r1:7b", 
                messages=[{"role": "user", "content": user_input}], 
                stream=True
            ):
                if "message" in chunk:
                    full_response += chunk["message"]["content"]
                    st.write(full_response)
    else:
        st.warning("Por favor ingresa un pregunta")