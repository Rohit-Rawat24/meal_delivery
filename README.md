->Meal_Info

In this project I have used MongoDB for NOSQL database,Jupyter,MongoDB Compass,PyMongo,Built-in packages like JSON and meal_info.json file.
As we are using MongoDB we can query and know about category of meal and the type of cuisine and meal has a unique id.
To query some of the commands which I have used are update_one,update_many,limit,find,drop.
To start with this first we will have to establish a connection between Jupyter and MongoDB and here PyMongo comes in handy, it establishes a connection between them. 
Every change done in Jupyter is being reflected in Compass.

# Service Function
->Search meal by meal_id, cuisine or the category of meal you wanna enjoy.

#Meal_info Service
1. insert_one():
  *It will insert one document in our collection.
  
2. insert_many():
  *It will insert multiple document in our collection.

3. find():
  *We can query by multiple conditions and it will give all the meals satisfying the condition.
  
4.find_one():
  *We can query by multiple conditions and it will give only one meal satisfying the condition.

5. update_many():
  *It is used to update multiple document using one command.

6. update_one():
  *It is used to update one document.

7. limit():
  *With the help of limit we can show the particular number of records we want to show.

8. skip():
  *It skips the number of records we don't want to see.

9. delete_one():
  *It deletes only one record which comes first.

10. delete_many():
  *It deletes multiple record satisfying the condition.

11.count():
  *It counts the number of documents present in our collection.

12. drop():
  *It is used to drop the collection from the database.It completely removes the collection from database. 
