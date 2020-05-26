# order_manager
Class OrderManager stores hashable values in ordered sequence.

This can be used if you need to control the order of some objects.
For example, you have Django model objects which handles articles for a web page. 
So, if you want to show these articles on the page in particular order, and also you want to have an ability to change this order, you can use class OrderManager to remember the order of your articles.

__init__
When you initialize an OrderManager object, it creates an empty dict() to store your objects.
You can access this dict at any time by interface with .sequence variable.

add_key(key)
You can pass a key to add_key function to add it into the sequence.
Given key extends sequence by one and save the given key to the end of the sequence by giving it last index number.
Key must be a hashable object, as it will be used as a key for a dict().
For example, you may give a primary_key from database (or a Django model).

get_key_by_index(index)
You can get a key by it's sequence index.

change_key_index(index_from, index_to)
If you want to change the order in sequence, use change_key_index function.
For example, you have a sequence: {'Key1': 0, 'Key2': 1, 'Key3': 2, 'Key4': 3}. 
Now you want that Key3 will stand in the 1st place: change_key_index(2, 0).
After it we get our sequence changed to: {'Key1': 1, 'Key2': 2, 'Key3': 0, 'Key4': 3}. 

delete_key(key)
If you no longer want to keep any key in sequence, just call delete_key() and OrderManager automatically removes given key value and rearrange the indexes.

Additional.
You can iterate through an OrderManager object in loops or any other context.
It also supports standart len() function and str() representation.
