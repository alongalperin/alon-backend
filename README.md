## Alon Home Assignment ##
---

**Base url:** https://alon-backend.herokuapp.com/api/v1

### Write Message ###
----
  Creates message on the server.

* **URL**

  /messages

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
   `messages-user=[string]` - The sender is a parameter in the headers of the request. This mimic a situation of user after login.
   `receiver=[string]`
   `subject=[string]`
   `message=[string]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12, name : "Michael Bloom" }`
 
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
