# 💻 Assignment 09 - Layered Architecture II
## Requirements
There are some new requirements for the program you've implemented for **A8**. 

1. Implement persistent storage for all entities using file-based repositories. For each entity, you will implement a text-file based repository and a binary-file based repository (using [Pickle](https://docs.python.org/3/library/pickle.html)). These will work alongside the existing repository that stores entities in memory. The program must work the same way using in-memory repositories, text-file repositories and binary file repositories. You can use inheritance in order to reuse existing repository source code.
2. Implement a `settings.properties` file to configure the application. The decision of which repositories are employed, as well as the location of the repository input files will be made in the program’s `settings.properties` file. An example is below:

    a. `settings.properties` for working with repositories that store entities in memory (in this case there are no input files):
    ```
    repository = inmemory
    cars = “”
    clients = “”
    rentals = “”
    ```
    b. `settings.properties` for working with repositories that store entities to binary files:
    ```
    repository = binaryfiles
    cars = “cars.pickle”
    clients = “clients.pickle”
    rentals = “rentals.pickle”
    ```
    
    **NB!** If your solution to **A8** uses layered architecture properly, these are the only places where source code needs to change:
    - *Repository layer* – for implementing the required code.
    - *Application start module* – to load the properties file and start the required repositories.

3. Implement unlimited undo/redo functionality using the [Command design pattern](https://refactoring.guru/design-patterns/command), which ensures a memory-efficient implementation of undo/redo operations. Each step will undo/redo the previous operation performed by the user. Undo/redo operations must cascade (e.g., deleting a student must also delete their grades; undoing the deletion must restore all deleted objects).
