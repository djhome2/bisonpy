#A Bison parser, made by GNU Bison 3.8.2.
  #
  


#Skeleton implementation for Bison LALR(1) parsers in python
  #
  
#
  
#Copyright (C) 2007-2015, 2018-2021 Free Software Foundation, Inc.
  #
  
#
  
#This program is free software: you can redistribute it and/or modify
  #
  
#it under the terms of the GNU General Public License as published by
  #
  
#the Free Software Foundation, either version 3 of the License, or
  #
  
#(at your option) any later version.
  #
  
#
  
#This program is distributed in the hope that it will be useful,
  #
  
#but WITHOUT ANY WARRANTY; without even the implied warranty of
  #
  
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  #
  
#GNU General Public License for more details.
  #
  
#
  
#You should have received a copy of the GNU General Public License
  #
  
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
  #
  


#As a special exception, you may create a larger work that contains
  #
  
#part or all of the Bison parser skeleton and distribute that work
  #
  
#under terms of your choice, so long as that work isn't itself a
  #
  
#parser generator using the skeleton or a modified version thereof
  #
  
#as a parser skeleton.  Alternatively, if you modify or redistribute
  #
  
#the parser skeleton itself, you may (at your option) remove this
  #
  
#special exception, which will cause the skeleton and the resulting
  #
  
#Bison output files to be licensed under the GNU General Public
  #
  
#License without this special exception.
  #
  
#
  
#This special exception was added by the Free Software Foundation in
  #
  
#version 2.2 of Bison.
  #
  


#DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
  #
  
#especially those whose name start with YY_ or yy_.  They are
  #
  
#private implementation details that can be changed or removed.
  #
  





# import java.text.MessageFormat;
# import java.util.ArrayList;
from abc import ABCMeta,abstractmethod
import sys
from enum import Enum
#"%code imports" blocks.
  #
  

#"Calc.y":37
  #
  


  #import java.io.BufferedReader;
  #import java.io.IOException;
  #import java.io.InputStream;
  #import java.io.InputStreamReader;
  #import java.io.Reader;
  #import java.io.StreamTokenizer;
  #import java.nio.CharBuffer;

import math

def i18n(s):
  return s;


#/**
# * A class defining a point in the input.
# */
class Position():
  line = 1
  column = 1

  def __init__(self, *args):
    count = len(args)
    if(count == 0):
      self.line = 1
      self.column = 1
      return
    if(count == 2):
      self.line = args[0]
      self.column = args[1]
      return
    assert(count == 1)
    p = args[0]
    assert(isinstance(p, Position))
    self.line = p.line;
    self.column = p.column;
    return
  

  #public Position(int l, int t) {
  #  line = l;
  #  column = t;
  #}

  #public Position(Position p) {
  #  line = p.line;
  #  column = p.column;
  #}

  def set(self, p):
    self.line = p.line
    self.column = p.column
  

  def __eq__(self, l):
    return l.line == self.line and l.column == self.column;
  

  def __str__(self):
    return str(self.line) + "." + str(self.column)
  

  def line(self):
    return self.line
  

  def column(self):
    return self.column
  


#"Calc.py":189
  #
  


# 
#  A Bison parser, automatically generated from <tt>Calc.y</tt>.
# 
#  @author LALR (1) parser skeleton written by Paolo Bonzini.
#  




  # /**
  #  * A class defining a pair of positions.  Positions, defined by the
  #  * <code>Position</code> class, denote a point in the input.
  #  * Locations represent a part of the input through the beginning
  #  * and ending positions.
  #  */
class Location():
  # /**
  #  * The first, inclusive, position in the range.
  #  */
  def __init__(self, *args):
    count = len(args)
    self.begin = None
    self.begin = None
    if(count > 0):
      self.begin = args[0]
    if(count > 1):
      self.end = args[1]
    return
  # public Position begin;

  # /**
  #  * The first position beyond the range.
  #  */
  # public Position end;

  # /**
  #  * Create a <code>Location</code> denoting an empty range located at
  #  * a given point.
  #  * @param loc The position at which the range is anchored.
  #  */
  # public Location (Position loc) {
    # this.begin = this.end = loc;
  # }

  # /**
  #  * Create a <code>Location</code> from the endpoints of the range.
  #  * @param begin The first position included in the range.
  #  * @param end   The first position beyond the range.
  #  */
  # public Location (Position begin, Position end) {
    # this.begin = begin;
    # this.end = end;
  # }

  # /**
  #  * Print a representation of the location.  For this to be correct,
  #  * <code>Position</code> should override the <code>equals</code>
  #  * method.
  #  */
  def __str__(self):
    if (self.begin == self.end):
      return str(self.begin)
    else:
      return str(self.begin) + "-" + str(self.end)
  # }
# }




S_YYEOF = 0                    #"end of file"
  #
  

S_YYerror = 1                  #error
  #
  

S_YYUNDEF = 2                  #"invalid token"
  #
  

S_BANG = 3                     #"!"
  #
  

S_PLUS = 4                     #"+"
  #
  

S_MINUS = 5                    #"-"
  #
  

S_STAR = 6                     #"*"
  #
  

S_SLASH = 7                    #"/"
  #
  

S_CARET = 8                    #"^"
  #
  

S_LPAREN = 9                   #"("
  #
  

S_RPAREN = 10                  #")"
  #
  

S_EQUAL = 11                   #"="
  #
  

S_EOL = 12                     #"end of line"
  #
  

S_NUM = 13                     #"number"
  #
  

S_NEG = 14                     #NEG
  #
  

S_YYACCEPT = 15                #$accept
  #
  

S_input = 16                   #input
  #
  

S_line = 17                    #line
  #
  

S_exp = 18                     #exp
  #
  


