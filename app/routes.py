from flask import Blueprint, render_template, request, flash, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print("Rendering index.html")
    return render_template('index.html')

@main.route('/send-message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service = request.form.get('service')
        message = request.form.get('message')
        
        # Here you would typically:
        # 1. Save to database
        # 2. Send email notification
        # 3. Process the form data
        
        # For now, we'll just redirect back with a success message
        flash('Thank you for your message! We will get back to you soon.')
        return redirect(url_for('main.index')) 


