; a) Write a function to return the union of two sets. 
(defun union-sets (S1 S2)
    (cond
        ((null S1) S2)
        ((null S2) S1)
        ((member (car S1) S2) (union-sets (cdr S1) S2))
        (t (cons (car S1) (union-sets (cdr S1) S2)))
    )
)
(print (union-sets '(1 2 3) '(2 3 4))) ; (1 2 3 4)

; b) Write a function to return the product of all numerical atoms in a list, at any level. 
(defun product-atoms (L)
    (cond
        ((null L) 1)
        ((numberp (car L)) (* (car L) (product-atoms (cdr L))))
        ((listp (car L)) (* (product-atoms (car L)) (product-atoms (cdr L))))
    )
)
(print (product-atoms '(1 (2 3) 4))) ; 24

; c) Write a function to sort a linear list with keeping the double values. 
(defun insert-inorder-list (L e)
    (cond 
        ((null L) (list e))
        ((<= e (car L)) (cons e L))
        (t (cons (car L) (insert-inorder-list (cdr L) e)))
    )
)
(print (insert-inorder-list '(1 2 3 5 6 ) 5)) ; (1 2 3 5 6 7 8 9 10)

(defun sortL (L)
    (cond
        ((null L) nil)
        (t (insert-inorder-list (sortL (cdr L)) (car L)))
    )
)

(print (sortL '(1 8 21 6 7 8 7 9 10 5))) ; (1 5 6 7 7 8 8 9 10 21)

; d) Build a list which contains positions of a minimum numeric element from a given linear list.
(defun my-min (a b)
    (cond
        ((null a) b)
        ((null b) a)
        ((< a b) a)
        (t b)
        )
)

(defun min-of-list (L)
    (cond
        ((null L) nil)
        ((listp (car L)) (my-min (min-of-list (car L)) (min-of-list (cdr L))))
        (t (my-min (car L) (min-of-list (cdr L))))
    )
)

(defun build-min-pos (L Res min pos)
    (cond
        ((null L) Res)
        ((= (car L) min) (build-min-pos (cdr L) (append Res (list pos)) min (+ pos 1)))
        (t (build-min-pos (cdr L) Res min (+ pos 1)))
    )
)

(defun main (L)
    (build-min-pos L nil (min-of-list L) 0)
)
(print (main '(1 20 -5 4 -5 6 31 7 18 -5 10)))