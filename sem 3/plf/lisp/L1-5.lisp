; a) Write twice the n-th element of a linear list. Example: for (10 20 30 40 50) and n=3 will produce (10 20 30 30 40 50). 
(defun doube-nth (L n)
    (cond
        ((null L) nil)
        ((= n 1) (cons (car L) (cons (car L) (cdr L))))
        (t (cons (car L) (doube-nth (cdr L) (- n 1))))
    )
)
(print (doube-nth '(10 20 30 40 50) 3))

; b) Write a function to return an association list with the two lists given as parameters.  
;      Example: (A B C) (X Y Z) --> ((A.X) (B.Y) (C.Z)). 
(defun associate-list(L1 L2)
    (cond
        ((null L1) nil)
        (t (cons (cons (car L1) (car L2)) (associate-list (cdr L1) (cdr L2))))
    )
)
(print (associate-list '(A B C) '(X Y Z)))

; c) Write a function to determine the number of all sublists of a given list, on any level.  
;      A sublist is either the list itself, or any element that is a list, at any level. Example:  
;      (1 2 (3 (4 5) (6 7)) 8 (9 10)) => 5 lists: 
;  (list itself, (3 ...), (4 5), (6 7), (9 10)). 
(defun num-of-sublist (L)
    (cond
        ((null L) 0)
        ((listp (car L)) (+ 1 (num-of-sublist (car L)) (num-of-sublist (cdr L))))
        (t (num-of-sublist (cdr L)))
    )
)
(print (num-of-sublist '((1 2 (3 (4 5) (6 7)) 8 (9 10)))))

; d) Write a function to return the number of all numerical atoms in a list at superficial level.
(defun num-of-nums (L)
    (cond 
        ((null L) 0)
        ((numberp (car L)) (+ 1 (num-of-nums (cdr L))))
        (t (num-of-nums (cdr L)))
    )
)
(print (num-of-nums '(1 2 A 4 (5) 6 (7 8 9) B)))