import streamlit as st
import datetime

st.title("Ordo – Husbyggets planering")

st.write("Här kan du lägga till och hålla koll på allt som ska fixas med huset!")

# Lista för att spara uppgifter
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Formulär för att lägga till nya uppgifter
with st.form("task_form"):
    task = st.text_input("Vad behöver göras?")
    due_date = st.date_input("Deadline", datetime.date.today())
    submitted = st.form_submit_button("Lägg till")

    if submitted and task:
        st.session_state.tasks.append((task, due_date))
        st.success(f"Uppgiften '{task}' är tillagd!")

# Visa alla uppgifter
st.subheader("Mina uppgifter")
for i, (task, due_date) in enumerate(st.session_state.tasks):
    st.write(f"{i+1}. {task} (Deadline: {due_date})")
