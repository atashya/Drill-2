from js import document

def generate_message(event):
    # Get input values
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # Clear previous message
    output_div = document.getElementById("output")
    output_div.innerHTML = ""

    # Escape characters example
    note = f"Rumi is currently {age} years old and studies at {school}.\nThis information was gathered through input fields and displayed using a multiline string in Python via PyScript.\nSpecial characters: \"Quotes\" and a tab space:\t<- see?"

    # Multiline string
    profile = f"""
    <b>👤 Student Profile</b><br>
    <b>Name:</b> {name}<br>
    <b>Age:</b> {age}<br>
    <b>School:</b> {school}<br><br>
    <b>📝 Notes:</b><br>
    {note}
    """

    # Display result
    output_div.innerHTML = profile

# Attach event listener to button
document.getElementById("generate-btn").addEventListener("click", generate_message)
