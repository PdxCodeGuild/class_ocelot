

# Lab 5: Todo2

Refer to [the previous solution](../solutions/todoproj) for some inspiration.

### Models


- **TodoList** represents a todo list which has many todo items. A TodoList should at least have a **name**, and a foreign key to **User**.

- **TodoItem** represents a todo item and contains at least some **text** and a foreign key to TodoList. You may also want to include a **created date** and a **completed date**.


### Pages

- Login / Register: This can be a single page or two pages. There should be two forms, one for logging a user in and one for registering them. Once logged-in or registered, a user should be redirected to the List of TodoLists page.

- List of TodoLists: List all the Todo Lists for the logged-in user. This page should be protected, meaning you cannot access it without being logged in.

- List of TodoItems for a given TodoList. The user should at lease be able to add an item to the todo list. You may also allow them to delete and/or complete an item.


