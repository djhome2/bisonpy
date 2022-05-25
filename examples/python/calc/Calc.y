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
  import sys
  def main(args):
    scanner = CalcLexer(System.in);
    parser = Calc(scanner);
    for arg in args:
      if (arg =="-p")
        parser.setDebugLevel(1);
    status = 0;
    while(true):
      token = scanner.getToken();
      lval = scanner.getValue();
      yyloc = scanner.getLocation();
      status = parser.push_parse(token, lval, yyloc);
      if(status != Calc.YYPUSH_MORE):
        break      
    if (status != Calc.YYACCEPT)
      sys.exit(1);
    return

 
  
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
class CalcLexer implements Calc.Lexer {

  StreamTokenizer st;
  PositionReader reader;

  public CalcLexer(InputStream is) {
    reader = new PositionReader(new InputStreamReader(is));
    st = new StreamTokenizer(reader);
    st.resetSyntax();
    st.eolIsSignificant(true);
    st.wordChars('0', '9');
  }

  Position start = new Position(1, 0);
  Position end = new Position(1, 0);

  /**
   * The location of the last token read.
   * Implemented with getStartPos and getEndPos in pull parsers.
   */
  public Calc.Location getLocation() {
    return new Calc.Location(new Position(start), new Position(end));
  }

  /**
   * Build and emit a syntax error message.
   */
  public void reportSyntaxError(Calc.Context ctx) {
    System.err.print(ctx.getLocation() + ": syntax error");
    {
      final int TOKENMAX = 10;
      Calc.SymbolKind[] arg = new Calc.SymbolKind[TOKENMAX];
      int n = ctx.getExpectedTokens(arg, TOKENMAX);
      for (int i = 0; i < n; ++i)
        System.err.print((i == 0 ? ": expected " : " or ")
                         + arg[i].getName());
    }
    {
      Calc.SymbolKind lookahead = ctx.getToken();
      if (lookahead != null)
        System.err.print(" before " + lookahead.getName());
    }
    System.err.println("");
  }

  /**
   * Emit an error referring to the given location in a user-defined way.
   *
   * @@param loc The location of the element to which the
   *                error message is related.
   * @@param msg The string for the error message.
   */
  public void yyerror(Calc.Location loc, String msg) {
    if (loc == null)
      System.err.println(msg);
    else
      System.err.println(loc + ": " + msg);
  }

  Integer yylval;

  /**
   * The value of the last token read.  Called getLVal in pull parsers.
   */
  public Object getValue() {
    return yylval;
  }

  /**
   * Fetch the next token.  Called yylex in pull parsers.
   */
  public int getToken() throws IOException {
    start.set(reader.getPosition());
    int ttype = st.nextToken();
    end.set(reader.getPosition());
    switch (ttype) {
    case StreamTokenizer.TT_EOF:
      return YYEOF;
    case StreamTokenizer.TT_EOL:
      end.line += 1;
      end.column = 0;
      return EOL;
    case StreamTokenizer.TT_WORD:
      yylval = Integer.parseInt(st.sval);
      end.set(reader.getPreviousPosition());
      return NUM;
    case ' ': case '\t':
      return getToken();
    case '!':
      return BANG;
    case '+':
      return PLUS;
    case '-':
      return MINUS;
    case '*':
      return STAR;
    case '/':
      return SLASH;
    case '^':
      return CARET;
    case '(':
      return LPAREN;
    case ')':
      return RPAREN;
    case '=':
      return EQUAL;
    default:
      throw new AssertionError("invalid character: " + ttype);
    }
  }
}

/**
 * A Stream reader that keeps track of the current Position.
 */
class PositionReader extends BufferedReader {

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
