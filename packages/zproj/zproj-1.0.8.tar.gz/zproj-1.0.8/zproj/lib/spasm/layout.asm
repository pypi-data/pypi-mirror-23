;;; Library for rendering circuit layouts.

;;; For the foreseeable future, it makes sense to consider only grid
;;; layouts.  Even with this restriction, however, a general solution
;;; is a daunting task.  Therefore, it makes sense to begin with a few
;;; basic cases in hopes of gaining insight into the general case.
;;;
;;; For example, the case of two nodes (the lowest practical number)
;;; is fairly simple: assuming no component joins a node to itself,
;;; all components are in connected in parallel.  In this case, then,
;;; the components can simply be oriented vertically side-by-side
;;; between the two nodes.
;;;
;;; For three nodes, the situation is more complicated, but a fairly
;;; simple general solution is still possible.  If we choose to
;;; place the ground node at the bottom of the diagram, we can place
;;; the remaining two nodes at the left and right top corners,
;;; allowing for any node to connect to any other node.
;;;
;;; There appears to be no easy general solution for four or more
;;; nodes.  However, the natural generalization of the above solutions
;;; for fewer nodes may work in many of the most important cases.
;;; Namely, consider the arrangement
;;;
;;;     2 - 3 -...- n
;;;     |   |  ...  |
;;;     1111111111111
;;;
;;; where node 1 is the ground node.  This arrangement relies on the
;;; possibility of forming a "chain" from the non-ground nodes, each node
;;; of which is connected via components only to its predecessor, its successor,
;;; or the ground node.  In particular, this condition is met by a strictly
;;; series circuit.
;;;
;;; However, we can extend this approach to handle some exceptions.
;;; For example, if there is only one component connected between non-
;;; ground nodes that does not fit the chain model, we can easily
;;; accommodate it by placing it horizontally above the chain.  We can
;;; accommodate additional such components as long as they connect
;;; nodes either strictly inside or strictly outside of any previous
;;; exceptions (for example, we can connect nodes 2 and n, nodes
;;; 3 and n - 1, etc.).
