from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    about_me = "My name is Bard, and I'm a large language model from Google AI."
    education = ["Master's in Artificial Intelligence", "Bachelor's in Computer Science"]
    hobbies = ["Coding", "Reading", "Playing music"]
    skills = ["Natural Language Processing", "Machine Learning", "Software Engineering"]
    return render_template("index.html", about=about_me, education=education, hobbies=hobbies, skills=skills)

@app.route("/education")
def education_page():
    # Add logic to display detailed information about your education
    return render_template("education.html")

# Similar routes for other pages like hobbies and skills

if __name__ == "__main__":
    app.run(debug=True)
