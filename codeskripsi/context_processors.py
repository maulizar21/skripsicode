# from django.conf import settings

def session_data(request):
    # Retrieve the session data you want to make available
    user_data = request.session.get('user_data')
    # Return a dictionary with the data
    return {'user_data': user_data}

def base_url(request):
    return {
        'base_url': request.scheme + '://' + request.get_host(),
    }