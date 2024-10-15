| **Test Case** | **Action**                                           | **Expected Output**                          | **Notes**                                             |
|---------------|------------------------------------------------------|---------------------------------------------|-------------------------------------------------------|
| **Test 1**    | Add contacts to the directory                       | "Adding contacts to the directory:"        | Insert "Paul", "Abhi", "Pawar"                       |
|               | `bst.insert("Paul", "5307175985")`                 |                                             |                                                       |
|               | `bst.insert("Abhi", "5307175984")`                  |                                             |                                                       |
|               | `bst.insert("Pawar", "5307175983")`                 |                                             |                                                       |
| **Test 2**    | Display all contacts in sorted order                | `Abhi: 5307175984`<br>`Paul: 5307175985`<br>`Pawar: 5307175983` | Check the order of contacts                           |
|               | `bst.display_directory()`                            |                                             | Expected order: Abhi, Paul, Pawar                    |
| **Test 3**    | Find a contact                                      | Finding 'Paul': `5307175985`               | Search for existing and non-existing contact          |
|               | `bst.search("Paul")`                                |                                             | Expected: 5307175985                                  |
|               | `bst.search("David")`                              | Sorry, David not found                      |                                                       |
| **Test 4**    | Remove a contact with no children (Abhi)           | Removing 'Abhi' (no children):             | Display the directory after removal                   |
|               | `bst.delete("Abhi")`                               | `Paul: 5307175985`<br>`Pawar: 5307175983` | Expected: Paul, Pawar                                 |
| **Test 5**    | Remove a contact with one child (Pawar)            | Removing 'Pawar' (one child):              | Display the directory after removal                   |
|               | `bst.delete("Pawar")`                              | `Paul: 5307175985`                         | Expected: Paul                                       |
| **Test 6**    | Remove the last contact (Paul)                      | Removing 'Paul':                           | Directory should be empty                             |
|               | `bst.delete("Paul")`                               | (No output)                                | Expected: No output, directory should be empty        |
