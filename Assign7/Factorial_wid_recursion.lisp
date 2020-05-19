(sdraw '(defun factorial(num)
    (cond((zerop num) 1)

    (t(* num (factorial(- num 1))))
))

(setq num 3)
(write(factorial num)))