class SymbolKind():
  # {

  # private final int yycode_;

  def __init__(self, n):
    self.yycode_ = n
    return
  # }

  values_ = (
    S_YYEOF,
    S_YYerror,
    S_YYUNDEF,
    S_BANG,
    S_PLUS,
    S_MINUS,
    S_STAR,
    S_SLASH,
    S_CARET,
    S_LPAREN,
    S_RPAREN,
    S_EQUAL,
    S_EOL,
    S_NUM,
    S_NEG,
    S_YYACCEPT,
    S_input,
    S_line,
    S_exp
  )

  def get(self, code):
    return self.values_[code]
  
  def getCode(self):
    return self.yycode_

    
  # /* YYNAMES_[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
  #      First, the terminals, then, starting at \a YYNTOKENS_, nonterminals.  */
    
  def yynames_init():  
      return (
  i18n("end of file"), i18n("error"), i18n("invalid token"), "!", "+", "-", "*",
  "/", "^", "(", ")", "=", i18n("end of line"), i18n("number"), "NEG",
  "$accept", "input", "line", "exp", None
    )
  yynames_ = yynames_init()
  

    # /* The user-facing name of this symbol.  */
  def getName(self):
    return self.yynames_[self.yycode_]
    
  # };





# /**
#  * Communication interface between the scanner and the Bison-generated
#  * parser <tt>Calc</tt>.
#  */
class Lexer():
    #/* Token kinds.  */
  #/** Token "end of file", to be returned by the scanner.  */
  YYEOF = 0
  #/** Token error, to be returned by the scanner.  */
  YYerror = 256
  #/** Token "invalid token", to be returned by the scanner.  */
  YYUNDEF = 257
  #/** Token "!", to be returned by the scanner.  */
  BANG = 258
  #/** Token "+", to be returned by the scanner.  */
  PLUS = 259
  #/** Token "-", to be returned by the scanner.  */
  MINUS = 260
  #/** Token "*", to be returned by the scanner.  */
  STAR = 261
  #/** Token "/", to be returned by the scanner.  */
  SLASH = 262
  #/** Token "^", to be returned by the scanner.  */
  CARET = 263
  #/** Token "(", to be returned by the scanner.  */
  LPAREN = 264
  #/** Token ")", to be returned by the scanner.  */
  RPAREN = 265
  #/** Token "=", to be returned by the scanner.  */
  EQUAL = 266
  #/** Token "end of line", to be returned by the scanner.  */
  EOL = 267
  #/** Token "number", to be returned by the scanner.  */
  NUM = 268
  #/** Token NEG, to be returned by the scanner.  */
  NEG = 269

  # /** Deprecated, use YYEOF instead.  */
  EOF = YYEOF

  # /**
  #  * Emit an error referring to the given locationin a user-defined way.
  #  *
  #  * @param loc The location of the element to which the
  #  *                error message is related.
  #  * @param msg The string for the error message.
  #  */
  def yyerror(loc, msg): pass


  # /**
  #  * Build and emit a "syntax error" message in a user-defined way.
  #  *
  #  * @param ctx  The context of the error.
  #  */
  def reportSyntaxError(ctx): pass

  # }

YYLAST_ = 77
YYEMPTY_ = -2
YYFINAL_ = 15
YYNTOKENS_ = 15



def yylloc(rhs, n):
  if (0 < n):
    return Location(rhs.locationAt(n-1).begin, rhs.locationAt(0).end)
  else:
    return Location(rhs.locationAt(0).end)




# /**
#  * Returned by a Bison action in order to stop the parsing process and
#  * return success (<tt>True</tt>).
#  */
YYACCEPT = 0

# /**
#  * Returned by a Bison action in order to stop the parsing process and
#  * return failure (<tt>False</tt>).
#  */
YYABORT = 1


# /**
#  * Returned by a Bison action in order to request a new token.
#  */
YYPUSH_MORE = 4


# /**
#  * Returned by a Bison action in order to start error recovery without
#  * printing an error message.
#  */
YYERROR = 2

# /**
#  * Internal return codes that are not supported for user semantic
#  * actions.
#  */
YYERRLAB = 3
YYNEWSTATE = 4
YYDEFAULT = 5
YYREDUCE = 6
YYERRLAB1 = 7
YYRETURN = 8
  
YYGETTOKEN = 9# /* Signify that a new token is expected when doing push-parsing.  */




