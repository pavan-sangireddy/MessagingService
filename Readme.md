I have used basic Abstract classes design in the application

There are two kinds of users in the normal chat:
1. Admin User
2. Normal user

We defined an abstract class with common functionalities of user and implement them in both the cases
If a normal user is not allowed to edit a user, we can simply throw an error.

Using Common class makes code easily readable.

Parameters can be added in remaining classes. This was the basic LLD of the use case I could think of.
Also, we can use an SQL and Non - SQL Databases for differnt use cases.

For example,
For storing username, password - we can resort to normal SQL DB.
but for storing the reactions of a message -> Non SQL database makes sense.

Apologies, I could not implement the whole functional API, I can quote this design as my mini LLD.