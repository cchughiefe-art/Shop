import streamlit as st

st.set_page_config(page_title="LQC Shop Manager", page_icon="📱")

# The Vibe Coder Header
st.markdown("<h1 style='text-align: center; color: #00f2fe;'>📱 LQC Shop Manager</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>Search by Market ID (Flex Code) or Model</b></p>", unsafe_allow_html=True)

def load_db():
    try:
        with open("database.txt", "r") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except:
        return []

db = load_db()

# Main Search Bar
query = st.text_input("🔍 Type Market ID (e.g., BF7, KI5, LG6) or Phone Name", "").strip().lower()

if query:
    results = [line for line in db if query in line.lower()]
    if results:
        st.write(f"Found {len(results)} Groups:")
        for res in results:
            # We split the line to highlight the Main ID (everything before the first '/')
            parts = res.split('/')
            main_id = parts[0].strip()
            others = " / ".join(parts[1:]) if len(parts) > 1 else ""
            
            with st.container():
                st.markdown(f"### 🏷️ {main_id}")
                if others:
                    st.write(f"**Also fits:** {others}")
                st.divider()
    else:
        st.error("Model not found in database.")

# Quick Guide for the Shop
st.sidebar.header("🛠️ Market ID Guide")
st.sidebar.markdown("""
- **BF7:** Pop 7 Pro / Smart 7 / A60
- **KI5:** Spark 10 / Smart 8 / P55
- **LG6:** Hot 12 Play / Pova Neo 2
- **KG5:** Smart 6 / Spark Go 2020
""")

st.sidebar.markdown("---")
st.sidebar.write("Developed by: **Vibe Coder**")
