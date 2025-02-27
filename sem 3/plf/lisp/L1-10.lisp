; a) Write a function to return the product of all the numerical atoms from a list, at superficial level. 
(defun prod-superficial (L)
    (cond
        ((null L) 1)
        ((numberp (car L)) (* (car L) (prod-superficial (cdr L))))
        (t (prod-superficial (cdr L)))
    )
)
(print (prod-superficial '(1 2 (3 4 5) 6 (7 8 (9))10)))

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

; c) Write a function to compute the result of an arithmetic expression memorised  
;      in preorder on a stack. Examples: 
;      (+ 1 3) ==> 4  (1 + 3) 
;      (+ * 2 4 3) ==> 11  [((2 * 4) + 3) 
;      (+ * 2 4 - 5 * 2 2) ==> 9  ((2 * 4) + (5 - (2 * 2)) 
(defun operand-expression (op a b)
	(cond
		((string= op "+") (+ a b))
		((string= op "-") (- a b))
		((string= op "*") (* a b))
		((string= op "/") (floor a b))
	)
)

(defun expression (l)
    (cond
        ((null l) nil)
        ((and (and (numberp (cadr l)) (numberp (caddr l))) (atom (car l))) (cons (operand-expression (car l) (cadr l) (caddr l)) (expression (cdddr l))))
        (T (cons (car l) (expression (cdr l))))
    )
)

(defun solve (l)
    (cond
        ((null (cdr l)) (car l))
        (T (solve (expression l)))
    )
)

(print (solve '(+ * 2 4 - 5 * 2 2)))

; d) Write a function to produce the list of pairs (atom n), where atom appears for n times in the parameter 
; list. Example: 
;      (A B A B A C A) --> ((A 4) (B 2) (C 1)).
(defun count-occ (L E)
    (cond 
        ((null L) 0)
        ((equal E (car L)) (+ 1 (count-occ (cdr L) E)))
        (t (count-occ (cdr L) E))
    )
)

(defun remove_duplicates (l e)
    (cond
        ((null l) nil)
        ((equal (car l) e) (remove_duplicates (cdr l) e))
        (T (cons (car l) (remove_duplicates (cdr l) e)))
    )
)

(defun count_all_occurences (l)
    (cond
        ((null l) nil)
        (T (cons (cons (car l) (count-occ l (car l))) (count_all_occurences (remove_duplicates l (car l)))))
    )
)

(print (count_all_occurences '(A B A B A C A)))