; For a given tree of type (2) return the path from the root node to a certain given node X.
; (A (B (C (D) (E (F) (G (H))))) (I (J) (K)))
;        A
;       / \
;      B   I
;     /    / \
;    C    J  K
;   / \
;  D   E
;     / \
;    F   G
;       /
;      H

(defun is-this-side (Tree X)
    (cond
        ((null Tree) nil)
        ((equal (car Tree) X) T)
        (T (or (is-this-side (cadr Tree) X) (is-this-side (caddr Tree) X)))
    )
)

(defun find-path (Tree X)
    (cond
        ((null Tree) nil)
        ((equal (car Tree) X) (list X))
        (T (if (is-this-side (cadr Tree) X)
               (cons (car Tree) (find-path (cadr Tree) X))
               (cons (car Tree) (find-path (caddr Tree) X))
           )
        )
    )
)
(print (find-path '(A (B (C (D) (E (F) (G (H))))) (I (J) (K))) 'H))
(print (find-path '(A (B (C (D) (E (F) (G (H))))) (I (J) (K))) 'J))