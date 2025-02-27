; Given a non-linear list, delete all numerical atoms that apear an even number of times.
; (1 g (1 h 8 e (2))) -> (g (h 8 e (2)))
(defun count-appearances (L x)
    (cond
        ((null L) 0)
        ((atom (car L))
            (if (equal (car L) x)
                (+ 1 (count-appearances (cdr L) x))
                (count-appearances (cdr L) x)
            )
        )
        ((listp (car L))
            (+ (count-appearances (car L) x) (count-appearances (cdr L) x))
        )
    )
)

(defun to-delete (L OG)
    (cond
        ((null L) nil)
        ((numberp (car L))
            (if (= 0 (mod (count-appearances OG (car L)) 2))
                (to-delete (cdr L) OG)
                (cons (car L) (to-delete (cdr L) OG))
            )
        )
        ((atom (car L)) (cons (car L) (to-delete (cdr L) OG)))
        ((listp (car L)) (cons (to-delete (car L) OG) (to-delete (cdr L) OG)))
    )
)

(defun sterg (L)
    (to-delete L L)
)

(print (sterg '(1 g (1 h 8 e (2)))))


; A binary tree is memories as (root (left-subtree) (right-subtree)). Determine the list of notes on level K. Root level is 0.
; EX: (A (B) (C)) 0 -> (A) ; 1 -> (B C)
(defun find-level (Tree K)
    (cond
        ((null Tree) nil)
        ((= K 0) (list (car Tree)))
        (T (append (find-level (car Tree) (- K 1)) (find-level (cadr Tree) (- K 1))))
    )
)
(print (find-level '(A (B) (C)) 1))
(print (find-level '(A (B (C (D) (E (F) (G (H))))) (I (J) (K))) 3))

;        A
;       / \
;      B   I
;     /    / \
;    C    J  K
;   / \
;  D   E
;     / \
;    F   G
;       /
;      H


; Write a function that deletes the 1st, 2nd, 4th, 8th, ... elements from a list.
; Ex: (1 2 3 4 5 6) -> (3 5 6)
(defun delete-nth (L n pos)
    (cond
        ((null L) nil)
        ((= pos n) 
            (delete-nth (cdr L) (* 2 n) (+ 1 pos)))
        (T (cons (car L) (delete-nth (cdr L) n (+ 1 pos))))
    )
)

(defun main (L)
    (delete-nth L 1 1)
)
(print (main '(1 2 3 4 5 6)))


; Write a function to produce the list of pairs (atom n), where atom appears for n times in the parameter list. 
; Ex: (A B A B A C A) --> ((A 4) (B 2) (C 1)).
(defun count-occurences (L E)
    (cond
        ((null L) 0)
        ((equal E (car L)) (+ 1 (count-occurences (cdr L) E)))
        (T (count-occurences (cdr L) E))
    )
)

(defun remove-remaining (L E)
    (cond
        ((null L) nil)
        ((equal (car L) E) (remove-remaining (cdr L) E))
        (T (cons (car L) (remove-remaining (cdr L) E)))
    )
)

(defun make-pairs (L)
    (cond
        ((null L) nil)
        (T (append (list (list (car L) (count-occurences L (car L)))) (make-pairs (remove-remaining L (car L)))))
    )
)
(print (make-pairs '(A B A B A C A)))