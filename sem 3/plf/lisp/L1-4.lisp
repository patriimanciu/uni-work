; a) Write a function to return the sum of two vectors. 
(defun sum-vectors (V1 V2)
    (cond 
        ((null V1) nil)
        (t (cons (+ (car V1) (car V2)) (sum-vectors (cdr V1) (cdr V2))))
    )
)
(print (sum-vectors '(1 2 3) '(4 5 6)))

; b) Write a function to get from a given list the list of all atoms, on any  
;      level, but on the same order. Example: 
;      (((A B) C) (D E)) ==> (A B C D E) 
(defun atoms-ordered (L)
    (cond
        ((null L) nil)
        ((atom (car L)) (append (list (car L)) (atoms-ordered (cdr L))))
        ((listp (car L)) (append (atoms-ordered (car L)) (atoms-ordered (cdr L))))
    )
)
(print (atoms-ordered '((A B) C (D E))))

; c) Write a function that, with a list given as parameter, inverts only continuous 
;      sequences of atoms. Example: 
;      (a b c (d (e f) g h i)) ==> (c b a (d (f e) i h g)) 
(defun reverse-list (L)
    (cond
        ((null L) nil)
        (t (append (reverse-list (cdr L)) (list (car L))))
    )
)

(defun reverse-cont (L aux)
    (cond
        ((null L) (reverse-list aux))
        ((atom (car L)) (reverse-cont (cdr L) (append aux (list (car L)))))
        ((listp (car L)) (append (reverse-list aux) (cons (reverse-cont (car l) nil) (reverse-cont (cdr l) nil))))
    )
)
(print (reverse-cont '(a b c (d (e f) g h i))))

; d) Write a list to return the maximum value of the numerical atoms from a list, at superficial level.
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
        (t (my-max (car L) (max-of-list (cdr L))))
    )
)
(print (max-of-list '(1 20 31 4 -5 6 7 18 9 10)))