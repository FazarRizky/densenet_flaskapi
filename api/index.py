from app import app  # Import Flask app dari file utama Anda
from werkzeug.wrappers import Response

def handler(request):
    with app.app_context():
        # Handle request dari Vercel
        path = request.path
        method = request.method
        headers = dict(request.headers)
        body = request.body
        
        # Simulate Flask request
        with app.test_request_context(
            path=path,
            method=method,
            headers=headers,
            data=body
        ):
            try:
                response = app.full_dispatch_request()
                return Response(
                    response=response.get_data(),
                    status=response.status_code,
                    headers=dict(response.headers)
                )
            except Exception as e:
                return Response(
                    response=str(e),
                    status=500,
                    headers={'Content-Type': 'application/json'}
                )