        IDENTIFICATION DIVISION.                        
        PROGRAM-ID. LASTFACTORIALDIGIT.                               
        ENVIRONMENT DIVISION.                           
        DATA DIVISION.                                  
        WORKING-STORAGE SECTION.                        
        77 USERINP PIC 9(10).                           
        77 LOOPINP PIC 9(10).                           
        77 COUNTER PIC 9(10) VALUE 0.                           
        PROCEDURE DIVISION.                             
           A-PARA.
           ACCEPT LOOPINP.
           PERFORM B-PARA UNTIL COUNTER = LOOPINP.
           STOP RUN.              

           B-PARA.
           ACCEPT USERINP.                          
           IF USERINP = 0 THEN
               DISPLAY "1"
           END-IF.
               
           IF USERINP = 1 THEN
               DISPLAY "1"
           END-IF.

           IF USERINP = 2 THEN
               DISPLAY "2"
           END-IF.

           IF USERINP = 3 THEN
               DISPLAY "6"
           END-IF.

           IF USERINP = 4 THEN
               DISPLAY "4"
           END-IF.

           IF USERINP > 4 THEN
               DISPLAY "0"
           END-IF        
           ADD 1 TO COUNTER.

