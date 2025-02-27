; Return the list of nodes on the k-th level of a tree of type (1).

; extract the left child of the current node
(defun left_traversal(l n m)
    (
        cond
        ((null l) nil)
        ((= n (+ 1 m)) nil)
        (t (cons (car l) (cons (cadr l) (left_traversal (cddr l) (+ 1 n) (+ (cadr l) m)))))
    )
)

; skips the left subtree and returns the rest of the tree after the current node's children.
(defun right_traversal(l n m)
    (
        cond
        ((null l) nil)
        ((= n (+ 1 m)) l)
        (t (right_traversal (cddr l) (+ 1 n) (+ (cadr l) m)))
    )
)

; returns the left subtree of the tree
(defun left(l)
  (left_traversal (cddr l) 0 0)
)

; returns the right subtree of the tree
(defun right(l)
  (right_traversal (cddr l) 0 0)
)

(defun nodes(L cnt lvl)
    (cond
        ((null L) nil)
        ((= cnt lvl) (list (car L)))
        (T (append (nodes (left L) (+ cnt 1) lvl) (nodes (right L) (+ cnt 1) lvl)))
    )
)
(print (nodes '(A 2 B 0 C 2 D 0 E 0) 0 2))