(defun Factorial (num)
    (setq fact 1)
    (loop for i from 1 to num
        do( 
            setq fact (* fact i)
        )
    )
    fact
)
(setq num 5)
(write (Factorial num))