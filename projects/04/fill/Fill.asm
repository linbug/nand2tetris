// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
@clear // M[clear] = 0
M=0
@pos   // M[pos] = 0
M=0

(LOOP)
@KBD   //
D=M    // checking if M[KBD] == 0
@THEN  //
D;JEQ  // if so, jump to THEN
@keypress // otherwise, set M[keypress] to 65535
M=1
@FI
0;JMP     // and jump over the THEN to get to FI
(THEN)
@keypress // set M[keypress] to 0
M=0
(FI)
@keypress
D=M
@clear
D=D-M     // D = M[keypress] - M[clear]
@CONTINUE
D;JEQ   // if M[keypress] - M[clear] == 0, goto CONTINUE
@keypress  // otherwise, changing state
D=M
@clear
M=D    // M[clear] = M[keypress]
@pos  // M[pos] = 0
M=0
@LOOP // goto LOOP
0;JMP
(CONTINUE)
@screenval
M=0 // M[screenval] = 0
@clear // test whether M[clear] == 0
D=M
@ZERO
D;JEQ // if so, skip down to (ZERO)
// otherwise, set M[screenval] to -1 (65535)
@screenval
M=M-1
(ZERO)
//now want: M[SCREEN+M[pos]] = M[screenval]
@SCREEN // A = SCREEN
D=A     // D = SCREEN
@pos    // A = pos
D=D+M // D = SCREEN+M[pos]
@screenpos // A = screenpos
M=D // M[screenpos] = SCREEN+M[pos]
@screenval // A = screenval
D=M // D = M[screenval]
@screenpos // A = screenpos
A=M // A = M[screenpos]
M=D // M[M[screenpos]] = D,
    // i.e., M[SCREEN+M[pos]] = M[screenval]
@8192 // A = 8192
D=A // D = 8192
@pos
D=D-M // D = 8192-M[pos]
@pos // A = pos
M=M+1 // M[pos] = M[pos]+1
@LOOP
D;JLT // jump to LOOP if 8192-(old)M[pos] < 0
@pos
M=0
@LOOP // goto LOOP
0;JMP

// clear = 0 // 0 = clearing, 1 = filling
// pos = 0 // which pixel on the screen we are up to
// LOOP do {
//   keypress = if KBD == 0 then 0 else 1
//   if keypress - clear == 0 { // keypress and clear are the same
//     SCREEN+pos = if clear == 0 then 0 else -1 (i.e. 65535)
//     if 8192-pos < 0 {
//       pos = 0
//     }
//     else {
//       pos += 1
//     }
//     goto LOOP
//   }
//   else { // keypress and clear are different, changing state
//     clear = keypress
//     pos = 0
//     goto LOOP
//   }
// }
