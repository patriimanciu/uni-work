; Convert a tree of type (1) to type (2).
(defun convert-tree (tree)
    (if (null tree) nil
        (cons (car tree) (process-subtrees (cddr tree) (cadr tree)))
    )
) 
      
(defun process-subtrees (tree count)
    (if (zerop count) nil
        (cons (convert-tree tree) (process-subtrees (skip-subtree tree) (1- count)))
    )
) 

(defun skip-subtree (tree)
    (if (null tree) nil
        (nthcdr (+ 2 (count-subtree-nodes tree (car (cdr tree)))) tree)
    )
)

(defun count-subtree-nodes (tree count)
    (if (zerop count) 0
        (+ 2 (count-subtree-nodes (cddr tree) (car (cdr (cddr tree)))))
    )
) 
      
(print (convert-tree '(A 2 B 0 C 2 D 0 E 0)))
