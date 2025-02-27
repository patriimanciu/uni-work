;  Determine the list of nodes accesed in preorder in a tree of type (2).
(defun preorder (Tree)
    (cond
        ((null Tree) nil)
        ((atom Tree) (list Tree)) ; a leaf
        (T (append (list (car Tree)) (preorder (cadr Tree)) (preorder (caddr Tree))))
    )
)
(print (preorder '(A (B D E) (C F G))))