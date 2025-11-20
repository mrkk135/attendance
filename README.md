Flask Attendance System - Project Archive

This document contains all 6 required files for your Flask application.

Project Structure:

app.py (in the root folder)

templates/base.html

templates/login.html

templates/index.html

templates/employees.html

templates/attendance.html

templates/summary.html

Setup Instructions

Create a main directory: attendance_system

Create a sub-directory: attendance_system/templates

Save the files: Copy the content below and save each section to its corresponding file path.

Install requirements: pip install Flask Flask-SQLAlchemy Flask-Login werkzeug

Run: python app.py

1. app.py (Main Python Application)

Save this content as app.py in the root folder.

from flask import Flask, render_template, redirect, url_for, request, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import csv
from io import StringIO
from pathlib import Path

# --- 1. App Configuration & Database Path Fix ---
app = Flask(__name__)

# Define the base directory (where app.py lives)
BASE_DIR = Path(__file__).parent 
# Define the instance folder path explicitly
INSTANCE_DIR = BASE_DIR / 'instance'

# Ensure the instance folder exists before connecting to the database
# This fixes the common 'unable to open database file' error
INSTANCE_DIR.mkdir(exist_ok=True) 

# Configure SQLAlchemy with the full, absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{INSTANCE_DIR / "database.db"}'

app.config['SECRET_KEY'] = 'YOUR_SUPER_SECURE_SECRET_KEY' # !!! CHANGE THIS IN PRODUCTION !!!
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Set the view function for the login page

# --- FIX: Make Python's datetime class available in all Jinja templates ---
app.jinja_env.globals.update(datetime=datetime)

# --- 2. Database Models ---
class User(UserMixin, db.Model):
    """Admin User for logging into the system."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Employee(db.Model):
    """Employee details for attendance tracking."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=True)
    # Relationship to Attendance records (cascade ensures attendance records are deleted with the employee)
    attendances = db.relationship('Attendance', backref='employee', lazy=True, cascade="all, delete-orphan")

class Attendance(db.Model):
    """Time clock records (Clock In/Out)."""
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    # Store time in UTC
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    type = db.Column(db.String(10), nullable=False) # 'IN' or 'OUT'

@login_manager.user_loader
def load_user(user_id):
    """Required function for Flask-Login to load a user."""
    return User.query.get(int(user_id))

# --- 3. Initial Setup and Run ---
with app.app_context():
    db.create_all()
    # Create a default admin user if one doesn't exist
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin')
        admin_user.set_password('adminpass') # !!! CHANGE THIS !!!
        db.session.add(admin_user)
        db.session.commit()
        print("Default admin user created: admin/adminpass")

# --- 4. Login and Logout Routes ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# --- 5. Main Routes (Protected by @login_required) ---
@app.route('/')
@login_required
def home():
    """Dashboard for Clocking and Today's Log."""
    today = datetime.utcnow().date()
    # Filter attendance records for today
    today_attendance = Attendance.query.filter(
        db.func.date(Attendance.timestamp) == today
    ).order_by(Attendance.timestamp.desc()).all()

    employees = Employee.query.all()

    return render_template('index.html', attendance_records=today_attendance, employees=employees)

@app.route('/clock', methods=['POST'])
@login_required
def clock():
    """Handles Clock IN/OUT submissions."""
    employee_id = request.form.get('employee_id')
    clock_type = request.form.get('clock_type') # 'IN' or 'OUT'

    if not employee_id or not clock_type:
        flash('Invalid clock request.', 'danger')
        return redirect(url_for('home'))

    employee = Employee.query.get(employee_id)
    if not employee:
        flash('Employee not found.', 'danger')
        return redirect(url_for('home'))

    new_attendance = Attendance(
        employee_id=employee_id,
        type=clock_type
    )
    db.session.add(new_attendance)
    db.session.commit()
    flash(f'Successfully Clocked {clock_type} for {employee.name} at {datetime.now().strftime("%H:%M:%S")}!', 'success')
    return redirect(url_for('home'))


# --- 6. Admin Panel (Employee Management CRUD) ---
@app.route('/employees')
@login_required
def employees():
    """View all employees and trigger CRUD actions."""
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

