; a) Determine the least common multiple of the numerical values of a nonlinear list. 
(defun my-gcd (a b)
    (cond 
        ((= a b) a)
        ((> a b) (my-gcd (- a b) b))
        (t (my-gcd a (- b a)))
    )
)

(defun least-common-multiple (a b)
    (/ (* a b) (my-gcd a b))
)

(defun lcm-list (L)
    (cond 
        ((and (atom (car L)) (null (cdr L))) (car L))
        ((listp (car L)) (least-common-multiple (lcm-list (car L)) (lcm-list (cdr L))))
        (t (least-common-multiple (car L) (lcm-list (cdr L))))
    )
)
(print (lcm-list '(2 7 (4 16) 13)))


; b) Write a function to test if a linear list of numbers has a "mountain" aspect (a list has a "mountain" 
; aspect if the items increase to a certain point and then decreases.  
;       Eg. (10 18 29 17 11 10). The list must have at least 3 atoms to fullfil this criteria. 
(defun mountain-aspect (E1 L state)
  (cond
    ((null L) (eq state 1))
    ((and (eq state 0) (< E1 (car L)))
     (mountain-aspect (car L) (cdr L) 0))
    ((and (eq state 0) (> E1 (car L)))
     (mountain-aspect (car L) (cdr L) 1))
    ((and (eq state 1) (> E1 (car L)))
     (mountain-aspect (car L) (cdr L) 1))
    (t nil)))

(defun main (L)
  (if (and L (cdr L))
      (mountain-aspect (car L) (cdr L) 0)
      nil))

(print (main '(10 18 29 17 11 10))) 
(print (main '(10 18 29 30 11 21))) 
(print (main '(10 18)))

; c) Remove all occurrences of a maximum numerical element from a nonlinear list. 
(defun my-max (a b)
  (cond
    ((null a) b) ; Handle nil cases
    ((null b) a)
    ((> a b) a)
    (t b)))

(defun max-of-list (L)
  (cond
    ((null L) nil) ; Empty list has no maximum
    ((listp (car L)) (my-max (max-of-list (car L)) (max-of-list (cdr L)))) ; Recurse into sublists
    (t (my-max (car L) (max-of-list (cdr L)))))) ; Compare scalar values

(defun remove-max (L m)
  (cond
    ((null L) nil) ; Base case: empty list
    ((and (not (listp (car L))) (= (car L) m)) (remove-max (cdr L) m)) ; Remove maximum element
    ((listp (car L)) ; Recurse into sublist
     (cons (remove-max (car L) m) (remove-max (cdr L) m)))
    (t (cons (car L) (remove-max (cdr L) m))))) ; Keep element if not maximum

(defun remove-my-maximum (L)
  (let ((max-val (max-of-list L)))
    (if max-val
        (remove-max L max-val)
        L))) ; If no maximum is found, return the original list

(print (remove-my-maximum '(1 20 31 (4 -5 6 31 7) 18 9 10))) ; Output: (1 20 (4 -5 6 7) 18 9 10)
(print (remove-my-maximum '((31 31) (31 (31 31))))) ; Output: NIL
(print (remove-my-maximum '((1 2) (3 4) 5))) ; Output: ((1 2) (3 4))


; d) Write a function which returns the product of numerical even atoms from a list, to any level.
(defun prod-even (L)
    (cond
        ((null L) 1)
        ((listp (car L)) (* (prod-even (car L)) (prod-even (cdr L))))
        ((and (numberp (car L)) (evenp (car L))) (* (car L) (prod-even (cdr L))))
        (t (prod-even (cdr L)))
    )
)
(print (prod-even '(1 2 3 4 5 6 7 8 9 10))) ; Output: 3840