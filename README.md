## Alon Home Assignment ##
---

**Base url:** https://alon-backend.herokuapp.com/api/v1

### Write Message ###
----
  Creates a message on the server.

* **URL**

  /messages

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
   
   None

* **Data Params**

   `messages-user=[string]` - The sender is a parameter in the headers of the request. This mimic a situation of user after login.
   `receiver=[string]`
   `subject=[string]`
   `message=[string]`

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:** `{'data': {'2e109eb2': {'sender': 'alon', 'receiver': 'test2', 'subject': 'Message head', 'message': 'Message body',
'id': '2e109eb2', 'date': '03/08/2020 12:49:38', 'is_read': False}}}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/users/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
