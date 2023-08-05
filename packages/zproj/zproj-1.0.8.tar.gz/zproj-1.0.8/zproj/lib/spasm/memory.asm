;;; memory.asm -- Library to support dynamic memory management.

;;; SAMPLE USAGE:
;;;
;;;     

memoryInit:
        ;; INPUT:
        ;;   <none>
        ;;
        ;; OUTPUT:
        ;;   <memory data initialized>
        ;;
        RET


memoryAlloc:
        ;; INPUT:
        ;;   BC -- number of bytes to allocate
        ;;
        ;; OUTPUT:
        ;;   HL -- pointer to memory if successful
        ;;   [carry flag] -- set for failure
        ;;
        SCF
        RET


memoryFree:
        ;; INPUT:
        ;;   HL -- pointer to previously allocated memory
