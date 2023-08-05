;;; Due to the tempting possibility of writing more than one game using this
;;; board scheme, it seems good to consider reorganizing the code in this
;;; file to be flexible enough to handle all of these possibilities without
;;; modification.
;;;
;;; The primary 

#define hexBoardPictureHook     hexBoardData + 0
#define hexBoardCursorHook      hexBoardPictureHook + 2
#define hexBoardCursor          hexBoardCursorHook + 2
#define hexBoardCursorColumn    hexBoardCursor + 0
#define hexBoardCursorRow       hexBoardCursor + 1
#define hexBoardArray           hexBoardCursor + 2
#define boardDataEnd            hexBoardArray + HEXBOARD_SIZE

#define HEXBOARD_SIZE           81
#define HEXBOARD_RADIUS         5
#define HEXBOARD_SIDE           2*HEXBOARD_RADIUS-1
#define HEXBOARD_HEIGHT         HEXBOARD_SIDE
#define HEXBOARD_WIDTH          HEXBOARD_SIDE

#define HEXBOARD_ROW            2
#define HEXBOARD_COLUMN         3

#define HEXBOARD_CELL_HEIGHT    5
#define HEXBOARD_CELL_WIDTH     5
#define HEXBOARD_CELL_DIM       HEXBOARD_CELL_HEIGHT * 256 + HEXBOARD_CELL_WIDTH


;;;==========================================================================;;;
;;; BOARD-WISE ROUTINES //////////////////////////////////////////////////// ;;;
;;;==========================================================================;;;

hexBoardInit:
        ;;
        ;;
        ;; EVEN AFTER THIS ROUTINE IS CALLED, this library is NOT required
        ;; to work (but also not guaranteed to fail) until a valid picture hook
        ;; has been established via hexBoardSetPictureHook.
        ;;
        RET


hexBoardExit:
        RET


hexBoardSetPictureHook:
        ;; INPUT:
        ;;   HL -- address of callback routine
        ;;
        ;; OUTPUT:
        ;;   <hexBoard data updated>
        ;;
        ;; The callback routine will be supplied the cell-wise location of
        ;; a cell in DE and must return a pointer to the picture corresponding
        ;; to that cell.
        ;;
        LD      (hexBoardPictureHook), HL  ; store in (hexBoardPictureHook)
        RET                                ; return


hexBoardDraw:
        ;; INPUT:
        ;;   <hexBoard data>
        ;;
        ;; OUTPUT:
        ;;   <updated board image drawn to buffer>
        ;;
        PUSH    BC
        PUSH    HL                    ; STACK: [PC HL]
        LD      B, HEXBOARD_RADIUS * HEXBOARD_CELL_HEIGHT + 3
        LD      C, HEXBOARD_COLUMN - 2
        LD      HL, hexBoardCellDraw  ; apply hexBoardCellDraw to each cell
        CALL    hexBoardIter          ;
        POP     HL                    ; STACK: [PC]
        POP     BC
        RET                           ; return


hexBoardIter:
        ;; INPUT:
        ;;   HL -- callback routine
        ;;
        ;; OUTPUT:
        ;;   <routine applied to each board cell>
        ;;
        ;; The callback routine will be supplied the cellwise row and column
        ;; of each cell in succession in DE.
        ;;
        PUSH    BC                        ; STACK: [PC BC]
        PUSH    DE                        ; STACK: [PC BC DE]
        LD      C, HEXBOARD_WIDTH            ; C = number of columns in board
        LD      E, 0                      ; E = first cellwise board column
hexBoardIter_columnLoop:                     ;
        CALL    hexBoard_getColumnCells            ; B = number of cells in column
        LD      B, A                      ;
        LD      D, 0                      ; D = first cellwise board row
hexBoardIter_rowLoop:                        ;
        CALL    hexBoard_jumpHL                    ; call callback
        INC     D                         ; next cellwise row
        DJNZ    hexBoardIter_rowLoop         ; repeat for each row
        INC     E                         ; next cellwise column
        DEC     C                         ; repeat for each column
        JR      NZ, hexBoardIter_columnLoop  ;
        POP     DE                        ; STACK: [PC BC]
        POP     BC                        ; STACK: [PC]
        RET                               ; return


hexBoard_getColumnCells:
        ;; INPUT:
        ;;   E -- cellwise column
        ;;
        ;; OUTPUT:
        ;;   ACC -- height (in cells) of column
        ;;
        CALL    hexBoard_getCenterDistance ; ACC = distance from center
        SUB     HEXBOARD_HEIGHT      ; ACC = height - distance
        NEG                       ; ACC = distance - height
        RET                       ; return


