# Workout Log

This is a REST API supporting the workout-log app. 

Supported functionality:
- Register a User
- Login
- Complete profile
- Update profile
- Plan and Track workouts

## Usage
### Register a user
`POST /register`

EXAMPLE:
```
http://192.81.215.35/register

{
    "first_name":"Abadan",
    "last_name": "Kano",
    "email": "kano87@gmail.com",
    "password": "kano87",
    "phone_number": "0700123458"
}
```

Response:
```
{
    "message": "registration, successful",
    "user": {
        "phone_number": "0700123458",
        "first_name": "Abadan",
        "user_id": "02ccb40e-79dd-4d9a-9df0-0bcc2de4b5f2",
        "last_name": "Kano",
        "email": "kano87@gmail.com"
    }
}
```

### Login a User
`POST /login`

EXAMPLE:
```
http://192.81.215.35/login

{
    "email": "kano87@gmail.com",
    "password": "kano87"
}
```
Response:
```
{
    "message": "login successful",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MTE3NjA3MywianRpIjoiZjhjMTZjYWUtMmI2Mi00YTUzLThmMGQtZTQ3Nzg5NmVmYjFlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjAyY2NiNDBlLTc5ZGQtNGQ5YS05ZGYwLTBiY2MyZGU0YjVmMiIsIm5iZiI6MTY2MTE3NjA3MywiZXhwIjoxNjYxMjYyNDczfQ.VrikfaSv_IJY1Z69cZf6NPKDOxFuC04vWCS9mCKn98M",
    "user_id": "02ccb40e-79dd-4d9a-9df0-0bcc2de4b5f2"
}
```

### Create a profile
`POST /profile`

EXAMPLE:
```
http://192.81.215.35/profile

{
    "user_id":"02ccb40e-79dd-4d9a-9df0-0bcc2de4b5f2",
    "sex": "FEMALE",
    "date_of_birth": "1998-08-22",
    "weight":61.7,
    "height":172
}
```
Response:
```
{
    "date_of_birth": "1998-08-22",
    "profile_id": "dd6b9b7b-9064-45aa-b171-cfc631fc9b9d",
    "sex": "FEMALE",
    "user_id": "02ccb40e-79dd-4d9a-9df0-0bcc2de4b5f2",
    "height": 172,
    "weight": 61.7
}
```

### Update Profile
`PUT /profile`

EXAMPLE:
```
http://192.81.215.35/profile/dd6b9b7b-9064-45aa-b171-cfc631fc9b9d

{
    "weight":65
}
```
Response:
```
{
    "date_of_birth": "1998-08-22",
    "profile_id": "dd6b9b7b-9064-45aa-b171-cfc631fc9b9d",
    "sex": "FEMALE",
    "user_id": "02ccb40e-79dd-4d9a-9df0-0bcc2de4b5f2",
    "height": 172,
    "weight": 65.0
}
```
