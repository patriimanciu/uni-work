; 5. Return the level (depth) of a node in a tree of type (1). The level of the root element is 0.
; 7. Return the level of a node X in a tree of type (1). The level of the root element is 0.
(defun right-traversal (L n m)
    (cond
        ((null L) nil)
        ((= n (+ 1 m)) L)
        (T (right-traversal (cddr L) (+ 1 n) (+ (cadr L) m)))
    )
)

(defun right (L)
    (right-traversal (cddr L) 0 0)
)

(defun left-traversal (L n m)
    (cond
        ((null L) nil)
        ((= n (+ 1 m)) nil)
        (T (cons (car L) (cons (cadr L) (left-traversal (cddr L) (+ 1 n) (+ (cadr L) m)))))
    )
)

(defun left (L)
    (left-traversal (cddr L) 0 0)
)

(defun check-if-exists (L elem)
    (cond
        ((null L) nil)
        ((equal (car L) elem) t)
        (T (check-if-exists (cdr L) elem))
    )
)

(defun check-existence-left (L elem)
    (check-if-exists (left L) elem)
)

(defun check-existence-right (L elem)
    (check-if-exists (right L) elem)
)

(defun level (L elem)
    (cond
        ((null L) nil)
        ((equal (car L) elem) 0)
        ((check-existence-right L elem) (+ 1 (level (right L) elem)))
        ((check-existence-left L elem) (+ 1 (level (left L) elem)))
    )
)

(print (level '(A 2 B 0 C 2 D 0 E 0) 'D))