class Calc():
# {
  
  # Version number for the Bison executable that generated this parser.  
  bisonVersion = "3.8.2";

  # Name of the skeleton that generated this parser. 
  bisonSkeleton = "lalr1.py";








  # /**
  #  * The object doing lexical analysis for us.
  #  */
  # yylexer = None





  # /**
  #  * Instantiates the Bison-generated parser.
  #  * @param yylexer The scanner that will supply tokens to the parser.
  #  */
  def __init__(self, yylexer):
  # {

    self.yylacStack = []
    self.yylacEstablished = False
    self.yylexer = yylexer
    return

  # }


  yyDebugStream = sys.stderr

  # /**
  #  * The <tt>PrintStream</tt> on which the debugging output is printed.
  #  */
  def getDebugStream(self):
    return self.yyDebugStream

  # /**
  #  * Set the <tt>PrintStream</tt> on which the debug output is printed.
  #  * @param s The stream that is used for debugging output.
  #  */
  def setDebugStream(self, s):
    self.yyDebugStream = s
    return

  yydebug = 0

  # /**
  #  * Answer the verbosity of the debugging output; 0 means that all kinds of
  #  * output from the parser are suppressed.
  #  */
  def getDebugLevel(self):
    return self.yydebug

  # /**
  #  * Set the verbosity of the debugging output; 0 means that all kinds of
  #  * output from the parser are suppressed.
  #  * @param level The verbosity level for debugging output.
  #  */
  def setDebugLevel(self, level):
    self.yydebug = level
    return


  yynerrs = 0;

  # /**
  #  * The number of syntax errors so far.
  #  */
  def getNumberOfErrors(self):
    return self.yynerrs

  # /**
  #  * Print an error message via the lexer.
  #  * Use a <code>None</code> location.
  #  * @param msg The error message.
  #  */
  def yyerror(self, *args):
    if(len(args) == 1):
      loc = None
      msg = args[0]
    else:
      loc = args[0]
      msg = args[1]
      if(isinstance(loc, Position)):
        loc = Location (loc)
      else:
        assert(isinstance(loc, Location))
    self.yylexer.yyerror(loc, msg)
    return
  

  # /**
  #  * Print an error message via the lexer.
  #  * @param loc The location associated with the message.
  #  * @param msg The error message.
  #  */
  # def yyerror(Location loc, String msg) {
  #     yylexer.yyerror(loc, msg);
  # }

  # /**
  #  * Print an error message via the lexer.
  #  * @param pos The position associated with the message.
  #  * @param msg The error message.
  #  */
  # public final void yyerror(Position pos, String msg) {
  #     yylexer.yyerror(new Location (pos), msg);
  # }

  def yycdebugNnl(self, s):
    if (0 < self.yydebug):
      print(s, file = self.yyDebugStream)
  

  def yycdebug(self, s):
    if (0 < self.yydebug):
      print(s, file = self.yyDebugStream)
  

  class YYStack():
    # private int[] stateStack = new int[16];
    stateStack = []
    # private Location[] locStack = new Location[16];
    locStack = []
    # private Object[] valueStack = new Object[16];
    valueStack = []

    # size = 16
    height = -1

    def setAt(self, list2, index, value):
      if(index < len(list2)):
        list2[index] = value
      else:
        list2.insert(index, value)

    def push(self, state, value, loc):
      self.height += 1
      # if (self.size == self.height):
      #   newStateStack = [0] * (size * 2)
      #   System.arraycopy(stateStack, 0, newStateStack, 0, height);
      #   stateStack = newStateStack;
      #   Location[] newLocStack = new Location[size * 2];
      #   System.arraycopy(locStack, 0, newLocStack, 0, height);
      #   locStack = newLocStack;

      #   Object[] newValueStack = new Object[size * 2];
      #   System.arraycopy(valueStack, 0, newValueStack, 0, height);
      #   valueStack = newValueStack;

      #   size *= 2;
      # }

      # stateStack[height] = state;
      # locStack[height] = loc;
      # valueStack[height] = value;
      self.setAt(self.stateStack, self.height, state)
      self.setAt(self.locStack, self.height, loc)
      self.setAt(self.valueStack, self.height, value)
      return
    # }

    # def pop() {
    #   pop(1);
    # }

    def pop(self, num=1):
      # // Avoid memory leaks... garbage collection is a white lie!
      # if (0 < num) {
      #   java.util.Arrays.fill(valueStack, height - num + 1, height + 1, None);
      #   java.util.Arrays.fill(locStack, height - num + 1, height + 1, None);
      # }
      self.height -= num
    

    def stateAt(self, i):
      return self.stateStack[self.height - i]
    


    def locationAt(self, i):
      return self.locStack[self.height - i]
    

    def valueAt(self, i):
      return self.valueStack[self.height - i]
    

    # // Print the state stack on the debug stream.
    def printf(self, out):
      print("Stack now", file = out)

      for i in range(self.height + 1):
        print(' ', file = out)
        print(self.stateStack[i], file = out)
      
      print('', file = out)
    
  # }

  yyerrstatus_ = 0


  # /* Lookahead token kind.  */
  yychar = YYEMPTY_
  # /* Lookahead symbol kind.  */
  yytoken = None

  # /* State.  */
  yyn = 0
  yylen = 0
  yystate = 0
  yystack = YYStack ()
  label = YYNEWSTATE


  # /* The location where the error started.  */
  yyerrloc = None

  # /* Location. */
  yylloc = Location (None, None)

  # /* Semantic value of the lookahead.  */
  yylval = None

  # /**
  #  * Whether error recovery is being done.  In this state, the parser
  #  * reads token until it reaches a known state, and then restarts normal
  #  * operation.
  #  */
  def recovering (self):
  
    return self.yyerrstatus_ == 0
  

  # /** Compute post-reduction state.
  #  * @param yystate   the current state
  #  * @param yysym     the nonterminal to push on the stack
  #  */
  def yyLRGotoState(self, yystate, yysym):
    yyr = self.yypgoto_[yysym - YYNTOKENS_] + yystate
    if (0 <= yyr and yyr <= YYLAST_ and self.yycheck_[yyr] == yystate):
      return self.yytable_[yyr]
    else:
      return self.yydefgoto_[yysym - YYNTOKENS_]
  

  def yyaction(self, yyn, yystack, yylen):
  
    # /* If YYLEN is nonzero, implement the default value of the action:
    #    '$$ = $1'.  Otherwise, use the top of the stack.

    #    Otherwise, the following line sets YYVAL to garbage.
    #    This behavior is undocumented and Bison
    #    users should not rely upon it.  */     
    if(0 < yylen):
      yyval = yystack.valueAt(yylen - 1)
    else:
      yyval = yystack.valueAt(0)
    yyloc = yylloc(yystack, yylen)
    

    self.yyReducePrint(yyn, yystack)

    # switch (yyn)
      # {
      #case 5: #line: exp "end of line"
  #
  

    if (yyn == 5):     
      #"Calc.y":148
  #
  

                      
      print(yystack.valueAt (1)); 
  
  # break;


  #case 7: #exp: "number"
  #
  

    if (yyn == 7):     
      #"Calc.y":155
  #
  

                      
      yyval = yystack.valueAt (0); 
  # break;


  #case 8: #exp: exp "=" exp
  #
  

    if (yyn == 8):     
      #"Calc.y":158
  #
  

  
      if (yystack.valueAt (2).intValue() != yystack.valueAt (0).intValue()):
        self.yyerror((yyloc), "calc: error: " + yystack.valueAt (2) + " != " + yystack.valueAt (0));
  
  # break;


  #case 9: #exp: exp "+" exp
  #
  

    if (yyn == 9):     
      #"Calc.y":162
  #
  

                      
      yyval = yystack.valueAt (2) + yystack.valueAt (0);  
  # break;


  #case 10: #exp: exp "-" exp
  #
  

    if (yyn == 10):     
      #"Calc.y":164
  #
  

                      
      yyval = yystack.valueAt (2) - yystack.valueAt (0);  
  # break;


  #case 11: #exp: exp "*" exp
  #
  

    if (yyn == 11):     
      #"Calc.y":166
  #
  

                      
      yyval = yystack.valueAt (2) * yystack.valueAt (0);  
  # break;


  #case 12: #exp: exp "/" exp
  #
  

    if (yyn == 12):     
      #"Calc.y":168
  #
  

                      
      yyval = yystack.valueAt (2) / yystack.valueAt (0);  
  # break;


  #case 13: #exp: "-" exp
  #
  

    if (yyn == 13):     
      #"Calc.y":170
  #
  

                      
      yyval = -yystack.valueAt (0); 
  # break;


  #case 14: #exp: exp "^" exp
  #
  

    if (yyn == 14):     
      #"Calc.y":172
  #
  

                      
      yyval = math.pow(yystack.valueAt (2), yystack.valueAt (0)); 
  # break;


  #case 15: #exp: "(" exp ")"
  #
  

    if (yyn == 15):     
      #"Calc.y":174
  #
  

                      
      yyval = yystack.valueAt (1); 
  # break;


  #case 16: #exp: "(" error ")"
  #
  

    if (yyn == 16):     
      #"Calc.y":176
  #
  

                      
      yyval = 1111; 
  # break;


  #case 17: #exp: "!"
  #
  

    if (yyn == 17):     
      #"Calc.y":178
  #
  

                      
      yyval = 0; return self.YYERROR; 
  # break;


  #case 18: #exp: "-" error
  #
  

    if (yyn == 18):     
      #"Calc.y":180
  #
  

                      
      yyval = 0; return self.YYERROR; 
  # break;