@app.route('/employee/add', methods=['POST'])
@login_required
def add_employee():
    """Adds a new employee."""
    name = request.form.get('name')
    position = request.form.get('position')
    
    new_employee = Employee(name=name, position=position)
    db.session.add(new_employee)
    db.session.commit()
    flash(f'Employee {name} added successfully!', 'success')
    return redirect(url_for('employees'))

@app.route('/employee/update/<int:id>', methods=['POST'])
@login_required
def update_employee(id):
    """Updates an existing employee."""
    employee = Employee.query.get_or_404(id)
    employee.name = request.form.get('name')
    employee.position = request.form.get('position')
    db.session.commit()
    flash(f'Employee {employee.name} updated successfully!', 'info')
    return redirect(url_for('employees'))

@app.route('/employee/delete/<int:id>', methods=['POST'])
@login_required
def delete_employee(id):
    """Deletes an employee and their related attendance records."""
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    flash(f'Employee {employee.name} deleted successfully.', 'danger')
    return redirect(url_for('employees'))

# --- 7. Attendance Viewing and Export ---
@app.route('/attendance')
@login_required
def view_attendance():
    """View all attendance records."""
    all_attendance = Attendance.query.join(Employee).order_by(Attendance.timestamp.desc()).all()
    return render_template('attendance.html', attendance_records=all_attendance)

@app.route('/export_csv')
@login_required
def export_csv():
    """Exports all attendance data to a CSV file."""
    all_attendance = Attendance.query.join(Employee).order_by(Attendance.timestamp.asc()).all()
    
    # Create an in-memory CSV file
    si = StringIO()
    cw = csv.writer(si)
    
    # Write header
    cw.writerow(['ID', 'Employee Name', 'Timestamp', 'Type'])

    # Write data rows
    for record in all_attendance:
        cw.writerow([
            record.id,
            record.employee.name,
            record.timestamp.strftime('%Y-%m-%d %H:%M:%S'), 
            record.type
        ])

    output = si.getvalue()
    
    # Send the file back to the user
    response = make_response(output)
    response.headers['Content-Disposition'] = 'attachment; filename=attendance_export.csv'
    response.headers['Content-type'] = 'text/csv'
    return response

# --- 8. Hours Summary Route ---
@app.route('/summary')
@login_required
def summary():
    """Calculates total hours worked by pairing IN and OUT records."""
    employees = Employee.query.all()
    summary_data = {}
    
    for emp in employees:
        # Get all attendance records sorted by time
        records = Attendance.query.filter_by(employee_id=emp.id).order_by(Attendance.timestamp).all()
        
        daily_log = {} # Key: date_str, Value: {'IN': datetime, 'OUT': datetime}

        # 1. Group records by date and type, ensuring proper pairing
        for record in records:
            date_str = record.timestamp.date().isoformat()
            if date_str not in daily_log:
                daily_log[date_str] = {'IN': None, 'OUT': None}
            
            # Use the first 'IN' of the day
            if record.type == 'IN' and daily_log[date_str]['IN'] is None:
                daily_log[date_str]['IN'] = record.timestamp
            
            # Use the latest 'OUT' of the day, ensuring it's after an 'IN'
            elif record.type == 'OUT' and daily_log[date_str]['IN'] is not None:
                if daily_log[date_str]['OUT'] is None or record.timestamp > daily_log[date_str]['OUT']:
                    daily_log[date_str]['OUT'] = record.timestamp

        total_duration = timedelta()
        daily_hours = {}

        # 2. Calculate duration for each day
        for date_str, times in daily_log.items():
            if times['IN'] and times['OUT']:
                duration = times['OUT'] - times['IN']
                total_duration += duration
                daily_hours[date_str] = str(duration).split('.')[0] # Format to HH:MM:SS
            elif times['IN']:
                daily_hours[date_str] = "Clocked IN, No OUT"
            # Unpaired 'OUT' records are ignored

        # 3. Store results
        summary_data[emp.name] = {
            'employee': emp,
            'total_hours': str(total_duration).split('.')[0], # Total formatted
            'daily_breakdown': daily_hours
        }

    return render_template('summary.html', summary_data=summary_data)

# --- 9. Run App ---
if __name__ == '__main__':
    app.run(debug=True)


2. templates/base.html (Base Layout)

