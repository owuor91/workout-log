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
`PUT /profile/<profile_id>`

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
### Exercise Categories
`GET /exercise-categories`

EXAMPLE:
```
http://192.81.215.35/exercise-categories
```
Response:
```
[
    {
        "category_id": "b4ee9800-fa15-496e-b820-f5daa41dc4fd",
        "category_name": "Chest"
    },
    {
        "category_id": "9ff3ea05-8265-4fdc-9818-f91ef05f19a3",
        "category_name": "Legs"
    },
    {
        "category_id": "1a51f824-aa80-496d-814c-c6e56297b8a1",
        "category_name": "Shoulders"
    },
    {
        "category_id": "8d2b9e1c-e6d8-46c6-99a1-d603ffe94f78",
        "category_name": "Back"
    }
]
```
### Exercises
`GET /exercises`

EXAMPLE:
```
http://192.81.215.35/exercises
```
Response:
```
[
    {
        "description": "",
        "exercise_id": "378c42b0-e8e8-4eed-bb83-7fd58b39b2a1",
        "image": "https://abc.xyz/123.jpg",
        "category_id": "9ff3ea05-8265-4fdc-9818-f91ef05f19a3",
        "exercise_name": "Barbell squat"
    },
    {
        "description": "",
        "exercise_id": "842bcbb9-0e67-42a4-a77e-c453d21e9e1f",
        "image": "https://abc.xyz/456.jpg",
        "category_id": "9ff3ea05-8265-4fdc-9818-f91ef05f19a3",
        "exercise_name": "Calf raises"
    },
    {
        "description": "",
        "exercise_id": "2079a742-3458-4497-a980-49ce5bfcb83f",
        "image": "https://abc.xyz/789.jpg",
        "category_id": "9ff3ea05-8265-4fdc-9818-f91ef05f19a3",
        "exercise_name": "Cable leg extensions"
    }
]
```