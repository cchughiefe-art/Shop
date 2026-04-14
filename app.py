import streamlit as st

# Custom Page Style
st.set_page_config(page_title="LQC Shop Manager", page_icon="📱")

st.markdown("<h1 style='text-align: center; color: #00f2fe;'>📱 LQC Smart Shop Manager</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><i>Vibe Coder Edition - Lagos 2026</i></p>", unsafe_allow_html=True)

# Load Database
def load_db():
    try:
        with open("database.txt", "r") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except:
        return []

db = load_db()

# Search Section
st.subheader("🔍 Search Compatibility")
query = st.text_input("Enter Model, Name, or Pin (e.g., X6816, A12, 37-pin)").lower()

if query:
    results = [line for line in db if query in line.lower()]
    if results:
        for res in results:
            st.success(res)
    else:
        st.error("No match found in database.")

# View All Section
with st.expander("📜 View Full Database"):
    for line in db:
        st.write(line)

# Sidebar Signature
st.sidebar.markdown("### 🛠️ Developer Info")
st.sidebar.info("Developed by: **Vibe Coder (Lagos)**")
st.sidebar.write("Built for fast shop diagnostics.")