hexBoard_getColumnRow:
        ;; INPUT:
        ;;   E -- cellwise column
        ;;
        ;; OUTPUT:
        ;;   ACC -- pixelwise row of top cell in column
        ;;
        PUSH    BC                 ; STACK: [PC BC]
        CALL    hexBoard_getCenterDistance  ; ACC = center distance * 3 + first row
        LD      C, A               ;
        ADD     A, A               ;
        ADD     A, C               ;
        ADD     A, HEXBOARD_ROW       ;
        POP     BC                 ; STACK: [PC]
        RET                        ; return


hexBoard_getCenterDistance:
        ;; INPUT:
        ;;   E -- cellwise column
        ;;
        ;; OUTPUT:
        ;;   ACC -- distance (in cellwise columns) from center column
        ;;
        ;; ACC = abs(HEXBOARD_WIDTH / 2 - E)
        ;;
        LD      A, HEXBOARD_WIDTH / 2 ; ACC = center column
        SUB     E                  ; ACC = center - input
        RET     NC                 ; return if nonnegative
        NEG                        ; ACC = input - center
        RET                        ; return


hexBoardCellDraw:
        ;; INPUT:
        ;;   D -- cell-wise row of cell
        ;;   E -- cell-wise column of cell
        ;;
        ;; OUTPUT:
        ;;   (cell drawn to screen buffer)
        ;;
        PUSH    BC                         ; STACK: [PC BC]
        PUSH    DE                         ; STACK: [PC BC DE]
        PUSH    HL                         ; STACK: [PC BC DE HL]
        LD      HL, (hexBoardPictureHook)  ; HL = picture
        CALL    hexBoard_jumpHL                     ;
        CALL    hexBoardCellLocation       ; DE = location
        LD      B, HEXBOARD_CELL_HEIGHT    ; B = height
        CALL    drawPicture                ; draw the picture
        POP     HL                         ; STACK: [PC BC DE]
        POP     DE                         ; STACK: [PC BC]
        POP     BC                         ; STACK: [PC]
        RET                                ; return


hexBoardCellErase:
        ;; INPUT:
        ;;   D -- cell-wise row of cell
        ;;   E -- cell-wise column of cell
        ;;
        ;; OUTPUT:
        ;;   (cell erased from screen buffer)
        ;;
        PUSH    BC                  ; STACK: [PC BC]
        PUSH    DE                  ; STACK: [PC BC DE]
        LD      BC, HEXBOARD_CELL_DIM ; BC = dimensions of cell
        CALL    hexBoardCellLocation     ; DE = location of cell
        CALL    drawClearRectangle  ; clear the rectangle
        POP     DE                  ; STACK: [PC BC]
        POP     BC                  ; STACK: [PC]
        RET                         ; return


hexBoardCellAddress:
        ;; INPUT:
        ;;   D -- cellwise row of cell
        ;;   E -- cellwise column of cell
        ;;
        ;; OUTPUT:
        ;;   HL -- address of cell data
        ;;
        PUSH    DE              ; STACK: [PC DE]
        LD      A, D            ; ACC = 9 * D
        ADD     A, A            ;
        ADD     A, A            ;
        ADD     A, A            ;
        ADD     A, D            ;
        ADD     A, E            ; DE = ACC = 9 * D + E
        LD      E, A            ;
        LD      D, 0            ;
        LD      HL, hexBoardArray  ; HL = hexBoardArray + offset
        ADD     HL, DE          ;
        POP     DE              ; STACK: [PC]
        RET                     ; return

hexBoardCellLocation:
        ;; INPUT:
        ;;   D -- cell-wise row of cell
        ;;   E -- cell-wise column of cell
        ;;
        ;; OUTPUT:
        ;;   D -- pixelwise row of cell
        ;;   E -- pixelwise column of cell
        ;;
        PUSH    HL                 ; STACK: [PC HL]
        LD      L, E               ; HL = DE
        LD      H, D               ;
        ADD     HL, HL             ; HL *= 6
        ADD     HL, DE             ;
        ADD     HL, HL             ;
        CALL    hexBoard_getColumnRow  ; D = top column row + cellwise row * 6
        ADD     A, H               ;
        LD      D, A               ;
        LD      A, HEXBOARD_COLUMN    ; E = left column + cellwise column * 6
        ADD     A, L               ;
        LD      E, A               ;
        POP     HL                 ; STACK: [PC]
        RET                        ; return


