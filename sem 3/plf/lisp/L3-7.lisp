; Write a function that substitutes an element E with all elements of a list L1 at all levels of a given list L
(defun substituteL (l e l1)
    (cond 
        ((numberp l) (if (= l e) l1 l))
        ((listp l) (mapcar #'(lambda (a) (substituteL a e l1)) l))
    )
)

(print (substituteL '(1 (2 1 3 (4 5 1) 6) 7 1 1 9) 1 '(a b c)))