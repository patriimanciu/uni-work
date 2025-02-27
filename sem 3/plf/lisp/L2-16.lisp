; Determine  if  a  tree  of  type  (2)  is  ballanced  (the  difference  between  the  depth  of  two  subtrees  is equal to 1).
(defun find-depth (Tree)
    (cond
        ((null Tree) 0)
        (T (+ 1 (max (find-depth (cadr Tree)) (find-depth (caddr Tree)))))
    )
)

(defun is-balanced (Tree)
    (cond
        ((null Tree) T)
        (T (let ((left-depth (find-depth (cadr Tree)))
                (right-depth (find-depth (caddr Tree))))
        (and (<= (abs (- left-depth right-depth)) 1)
             (is-balanced (cadr Tree)) (is-balanced (caddr Tree)))))
    )
)
(print (is-balanced '(A (B (C (D) (E (F) (G (H))))) (I (J) (K)))))
(print (is-balanced '(A (B) (C) (D))))