Save this content as templates/base.html.

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Office Attendance System</title>
    <!-- Bootstrap CSS -->
    <link href="[https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css](https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css)" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .navbar-brand {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm">
        <div class="container-fluid">
            <a class="navbar-brand" href="{{ url_for('home') }}">
                <span style="font-size: 1.5rem;">⏱️</span> Attendance Admin
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    {% if current_user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('home') }}">Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('employees') }}">Employees (CRUD)</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('view_attendance') }}">Attendance Log</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('summary') }}">Hours Summary</a>
                    </li>
                    {% endif %}
                </ul>
                <ul class="navbar-nav">
                    {% if current_user.is_authenticated %}
                    <li class="nav-item">
                        <a class="nav-link btn btn-outline-light btn-sm px-3" href="{{ url_for('logout') }}">
                            Logout ({{ current_user.username }})
                        </a>
                    </li>
                    {% else %}
                    <li class="nav-item">
                        <a class="nav-link btn btn-outline-light btn-sm px-3" href="{{ url_for('login') }}">Login</a>
                    </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>

    <div class="container mt-5">
        <!-- Flash Messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }} alert-dismissible fade show" role="alert">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <!-- Content Block -->
        {% block content %}{% endblock %}
    </div>

    <!-- Bootstrap JS -->
    <script src="[https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js](https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js)"></script>
</body>
</html>


3. templates/login.html (Login Page)

Save this content as templates/login.html.

{% extends "base.html" %}
{% block content %}
<div class="row justify-content-center">
    <div class="col-md-5">
        <div class="card shadow-lg border-0 rounded-3">
            <div class="card-header bg-primary text-white text-center py-3">
                <h3 class="mb-0">🔑 System Login</h3>
                <p class="mb-0 small">Admin Access Required</p>
            </div>
            <div class="card-body p-4">
                <form method="POST">
                    <div class="mb-3">
                        <label for="username" class="form-label fw-bold">Username</label>
                        <input type="text" class="form-control form-control-lg rounded-pill" id="username" name="username" placeholder="Enter admin username" required>
                    </div>
                    <div class="mb-4">
                        <label for="password" class="form-label fw-bold">Password</label>
                        <input type="password" class="form-control form-control-lg rounded-pill" id="password" name="password" placeholder="Enter password" required>
                    </div>
                    <button type="submit" class="btn btn-success btn-lg w-100 rounded-pill shadow-sm">
                        Login to Admin Panel
                    </button>
                </form>
            </div>
            <div class="card-footer text-center text-muted small">
                Default: admin / adminpass (Please change this in app.py)
            </div>
        </div>
    </div>
</div>
{% endblock %}


4. templates/index.html (Dashboard & Clocking)

Save this content as templates/index.html.

{% extends "base.html" %}
{% block content %}
<h2 class="mb-4 text-primary">🏠 Office Dashboard & Time Clock</h2>

<div class="row">
    <div class="col-md-4">
        <!-- Clock In/Out Form -->
        <div class="card shadow-lg mb-4 border-info">
            <div class="card-header bg-info text-white">
                <h4 class="mb-0">Time Clock</h4>
            </div>
            <div class="card-body">
                <form method="POST" action="{{ url_for('clock') }}">
                    <div class="mb-3">
                        <label for="employee_id" class="form-label fw-bold">Select Employee</label>
                        <select class="form-select form-select-lg rounded-3" id="employee_id" name="employee_id" required>
                            <option value="">-- Choose Employee --</option>
                            {% for employee in employees %}
                            <option value="{{ employee.id }}">{{ employee.name }} ({{ employee.position or 'N/A' }})</option>
                            {% endfor %}
                        </select>
                    </div>
                    <div class="mb-4">
                        <label class="form-label fw-bold">Action</label>
                        <div class="d-flex justify-content-around">
                            <div class="form-check form-check-inline">
                                <input class="form-check-input" type="radio" name="clock_type" id="clock_in" value="IN" required>
                                <label class="form-check-label text-success fw-bold" for="clock_in">✅ Clock IN</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input class="form-check-input" type="radio" name="clock_type" id="clock_out" value="OUT" required>
                                <label class="form-check-label text-danger fw-bold" for="clock_out">❌ Clock OUT</label>
                            </div>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary btn-lg w-100 shadow-sm rounded-3">Submit Time</button>
                </form>
            </div>
        </div>
    </div>
    <div class="col-md-8">
        <!-- Today's Attendance Log -->
        <div class="card shadow-lg border-success">
            <div class="card-header bg-success text-white">
                <h4 class="mb-0">📅 Today's Attendance Log ({{ datetime.utcnow().strftime('%Y-%m-%d') }})</h4>
            </div>
            <div class="card-body">
                <table class="table table-striped table-hover">
                    <thead class="table-light">
                        <tr>
                            <th>Employee</th>
                            <th>Time (UTC)</th>
                            <th>Type</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for record in attendance_records %}
                        <tr>
                            <td>{{ record.employee.name }}</td>
                            <td>{{ record.timestamp.strftime('%H:%M:%S') }}</td>
                            <td>
                                <span class="badge rounded-pill bg-{% if record.type == 'IN' %}success{% else %}danger{% endif %} p-2">
                                    {{ record.type }}
                                </span>
                            </td>
                        </tr>
                        {% else %}
                        <tr>
                            <td colspan="3" class="text-center text-muted py-3">No attendance recorded today.</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
{% endblock %}


