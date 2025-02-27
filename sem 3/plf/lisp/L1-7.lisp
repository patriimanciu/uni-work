; a) Write a function to eliminate the n-th element of a linear list. 
(defun eliminate-nth (L n)
    (cond
        ((null L) nil)
        ((= n 1) (cdr L))
        (t (cons (car L) (eliminate-nth (cdr L) (- n 1))))
    )
)
(print (eliminate-nth '(1 2 3 4 5) 2))

; b) Write a function to determine the successor of a number represented digit by digit as a list, without 
; transforming the representation of the number from list to number. Example: (1 9 3 5 9 9) --> (1 9 3 6 0 0)
(defun reverse-list (L)
    (cond
        ((null L) nil)
        (t (append (reverse-list (cdr L)) (list (car L))))
    )
)

(defun transform (L)
    (cond 
        ((null L) nil)
        ((= (car L) 9) (cons 0 (transform (cdr L))))
        (t (cons (+ 1 (car L)) (cdr L)))
    )
)

(defun main (L)
    (reverse-list (transform (reverse-list L)))
)

(print (main '(1 9 3 5 9 9)))

; c) Write a function to return the set of all the atoms of a list. 
;      Exemplu: (1 (2 (1 3 (2 4) 3) 1) (1 4)) ==> (1 2 3 4) 
(defun atom-set (L S)
    (cond
        ((null L) S)
        ((and (atom (car L)) (not (member (car L) S))) (atom-set (cdr L) (cons (car L) S)))
        ((listp (car L)) (atom-set (cdr L) (atom-set (car L) S)))
        (t (atom-set (cdr L) S))
    )
)
(print (atom-set '(1 (2 (1 3 (2 4) 3) 1) (1 4)) nil))

; d) Write a function to test whether a linear list is a set.
(defun is-set (L)
    (cond
        ((null L) t)
        ((member (car L) (cdr L)) nil)
        (t (is-set (cdr L)))
    )
)
(print (is-set '(1 2 3 4 5)))