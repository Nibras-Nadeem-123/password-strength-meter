import streamlit as st
import re
import random
import string

# Function to check password strength and provide recommendations
def check_strength(password):
    strength = 0
    recommendations = []

    if len(password) < 8:
        recommendations.append("Increase the length to at least 8 characters.")
    else:
        strength += 1

    if not re.search(r'[A-Z]', password):
        recommendations.append("Include at least one uppercase letter (A-Z).")
    else:
        strength += 1

    if not re.search(r'[a-z]', password):
        recommendations.append("Include at least one lowercase letter (a-z).")
    else:
        strength += 1

    if not re.search(r'\d', password):
        recommendations.append("Include at least one number (0-9).")
    else:
        strength += 1

    if not re.search(r'[\W]', password):  # Special characters
        recommendations.append("Include at least one special character (!@#$%^&*).")
    else:
        strength += 1

    return strength, recommendations

# Function to generate a strong password
def generate_password(length=12):
    if length < 8:
        length = 8  # Ensure minimum length of 8

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit App UI
st.title("🔒 Password Strength Meter & Generator")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, recommendations = check_strength(password)
    
    # Strength levels and colors
    strength_levels = ["Too Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
    colors = ["red", "orange", "yellow", "blue", "green"]

    # Display password strength
    st.markdown(f"**Strength:** {strength_levels[strength]}")
    
    # Display progress bar
    st.progress(strength / 5)

    # Display recommendations if weak
    if strength < 5:
        st.markdown("### 🔹 How to Improve Your Password")
        for rec in recommendations:
            st.write(f"✅ {rec}")

    # Change text color based on strength
    st.markdown(f'<p style="color:{colors[strength-1]}; font-weight:bold;">{strength_levels[strength]}</p>', unsafe_allow_html=True)

# Password Generator Section
st.markdown("---")
st.subheader("🔑 Generate a Strong Password")
length = st.slider("Select password length:", min_value=8, max_value=20, value=12)

if st.button("Generate Password"):
    strong_password = generate_password(length)
    st.session_state["generated_password"] = strong_password  # Store in session state

# Display generated password if available
if "generated_password" in st.session_state:
    generated_password = st.session_state["generated_password"]
    
    # Use st.code which provides a copy button automatically
    st.code(generated_password, language="")

