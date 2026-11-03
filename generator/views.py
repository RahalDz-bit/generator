from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import string
@api_view(['GET'])
def home(request) :
    return Response({

        "message" : "Hello , how can i help you ?",
        "description" : "API that generate a username and a password from data given ."
    })

@api_view(['POST']) 
def generate_username(request) :
    response = {}
    name =  request.data.get('name')
    
    if not isinstance(name, str) or not name.strip() :
        return Response(
        {"error": "Name is required"},
        status=400
    )
    else :
        random_number1 = random.randint(1,100)
        random_number2 = random.randint(1,100)
        
        response.update({
            "usernames" :[ name+"_"+str(random_number1) ,"real."+name+"_"+str(random_number2) , name+ "2026",],

            "message": "Usernames generated successfully"

        })

    return Response(
        response
        
    )


@api_view (['POST']) 
def generate_password(request) :
    response = {}
    password = ''
    password_length = request.data.get('length')
    check_error = [
        request.data.get('include_uppercase'),
        request.data.get('include_lowercase'),
        request.data.get('include_numbers'),
        request.data.get('include_symbols')
    ]    
    elements =  [{"include_uppercase" : request.data.get('include_uppercase')},
                 {"include_lowercase" : request.data.get('include_lowercase')},
                 {"include_numbers" : request.data.get('include_numbers')},
                 {"include_symbols" : request.data.get('include_symbols')}]
    if check_error == [False, False, False , False] :
        response.update({
            'error' : 'wth bro ...'
        })
        return Response(
            response
        )
    while password_length > 0 :
        element = random.choice(elements)
        if list(element.values()) == [True] :
            if list(element.keys()) == ["include_uppercase"] :
                password+= random.choice(string.ascii_uppercase)
                
            elif list(element.keys()) == ["include_lowercase"] :
                password+= random.choice(string.ascii_lowercase)
                
            elif list(element.keys()) == ["include_numbers"] :
                password+= random.choice(string.digits)
                
            else :
                password+= random.choice(string.punctuation)

            password_length -= 1
            
    password_length = request.data.get('length')
    response.update({
                "password" : password,
                "length" : password_length,
                "message" : "The password is generated"
            })              

    return Response (
        response
    )