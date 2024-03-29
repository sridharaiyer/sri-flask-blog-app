import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail
from threading import Thread


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    pic_filename = random_hex + f_ext
    pic_path = os.path.join(
        current_app.root_path, 'static/profile_pics', pic_filename)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(pic_path)
    return pic_filename

# -------------------------------------------------------------------------------------
# Following 2 functions, related to threading are not working due to an error message:
# RuntimeError: Working outside of application context.

# This typically means that you attempted to use functionality that needed
# to interface with the current application object in some way. To solve
# this, set up an application context with app.app_context().  See the
# documentation for more information.

# TODO: Fix later
# -------------------------------------------------------------------------------------
# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
#
#
# def send_reset_email(user):
#     token = user.get_reset_token()
#     msg = Message('Password Reset Request',
#                   sender='noreply@flaskblogdemo.com', recipients=[user.email])
#     msg.body = f'''
# To reset your password, visit the following link:
# {url_for('users.reset_token', token=token, _external=True)}
#
# If you did not receive this email then simply ignore this email and no changes will be made.
#     '''
#
#     # mail.send(msg)
#     Thread(target=send_async_email, args=(current_app, msg)).start()


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
