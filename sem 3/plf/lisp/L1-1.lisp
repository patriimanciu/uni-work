; a) Write a function to return the n-th element of a list, or NIL if such an element does not exist. 

(defun nth-element (n L)
    (cond
        ((null L) nil)
        ((equal n 1) (car L))
        (t (nth-element (- n 1) (cdr L)))
    )
)
(print (nth-element 3 '(10 9 8 7 6 5 4 3 2 1)))

; b) Write a function to check whether an atom E is a member of a list which is not necessarily linear. 

(defun is-atom (E L)
    (cond
        ((null L) nil)
        ((atom (car L)) 
            (if (equal E (car L))
                t
                (is-atom E (cdr L))
            )
        )
        ((listp (car L))
            (if (is-atom E (car L))
                t
                (is-atom E (cdr L))
            )
        )
    )
)
(print (is-atom 5 '(1 2 3 4 (5) 6 (7 8 9) 10)))

; c) Write a function to determine the list of all sublists of a given list, on any level.  
;      A sublist is either the list itself, or any element that is a list, at any level. Example:  
;      (1 2 (3 (4 5) (6 7)) 8 (9 10)) => 5 sublists : 
;     (  (1 2 (3 (4 5) (6 7)) 8 (9 10))    (3 (4 5) (6 7))     (4 5)   (6 7)   (9 10) ) 
(defun sublists (L)
    (cond 
        ((null L) nil)
        ((listp (car L)) (append (list (car L)) (sublists (car L)) (sublists (cdr L))))
        (t (sublists (cdr L)))
    )
)
(print (sublists '((1 2 (3 (4 5) (6 7)) 8 (9 10)))))


; d) Write a function to transform a linear list into a set. 
(defun removeDuplicates (L e)
    (cond
        ((null L) nil)
        ((equal e (car L)) (removeDuplicates (cdr L) e))
        (t (cons (car L) (removeDuplicates (cdr L) e)))
    )
)


(defun list-to-set (L)
    (cond
        ((null L) nil)
        (t (cons (car L) (list-to-set (removeDuplicates (cdr L) (car L)))))
    )
)
(print (list-to-set '(1 1 2 3 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10)))