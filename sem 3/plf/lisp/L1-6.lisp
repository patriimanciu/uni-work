; a) Write a function to test whether a list is linear. 
(defun is-linear (L)
    (cond 
        ((null L) t)
        ((listp (car L)) nil)
        (t (is-linear (cdr L)))
    )
)
(print (is-linear '(1 2 3 4 5 6 7 8 9 10)))
(print (is-linear '(1 2 3 (4 5 (6 7) 8 (9 10)))))

; b) Write a function to replace the first occurence of an element E in a given list with an other element O.
(defun replace-first-occ (L E O) 
    (cond
        ((null L) nil)
        ((equal E (car L)) (cons O (cdr L)))
        (t (cons (car L) (replace-first-occ (cdr L) E O)))
    )
)
(print (replace-first-occ '(1 2 3 4 5 6 7 8 9 10) 5 100))
(print (replace-first-occ '(1 2 3 4 5 6 7 5 5 10) 5 100))

; c) Write a function to replace each sublist of a list with its last element. 
;      A sublist is an element from the first level, which is a list. 
;      Example: (a (b c) (d (e (f)))) ==> (a c (e (f))) ==> (a c (f)) ==> (a c f) 
;          (a (b c) (d ((e) f))) ==> (a c ((e) f)) ==> (a c f) 

(defun get-last-elem (L)
    (cond
        ((null L) nil)
        ((null (cdr L)) (car L))
        (t (get-last-elem (cdr L)))
    )
)
(print (get-last-elem '(a b c d e f)))
(print (get-last-elem '(a b c d)))



(defun replace-sublist (L)
    (cond
        ((null L) nil)

    )
)

; d) Write a function to merge two sorted lists without keeping double values. 
(defun merge-lists (L1 L2)
    (cond
        ((null L1) L2)
        ((null L2) L1)
        ((= (car L1) (car L2)) (cons (car L1) (merge-lists (cdr L1) (cdr L2))))
        ((< (car L1) (car L2)) (cons (car L1) (merge-lists (cdr L1) L2)))
        (t (cons (car L2) (merge-lists L1 (cdr L2))))
    )
)
(print (merge-lists '(1 2 7 8 9) '(1 2 3 4 8 9 10)))