5. templates/employees.html (Employee CRUD)

Save this content as templates/employees.html.

{% extends "base.html" %}
{% block content %}
<h2 class="mb-4 text-info">⚙️ Employee Management (CRUD)</h2>

<div class="row mb-4">
    <div class="col text-end">
        <!-- Button to trigger Add Employee Modal -->
        <button type="button" class="btn btn-primary btn-lg shadow" data-bs-toggle="modal" data-bs-target="#addEmployeeModal">
            ➕ Add New Employee
        </button>
    </div>
</div>

<div class="card shadow-lg">
    <div class="card-header bg-dark text-white">
        <h4 class="mb-0">Current Employees</h4>
    </div>
    <div class="card-body">
        <table class="table table-striped table-hover">
            <thead class="table-light">
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Position</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for employee in employees %}
                <tr>
                    <td>{{ employee.id }}</td>
                    <td>{{ employee.name }}</td>
                    <td>{{ employee.position or '—' }}</td>
                    <td>
                        <!-- Edit Button (triggers specific Update Modal) -->
                        <button type="button" class="btn btn-sm btn-info text-white me-2" 
                                data-bs-toggle="modal" data-bs-target="#updateEmployeeModal{{ employee.id }}">
                            <i class="fas fa-edit"></i> Edit
                        </button>
                        
                        <!-- Delete Form -->
                        <form action="{{ url_for('delete_employee', id=employee.id) }}" method="POST" class="d-inline"
                              onsubmit="return confirm('Are you sure you want to delete {{ employee.name }}? This will permanently delete ALL their attendance records!');">
                            <button type="submit" class="btn btn-sm btn-danger">
                                <i class="fas fa-trash"></i> Delete
                            </button>
                        </form>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        
        {% if not employees %}
        <p class="text-center text-muted mt-3 py-3">No employees found in the system.</p>
        {% endif %}
    </div>
</div>

<!-- ==================================== -->
<!-- MODALS SECTION -->
<!-- ==================================== -->

<!-- 1. Add New Employee Modal -->
<div class="modal fade" id="addEmployeeModal" tabindex="-1" aria-labelledby="addEmployeeLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content rounded-3 shadow">
            <div class="modal-header bg-primary text-white">
                <h5 class="modal-title" id="addEmployeeLabel">Add New Employee</h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <form action="{{ url_for('add_employee') }}" method="POST">
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="name" class="form-label">Employee Name</label>
                        <input type="text" class="form-control" id="name" name="name" required>
                    </div>
                    <div class="mb-3">
                        <label for="position" class="form-label">Job Position (Optional)</label>
                        <input type="text" class="form-control" id="position" name="position">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    <button type="submit" class="btn btn-success">Save Employee</button>
                </div>
            </form>
        </div>
    </div>
</div>

