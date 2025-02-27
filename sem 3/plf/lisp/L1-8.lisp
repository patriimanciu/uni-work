; a) Write a function to return the difference of two sets. 
(defun set-dif (A B)
    (cond
        ((null A) nil)
        ((member (car A) B) (set-dif (cdr A) B))
        (t (cons (car A) (set-dif (cdr A) B)))
    )
)
(print (set-dif '(1 2 3 4 5) '(3 4 5 6 7)))
(print (set-dif '(3 4 5 6 7) '(1 2 3 4 5)))

; b) Write a function to reverse a list with its all sublists, on all levels. 
(defun reverse-list (L)
    (cond
        ((null L) nil)
        (t (append (reverse-list (cdr L)) (list (car L))))
    )
)

(defun reverse-list-all (L)
    (cond
        ((null L) nil)
        ((atom (car L)) (append (reverse-list-all (cdr L)) (list (car L))))
        (t (append (reverse-list-all (cdr L)) (list (reverse-list (car L)))))
    )
)
(print (reverse-list-all '((1 2 3) ((4 5) 6) 7 8 (9 10 11))))

; c) Write a function to return the list of the first elements of all list  elements of a given list with an odd 
; number of elements at superficial level. Example: 
;      (1 2 (3 (4 5) (6 7)) 8 (9 10 11)) => (1 3 9).
(defun count-elems-superficial (L)
    (cond
        ((null L) 0)
        ((atom (car L)) (+ 1 (count-elems-superficial (cdr L))))
        (t (count-elems-superficial (cdr L)))
    )
)
; (print (count-elems-superficial '(1 2 (3 (4 5) (6 7)) 8 (9 10 11))))

(defun first-odd-elems (L)
    (cond
        ((null L) nil)
        ((atom (car L)) (first-odd-elems (cdr L)))
        ((= 1 (mod (count-elems-superficial (car L)) 2)) (append (list (car (car L))) (append (first-odd-elems (car L)) (first-odd-elems (cdr L)))))
    )
)
(print (first-odd-elems '((1 2 (3 (4 5 6) (6 7)) 8 (9 10 11)))))

; d) Write a function to return the sum of all numerical atoms in a list at superficial level.
(defun sum-atoms-superficial (L)
    (cond
        ((null L) 0)
        ((atom (car L)) (+ (car L) (sum-atoms-superficial (cdr L))))
        (t (sum-atoms-superficial (cdr L)))
    )
)
(print (sum-atoms-superficial '(1 2 (3 (4 5) (6 7)) 8 (9 10 11))))