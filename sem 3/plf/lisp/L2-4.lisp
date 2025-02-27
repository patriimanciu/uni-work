; Convert a tree of type (2) to type (1).
(defun convert-2-1 (L)
    (cond
        ((null L) nil)
        ((and (not (null (car (cdr L)))) (not (null (caddr L)))) (append (list (car L)) '(2) (convert-2-1(cadr L))
                                                                     (convert-2-1(caddr L))))
        ((not (null (cadr L))) (append (list (car L)) '(1) (convert-2-1(cadr L)) ))
        ((not (null (caddr L))) (append (list (car L)) '(1) (convert-2-1(caddr L)) ))
        (T (append (list (car L)) '(0)))
    )
)
(print (convert-2-1 '(A (B (D) (E)) (C (F) (G)))))