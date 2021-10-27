# GreenThumb - API


## Headers

Requests to endpoints requiring authentication should set the Authorization header to **Token <token>**, where **<token>** is the token received in the login response.

POST requests with a body should set the **Content-Type** header to **application/json**

.

## Login

https://questionbox-team-skywalker.herokuapp.com/auth/token/login/

### request

```jsx
POST auth/token/login/

{
"username": "admin",
"password": "somepassword"
}
```

### response

```jsx
200 OK

{
"auth_token": "c312049c7f034a3d1b52eabc2040b46e094ff34c"
}
```

## Logout

https://questionbox-team-skywalker.herokuapp.com/auth/token/logout/

### request

```jsx
POST auth/token/logout/
```

### response

```jsx
HTTP_204_NO_CONTENT
```

## Register

https://questionbox-team-skywalker.herokuapp.com/auth/users/

### request

username, first_name, last_name, email, password, re_password are required fields.

```jsx
POST auth/users/

{
	"username": "batman",
	"first_name": "Bruce",
	"last_name": "Wayne",
	"email": "batman@email.com",
	"password": "thisispassword",
	"re_password": "thisispassword"
}
```

### response

```jsx
201 Created

{
  "first_name": "Bruce",
  "last_name": "Wayne",
  "email": "batman@email.com",
  "username": "batman",
  "id": 8
}
```

## Profile

https://questionbox-team-skywalker.herokuapp.com/auth/users/me

### request

Requires authentication.

```jsx
GET auth/users/me
```

### response

```jsx
200 OK

{
    "pk": 1,
    "username": "luke",
    "email": "",
    "questions": [
      {
        "pk": 1,
        "title": "Do lilies require direct sun?",
        "owner": "luke",
        "created_at": "Sep. 15, 2021 at 07:13 PM",
        "favorited_by": [
          "leia",
          "luke",
          "anakin"
        ],
        "answer_count": {
          "id__count": 4
        }
      }
    ],
    "answers": [
      {
        "pk": 14,
        "body": "Test",
        "created_at": "Sep. 19, 2021 at 09:29 PM",
        "accepted": false,
        "owner": "luke",
        "question": "Do lilies require direct sun?",
        "favorited_by": []
      },
      {
        "pk": 13,
        "body": "Test",
        "created_at": "Sep. 19, 2021 at 08:43 PM",
        "accepted": false,
        "owner": "luke",
        "question": null,
        "favorited_by": []
      },
      {
        "pk": 12,
        "body": "Test",
        "created_at": "Sep. 19, 2021 at 07:27 PM",
        "accepted": false,
        "owner": "luke",
        "question": "Do lilies require direct sun?",
        "favorited_by": []
      }
    ]
  }
```

## List Questions

https://questionbox-team-skywalker.herokuapp.com/api/questions/

### request

```jsx
GET api/questions/
```

### response

```jsx
200 OK

{
    "pk": 9,
    "title": "How close should bulbs be planted?",
    "owner": "admin",
    "created_at": "Sep. 17, 2021 at 07:24 PM",
    "favorited_by": [],
    "answer_count": {
      "id__count": 0
    }
  },
  {
    "pk": 8,
    "title": "How close should bulbs be planted?",
    "owner": "admin",
    "created_at": "Sep. 16, 2021 at 08:00 PM",
    "favorited_by": [],
    "answer_count": {
      "id__count": 0
    }
  },
  {
    "pk": 7,
    "title": "When should I plant tulips in PA?",
    "owner": "luke",
    "created_at": "Sep. 16, 2021 at 02:05 AM",
    "favorited_by": [
      "C3PO"
    ],
    "answer_count": {
      "id__count": 2
    }
```

## Search Questions

hhttps://questionbox-team-skywalker.herokuapp.com/api/questions/?search={searchterm}

Users can search and get results referencing the title and owner.

### request

```jsx
GET api/questions/?search=bulbs
```

### response

```jsx
200 OK

{
    "pk": 9,
    "title": "How close should bulbs be planted?",
    "owner": "admin",
    "created_at": "Sep. 19, 2021 at 11:02 PM",
    "favorited_by": [],
    "answer_count": {
      "id__count": 0
    }
  },
  {
    "pk": 3,
    "title": "How close should I plant bulbs?",
    "owner": "leia",
    "created_at": "Sep. 16, 2021 at 01:22 AM",
    "favorited_by": [],
    "answer_count": {
      "id__count": 0
    }
  }
```

