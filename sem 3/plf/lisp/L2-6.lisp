; Return the list of nodes of a tree of type (1) accessed inorder.
(defun right-traversal (L n m)
    (cond
        ((null L) nil)
        ((= n (+ 1 m)) L)
        (T (right-traversal (cddr L) (+ 1 n) (+ (cadr L) m)))
    )
)

(defun right (L)
    (right-traversal (cddr L) 0 0)
)

(defun left-traversal (L n m)
    (cond
        ((null L) nil)
        ((= n (+ 1 m)) nil)
        (T (cons (car L) (cons (cadr L) (left-traversal (cddr L) (+ 1 n) (+ (cadr L) m)))))
    )
)

(defun left (L)
    (left-traversal (cddr L) 0 0)
)

(defun inorder (L)
    (cond
        ((null L) nil)
        (T (append (inorder (left L)) (list (car L)) (inorder (right L))))
    )
)
(print (inorder '(A 2 B 0 C 2 D 0 E 0)))
