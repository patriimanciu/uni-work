; a) Write a function that merges two sorted linear lists and keeps double values. 
(defun merge-lists (L1 L2)
    (cond
        ((null L1) L2)
        ((null L2) L1)
        ((= (car L1) (car L2)) (cons (car L1) (merge-lists (cdr L1) L2)))
        ((< (car L1) (car L2)) (cons (car L1) (merge-lists (cdr L1) L2)))
        (t (cons (car L2) (merge-lists L1 (cdr L2))))
    )
)
(print (merge-lists '(1 2 7 8 9) '(1 2 3 4 8 9 10)))

; b) Write a function to replace an element E by all elements of a list L1 at all levels of a given list L.
(defun replace-element (L E L1)
    (cond
        ((null L) nil)
        ((atom (car L))
            (if (= (car L) E) (append L1 (replace-element (cdr L) E L1))
            (cons (car L) (replace-element (cdr L) E L1)))
        )
        (t (cons (replace-element (car L) E L1) (replace-element (cdr L) E L1)))
    )
)
(print (replace-element '(1 (2 1 3 (4 5 1) 6) 7 1 1 9) 1 '(a b c)))

; c)  Write  a  function  to  determines  the  sum  of  two  numbers  in  list  representation,  and  returns  the 
; corresponding  decimal  number,  without  transforming  the  representation  of  the  number  from  list  to number. 
(defun reverse-list (L)
    (cond
        ((null L) nil)
        (t (append (reverse-list (cdr L)) (list (car L))))
    )
)

(defun sum-list (L1 L2 carry Res) 
    (cond
        ((null L1) (append Res (if (> carry 0) (list carry) nil)))
        ((null L2) (append Res (if (> carry 0) (list carry) nil)))
        ((> (+ (car L1) (car L2) carry) 9) (sum-list (cdr L1) (cdr L2) 1 (append Res (list (mod (+ (car L1) (car L2) carry) 10)))))
        (t (sum-list (cdr L1) (cdr L2) 0 (append Res (list (+ (car L1) (car L2) carry)))))
    )
)

(defun sum (L1 L2)
    (reverse-list (sum-list (reverse-list L1) (reverse-list L2) 0 nil))
)

(print (sum '(1 2 4) '(9 5 6)))

; d) Write a function to return the greatest common divisor of all numbers in a linear list.
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
        (t (my-gcd (car L) (gcd-list (cdr L))))
    )
)
(print (gcd-list '(24 48 36 12 60 72 84 96 108 120)))