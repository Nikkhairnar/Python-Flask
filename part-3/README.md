# Part 3: Jinja2 Variables - Passing Data to Templates

## 🎯 Learning Goals
- Pass variables from Python to HTML templates
- Use `{{ variable }}` syntax to display data
- Use Jinja2 filters (`|upper`, `|length`, etc.)
- Loop through lists with `{% for %}`
- Use conditionals with `{% if %}`

## 📖 Concepts Covered

### Passing Variables
```python
@app.route('/')
def home():
    name = "Alex"
    return render_template('index.html', name=name)
```

In the template:
```html
<h1>Hello, {{ name }}!</h1>
```

### Jinja2 Filters
```html
{{ name|upper }}      <!-- ALEX -->
{{ name|lower }}      <!-- alex -->
{{ name|length }}     <!-- 4 -->
{{ name|title }}      <!-- Alex -->
```

### Conditionals
```html
{% if is_enrolled %}
    <span>Enrolled</span>
{% else %}
    <span>Not Enrolled</span>
{% endif %}
```

### For Loops
```html
{% for skill in skills %}
    <li>{{ skill }}</li>
{% endfor %}
```

### Loop Variables
- `loop.index` - Current iteration (starts at 1)
- `loop.index0` - Current iteration (starts at 0)
- `loop.first` - True if first iteration
- `loop.last` - True if last iteration
- `loop.length` - Total number of items

## 🚀 How to Run

```bash
cd part-3
python app.py
```

Visit:
- `http://localhost:5000/` - Single variable demo
- `http://localhost:5000/profile` - Multiple variables + conditionals
- `http://localhost:5000/skills` - Looping through a list
- `http://localhost:5000/projects` - List of dictionaries

## 1. Enhanced Profile Implementation
Task: Add email and city to the dictionary and display them on the profile page.

The Python Logic (app.py):

@app.route('/profile')
def profile():
    user_data = {
        'name': 'Nik',
        'age': 22,
        'course': 'Web Development',
        'is_enrolled': False,
        'city':'Nashik',  # Added city
        'email':'nhkhairnar11122004@gmail.com' # Added email
    }
    return render_template('profile.html', 
                           name=user_data['name'],
                           # ... other variables ...
                           city=user_data['city'], # Passed to HTML
                           email=user_data['email']) # Passed to HTML

The HTML Display (profile.html):

<div class="profile-item">
    <span>city:</span>{{city}} </div>
<div class="profile-item">
    <span>email:</span>{{email}} </div>

## 2. Conditional Enrollment Implementation
Task: Use an if/else block to show a green "Enrolled" badge or an orange "Not Enrolled" badge.

The HTML Logic (profile.html):

<div class="profile-item">
    <span>Status:</span>
    {% if is_enrolled %}
        <span class="badge badge-success">Enrolled</span>
    {% else %}
        <span class="badge badge-warning">Not Enrolled</span>
    {% endif %}
</div>

Proof of implementation: Since you set is_enrolled: False in app.py, the website will currently display the orange "Not Enrolled" badge.

## 3. Grades Table Implementation
Task: Create a /grades route and a table that loops through a dictionary of subjects.

The Python Route (app.py):

@app.route('/grades')
def grades():
    student_grades = {
        "Mathematics": "A",
        "Artificial Intelligence": "A+",
        "Database Management": "B+",
        "Computer Networks": "A",
        "Statistics": "B"
    }
    return render_template('grades.html', grades=student_grades) # Passed dict

The HTML Table Loop (grades.html):

<table>
    <tr>
        <th>Subject</th>
        <th>Grade</th>
    </tr>

    {% for subject, grade in grades.items() %}
    <tr>
        <td>{{ subject }}</td>
        <td>{{ grade }}</td>
    </tr>
    {% endfor %}
</table>