;;;==========================================================================;;;
;;; CELL NEIGHBORS ///////////////////////////////////////////////////////// ;;;
;;;==========================================================================;;;

hexBoardCellNIter:
        ;; INPUT:
        ;;   D -- cell-wise row of central cell
        ;;   E -- cell-wise column of central cell
        ;;   HL -- callback routine
        ;;
        ;; OUTPUT:
        ;;   <callback applied to all neighbors of cell>
        ;;
        ;; The callback routine will be supplied the row and column of each
        ;; neighbor in succession in D and E, respectively.  This routine is
        ;; required to preserve ALL registers.
        ;;
        PUSH    BC                         ; STACK: [PC BC]
        LD      BC, hexBoardCellNUL        ; apply routine to upper left neighbor
        CALL    hexBoardCellNIter_wrapper  ;
        LD      BC, hexBoardCellNU         ; apply routine to upper neighbor
        CALL    hexBoardCellNIter_wrapper  ;
        LD      BC, hexBoardCellNUR  ; apply routine to upper right neighbor
        CALL    hexBoardCellNIter_wrapper         ;
        LD      BC, hexBoardCellNDR  ; apply routine to lower right neighbor
        CALL    hexBoardCellNIter_wrapper         ;
        LD      BC, hexBoardCellND   ; apply routine to lower neighbor
        CALL    hexBoardCellNIter_wrapper         ;
        LD      BC, hexBoardCellNDL  ; apply routine to lower left neighbor
        CALL    hexBoardCellNIter_wrapper         ;
        POP     BC                   ; STACK: [PC]
        RET                          ; return
        ;;
hexBoardCellNIter_wrapper:
        ;; INPUT:
        ;;   BC -- callback routine to move to neighbor
        ;;   D -- cell-wise row of initial cell
        ;;   E -- cell-wise column of initial cell
        ;;   HL -- callback routine to apply to neighbor
        ;;
        ;; OUTPUT:
        ;;   <routine HL applied to neighbor of (D, E) computed by routine BC>
        ;;
        ;; Routine HL will receive the location of the neighbor in DE and must
        ;; preserve ALL registers.
        ;;
        ;; Routine BC will receive the location of the
        ;; INITIAL cell in DE, and must meet the following conditions:
        ;;
        ;;      (1) If the requested neighbor exists, the routine must return
        ;;          its location in DE and RESET the carry flag.
        ;;
        ;;      (2) Otherwise, the routine must SET the carry flag.
        ;;
        ;;      (3) Whether or not the neighbor exists, all registers except
        ;;          for DE must be preserved.
        ;;
        PUSH    DE
        CALL    hexBoard_jumpBC
        CALL    NC, hexBoard_jumpHL
        POP     DE
        RET


;;; The following cellMove* routines all have the same contract:
;;;
;;;     INPUT:
;;;       D -- initial cell-wise row
;;;       E -- initial cell-wise column
;;;
;;;     OUTPUT:
;;;       D -- new cell-wise row (if move succeeded)
;;;       E -- new cell-wise column (if move succeeded)
;;;       [carry flag] -- set iff move failed
;;;
;;; It occurred to me recently that an easier way to implement the neighbor
;;; routines would be as follows:
;;;
;;;     (1) Computing the location of the desired neighbor ASSUMING that this
;;;         neighbor is in range.
;;;
;;;     (2) Fall into a routine that checks whether an arbitrary location (D, E)
;;;         is in range and sets the carry flag if and only if it is not.
;;;
;;; An important assumption here is that the code for part (1) must not result
;;; in (D, E) containing a valid location if the desired neighbor did not
;;; exist.

hexBoardCheckLocation:
        ;; INPUT:
        ;;   D -- cell-wise row
        ;;   E -- cell-wise column
        ;;
        ;; OUTPUT:
        ;;   [carry flag] -- set iff cell-wise location is out of range
        ;;
        LD      A, HEXBOARD_WIDTH - 1    ; return carry if E >= width
        CP      E                        ;
        RET     C                        ;
        CALL    hexBoard_getColumnCells  ; set carry iff D >= height
        DEC     A                        ;
        CP      D                        ;
        RET                              ; return


hexBoardCellNL:
        DEC     E
        JP      hexBoardCheckLocation

        ;; LD      A, E            ; ACC = E - 1 (setting carry)
        ;; SUB     1               ;
        ;; RET     C               ;
        ;; LD      E, A            ; E = E - 1
        ;; CALL    hexBoard_getColumnCells  ; return no carry if location in range
        ;; CP      D               ;
        ;; RET     NZ              ;
        ;; INC     E               ; restore E otherwise
        ;; SCF                     ; set carry for fail
        ;; RET                     ; return

