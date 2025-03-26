from flask import Flask
from app.api.fibonacci import fibonacci_endpoint
from app.api.palindrome import palindrome_endpoint
from app.api.linked_list import linked_list_endpoint

def create_app():
    app = Flask(__name__)
    
    # Регистрация endpoint'ов
    app.add_url_rule('/api/v1/fibonacci', view_func=fibonacci_endpoint, methods=['GET'])
    app.add_url_rule('/api/v1/palindrome', view_func=palindrome_endpoint, methods=['GET'])
    app.add_url_rule('/api/v1/linked-list/reverse', view_func=linked_list_endpoint, methods=['POST'])
    
    return app
