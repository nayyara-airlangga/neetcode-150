# Binary Tree

## References

- [Invert a Binary Tree (Python Code with example)](https://favtutor.com/blogs/invert-binary-tree)

## Overview

A binary tree is a data structure that arranges objects in a tree with each node containing an object and up to two additional nodes associated with the child objects. This structure is advantageous because of its ability to reorganize and easily retrieve data. Along with this, it has the benefits of both an ordered array and a linked list, making it easy to navigate and search within. A node of the binary tree has the following parts:

1. Data
2. Pointer to the right child
3. Pointer to the left child

![Binary Tree Example](https://favtutor.com/resources/images/uploads/mceu_29902051241637063815125.png)

### Preorder Traversal

A traversal visits the nodes of a tree in a systematic manner. In a preorder traversal, a node is visited before its descendants. Application: print a structured document

```
Algorithm preOrder(v)
  visit(v)
  for each child w of v
    preOrder(w)
```

## Visualizing Binary Trees as Arrays

We could imagine a tree as an array. To get the indexes of the child of a node, because of the nature of binary trees, we can calculate it as

- Left child = parent index \* 2 + 1
- Right child = parent index \* 2 + 2
