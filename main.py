from js import document, window

def check(event=None):
    output = document.getElementById("output")
    output.innerHTML = ""

    # registration and medical
    registration = ""
    medical = ""
    for r in document.getElementsByName("registration"):
        if r.checked:
            registration = r.value
    for m in document.getElementsByName("medical"):
        if m.checked:
            medical = m.value

    # grade & section
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    # validation
    if registration == "" or medical == "" or grade == "" or section == "":
        output.innerHTML = "❌ Please complete all fields."
        return

    grade = int(grade)

    if registration != "yes":
        output.innerHTML = "❌ Please complete the online registration."
        return

    if medical != "yes":
        output.innerHTML = "❌ Please secure a medical clearance."
        return

    if grade < 7 or grade > 10:
        output.innerHTML = "❌ Only Grades 7 to 10 are eligible."
        return

    # assign team
    if grade == 7:
        team = "Blue Bears"
    elif grade == 8:
        team = "Red Bulldogs"
    elif grade == 9:
        team = "Yellow Tigers"
    else:
        team = "Green Hornets"

    # show result
    output.innerHTML = f"🎉 Congratulations! You are part of the <strong>{team}</strong><br>Grade {grade} – {section}"

# BIND AFTER DOM LOADED
def bind_button():
    button = document.getElementById("signupBtn")
    button.addEventListener("click", check)

# Wait until the DOM is fully loaded
window.addEventListener("load", bind_button)
