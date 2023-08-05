;;; TI's code for exiting an application, with some extras.

; Note that this is NOT a routine; just JP to Exit
exitApp:
        IM      1
        LD      A, 01h
        CALL    000Bh
        OUT     (10h), A
        LD      A, 05h
        CALL    000Bh
        OUT     (10h), A
        bcall(_GrBufClr)
        bcall(_ClrLCDFull)
        LD      (IY+textFlags),0    ; reset text flags
        EI
        ;
        ; This next call is done only if application used the Graph Backup Buffer
        ;
        bcall(_SetTblGraphDraw)
        ;
        bcall(_ReloadAppEntryVecs)  ; make sure Application Loader set
        ;
        bcall(_JForceCmdNoChar)     ; force to home screen
