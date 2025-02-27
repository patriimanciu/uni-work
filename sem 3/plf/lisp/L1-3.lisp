; a) Write a function that inserts in a linear list a given atom A after the 2nd, 4th, 6th, ... element. 
(defun insert-even (L A pos)
    (cond 
        ((null L) nil)
        ((= pos 0) (cons (car L) (cons A (insert-even (cdr L) A 1)))) ;if the position is 0, insert the element
        ((= pos 1) (cons (car L) (insert-even (cdr L) A 0)))
    )
)
(print (insert-even '(1 2 3 4 5 6 7 8 9 10) 100 1))

; b) Write a function to get from a given list the list of all atoms, on any  
;      level, but reverse order. Example: 
;      (((A B) C) (D E)) ==> (E D C B A) 
(defun atoms-reverse (L)
    (cond
        ((null L) nil)
        ((atom (car L)) (append (atoms-reverse (cdr L)) (list (car L))))
        ((listp (car L)) (append (atoms-reverse (cdr L)) (atoms-reverse (car L))))
    )
)
(print (atoms-reverse '((A B) C (D E))))

; c) Write a function that returns the greatest common divisor of all numbers in a nonlinear list. 
(defun my-gcd (a b)
    (cond 
        ((= a b) a)
        ((> a b) (my-gcd (- a b) b))
        (t (my-gcd a (- b a)))
    )
)
(defun gcd-list (L) 
    (cond 
        ((and (atom (car l)) (null (cdr l))) (car l))
        ((listp (car L)) (my-gcd (gcd-list (car L)) (gcd-list (cdr L))))
        (t (my-gcd (car L) (gcd-list (cdr L))))
    )
)
(print (gcd-list '(24 48 36 12 60 72 84 96 108 120)))


; d) Write a function that determines the number of occurrences of a given atom in a nonlinear list.
(defun num-occurences (L A counter)
    (cond
        ((null L) counter)
        ((atom (car L)) 
            (if (equal A (car L))
                (num-occurences (cdr L) A (+ counter 1))
                (num-occurences (cdr L) A counter)))
        ((listp (car L)) (num-occurences (cdr L) A (num-occurences (car L) A counter)))
    )
)
(print (num-occurences '(1 2 5 4 (5) 6 (7 (5) 9) 5) 5 0))