;  Return the level of a node X in a tree of type (2). The level of the root element is 0.
(defun find-level-of-node (Tree X)
    (cond 
        ((null Tree) nil)
        ((equal (car Tree) X) 0)
        (T (max (+ 1 (find-level-of-node (cadr Tree) X)) (+ 1 (find-level-of-node (caddr Tree) X))))
    )
)
(print (find-level-of-node '(A (B (C (D) (E (F) (G (H))))) (I (J) (K))) 'H))