from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    student_name = "Nikk"
    return render_template('index.html', name=student_name)  # Pass variable to template as {{ name }}


@app.route('/profile')
def profile():
    user_data = {
        'name': 'Nik',
        'age': 22,
        'course': 'Web Development',
        'is_enrolled': False,
        'city':'Nashik',
        'email':'nhkhairnar11122004@gmail.com'
    }
    return render_template('profile.html',  # Pass multiple variables to template
                           name=user_data['name'],
                           age=user_data['age'],
                           course=user_data['course'],
                           is_enrolled=user_data['is_enrolled'],
                           city=user_data['city'],
                           email=user_data['email'])


@app.route('/skills')
def skills():
    programming_skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask']
    return render_template('skills.html', skills=programming_skills)  # Pass list to loop through in template


@app.route('/projects')
def projects():
    project_list = [  # List of dictionaries - common pattern for database-like data
        {'name': 'Personal Website', 'status': 'Completed', 'tech': 'HTML/CSS'},
        {'name': 'Flask Blog', 'status': 'In Progress', 'tech': 'Python/Flask'},
        {'name': 'Weather App', 'status': 'Planned', 'tech': 'JavaScript'},
    ]
    return render_template('projects.html', projects=project_list)

@app.route('/grades')
def grades():
    student_grades = {
        "Mathematics": "A",
        "Artificial Intelligence": "A+",
        "Database Management": "B+",
        "Computer Networks": "A",
        "Statistics": "B"
    }
    return render_template('grades.html', grades=student_grades)
if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# JINJA2 SYNTAX QUICK REFERENCE:
# =============================================================================
#
# {{ variable }}          - Output a variable
# {{ variable|upper }}    - Use a filter (uppercase)
# {{ variable|default('N/A') }} - Default value if variable is empty
#
# {% if condition %}      - If statement
#   ...
# {% endif %}
#
# {% for item in list %}  - For loop
#   {{ item }}
# {% endfor %}
#
# =============================================================================
