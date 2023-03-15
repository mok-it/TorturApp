<h1>Documentation for developers</h1>
<h2>Basic information</h2>

- The language of the code is English (every variables, functions)
- Every variable and function should have an talking names
(obvious), so if you define a variable please be sure that
it has talking name.
If somebody read it they should know what hide this.
- Above every function please write a short documentation about the inputs, outputs and the what the function does
- Before you create a merge/pull request be sure there is no other. If there is than please review it.

<h2>Code syntax</h2>

- Files
  - Files should be written with snake_case
  - Example: main_window.py
- Classes
  - Classes should be written with CamelCase
  - Example: class MainWindow
- Functions
  - Functions should be written with camelCase
  - Example: def countTheExcercises()
  - Please write the input types and output type
  - Example: def increaseByOne(num: int) -> int
- Variables
  - Variables should be written with snake_case
  - Example: number_of_groups = 10
  - Please write the type of the variable
  - Example: number_of_groups : int = 10