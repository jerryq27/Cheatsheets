# Spring

Spring is a framework for building complex Java applications. One
of the more common use cases is for web applications.

## Basics

Spring projects are built by bringing certain dependencies together using
the [Spring Initializer](https://start.spring.io).

Alternatively, the initializer can generate a project from the command line:

```bash
$ mkdir sample && cd sample;
$ curl https://start.spring.io/starter.zip -d language=$LANG -d dependencies=$DEP1,$DEP2,$DEP3 -d packageName=$PKG -d name=$NAME -d type=$TYPE -o $ZIP
```

1. `$LANG` - can be either _java_ or _kotlin_.
1. `$DEP` - dependencies like web, jpa, h2, etc.
1. `$PKG` - package name like 'com.example.sample'.
1. `$NAME` - project name like 'Sample'.
1. `$TYPE` - build type like 'gadle-project' or 'maven-project'.
1. `$ZIP` - output *.zip file name.

Some common dependencies are:

* Spring Web - Provides functionality to create RESTful APIs/Web applications.
* Spring JPA - Provides functionality to connect with databases.
* Spring H2 - Fast in-memory database, good for testing without downloading/setting up a real database.
* Spring Boot Actuator - Pre-defined API endpoints for checking health and status of the application.
* Spring Boot Developer Tools - Developer tools like automatic reloads on file changes.


## Workflow

### Data Access Objects

Spring  has DAOs, but in Spring these objects are known as _Repositories_. To create a repository,
the Entitiy and it's Id type are needed in a Java interface:

```java
public interface HobbitRepository extends CrudRepository<Hobbit, Integer> {

    Hobbit findHobbitById(Integer id);

}
```

## Model View Controller Pattern
### Model

Models in Spring are called Entities and a marked with the `@Entity` annotation.

```java
@Entity
public class Hobbit {
    
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer id;

    private String firstName;
    private String lastName;

    public Hobbit(String fname, String lname) {
        firstName = fname;
        lastName = lname;
    }
    /*
     * Getters and setters..
     */
}
```

Annotations:

* @Entity - 
- @Id
- @GeneratedValue

### View
### Controller

Spring Web Controllers are the same as other framework controllers. They handle
HTTP requests by mapping API endpoints to functions. In Spring Web, classes
with the marker annotation `@RestController` are able to define these methods:

```java
@RestController
public class HobbitController {

    @Autowired
    private HobbitRepository hobbitRepo;

    @GetMapping("/list")
    public List<Hobbit> getHobbits() {
        return List.of(
            new Hobbit("Frodo", "Baggins"),
            new Hobbit("Samwise", "Gamgee")
        );
    }

    @PostMapping("/add")
    public String addHobbit(@RequestParam String first, @RequestParam String last) {
        Hobbit hobbit = new Hobbit(first, last);
        hobbitRepo.save(hobbit);

        return "Added new hobbit: " + first;
    }

    @GetMapping("/find/{id}")
    public Hobbit findHobbitById(@PathVariable Integer id) {
        return hobbitRepo.findHobbitById(id);
    }
}
```

Annotations:

* @RestController - marks a class as a _Controller_ and able to handle requests.
* @Autowired - to inject the object through Spring, this pattern is encouraged in Spring instead of manually creating these types of objects.
* @GetMapping - defines a **GET** request endpoint and marks the function as the handler.
* @PostMapping - defines a **POST** request endpoint and marks the funciton as the handler.
* @RequestParam - marks a parameter as a url query variable (values after '?').
* @PathVariable - maps the parameter with a '{}' variable in the defined endpoint.