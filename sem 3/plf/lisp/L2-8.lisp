; Return the list of nodes of a tree of type (2) accessed inorder.
(defun inorder (Tree)
    (cond
        ((null Tree) nil)
        ((atom Tree) (list Tree)) ; a leaf
        (T (append (inorder (cadr Tree)) (list (car Tree)) (inorder (caddr Tree))))
    )
)
(print (inorder '(A (B D E) (C F G))))