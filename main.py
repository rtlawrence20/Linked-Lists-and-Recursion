from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    print("\n--- LINKED LIST ---\n")

    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert some sample data using insert_at_front or insert_at_end
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(5)

    # 3) Display the list to verify insertion
    print("Initial list:")
    ll.display()

    # 4) Call recursive_sum and print the result
    total = ll.recursive_sum()
    print(f"\nSum of all nodes (recursive): {total}")

    # 5) Call recursive_search with a target and print result
    target = 10
    found = ll.recursive_search(target)
    print(f"\nSearching for {target}: {'Found' if found else 'Not Found'}")

    # 6) Call recursive_reverse, then display the reversed list
    print("\nReversing list (recursive)...")
    ll.recursive_reverse()

    print("Reversed list:")
    ll.display()
