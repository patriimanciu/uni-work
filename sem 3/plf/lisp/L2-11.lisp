; Return the level (and coresponded list of nodes) with maximum number of nodes for a tree of type 
; (2). The level of the root element is 0.
; (A (B (C (D) (E (F) (G (H))))) (I (J) (K))) -> (3 (C J K))
(defun find-level-of-node (Tree level)
    (cond 
        ((null Tree))
        (T (append (list level) (find-level-of-node (cadr Tree) (+ 1 level)) (find-level-of-node (caddr Tree) (+ 1 level))))
    )
)
(print (find-level-of-node '(A (B (C (D) (E (F) (G (H))))) (I (J) (K)))))

(defun remove-the-duplicates (L X)
  (cond
    ((null L) nil)
    ((equal (car L) X) (remove-the-duplicates (cdr L) X))
    (T (cons (car L) (remove-the-duplicates (cdr L) X)))
  )
)

(defun count-appearances (L X)
    (cond
        ((null L) 0)
        ((equal (car L) X) (+ 1 (count-appearances (cdr L) X)))
        (T (count-appearances (cdr L) X))
    )
)

; list (cate apar, ce nr)
(defun find-max-occurances(L m X)
    (cond
        ((null L) (list m X))
        ((> (count-appearances L (car L)) m) (find-max-occurances (remove-the-duplicates L (car L)) (count-appearances L (car L)) (car L)))
        (T (find-max-occurances (remove-the-duplicates L (car L)) m X))
    )
)

(print (find-max-occurances '(1 2 3 2 3 3 2 2 1) 0 0))

(defun find-level (Tree K)
    (cond
        ((null Tree) nil)
        ((= K 0) (list (car Tree)))
        (T (append (find-level (car Tree) (- K 1)) (find-level (cadr Tree) (- K 1))))
    )
)

(defun find-max-level (Tree)
    (find-level(Tree (cadr (find-max-occurances (find-level-of-node Tree 0) 0 0))))
)
(print (find-max-level '(A (B (C (D) (E (F) (G (H))))) (I (J) (K)))))


; --------------------------
(defun find-level-of-node (Tree level)
  "Transform the tree into a list of levels."
  (cond
    ((null Tree) nil)
    (t (append (list level)
               (find-level-of-node (second Tree) (+ 1 level))
               (find-level-of-node (third Tree) (+ 1 level))))))

(defun remove-the-duplicates (L X)
  "Remove all occurrences of X from list L."
  (cond
    ((null L) nil)
    ((equal (car L) X) (remove-the-duplicates (cdr L) X))
    (t (cons (car L) (remove-the-duplicates (cdr L) X)))))

(defun count-appearances (L X)
  "Count how many times X appears in list L."
  (cond
    ((null L) 0)
    ((equal (car L) X) (+ 1 (count-appearances (cdr L) X)))
    (t (count-appearances (cdr L) X))))

(defun find-max-occurances (L m X)
  "Find the level with the maximum occurrences in list L."
  (cond
    ((null L) (list m X)) ; Base case
    (t (let* ((current (car L)) ; Current level
              (count (count-appearances L current)) ; Count occurrences
              (updated-list (remove-the-duplicates L current))) ; Remove duplicates
         (if (> count m)
             (find-max-occurances updated-list count current)
             (find-max-occurances updated-list m X)))))) ; Continue with same max

(defun find-level (Tree K)
  "Find the list of nodes at level K."
  (cond
    ((null Tree) nil) ; Empty tree
    ((= K 0) (list (car Tree))) ; Reached the desired level
    (t (append (find-level (second Tree) (- K 1)) ; Process left subtree
               (find-level (third Tree) (- K 1)))))) ; Process right subtree

(defun find-max-level (Tree)
  "Return the level with the maximum number of nodes and the list of nodes at that level."
  (let* ((level-list (find-level-of-node Tree 0)) ; Convert tree to list of levels
         (max-info (find-max-occurances level-list 0 0)) ; Find level with max nodes
         (max-level (second max-info))) ; Extract the level
    (list max-level (find-level Tree max-level)))) ; Get nodes at that level

;; Example usage
(print (find-max-level '(A (B (C (D) (E (F) (G (H))))) (I (J) (K)))))
