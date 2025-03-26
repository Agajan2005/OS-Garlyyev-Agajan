from flask import request, jsonify
from app.services.fibonacci import FibonacciService
from app.utils.error_handlers import handle_api_errors

@handle_api_errors
def fibonacci_endpoint():
    n = request.args.get('n', type=int)
    if n is None:
        raise ValueError("Missing required parameter 'n'")
    
    sequence = FibonacciService.generate(n)
    return jsonify({
        "status": "success",
        "data": sequence,
        "metadata": {"length": len(sequence)}
    })
