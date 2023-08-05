;;; This file contains code to jump to the contents of each of the five
;;; 16-bit registers: BC, DE, HL, IX, and IY.  However, the primary use
;;; case for this library is to perform CALLs to the contents of these
;;; registers, since such a CALL is much more difficult to do inline.

jumpBC:
        PUSH    BC
        RET
jumpDE:
        PUSH    DE
        RET
jumpHL:
        JP      (HL)
jumpIX:
        JP      (IX)
jumpIY:
        JP      (IY)
