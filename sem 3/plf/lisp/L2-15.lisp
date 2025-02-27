; Determine the list of nodes accesed in postorder in a tree of type (2).
(defun postorder (Tree)
    (cond
        ((null Tree) nil)
        ((atom Tree) (list Tree)) ; a leaf
        (T (append (postorder (cadr Tree)) (postorder (caddr Tree)) (list (car Tree))))
    )
)
(print (postorder '(A (B D E) (C F G))))