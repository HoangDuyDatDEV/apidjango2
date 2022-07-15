from api_weight.models import User

def checkLogin(username, password):
    try:
        user = User.objects.get(username=username, password=password)
        if user is not None: 
        
            return {
                'id': user.id,
                'username': user.username,
                'password': user.password,
            }
        else: 
            return {
                'id': None,
                'username': None,
                'password': None,
            }
    except: 
        print('CheckLogin ERROR')
        return False