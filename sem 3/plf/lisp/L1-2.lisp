; a) Write a function to return the product of two vectors. 
; https://en.wikipedia.org/wiki/Dot_product 

(defun dot-product (V1 V2)
    (cond
        ((null V1) 0)
        (t (+ (* (car V1) (car V2)) (dot-product (cdr V1) (cdr V2))))
    )
)
(print (dot-product '(1 2 3) '(4 5 6)))

; b) Write a function to return the depth of a list. Example: the depth of a linear list is 1. 
(defun depth (L)
    (cond
        ((null L) 0)
        ((listp (car L)) ( + 1 (depth (car L))))
        (t (depth (cdr L)))
    )
)
(print (depth '(1 2 3 4 5 6 7 8 9 10)))
(print (depth '(1 2 3 (4 5 (6 7) 8 (9 10)))))


; c) Write a function to sort a linear list without keeping the double values. 
(defun insert-inorder-list (L e)
    (cond
        ((null L) (list e))
        ((= e (car L)) L)
        ((< e (car L)) (cons e L))
        (t (cons (car L) (insert-inorder-list (cdr L) e)))
    )
)
(print (insert-inorder-list '(1 2 3 6 7 8 9 10) 5))

(defun sortL (L)
    (cond
        ((null L) nil)
        (t (insert-inorder-list (sortL (cdr L)) (car L)))
    )
)
(print (sortL '(1 8 21 6 7 8 7 9 10 5)))

; d) Write a function to return the intersection of two sets.
(defun intersection-of-sets (S1 S2)
    (cond
        ((null S1) nil) ;if the set is empty there's no intersection
        ((member (car S1) S2) (cons (car S1) (intersection-of-sets (cdr S1) S2)))
        (t (intersection-of-sets (cdr S1) S2))
    )
)
(print (intersection-of-sets '(1 2 3 4 5) '(3 4 5 6 7 8 9 10)))