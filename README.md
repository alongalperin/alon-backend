## Alon Home Assignment ##
---

**Base url:** https://alon-backend.herokuapp.com/api/v1
  
----
### Write Message ###
  Creates a message on the server.

* **URL**

  /messages

* **Method:**

  `POST`
  
*  **URL Params**
   
   None
  
* **Data Params**
  
     **Required:**

   `messages-user=[string]` - The sender is a parameter in the headers of the request. This mimic a situation of user after login.
   `receiver=[string]`  
   `subject=[string]`  
   `message=[string]`  

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:** `{'data': {'2e109eb2': {'sender': 'alon', 'receiver': 'test2', 'subject': 'Message head', 'message': 'Message body',
'id': '2e109eb2', 'date': '03/08/2020 12:49:38', 'is_read': False}}}`
 
* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{'error': ['Please add messages-user parameter to the request header set the username as the value']}`
----  
  
### Get all messages for a specific user ###
  Get all messages of a specific **receiver**.

* **URL**

  `/users/<receiver-name>/messages`

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
   
   `receiver-name=[string]`
  
* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{'data': [{'sender': 'alon', 'receiver': 'test-user', 'subject': 'Message head', 'message': 'Message body', 'id':
'93b97cc1', 'date': '03/08/2020 16:41:14', 'is_read': False}]}}`
 
* **Error Response:**
  
  None
  
----  
### Get all unread messages for a specific user ###
  Get all unread messages of a specific **receiver**.

* **URL**

  `/users/<receiver-name>/messages/unread`

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
   
   `receiver-name=[string]`
  
* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{'data': [{'sender': 'alon', 'receiver': 'test-user', 'subject': 'Message head', 'message': 'Message body', 'id':
'93b97cc1', 'date': '03/08/2020 16:41:14', 'is_read': False}]}}`
 
* **Error Response:**
  
  None

----  
### Read message (return one message) ###
Changes the is_read of a specific message to true. Returns the message after the update.

* **URL**

  `/messages/<message_id>/read`

* **Method:**

  `PATCH`
  
*  **URL Params**

   **Required:**
   
   `message_id=[string]`
  
* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{'data': [{'sender': 'alon', 'receiver': 'test-user', 'subject': 'Message head', 'message': 'Message body', 'id':
'93b97cc1', 'date': '03/08/2020 16:41:14', 'is_read': True}]}}`
 
* **Error Response:**
  
  None
  
----  
  ### Delete message (as owner or as receiver) ###

Delete message by ID. This Method requires that the deleting user will be or the receiver or sender of the message.
The user is defined in the headers as messages-user.

* **URL**

  `/messages/<message_id>`

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
   
   `message_id=[string]`
  
* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{}`
 
* **Error Response:**
    * **Code:** 403 Forbidden <br />
    **Content:** `{'error': 'Only message sender or receiver can delete messages'}`
  
