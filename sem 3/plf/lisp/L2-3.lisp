; Return the number of levels of a tree of type (1)
; (A 2 B 0 C 2 D 0 E 0)

(defun right-traversal (L n m)
    (cond
        ((null L) nil)
        ((= n (+ 1 m)) L)
        (T (right-traversal (cdr (cdr L)) (+ 1 n) (+ (car (cdr L)) m)))
    )
)

(defun right (L)
    (right-traversal (cddr L) 0 0)
)

(defun left-traversal (L n m)
    (cond
        ((null L) nil)
        ((= n (+ 1 m)) nil)
        (t (cons (car L) (cons (car (cdr L)) (left-traversal (cddr L) (+ 1 n) (+ (car (cdr L)) m)))))
    )
)

(defun left (L)
    (left-traversal (cddr L) 0 0)
)

(defun tree-level (L)
    (cond
        ((null L) 0)
        ((equal (car (cdr L)) 0) 1)
        ((equal (car (cdr L)) 1) (+ 1 (tree-level (cdr (cdr L)))))
        (T (+ 1 (max (tree-level (left L)) (tree-level (right L)))))
    )
)

(print (tree-level '(A 2 B 0 C 2 D 0 E 0)))