hexBoardCellNR:
        INC     E
        JP      hexBoardCheckLocation

        ;; LD      A, HEXBOARD_WIDTH - 2  ; return carry if E > HEXBOARD_WIDTH - 2
        ;; CP      E                   ;
        ;; RET     C                   ;
        ;; INC     E                   ; increment E otherwise
        ;; CALL    hexBoard_getColumnCells      ; return no carry if location in range
        ;; CP      D                   ;
        ;; RET     NZ                  ;
        ;; DEC     E                   ; restore E otherwise
        ;; SCF                         ; set carry for fail
        ;; RET                         ; return

hexBoardCellNU:
        DEC     D
        JP      hexBoardCheckLocation

        ;; LD      A, D            ; ACC = D
        ;; CP      1               ; set carry if 0
        ;; RET     C               ; return carry if 0
        ;; DEC     D               ; decrement D otherwise
        ;; RET                     ; return

hexBoardCellND:
        INC     D
        JP      hexBoardCheckLocation

        ;; CALL    hexBoard_getColumnCells  ; ACC = height of column - 2
        ;; SUB     2               ;
        ;; CP      D               ; return carry if D > height - 2
        ;; RET     C               ;
        ;; INC     D               ; increment D otherwise
        ;; RET                     ; return

hexBoardCellNUR:
        INC     E                        ; column += 1
        LD      A, HEXBOARD_RADIUS - 1   ; carry = not (column < radius)
        CP      E                        ;
        LD      A, D                     ; row -= carry
        SBC     A, 0                     ;
        LD      D, A                     ;
        JP      hexBoardCheckLocation    ; check and return

        ;; LD      A, HEXBOARD_WIDTH - 2    ; if column >= width - 1: return failure
        ;; CP      E                        ;
        ;; RET     C                        ;
        ;; INC     E                        ; column += 1
        ;; LD      A, HEXBOARD_RADIUS - 1   ; if column < radius: return success
        ;; CP      E                        ;
        ;; RET     NC                       ;
        ;; LD      A, D                     ; row -= 1
        ;; SUB     1                        ;
        ;; LD      D, A                     ;
        ;; RET     NC                       ; if row >= 0: return success
        ;; DEC     E                        ; column -= 1
        ;; INC     D                        ; row += 1
        ;; SCF                              ; [1]
        ;; RET                              ; return failure
        ;;
        ;; [1] We shouldn't have to do this, since INC and DEC instructions
        ;;     are not supposed to affect the carry flag, but TI's debugger
        ;;     is apparently buggy in this respect.

hexBoardCellNDR:
        INC     E                        ; column += 1
        LD      A, E                     ; carry = (column < radius)
        CP      HEXBOARD_RADIUS          ;
        LD      A, D                     ; row += carry
        ADC     A, 0                     ;
        LD      D, A                     ;
        JP      hexBoardCheckLocation    ; check and return

        ;; LD      A, HEXBOARD_WIDTH - 2    ; if column >= width - 1: return failure
        ;; CP      E                        ;
        ;; RET     C                        ;
        ;; ;; INC     E                        ; column += 1
        ;; SCF
        ;; RET

hexBoardCellNDL:
        DEC     E                       ; column -= 1
        LD      A, HEXBOARD_RADIUS - 2  ; carry = not (column < radius - 1)
        CP      E                       ;
        LD      A, D                    ; row += carry
        ADC     A, 0                    ;
        LD      D, A                    ;
        JP      hexBoardCheckLocation   ; check and return

        ;; SCF
        ;; RET

hexBoardCellNUL:
        DEC     E                       ; column -= 1
        LD      A, E                    ; carry = column < radius - 1
        CP      HEXBOARD_RADIUS - 1     ;
        LD      A, D                    ; row -= carry
        SBC     A, 0                    ;
        LD      D, A                    ;
        JP      hexBoardCheckLocation   ; check and return

        ;; SCF
        ;; RET


        LD      A, E                 ; ACC = E - 1 (with carry)
        SUB     1                    ;
        RET     C                    ; return fail if E was 0
        LD      E, A                 ; E = new column (tentatively)
        CP      HEXBOARD_RADIUS - 1  ; return success if new E in right half
        RET     NC                   ;
        INC     D
        DEC     D
        RET     Z
        
