
## annnounces-api built with Django Rest Framework and handle 'announces' and 'comments' crud operations 

## features:
- authentication system (BasicAuthentication SessionAuthentication TokenAuthentication)
- announces crud operations (hard-coded using class-based views)
- comments crud operations (hard-coded using class-based views)
    note: announces and comments models are very simple but you could extend the as you want


### using BasicAuthentication:
    http -a yourusername localhost:8000/announces/ title='announce 12'
    {
        "id": 10,
        "owner": "yourusername",
        "title": "announce 12",
    }

### using SessionAuthentication:
    use the borwsable API

### using TokenAuthentication:
    step 1- obtain auth token
    step 2- make post request with the Token 

    step 1: obtain auth token
        http POST localhost:8000/obtain-auth-token/ username='yourusername' password='yourusernamepassword'
        {
            "email": "yourusername@gmail.com",
            "token": "efa0b636c88325dcd8d5aacd6f45f00c6606274a",
            "user_id": 1,
        }

    step 2: make post request with the Token 
        http localhost:8000/announce/ title='announce 12' "Authorization: Token efa0b636c88325dcd8d5aacd6f45f00c6606274a"
        {
            "id": 11,
            "owner": "yourusername",
            "title": "announce 12",
        }