#"Calc.py":982
  #
  


        # default: break;
    

    self.yySymbolPrint("-> $$ =", SymbolKind.get(self.yyr1_[yyn]), yyval, yyloc);

    yystack.pop(yylen);
    yylen = 0;
    # /* Shift the result of the reduction.  */
    yystate = self.yyLRGotoState(yystack.stateAt(0), self.yyr1_[yyn]);
    yystack.push(yystate, yyval, yyloc);
    return self.YYNEWSTATE;
  


  # /*--------------------------------.
  # | Print this symbol on YYOUTPUT.  |
  # `--------------------------------*/

  def yySymbolPrint(self, s, yykind, yyvalue, yylocation):
      if (0 < self.yydebug):
        if(yykind.getCode() < YYNTOKENS_):
          sToken = " token "
        else:
          sToken = " nterm "
        if(yyvalue == None):
          s_yyvalue = "(None)"
        else:
          s_yyvalue = str(yyvalue)
        self.yycdebug(s
                   + sToken
                   + yykind.getName() + " ("
                   + yylocation + ": "
                   + s_yyvalue + ")")
      
  



  # /**
  #  * Push Parse input from external lexer
  #  *
  #  * @param yylextoken current token
  #  * @param yylexval current lval
  #  * @param yylexloc current position
  #  *
  #  * @return <tt>YYACCEPT, YYABORT, YYPUSH_MORE</tt>
  #  */
  def push_parse(self, yylextoken, yylexval, yylexloc):
  
    # /* @$.  */
    yyloc = None
    if(yylexloc != None and isinstance(yylexloc, Position)):
      yylexloc = Location(yylexloc)



    if (not self.push_parse_initialized):
      # {
        self.push_parse_initialize ();

        self.yycdebug ("Starting parse");
        self.yyerrstatus_ = 0;
    else:
        label = self.YYGETTOKEN;

    push_token_consumed = True

    while (True):
      # switch (label)
      # {
        # /* New state.  Unlike in the C/C++ skeletons, the state is already
        #    pushed when we come here.  */
      if(label == self.YYNEWSTATE):
        self.yycdebug ("Entering state " + self.yystate);
        if (0 < self.yydebug):
          self.yystack.print (self.yyDebugStream);

        # /* Accept?  */
        if (self.yystate == self.YYFINAL_):
          
          label = self.YYACCEPT
          continue

        # /* Take a decision.  First try without lookahead.  */
        yyn = self.yypact_[self.yystate]
        if (self.yyPactValueIsDefault (yyn)):
          # {
          label = self.YYDEFAULT
          continue
          # }
        
  # /* Fall Through */

      if(label == self.YYGETTOKEN):
        # /* Read a lookahead token.  */
        if (self.yychar == YYEMPTY_):
          # {

            if (not push_token_consumed):
              return self.YYPUSH_MORE
            self.yycdebug ("Reading a token");
            self.yychar = yylextoken
            self.yylval = yylexval
            self.yylloc = yylexloc
            push_token_consumed = False
          # }

        # /* Convert token to internal form.  */
        self.yytoken = self.yytranslate_ (self.yychar)
        self.yySymbolPrint("Next token is", self.yytoken,
                      self.yylval, self.yylloc);

        if (self.yytoken == SymbolKind.S_YYerror):
          # {
            # // The scanner already issued an error message, process directly
            # // to error recovery.  But do not keep the error token as
            # // lookahead, it is too special and may lead us to an endless
            # // loop in error recovery. */
            self.yychar = Lexer.YYUNDEF;
            self.yytoken = SymbolKind.S_YYUNDEF;
            self.yyerrloc = yylloc;
            label = self.YYERRLAB1;
          # }
        else:
          # {
            # /* If the proper action on seeing token YYTOKEN is to reduce or to
            #    detect an error, take that action.  */
            yyn += self.yytoken.getCode();
            if (yyn < 0 or YYLAST_ < yyn or self.yycheck_[yyn] != self.yytoken.getCode()) :
              if (not self.yylacEstablish(self.yystack, self.yytoken)) :
                label = self.YYERRLAB
              else:
                label = self.YYDEFAULT
              continue
            # }

            # /* <= 0 means reduce or error.  */
            yyn = self.yytable_[yyn]
            if(yyn <= 0):
              # {
                if (self.yyTableValueIsError(yyn)) :
                  label = self.YYERRLAB;
                elif (not self.yylacEstablish(self.yystack, self.yytoken)) :
                  label = self.YYERRLAB;
                else:
                  yyn = -yyn;
                  label = self.YYREDUCE;
                # }
              # }

            else:
              # {
                # /* Shift the lookahead token.  */
                self.yySymbolPrint("Shifting", self.yytoken,
                              self.yylval, self.yylloc);

                # /* Discard the token being shifted.  */
                self.yychar = YYEMPTY_;

                # /* Count tokens shifted since error; after three, turn off error
                #    status.  */
                if (self.yyerrstatus_ > 0):
                  self.yyerrstatus_ -= 1

                self.yystate = yyn;
                self.yystack.push(self.yystate, self.yylval, self.yylloc);
                self.yylacDiscard("shift");
                label = self.YYNEWSTATE;
              # }
          # }
        continue

      # /*-----------------------------------------------------------.
      # | yydefault -- do the default action for the current state.  |
      # `-----------------------------------------------------------*/
      if(label == self.YYDEFAULT):
        yyn = self.yydefact_[self.yystate];
        if (yyn == 0):
          label = self.YYERRLAB;
        else:
          label = self.YYREDUCE;
        continue

      # /*-----------------------------.
      # | yyreduce -- Do a reduction.  |
      # `-----------------------------*/
      if(label == self.YYREDUCE):
        yylen = self.yyr2_[yyn];
        label = self.yyaction(yyn, self.yystack, yylen);
        self.yystate = self.yystack.stateAt(0);
        continue

      # /*------------------------------------.
      # | yyerrlab -- here on detecting error |
      # `------------------------------------*/
      if(label == self.YYERRLAB):
        # /* If not already recovering from an error, report this error.  */
        if (self.yyerrstatus_ == 0):
          # {
            yynerrs += 1
            if (self.yychar == YYEMPTY_):
              self.yytoken = None
            self.yyreportSyntaxError(self.Context(self, self.yystack, self.yytoken, self.yylloc));
          # }

        yyerrloc = yylloc;
        if (yyerrstatus_ == 3):
          # {
            # /* If just tried and failed to reuse lookahead token after an
            #    error, discard it.  */

            if (yychar <= Lexer.YYEOF):
              # {
                # /* Return failure if at end of input.  */
                if (yychar == Lexer.YYEOF):
                  label = self.YYABORT; continue;
              # }
            else:
              yychar = YYEMPTY_;
          # }

        # /* Else will try to reuse lookahead token after shifting the error
        #    token.  */
        label = self.YYERRLAB1;
        continue;

      # /*-------------------------------------------------.
      # | errorlab -- error raised explicitly by YYERROR.  |
      # `-------------------------------------------------*/
      if(label == self.YYERROR):
        yyerrloc = self.yystack.locationAt (yylen - 1);
        # /* Do not reclaim the symbols of the rule which action triggered
        #    this YYERROR.  */
        self.yystack.pop (yylen);
        yylen = 0;
        yystate = self.yystack.stateAt(0);
        label = self.YYERRLAB1;
        continue;

      # /*-------------------------------------------------------------.
      # | yyerrlab1 -- common code for both syntax error and YYERROR.  |
      # `-------------------------------------------------------------*/
      if(label == self.YYERRLAB1):
        yyerrstatus_ = 3;      # /* Each real token shifted decrements this.  */

        # // Pop stack until we find a state that shifts the error token.
        while (True):
          # {
            yyn = self.yypact_[yystate];
            if (not self.yyPactValueIsDefault (yyn)):
              # {
                yyn += SymbolKind.S_YYerror.getCode();
                if (0 <= yyn and yyn <= YYLAST_
                    and self.yycheck_[yyn] == SymbolKind.S_YYerror.getCode()):
                  # {
                    yyn = self.yytable_[yyn];
                    if (0 < yyn):
                      break;
                  # }
              # }

            # /* Pop the current state because it cannot handle the
            #  * error token.  */
            if (self.yystack.height == 0):
              label = self.YYABORT; break;


            yyerrloc = self.yystack.locationAt (0);
            self.yystack.pop ();
            yystate = self.yystack.stateAt(0);
            if (0 < self.yydebug):
              self.yystack.print (self.yyDebugStream);
          # }

        if (label == self.YYABORT):
          # /* Leave the switch.  */
          continue;


        # /* Muck with the stack to setup for yylloc.  */
        self.yystack.push (0, None, yylloc);
        self.yystack.push (0, None, yyerrloc);
        yyloc = yylloc (self.yystack, 2);
        self.yystack.pop (2);

        # /* Shift the error token.  */
        self.yylacDiscard("error recovery");
        self.yySymbolPrint("Shifting", SymbolKind.get(self.yystos_[yyn]),
                      self.yylval, yyloc);

        self.yystate = yyn;
        self.yystack.push (yyn, self.yylval, yyloc);
        label = self.YYNEWSTATE;
        continue;

        # /* Accept.  */
      if(label == self.YYACCEPT):
        self.push_parse_initialized = False; return self.YYACCEPT;

        # /* Abort.  */
      if(label == self.YYABORT):
        self.push_parse_initialized = False; return self.YYABORT;
      # }
