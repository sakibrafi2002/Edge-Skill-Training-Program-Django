# SOLID principle

***S*** -> Single Dependency principle : A class must perform a single task.</br>
***O*** -> Open Close principle : A core or parent class is closed for modifications and open for extension (child class).</br>
***L*** -> Liskov substitution principle: The child class must support all the method of parent class, otherwise substitute the parent class in other different classes.</br>
***I*** -> Interface segregation principle : If a parent class contains methods where some child explicitly use some method and the other use the other methods, then separate these feature by having multiple parent class so that it does not have any impact on other.</br>
***D*** -> Dependency inversion principle : The higher level classes (parent) must not depend on lower (child) level  class.</br>

## **By Chatgpt:**
Certainly! Here’s a corrected and organized explanation of the SOLID principles:

### SOLID Principles

**S - Single Responsibility Principle (SRP)**  
A class should have only one reason to change, meaning it should only perform one task or responsibility. This makes the class easier to understand, maintain, and test.

---

**O - Open/Closed Principle (OCP)**  
Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means you can add new functionality (via child classes or modules) without changing existing code, reducing the risk of introducing bugs.

---

**L - Liskov Substitution Principle (LSP)**  
Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. In other words, a subclass should be able to stand in for its parent class without altering the desired behavior.

---

**I - Interface Segregation Principle (ISP)**  
Clients should not be forced to depend on interfaces they do not use. Instead of a large, general-purpose interface, it’s better to have several smaller, specific interfaces. This way, classes only need to implement the methods that are relevant to them.

---

**D - Dependency Inversion Principle (DIP)**  
High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g., interfaces). This encourages decoupling and makes the system easier to modify and extend.

---
