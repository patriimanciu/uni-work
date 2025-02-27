; a) Write a function to return the dot product of two vectors. 
; https://en.wikipedia.org/wiki/Dot_product 
(defun dot-product (V1 V2)
    (cond
        ((null V1) 0)
        (t (+ (* (car V1) (car V2)) (dot-product (cdr V1) (cdr V2))))
    )
)

(print (dot-product '(1 2 3) '(4 5 6)))

; b) Write a function to return the maximum value of all the numerical atoms of a list, at any level. 
(defun my-max (a b)
    (cond
        ((and (not (numberp a)) (not (numberp b))) nil)
        ((not (numberp a)) b)
        ((not (numberp b)) a)
        ((> a b) a)
        (t b)
    )
)

(defun max-of-list (L)
    (cond
        ((null L) nil)
        ((numberp (car L)) (my-max (car L) (max-of-list (cdr L))))
        ((listp (car L)) (my-max (max-of-list (car L)) (max-of-list (cdr L))))
    )
)

(print (max-of-list '(1 20 (31 4 -5 6) 7 18 9 10)))

; c) All permutations to be replaced by: Write a function to compute the result of an arithmetic expression 
; memorised  
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

; d) Write a function to return T if a list has an even number of elements on the first level, and NIL on the 
; contrary case, without counting the elements of the list.
(defun even-number-of-elements (L)
    (cond
        ((null L) T)
        ((null (cdr L)) NIL)
        (T (even-number-of-elements (cddr L)))
    )
)

(print (even-number-of-elements '(1 2 3 4 5 6 7 8 9 10)))
(print (even-number-of-elements '(1 2 3 (4 5) 6 (7 8) 9 (10) 11)))