<!-- 2. Update Employee Modals (one for each employee) -->
{% for employee in employees %}
<div class="modal fade" id="updateEmployeeModal{{ employee.id }}" tabindex="-1" aria-labelledby="updateEmployeeLabel{{ employee.id }}" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content rounded-3 shadow">
            <div class="modal-header bg-info text-white">
                <h5 class="modal-title" id="updateEmployeeLabel{{ employee.id }}">Update Employee: {{ employee.name }}</h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <form action="{{ url_for('update_employee', id=employee.id) }}" method="POST">
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="name{{ employee.id }}" class="form-label">Employee Name</label>
                        <input type="text" class="form-control" id="name{{ employee.id }}" name="name" value="{{ employee.name }}" required>
                    </div>
                    <div class="mb-3">
                        <label for="position{{ employee.id }}" class="form-label">Job Position</label>
                        <input type="text" class="form-control" id="position{{ employee.id }}" name="position" value="{{ employee.position or '' }}">
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    <button type="submit" class="btn btn-info text-white">Save Changes</button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endfor %}
{% endblock %}


6. templates/attendance.html (Full Log & CSV Export)

Save this content as templates/attendance.html.

{% extends "base.html" %}
{% block content %}
<h2 class="mb-4 text-warning">📜 Full Attendance Log</h2>

<div class="row mb-3">
    <div class="col text-end">
        <!-- Export Functionality -->
        <a href="{{ url_for('export_csv') }}" class="btn btn-warning btn-lg shadow">
            ⬇️ Export ALL Attendance to CSV
        </a>
    </div>
</div>

<div class="card shadow-lg">
    <div class="card-header bg-dark text-white">
        <h4 class="mb-0">All Time Clock Records</h4>
    </div>
    <div class="card-body">
        <table class="table table-hover table-bordered">
            <thead class="table-light">
                <tr>
                    <th>ID</th>
                    <th>Employee Name</th>
                    <th>Date & Time (UTC)</th>
                    <th>Type</th>
                </tr>
            </thead>
            <tbody>
                {% for record in attendance_records %}
                <tr>
                    <td>{{ record.id }}</td>
                    <td>{{ record.employee.name }}</td>
                    <td>{{ record.timestamp.strftime('%Y-%m-%d %H:%M:%S') }}</td>
                    <td>
                        <span class="badge rounded-pill bg-{% if record.type == 'IN' %}success{% else %}danger{% endif %} p-2">
                            {{ record.type }}
                        </span>
                    </td>
                </tr>
                {% else %}
                <tr>
                    <td colspan="4" class="text-center text-muted py-3">No attendance records found yet.</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
{% endblock %}


7. templates/summary.html (Hours Calculation)

Save this content as templates/summary.html.

{% extends "base.html" %}
{% block content %}
<h2 class="mb-4 text-secondary">📊 Total Work Hours Summary</h2>

<div class="card shadow-lg">
    <div class="card-header bg-secondary text-white">
        <h4 class="mb-0">Employee Work Hours Calculation (IN to OUT)</h4>
        <p class="mb-0 small fst-italic">Note: Calculates duration between first IN and last OUT per day.</p>
    </div>
    <div class="card-body">
        <div class="table-responsive">
            <table class="table table-striped table-bordered align-middle">
                <thead class="table-light">
                    <tr>
                        <th class="text-nowrap">Employee Name</th>
                        <th class="text-nowrap text-center">Total Hours Worked (All Time)</th>
                        <th>Daily Breakdown (Latest 10 Days)</th>
                    </tr>
                </thead>
                <tbody>
                    {% for name, data in summary_data.items() %}
                    <tr>
                        <td class="fw-bold">{{ name }}</td>
                        <td class="text-center">
                            <span class="badge bg-success fs-6 p-2 shadow-sm">{{ data.total_hours }}</span>
                        </td>
                        <td>
                            <ul class="list-group list-group-flush border-0">
                            {% for date, hours in data.daily_breakdown.items() | sort(attribute='0', reverse=true) | list | slice(0, 10) %}
                                <li class="list-group-item d-flex justify-content-between align-items-center py-1 px-0 border-0">
                                    <strong class="text-muted">{{ date }}</strong>
                                    {% if hours == "Clocked IN, No OUT" %}
                                        <span class="badge bg-danger rounded-pill">{{ hours }}</span>
                                    {% else %}
                                        <span class="badge bg-primary rounded-pill">{{ hours }}</span>
                                    {% endif %}
                                </li>
                            {% else %}
                                <li class="list-group-item py-1 px-0 border-0 text-center text-muted small">No completed shifts recorded.</li>
                            {% endfor %}
                            </ul>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>
{% endblock %}


This provides all the code you need in one file, ready for deployment!
