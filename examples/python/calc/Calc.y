/* Parser and scanner for calc in Java.   -*- Java -*-

   Copyright (C) 2018-2021 Free Software Foundation, Inc.

   This file is part of Bison, the GNU Compiler Compiler.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

%language "python"

%define api.parser.class {Calc}
%define api.parser.public
%define api.push-pull push

// Customized syntax error messages (see reportSyntaxError)...
%define parse.error custom

// ... with locations...
%locations

// ... and accurate list of expected tokens.
%define parse.lac full

%define parse.trace

%code imports {
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
  

}

%code {
  

 
  
}

/* Bison Declarations */
%token
    BANG   "!"
    PLUS   "+"
    MINUS  "-"
    STAR   "*"
    SLASH  "/"
    CARET  "^"
    LPAREN "("
    RPAREN ")"
    EQUAL  "="
    EOL    _("end of line")
  <Integer>
    NUM    _("number")
%type  <Integer> exp

%nonassoc "="       /* comparison            */
%left "-" "+"
%left "*" "/"
%precedence NEG     /* negation--unary minus */
%right "^"          /* exponentiation        */

/* Grammar follows */
%%
input:
  line
| input line
;

line:
  EOL
| exp EOL            { 
      print($exp); 
  }
| error EOL
;

exp:
  NUM                { 
      $$ = $1; }
| exp "=" exp
  {
      if ($1.intValue() != $3.intValue()):
        self.yyerror(@$, "calc: error: " + $1 + " != " + $3);
  }
| exp "+" exp        { 
      $$ = $1 + $3;  }
| exp "-" exp        { 
      $$ = $1 - $3;  }
| exp "*" exp        { 
      $$ = $1 * $3;  }
| exp "/" exp        { 
      $$ = $1 / $3;  }
| "-" exp  %prec NEG { 
      $$ = -$2; }
| exp "^" exp        { 
      $$ = math.pow($1, $3); }
| "(" exp ")"        { 
      $$ = $2; }
| "(" error ")"      { 
      $$ = 1111; }
| "!"                { 
      $$ = 0; return self.YYERROR; }
| "-" error          { 
      $$ = 0; return self.YYERROR; }
;

%%
class CalcLexer (Lexer)  :

  #StreamTokenizer st;
  #PositionReader reader;

  def __init__( self, is):
    self.reader =  PositionReader( InputStreamReader(is));
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
    System.err.print(ctx.getLocation() + ": syntax error");
    #{
    TOKENMAX = 10;
    arg =  [None] * TOKENMAX
    n = ctx.getExpectedTokens(arg, TOKENMAX);
    for  i in range( n):
      System.err.print((i == 0 ? ": expected " : " or ")
                        + arg[i].getName());
  #}
  #{
    lookahead = ctx.getToken();
    if (lookahead != None):
      System.err.print(" before " + lookahead.getName());
  #}
    System.err.println("");
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

#/**
# * A Stream reader that keeps track of the current Position.
# */
class PositionReader ( BufferedReader) {

  private Position position = new Position();
  // Position before the latest call to "read", i.e. position
  // of the last character of the current token.
  private Position previousPosition = new Position();

  public PositionReader(Reader reader) {
    super(reader);
  }

  public int read() throws IOException {
    previousPosition.set(position);
    int res = super.read();
    if (res > -1) {
      char c = (char) res;
      if (c == '\r' || c == '\n') {
        position.line += 1;
        position.column = 1;
      } else {
        position.column += 1;
      }
    }
    return res;
  }

  public Position getPosition() {
    return position;
  }

  public Position getPreviousPosition() {
    return previousPosition;
  }
}


import sys
def main(args):
  scanner = CalcLexer(sys.stdin);
  parser = Calc(scanner);
  for arg in args:
    if (arg =="-p")
      parser.setDebugLevel(1);
  status = 0;
  while(True):
    token = scanner.getToken();
    lval = scanner.getValue();
    yyloc = scanner.getLocation();
    status = parser.push_parse(token, lval, yyloc);
    if(status != Calc.YYPUSH_MORE):
      break      
  if (status != Calc.YYACCEPT)
    sys.exit(1);
  return

if __name__ == "__main__":
    # execute only if run as a script
    import sys
    main(sys.args)
