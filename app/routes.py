from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message
from app import mail

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
        
        # Create email content
        email_body = f"""
        New Message from TrueSparKles Website
        
        From: {name}
        Email: {email}
        Phone: {phone}
        Service Requested: {service}
        
        Message:
        {message}
        """
        
        try:
            # Send email to business
            msg = Message(
                subject='New Cleaning Service Inquiry',
                recipients=['truespakles@gmail.com'],  # Changed from info@truesparkles.com
                body=email_body
            )
            mail.send(msg)
            
            # Send confirmation email to customer
            confirmation_msg = Message(
                subject='Thank you for contacting TrueSparKles',
                recipients=[email],
                body=f"""
                Dear {name},
                
                Thank you for contacting TrueSparKles. We have received your inquiry and will get back to you shortly.
                
                Best regards,
                TrueSparKles Team
                """
            )
            mail.send(confirmation_msg)
            
            flash('Thank you for your message! We will get back to you soon.')
        except Exception as e:
            print(f"Error sending email: {e}")
            flash('There was an error sending your message. Please try again later.')
            
        return redirect(url_for('main.index')) 


