; a) Write a function to insert an element E on the n-th position of a linear list. 
(defun insert-nth (L n E)
    (cond
        ((null L) (list E))
        ((= n 0) (cons E L))
        (t (cons (car L) (insert-nth (cdr L) (- n 1) E)))
    )
)
(print (insert-nth '(1 2 3 4) 2 5))

; b) Write a function to return the sum of all numerical atoms of a list, at any level. 
(defun sum-atoms (L)
    (cond
        ((null L) 0)
        ((atom (car L)) (+ (car L) (sum-atoms (cdr L))))
        ((listp (car L)) (+ (sum-atoms (car L)) (sum-atoms (cdr L))))
        (t (sum-atoms-superficial (cdr L)))
    )
)
(print (sum-atoms '(1 2 (3 (4 5) (6 7)) 8 (9 10 11))))

; c) Write a function to return the set of all sublists of a given linear list. 
; Ex. For list  ((1 2 3) ((4 5) 6)) => ((1 2 3) (4 5) ((4 5) 6))  
(defun set-sublists (L)
    (cond
        ((null L) nil)
        ((listp (car L)) (append (list (car L)) (append (set-sublists (cdr L)) (set-sublists (car L)))))
        (t (set-sublists (cdr L)))
    )
)
(print (set-sublists '((1 2 3) ((4 5) 6))))

; d) Write a function to test the equality of two sets, without using the difference of two sets. 
(defun set-equal (A B)
    (cond
        ((null A) (null B))
        ((null B) nil)
        ((member (car A) B) (set-equal (cdr A) (remove (car A) B)))
        (t nil)
    )
)
(print (set-equal '(1 2 3 4 5) '(3 4 5 6 7)))