;;;==========================================================================;;;
;;; CURSOR ROUTINES //////////////////////////////////////////////////////// ;;;
;;;==========================================================================;;;

hexBoardSetCursorHook:
        ;; INPUT:
        ;;   HL -- address of callback routine
        ;;
        ;; OUTPUT:
        ;;   <hexBoard data updated>
        ;;
        ;; The callback routine will be supplied the cell-wise location of
        ;; a cell in DE and must return a cursor picture for that cell.
        ;;
        LD      (hexBoardCursorHook), HL  ; store in (hexBoardCursorHook)
        RET                               ; return


hexBoardCursorSet:
        ;; INPUT:
        ;;   D -- cell-wise row
        ;;   E -- cell-wise column
        ;;
        ;; OUTPUT:
        ;;   <hexBoard data> -- cursor location set to D, E
        ;;
        LD      (hexBoardCursor), DE
        RET


hexBoardCursorGet:
        ;; INPUT:
        ;;   <hexBoard data>
        ;;
        ;; OUTPUT:
        ;;   D -- cell-wise cursor row
        ;;   E -- cell-wise cursor column
        ;;
        LD      DE, (hexBoardCursor)
        RET


hexBoardCursorShow:
        ;; INPUT:
        ;;   <hexBoard data>
        ;;
        ;; OUTPUT:
        ;;   <screen buffer> -- cursor drawn in position
        ;;
        PUSH    DE                    ; STACK: [PC DE]
        LD      DE, (hexBoardCursor)  ; DE = current cursor position
        CALL    hexBoardCursorDraw    ; draw cursor at this position
        POP     DE                    ; STACK: [PC]
        RET                           ; return


hexBoardCursorHide:
        ;; INPUT:
        ;;   <hexBoard data>
        ;;
        ;; OUTPUT:
        ;;   <screen buffer> -- cursror no longer drawn in position
        ;;
        PUSH    DE                    ; STACK: [PC DE]
        LD      DE, (hexBoardCursor)  ; DE = current cursor position
        CALL    hexBoardCellErase     ; ERASE cell at this position...
        CALL    hexBoardCellDraw      ; ...and then redraw it
        POP     DE                    ; STACK: [PC]
        RET                           ; return


hexBoardCursorMoveUp:
        PUSH    HL
        LD      HL, hexBoardCellNU
        CALL    hexBoardCursorMover
        POP     HL
        RET

hexBoardCursorMoveDown:
        PUSH    HL
        LD      HL, hexBoardCellND
        CALL    hexBoardCursorMover
        POP     HL
        RET

hexBoardCursorMoveLeft:
        PUSH    HL
        LD      HL, hexBoardCellNL
        CALL    hexBoardCursorMover
        POP     HL
        RET

hexBoardCursorMoveRight:
        PUSH    HL
        LD      HL, hexBoardCellNR
        CALL    hexBoardCursorMover
        POP     HL
        RET


hexBoardCursorMover:
        ;; INPUT:
        ;;   (cursorRow) -- current cursor row
        ;;   (cursorColumn) -- current cursor column
        ;;   HL -- address of callback routine
        ;;
        ;; OUTPUT:
        ;;   (cursorRow) -- updated to new row
        ;;   (cursorColumn) -- updated to new column
        ;;   (board) -- old cell unselected, new cell selected
        ;;   <screen buffer> -- affected cells redrawn
        ;;
        PUSH    BC
        PUSH    DE
        LD      DE, (hexBoardCursor)
        CALL    hexBoardCellErase
        CALL    hexBoardCellDraw
        LD      C, E
        LD      B, D
        CALL    hexBoard_jumpHL
        JR      NC, $+4
        LD      E, C
        LD      D, B
        CALL    hexBoardCellErase
        CALL    hexBoardCursorDraw
        LD      (hexBoardCursor), DE
        POP     DE
        POP     BC
        RET


hexBoardCursorDraw:
        ;; INPUT:
        ;;   D -- cell-wise row
        ;;   E -- cell-wise column
        ;;   <hexBoard data>
        ;;
        ;; OUTPUT:
        ;;   <screen buffer>
        ;;
        PUSH    BC
        PUSH    DE
        PUSH    HL
        LD      HL, (hexBoardCursorHook)
        CALL    hexBoard_jumpHL
        CALL    hexBoardCellLocation
        LD      B, HEXBOARD_CELL_HEIGHT
        CALL    drawPicture
        POP     HL
        POP     DE
        POP     BC
        RET


hexBoard_jumpBC:
        PUSH    BC
        RET

hexBoard_jumpHL:
        JP      (HL)
