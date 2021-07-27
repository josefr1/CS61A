(define-macro (switch expr cases)
	(cons 'cond
		(map (lambda (case) (cons `(equal? ,expr (quote ,(car case))) (cdr case)))
    			cases))
)
