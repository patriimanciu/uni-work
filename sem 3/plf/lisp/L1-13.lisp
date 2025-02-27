; a) A linear list is given. Eliminate from the list all elements from N to N steps, N-given. 
(defun elim-nth (L n initial)
    (cond
        ((null L) nil)
        ((= n 1) (elim-nth (cdr L) initial initial))
        (t (cons (car L) (elim-nth (cdr L) (- n 1) initial)))
    )
)

(print (elim-nth '(1 2 3 4 5 6 7 8 9 10) 3 3))

; b)  Write  a function to test  if a  linear  list of  integer  numbers has  a "valley" aspect (a list  has a valley 
; aspect if the items decrease to a certain point and then increase. Eg. (10 8 6 17 19 20). A list must have at least 3 elements to fullfill this condition. 
(defun valley-aspect (E1 L state)
    (cond
        ((null L) (equal state 1))
        ((and (equal state 0) (> E1 (car L)))
            (valley-aspect (car L) (cdr L) 0))
        ((and (equal state 0) (< E1 (car L)))
            (valley-aspect (car L) (cdr L) 1))
        ((and (equal state 1) (< E1 (car L)))
            (valley-aspect (car L) (cdr L) 1))
        (t nil)
    )
)

(defun main (L)
  (if (and L (cdr L))
      (valley-aspect (car L) (cdr L) 0)
      nil))

(print (main '(10 8 6 17 19 20)))

; c) Build a function that returns the minimum numeric atom from a list, at any level. 
(defun my-min (a b)
    (cond
        ((null a) b)
        ((null b) a)
        ((< a b) a)
        (t b)
    )
)

(defun min-of-list (L)
    (cond
        ((null L) nil)
        ((listp (car L)) (my-min (min-of-list (car L)) (min-of-list (cdr L))))
        (t (my-min (car L) (min-of-list (cdr L))))
    )
)

(print (min-of-list '(1 20 31 (4 -5 6 31 7) 18 9 10)))

; d) Write a function that deletes from a linear list of all occurrences of the maximum element. 
(defun my-max (a b)
  (cond
    ((null a) b)
    ((null b) a)
    ((> a b) a)
    (t b)
    )
)

(defun max-of-list (L)
  (cond
    ((null L) nil)
    ((listp (car L)) (my-max (max-of-list (car L)) (max-of-list (cdr L))))
    (t (my-max (car L) (max-of-list (cdr L))))))

(defun delete-max (L m)
  (cond
    ((null L) nil) 
    ((listp (car L)) 
     (cons (delete-max (car L) m) (delete-max (cdr L) m)))
    ((= (car L) m) 
     (delete-max (cdr L) m))
    (t (cons (car L) (delete-max (cdr L) m))))) 

(defun main (L)
  (delete-max L (max-of-list L)))

(print (main '(1 20 31 (4 -5 6 31 7) 18 9 10)))
