(defun nthlist (lis n)
     (nth n lis)
)
(setq lis '(0 1 2))
(setq n 2)
(format t "~% ~ath elemnt is ~a" n (nthlist  lis n))