# }

  push_parse_initialized = False;

    # /**
    #  * (Re-)Initialize the state of the push parser.
    #  */
  def push_parse_initialize (self):
  # {
  #   /* Lookahead and lookahead in internal form.  */
    self.yychar = YYEMPTY_;
    self.yytoken = None;

    # /* State.  */
    self.yyn = 0
    self.yylen = 0
    self.yystate = 0
    self.yystack = self.YYStack()
    self.yylacStack = []
    self.yylacEstablished = False;
    self.label = self.YYNEWSTATE

    # /* Error handling.  */
    self.yynerrs = 0
    # /* The location where the error started.  */
    self.yyerrloc = None
    self.yylloc = Location (None, None)

    # /* Semantic value of the lookahead.  */
    self.yylval = None;

    self.yystack.push (self.yystate, self.yylval, self.yylloc)

    self.push_parse_initialized = True

  # }

  # /**
  #  * Push parse given input from an external lexer.
  #  *
  #  * @param yylextoken current token
  #  * @param yylexval current lval
  #  * @param yyylexpos current position
  #  *
  #  * @return <tt>YYACCEPT, YYABORT, YYPUSH_MORE</tt>
  #  */
  # def push_parse(int yylextoken, Object yylexval, Position yylexpos) throws java.io.IOException :
  #     return push_parse(yylextoken, yylexval, new Location(yylexpos));
  # }




  # /**
  #  * Information needed to get the list of expected tokens and to forge
  #  * a syntax error diagnostic.
  #  */
  class Context():
    def __init__(self, parser, stack, token, loc):
      self.yyparser = parser
      self.yystack = stack
      self.yytoken = token
      self.yylocation = loc
      self.yylacStack = []
      self.yylacEstablished = False
    # }

    # private Calc yyparser;
    # private YYStack yystack;


    # /**
    #  * The symbol kind of the lookahead token.
    #  */
    def getToken(self):
      return self.yytoken;
    # }

    # private SymbolKind yytoken;

    # /**
    #  * The location of the lookahead.
    #  */
    def getLocation(self):
      return self.yylocation;
    # }

    # private Location yylocation;
    NTOKENS = YYNTOKENS_

    # /**
    #  * Put in YYARG at most YYARGN of the expected tokens given the
    #  * current YYCTX, and return the number of tokens stored in YYARG.  If
    #  * YYARG is None, return the number of expected tokens (guaranteed to
    #  * be less than YYNTOKENS).
    #  */
    # def getExpectedTokens(self, yyarg, yyargn):
    #   return getExpectedTokens (yyarg, 0, yyargn);
    # }

    def getExpectedTokens(self, yyarg, yyoffset=0, yyargn=0):
      yycount = yyoffset;
      # // Execute LAC once. We don't care if it is successful, we
      # // only do it for the sake of debugging output.
      if (not self.yyparser.yylacEstablished):
        self.yyparser.yylacCheck(self.yystack, self.yytoken)

      for yyx in range(YYNTOKENS_):
        # {
        yysym = SymbolKind.get(yyx);
        if (yysym != SymbolKind.S_YYerror
            and yysym != SymbolKind.S_YYUNDEF
            and self.yyparser.yylacCheck(self.yystack, yysym)):
          # {
            if (yyarg == None):
              yycount += 1
            elif (yycount == yyargn):
              return 0
            else:
              yyarg[yycount] = yysym
              yycount += 1
          # }
        
      if (yyarg != None and yycount == yyoffset and yyoffset < yyargn):
        yyarg[yycount] = None
      return yycount - yyoffset
    # }
  # }


    # /** Check the lookahead yytoken.
    #  * \returns  True iff the token will be eventually shifted.
    #  */
    def yylacCheck(self, yystack, yytoken):
    # {
      # // Logically, the yylacStack's lifetime is confined to this function.
      # // Clear it, to get rid of potential left-overs from previous call.
      yylacStack = self.yylacStack
      yylacStack.clear()
      # // Reduce until we encounter a shift and thereby accept the token.
      Calc.yycdebugNnl("LAC: checking lookahead " + yytoken.getName() + ":")
      lacTop = 0;
      while (True):
        # {
        if(yylacStack.isEmpty()):
          topState = yystack.stateAt(lacTop)
        else:
          topState = yylacStack.get(yylacStack.size() - 1)
        # topState = (yylacStack.isEmpty()
        #                 ? yystack.stateAt(lacTop)
        #                 : yylacStack.get(yylacStack.size() - 1));
        yyrule = Calc.yypact_[topState];
        check = Calc.yyPactValueIsDefault(yyrule)
        if (not check):
          yyrule += yytoken.getCode()
          check = yyrule < 0 or YYLAST_ < yyrule or yycheck_[yyrule] != yytoken.getCode()
        if (check):
          # {
            # // Use the default action.
            yyrule = yydefact_[+topState];
            if (yyrule == 0) :
              Calc.yycdebug(" Err");
              return False;
            # }
          # }
        else:
          # {
            # // Use the action from yytable.
            yyrule = yytable_[yyrule];
            if (Calc.yyTableValueIsError(yyrule)) :
              Calc.yycdebug(" Err");
              return False;
            # }
            if (0 < yyrule) :
              Calc.yycdebug(" S" + yyrule);
              return True;
            # }
            yyrule = -yyrule;
          # }
        # // By now we know we have to simulate a reduce.
        Calc.yycdebugNnl(" R" + (yyrule - 1));
        # // Pop the corresponding number of values from the stack.
        # {
        yylen = yyr2_[yyrule];
        # // First pop from the LAC stack as many tokens as possible.
        lacSize = yylacStack.size();
        if (yylen < lacSize) :
          # // yylacStack.setSize(lacSize - yylen);
          # for (/* Nothing */; 0 < yylen; yylen -= 1) {
          #   yylacStack.remove(yylacStack.size() - 1);
          while(0 < yylen):
            yylacStack.remove(yylacStack.size() - 1)
            yylen -= 1
          # }
          yylen = 0;
        elif (lacSize != 0) :
          yylacStack.clear();
          yylen -= lacSize;
        # }
        # // Only afterwards look at the main stack.
        # // We simulate popping elements by incrementing lacTop.
        lacTop += yylen;
        # }
        # // Keep topState in sync with the updated stack.
        if(yylacStack.isEmpty()):
          topState = yystack.stateAt(lacTop)
        else:
          topState = yylacStack.get(yylacStack.size() - 1)
        # topState = (yylacStack.isEmpty()
        #             ? yystack.stateAt(lacTop)
        #             : yylacStack.get(yylacStack.size() - 1));
        # // Push the resulting state of the reduction.
        state = Calc.yyLRGotoState(topState, yyr1_[yyrule]);
        Calc.yycdebugNnl(" G" + state);
        yylacStack.add(state);
      # }
    # }

    # /** Establish the initial context if no initial context currently exists.
    #  * \returns  True iff the token will be eventually shifted.
    #  */
    def yylacEstablish(self, yystack, yytoken) :
      # /* Establish the initial context for the current lookahead if no initial
      #    context is currently established.

      #    We define a context as a snapshot of the parser stacks.  We define
      #    the initial context for a lookahead as the context in which the
      #    parser initially examines that lookahead in order to select a
      #    syntactic action.  Thus, if the lookahead eventually proves
      #    syntactically unacceptable (possibly in a later context reached via a
      #    series of reductions), the initial context can be used to determine
      #    the exact set of tokens that would be syntactically acceptable in the
      #    lookahead's place.  Moreover, it is the context after which any
      #    further semantic actions would be erroneous because they would be
      #    determined by a syntactically unacceptable token.

      #    yylacEstablish should be invoked when a reduction is about to be
      #    performed in an inconsistent state (which, for the purposes of LAC,
      #    includes consistent states that don't know they're consistent because
      #    their default reductions have been disabled).

      #    For parse.lac=full, the implementation of yylacEstablish is as
      #    follows.  If no initial context is currently established for the
      #    current lookahead, then check if that lookahead can eventually be
      #    shifted if syntactic actions continue from the current context.  */
      if (self.yylacEstablished) :
        return True;
      else:
        yycdebug("LAC: initial context established for " + yytoken.getName());
        self.yylacEstablished = True;
        return yylacCheck(yystack, yytoken);
      # }
    # }

    # /** Discard any previous initial lookahead context because of event.
    #  * \param event  the event which caused the lookahead to be discarded.
    #  *               Only used for debbuging output.  */
    def yylacDiscard(self,  event):
    #  /* Discard any previous initial lookahead context because of Event,
    #     which may be a lookahead change or an invalidation of the currently
    #     established initial context for the current lookahead.

    #     The most common example of a lookahead change is a shift.  An example
    #     of both cases is syntax error recovery.  That is, a syntax error
    #     occurs when the lookahead is syntactically erroneous for the
    #     currently established initial context, so error recovery manipulates
    #     the parser stacks to try to find a new initial context in which the
    #     current lookahead is syntactically acceptable.  If it fails to find
    #     such a context, it discards the lookahead.  */
      if (self.yylacEstablished) :
        yycdebug("LAC: initial context discarded due to " + event);
        self.yylacEstablished = False;
      # }
    # }

    # /** The stack for LAC.
    #  * Logically, the yylacStack's lifetime is confined to the function
    #  * yylacCheck. We just store it as a member of this class to hold
    #  * on to the memory and to avoid frequent reallocations.
    #  */
    # yylacStack = []
    # /**  Whether an initial LAC context was established. */
    # yylacEstablished = False




  # /**
  #  * Build and emit a "syntax error" message in a user-defined way.
  #  *
  #  * @param ctx  The context of the error.
  #  */
  def  yyreportSyntaxError(self,  yyctx) :
      self.yylexer.reportSyntaxError(yyctx);
  # }

  # /**
  #  * Whether the given <code>yypact_</code> value indicates a defaulted state.
  #  * @param yyvalue   the value to check
  #  */
  def  yyPactValueIsDefault(self, yyvalue) :
    return yyvalue == self.yypact_ninf_;
  # }

  # /**
  #  * Whether the given <code>yytable_</code>
  #  * value indicates a syntax error.
  #  * @param yyvalue the value to check
  #  */
  def  yyTableValueIsError(self,  yyvalue):
    return yyvalue == self.yytable_ninf_;
  # }

  yypact_ninf_ = -10;
  yytable_ninf_ = -1;

#YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
  #
  
#STATE-NUM.
  #
  

  
  def yypact_init():  
      return (
      25,    -9,   -10,    38,    39,   -10,   -10,    20,   -10,    49,
     -10,   -10,    -2,    -5,    58,   -10,   -10,    -1,    -1,    -1,
      -1,    -1,    -1,   -10,   -10,   -10,     3,     3,    -2,    -2,
      -2,    66
    )
  yypact_ = yypact_init()
  

#YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
  #
  
#Performed when YYTABLE does not specify something else to do.  Zero
  #
  
#means the default is an error.
  #
  

  
  def yydefact_init():  
      return (
       0,     0,    17,     0,     0,     4,     7,     0,     2,     0,
       6,    18,    13,     0,     0,     1,     3,     0,     0,     0,
       0,     0,     0,     5,    16,    15,     9,    10,    11,    12,
      14,     8
    )
  yydefact_ = yydefact_init()
  

#YYPGOTO[NTERM-NUM].
  #
  

  
  def yypgoto_init():  
      return (
     -10,   -10,     0,    -3
    )
  yypgoto_ = yypgoto_init()
  

#YYDEFGOTO[NTERM-NUM].
  #
  

  
  def yydefgoto_init():  
      return (
       0,     7,     8,     9
    )
  yydefgoto_ = yydefgoto_init()
  

#YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
  #
  
#positive, shift that token.  If negative, reduce the rule whose
  #
  
#number is the opposite.  If YYTABLE_NINF, syntax error.
  #
  

  
  def yytable_init():  
      return (
      12,    14,     2,    10,     3,    24,    21,    16,     4,    19,
      20,    21,     6,     0,    26,    27,    28,    29,    30,    31,
      15,     1,     0,     2,     0,     3,     1,     0,     2,     4,
       3,     0,     5,     6,     4,     0,     0,     5,     6,    11,
      13,     2,     2,     3,     3,     0,     0,     4,     4,     0,
       0,     6,     6,    17,    18,    19,    20,    21,     0,     0,
      22,    23,    17,    18,    19,    20,    21,     0,    25,    22,
      17,    18,    19,    20,    21,     0,     0,    -1
    )
  yytable_ = yytable_init()
  


  def yycheck_init():  
      return (
       3,     4,     3,    12,     5,    10,     8,     7,     9,     6,
       7,     8,    13,    -1,    17,    18,    19,    20,    21,    22,
       0,     1,    -1,     3,    -1,     5,     1,    -1,     3,     9,
       5,    -1,    12,    13,     9,    -1,    -1,    12,    13,     1,
       1,     3,     3,     5,     5,    -1,    -1,     9,     9,    -1,
      -1,    13,    13,     4,     5,     6,     7,     8,    -1,    -1,
      11,    12,     4,     5,     6,     7,     8,    -1,    10,    11,
       4,     5,     6,     7,     8,    -1,    -1,    11
    )
  yycheck_ = yycheck_init()
  

#YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
  #
  
#state STATE-NUM.
  #
  

  
  def yystos_init():  
      return (
       0,     1,     3,     5,     9,    12,    13,    16,    17,    18,
      12,     1,    18,     1,    18,     0,    17,     4,     5,     6,
       7,     8,    11,    12,    10,    10,    18,    18,    18,    18,
      18,    18
    )
  yystos_ = yystos_init()
  

#YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.
  #
  

  
  def yyr1_init():  
      return (
       0,    15,    16,    16,    17,    17,    17,    18,    18,    18,
      18,    18,    18,    18,    18,    18,    18,    18,    18
    )
  yyr1_ = yyr1_init()
  

#YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.
  #
  

  
  def yyr2_init():  
      return (
       0,     2,     1,     2,     1,     2,     2,     1,     3,     3,
       3,     3,     3,     2,     3,     3,     3,     1,     2
    )
  yyr2_ = yyr2_init()
  



  #YYRLINE[YYN] -- Source line where rule number YYN was defined.
  #
  

  
  def yyrline_init():  
      return (
       0,   142,   142,   143,   147,   148,   151,   155,   157,   162,
     164,   166,   168,   170,   172,   174,   176,   178,   180
    )
  yyrline_ = yyrline_init()
  


  # // Report on the debug stream that the rule yyrule is going to be reduced.
  def yyReducePrint ( yyrule, yystack):
  # {
    if (yydebug == 0):
      return;

    yylno = yyrline_[yyrule];
    yynrhs = yyr2_[yyrule];
    # /* Print the symbols being reduced, and their result.  */
    yycdebug ("Reducing stack by rule " + (yyrule - 1)
              + " (line " + yylno + "):");

    # /* The symbols being reduced.  */
    for  yyi in range( yynrhs):
      yySymbolPrint("   $" + (yyi + 1) + " =",
                    SymbolKind.get(yystos_[yystack.stateAt(yynrhs - (yyi + 1))]),
                    yystack.valueAt ((yynrhs) - (yyi + 1)),
                    yystack.locationAt ((yynrhs) - (yyi + 1)));
  

  # /* YYTRANSLATE_(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
  #    as returned by yylex, with out-of-bounds checking.  */
  def yytranslate_(self, t):
  
    # // Last valid token kind.
    code_max = 269;
    if (t <= 0):
      return SymbolKind.S_YYEOF;
    elif (t <= code_max):
      return SymbolKind.get(yytranslate_table_[t]);
    else:
      return SymbolKind.S_YYUNDEF;
  # }
  
  def yytranslate_table_init():  
      return (
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14
    )
  yytranslate_table_ = yytranslate_table_init()
  




#Unqualified %code blocks.
  #
  

#"Calc.y":110
  #
  


  

 
  

#"Calc.py":1853
  #
  


# }
#"Calc.y":184
  #
  




#/**
# * A Stream reader that keeps track of the current Position.
# */
class PositionReader ( ) :

  #position =  Position()
  #// Position before the latest call to "read", i.e. position
  #// of the last character of the current token.
  #previousPosition =  Position()

  def __init__( self, reader) :
    self.reader = reader
    self.position = Position()
    self.previousPosition = Position()
  

  def  read(self):
    self.previousPosition.set(self.position);
    res = super.read(1);
    if (res > -1) :
      c = int( res);
      if (c == '\r' or c == '\n'):
        position.line += 1;
        position.column = 1;
      else:
        position.column += 1;
      #}
    #}
    return res;
  #}

  def  getPosition(self) :
    return self.position;
  

  def  getPreviousPosition(self):
    return self.previousPosition;
  #}
#}


class CalcLexer (Lexer)  :

  #StreamTokenizer st;
  #PositionReader reader;

  def __init__( self, is2):
    self.reader =  PositionReader(is2)
    self.st =  StreamTokenizer(reader);
    self.st.resetSyntax();
    self.st.eolIsSignificant(True);
    self.st.wordChars('0', '9');
  #}

  start =  Position(1, 0);
  end =  Position(1, 0);

  #/**
  # * The location of the last token read.
  # * Implemented with getStartPos and getEndPos in pull parsers.
  # */
  def  getLocation(self) :
    return Location( Position(self.start),  Position(self.end));
  #}

  #/**
  # * Build and emit a syntax error message.
  # */
  def  reportSyntaxError(self,  ctx) :
    print(ctx.getLocation() + ": syntax error", file = sys.stderr);
    #{
    TOKENMAX = 10;
    arg =  [None] * TOKENMAX
    n = ctx.getExpectedTokens(arg, TOKENMAX);
    for  i in range( n):
      if(i == 0):
        print(": expected " + arg[i].getName(), file = sys.stderr)
      else:
        print(" or " + arg[i].getName(), file = sys.stderr);
  #}
  #{
    lookahead = ctx.getToken();
    if (lookahead != None):
      print(" before " + lookahead.getName(), file = sys.stderr);
  #}
    println("", file = sys.stderr);
  #}

  #/**
  # * Emit an error referring to the given location in a user-defined way.
  # *
  # * @@param loc The location of the element to which the
  # *                error message is related.
  # * @@param msg The string for the error message.
  # */
  def  yyerror(self,  loc,  msg):
    if (loc == None):
      System.err.println(msg);
    else:
      System.err.println(loc + ": " + msg);
  #}

  yylval = None;

  #/**
  # * The value of the last token read.  Called getLVal in pull parsers.
  # */
  def  getValue():
    return self.yylval;
  #}

  #/**
  # * Fetch the next token.  Called yylex in pull parsers.
  # */
  def  getToken():
    start.set(reader.getPosition());
    ttype = st.nextToken();
    end.set(reader.getPosition());
    if (ttype == StreamTokenizer.TT_EOF):
      return YYEOF;
    if (ttype ==  StreamTokenizer.TT_EOL):
      end.line += 1;
      end.column = 0;
      return EOL;
    if (ttype ==  StreamTokenizer.TT_WORD):
      yylval = Integer.parseInt(st.sval);
      end.set(reader.getPreviousPosition());
      return NUM;
    if (ttype ==  ' ' or ttype ==  '\t'):
      return getToken();
    if (ttype ==  '!'):
      return BANG;
    if (ttype ==  '+'):
      return PLUS;
    if (ttype ==  '-'):
      return MINUS;
    if (ttype ==  '*'):
      return STAR;
    if (ttype ==  '/'):
      return SLASH;
    if (ttype ==  '^'):
      return CARET;
    if (ttype ==  '('):
      return LPAREN;
    if (ttype ==  ')'):
      return RPAREN;
    if (ttype ==  '='):
      return EQUAL;
    
    raise  AssertionError("invalid character: " + ttype);
    #}
  #}
#}


import sys
def main(args):
  scanner = CalcLexer(sys.stdin);
  parser = Calc(scanner);
  for arg in args:
    if (arg =="-p"):
      parser.setDebugLevel(1);
  status = 0;
  while(True):
    token = scanner.getToken();
    lval = scanner.getValue();
    yyloc = scanner.getLocation();
    status = parser.push_parse(token, lval, yyloc);
    if(status != Calc.YYPUSH_MORE):
      break      
  if (status != Calc.YYACCEPT):
    sys.exit(1);
  return

if __name__ == "__main__":
    # execute only if run as a script
    import sys
    main(sys.argv)
