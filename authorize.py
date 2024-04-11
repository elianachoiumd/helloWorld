# importing Flask libraries
from flask_login import current_user
from flask import render_template, flash, current_app
from functools import wraps

# Establishing roles permitted
def role_required(roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            #Identifies if a user's role is a valid role
            if current_user and current_user.role in roles:
                pass
            else:
            #Message returned if not a valid role and redirect to access denial page
                flash('You do not have permission to access this function.', 'error')
                return render_template('access_denied.html')
            if callable(getattr(current_app, "ensure_sync", None)):
                return current_app.ensure_sync(func)(*args, **kwargs)
            return func(*args, *kwargs)
        return wrapper
    return decorator