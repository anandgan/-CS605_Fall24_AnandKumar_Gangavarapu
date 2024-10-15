class TreeNode:
    def __init__(self, contact):
        self.contact = contact  # (name, phone_number) tuple
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None  # The tree starts empty

    # Insert a new contact (name, phone number)
    def insert(self, name, phone_number):
        new_contact = (name, phone_number)
        self.root = self._insert(self.root, new_contact)

    def _insert(self, current_node, contact):
        if current_node is None:
            return TreeNode(contact)  # Base case: add a new node here
        if contact[0] < current_node.contact[0]:  # Compare names
            current_node.left = self._insert(current_node.left, contact)
        else:
            current_node.right = self._insert(current_node.right, contact)
        return current_node

    # Search for a phone number by name
    def search(self, name):
        found_node = self._search(self.root, name)
        if found_node:
            return found_node.contact[1]
        else:
            return f"Sorry, {name} not found in the directory."

    def _search(self, current_node, name):
        if current_node is None or current_node.contact[0] == name:
            return current_node
        if name < current_node.contact[0]:
            return self._search(current_node.left, name)
        return self._search(current_node.right, name)

    # Delete a contact by name
    def delete(self, name):
        self.root = self._delete(self.root, name)

    def _delete(self, current_node, name):
        if not current_node:
            return None

        if name < current_node.contact[0]:
            current_node.left = self._delete(current_node.left, name)
        elif name > current_node.contact[0]:
            current_node.right = self._delete(current_node.right, name)
        else:
            # Case: No child or one child
            if not current_node.left:
                temp = current_node.right
                current_node = None
                return temp
            elif not current_node.right:
                temp = current_node.left
                current_node = None
                return temp

            # Case: Two children, find the in-order successor (smallest in the right subtree)
            temp = self._find_min(current_node.right)
            current_node.contact = temp.contact
            current_node.right = self._delete(current_node.right, temp.contact[0])

        return current_node

    # Helper to find the minimum node
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # In-order traversal to display contacts in sorted order
    def display_directory(self):
        def inorder_traverse(node):
            if node:
                inorder_traverse(node.left)
                print(f"{node.contact[0]}: {node.contact[1]}")
                inorder_traverse(node.right)
        inorder_traverse(self.root)


# Test cases for BinarySearchTree
def test_phone_directory():
    bst = BinarySearchTree()

    # Test 1: Add contacts to the directory
    print("Adding contacts to the directory:")
    bst.insert("Paul", "5307175985")
    bst.insert("Abhi", "5307175984")
    bst.insert("Pawar", "5307175983")
    
    # Test 2: Display all contacts in the directory (in-order)
    print("\nDisplaying contacts in sorted order:")
    bst.display_directory()  # Expected order: Abhi, Paul, Pawar

    # Test 3: Find a contact
    print("\nFinding 'Paul':", bst.search("Paul"))  # Expected: 5307175985
    print("Finding 'David':", bst.search("David"))  # Expected: Sorry, David not found

    # Test 4: Remove a contact with no children (Abhi)
    print("\nRemoving 'Abhi' (no children):")
    bst.delete("Abhi")
    bst.display_directory()  # Expected: Paul, Pawar

    # Test 5: Remove a contact with one child (Pawar)
    print("\nRemoving 'Pawar' (one child):")
    bst.delete("Pawar")
    bst.display_directory()  # Expected: Paul

    # Test 6: Remove the last contact (Paul)
    print("\nRemoving 'Paul':")
    bst.delete("Paul")
    bst.display_directory()  # Expected: No output, directory should be empty

# Run the test cases
test_phone_directory()