## Create a question

https://questionbox-team-skywalker.herokuapp.com/api/questions/

### request

Title is a required field.

```jsx
POST api/questions/

{
  "title": "How close should bulbs be planted?",
  "body": "Working on my spring garden plans."
}
```

### response

```jsx
201 Created

{
  "pk": 8,
  "title": "How close should bulbs be planted?",
  "body": "Working on my spring garden plans.",
  "owner": "admin",
  "created_at": "Sep. 16, 2021 at 08:00 PM"
}
```

## Question Detail

https://questionbox-team-skywalker.herokuapp.com/api/questions/pk/

### request

Requires authentication.

```jsx
GET api/questions/7/
```

### response

```jsx
200 OK

{
  "pk": 7,
  "title": "When should I plant tulips in PA?",
  "body": "",
  "owner": "luke",
  "created_at": "Sep. 16, 2021 at 02:05 AM",
  "favorited_by": [
    "C3PO"
  ],
  "answers": [
    {
      "pk": 8,
      "body": "Fall is the best time to plant spring flowering bulbs. Here in Maine, that means between September and November. However, bulbs can be planted even if winter frost has appeared as long as the soil or compost is easily cultivated.",
      "created_at": "Sep. 16, 2021 at 02:06 AM",
      "accepted": true,
      "owner": "leia",
      "question": 7,
      "favorited_by": [
        "C3PO"
      ]
    },
    {
      "pk": 9,
      "body": "It's important to plant tulips at the proper time to ensure healthy growth. For USDA hardiness zones seven and below, tulip bulbs should be planted in the fall before frost arrives. For zones eight and above, plant bulbs in late December or January to see spring blooms.",
      "created_at": "Sep. 16, 2021 at 02:06 AM",
      "accepted": false,
      "owner": "C3PO",
      "question": 7,
      "favorited_by": []
    }
  ]
}
```

## Edit Question

https://questionbox-team-skywalker.herokuapp.com/api/questions/pk/

### request

Requires authentication. 

Only owner can edit. 

Question may not be edited after it has answers. (not functional yet, still working on it)

Title is a required field.

```jsx
PUT api/questions/7/

{
	"title": "updating this bby again",
	"body": "Fingers crossed this works."
}
```

### response

```jsx
200 OK

{
  "pk": 11,
  "title": "updating this bby again",
  "body": "Fingers crossed this works.",
  "owner": "admin",
  "created_at": "Sep. 21, 2021 at 10:27 AM"
}
```

## Delete a Question

https://questionbox-team-skywalker.herokuapp.com/api/questions/pk/

### request

Requires authentication. 

Only owner may delete.

```jsx
DELETE api/questions/7/
```

### response

```jsx
204 No Content
```

## Create an answer

https://questionbox-team-skywalker.herokuapp.com/api/answers/new

### request,

Requires authentication. 

Must pass through a question's primary key.

body and question are required fields.

```jsx
POST api/answers/new

{
	"question": "{pk}"
	"body": "Test"
}
```

### response

```jsx
201 Created

{
  "pk": 11,
  "body": "Test",
  "owner": "luke",
  "question": {pk},
  "created_at": "Sep. 19, 2021 at 06:55 PM"
}
```

## Add Favorited

https://questionbox-team-skywalker.herokuapp.com/api/questions/pk/

### request

Requires authentication. 

```jsx
PATCH api/questions/7/
```

### response

```jsx
200 OK

{
  "pk": 11,
  "title": "updating this bby again",
  "body": "Fingers crossed this works.",
  "owner": "admin",
  "created_at": "Sep. 21, 2021 at 10:27 AM",
  "favorited_by": [
    "admin",
    "luke" (Username is added to list based on token authentication)
  ],
  "answers": []
}
```

## Accepted Answer

https://questionbox-team-skywalker.herokuapp.com/api/answers/pk

### request

Requires authentication. 

Currently not limited by question owner to accept.

```jsx
PATCH api/answers/16/

{
	"accepted": true
}
```

### response

```jsx
200 OK

{
  "pk": 16,
  "body": "but I guess I am using luke",
  "created_at": "Sep. 21, 2021 at 01:52 PM",
  "accepted": true,
  "owner": "luke",
  "question": "updating this bby again and again to check, with forbidden",
  "favorited_by": []
}
```
