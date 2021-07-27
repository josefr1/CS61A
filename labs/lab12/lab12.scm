(define (tail-replicate x n)
  (define (helper n so-far)
      (if (= n 0) so-far
        (helper (- n 1) (cons x so-far))
        )
  )
  (helper n '())
)

(define-macro (def func args body)
    `(define ,func (lambda ,args ,body))

)

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ( (y (repeatedly-cube (- n 1) x)))
        (* y y y))))
