import streamlit as st

st.title("Ordo – Husbyggets planering")
st.write("Här kan du lägga till och hålla koll på allt som ska fixas med huset!")

# Hög prioritet
st.subheader("✅ Hög prioritet (klart inom 2 veckor)")
high_priority_tasks = [
    "Kontakta vägföreningen 'Kjell' för intyg (Ermin)",
    "Besiktning av vägen med Kjell (Ermin)",
    "Tekniskt sektion för garaget (Dzana)",
    "Kompletta handlingar till Daniel (Dzana)",
    "Lämna ritningar till Mats för offert på extra arbete (Ermin/Dzana)",
    "Inhämta offert från Markarbete och Snickare (Dzana)",
    "Offert på garagebygget (Dzana)",
    "Maila Nordea om kalkyl och offert för mark/övervåning (Dzana)",
    "Kontakta Kristin för förhandsvärdering (Dzana)",
    "Boka möte med banken för att starta upp krediten (Dzana)",
    "Maila Avlin angående ändringar (Dzana)",
    "Boka el-möte (Dzana)",
    "Maila Niklas elektriker om spotlights och smart8plus (Dzana)"
]

for task in high_priority_tasks:
    st.checkbox(task)

# Mellanprioritet
st.subheader("✅ Mellanprioritet (klart senast vecka 23)")
medium_priority_tasks = [
    "Välja kakel (två offerter för två våningar, Happy Homes Bildahl) (Dzana)",
    "Besöka FF Kakel och välja kakel till kök, toalett och golv (Dzana)",
    "Kontakta Jonas kontrollansvarig om separat beskärning (Dzana)"
]

for task in medium_priority_tasks:
    st.checkbox(task)

# Låg prioritet
st.subheader("✅ Låg prioritet (klart senast oktober 2025)")
low_priority_tasks = [
    "Budget för inredning av huset (Dzana)",
    "Planering av möblering enligt Addes plan (Dzana)",
    "Planera bygge av altan (vem snickrar?) (Dzana)"
]

for task in low_priority_tasks:
    st.checkbox(task)
