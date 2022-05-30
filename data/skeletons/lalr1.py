# python skeleton for Bison                           -*- python -*-

# Copyright (C) 2007-2015, 2018-2021 Free Software Foundation, Inc.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

m4_include(b4_skeletonsdir/[python.m4])

b4_header_if([b4_complain([%header/%defines does not make sense in python])])

m4_define([b4_symbol_no_destructor_assert],
[b4_symbol_if([$1], [has_destructor],
              [b4_complain_at(m4_unquote(b4_symbol([$1], [destructor_loc])),
                              [%destructor does not make sense in python])])])
b4_symbol_foreach([b4_symbol_no_destructor_assert])

## --------------- ##
## api.push-pull.  ##
## --------------- ##

b4_percent_define_default([[api.push-pull]], [[pull]])
b4_percent_define_check_values([[[[api.push-pull]],
                                 [[pull]], [[push]], [[both]]]])

# Define m4 conditional macros that encode the value
# of the api.push-pull flag.
b4_define_flag_if([pull]) m4_define([b4_pull_flag], [[1]])
b4_define_flag_if([push]) m4_define([b4_push_flag], [[1]])
m4_case(b4_percent_define_get([[api.push-pull]]),
        [pull], [m4_define([b4_push_flag], [[0]])],
        [push], [m4_define([b4_pull_flag], [[0]])])

# Define a macro to be True when api.push-pull has the value "both".
m4_define([b4_both_if],[b4_push_if([b4_pull_if([$1],[$2])],[$2])])

# Handle BISON_USE_PUSH_FOR_PULL for the test suite.  So that push parsing
# tests function as written, do not let BISON_USE_PUSH_FOR_PULL modify the
# behavior of Bison at all when push parsing is already requested.
b4_define_flag_if([use_push_for_pull])
b4_use_push_for_pull_if([
  b4_push_if([m4_define([b4_use_push_for_pull_flag], [[0]])],
             [m4_define([b4_push_flag], [[1]])])])

# Define a macro to encapsulate the parse state variables.  This
# allows them to be defined either in parse() when doing pull parsing,
# or as class instance variable when doing push parsing.
m4_define([b4_define_state],
[[
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

]b4_locations_if([[
  # /* The location where the error started.  */
  yyerrloc = None

  # /* Location. */
  yylloc = ]b4_location_type[ (None, None)]])[

  # /* Semantic value of the lookahead.  */
  yylval = None
]])

# parse.lac
b4_percent_define_default([[parse.lac]], [[none]])
b4_percent_define_check_values([[[[parse.lac]], [[full]], [[none]]]])
b4_define_flag_if([lac])
m4_define([b4_lac_flag],
          [m4_if(b4_percent_define_get([[parse.lac]]),
                 [none], [[0]], [[1]])])


## ------------- ##
## Parser File.  ##
## ------------- ##

b4_output_begin([b4_parser_file_name])[
]b4_copyright([Skeleton implementation for Bison LALR(1) parsers in python],
              [2007-2015, 2018-2021])[
]b4_disclaimer[
]b4_percent_define_ifdef([api.package], [package b4_percent_define_get([api.package]);[
]])[
]b4_user_pre_prologue[
]b4_user_post_prologue[
# import java.text.MessageFormat;
# import java.util.ArrayList;
from abc import ABCMeta,abstractmethod
import sys
from enum import Enum
]b4_percent_code_get([[imports]])[
# 
#  A Bison parser, automatically generated from <tt>]m4_bpatsubst(b4_file_name, [^"\(.*\)"$], [\1])[</tt>.
# 
#  @@author LALR (1) parser skeleton written by Paolo Bonzini.
#  



]b4_locations_if([[
  # /**
  #  * A class defining a pair of positions.  Positions, defined by the
  #  * <code>]b4_position_type[</code> class, denote a point in the input.
  #  * Locations represent a part of the input through the beginning
  #  * and ending positions.
  #  */
class ]b4_location_type[():
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
  # public ]b4_position_type[ begin;

  # /**
  #  * The first position beyond the range.
  #  */
  # public ]b4_position_type[ end;

  # /**
  #  * Create a <code>]b4_location_type[</code> denoting an empty range located at
  #  * a given point.
  #  * @@param loc The position at which the range is anchored.
  #  */
  # public ]b4_location_type[ (]b4_position_type[ loc) {
    # this.begin = this.end = loc;
  # }

  # /**
  #  * Create a <code>]b4_location_type[</code> from the endpoints of the range.
  #  * @@param begin The first position included in the range.
  #  * @@param end   The first position beyond the range.
  #  */
  # public ]b4_location_type[ (]b4_position_type[ begin, ]b4_position_type[ end) {
    # this.begin = begin;
    # this.end = end;
  # }

  # /**
  #  * Print a representation of the location.  For this to be correct,
  #  * <code>]b4_position_type[</code> should override the <code>equals</code>
  #  * method.
  #  */
  def __str__(self):
    if (self.begin == self.end):
      return str(self.begin)
    else:
      return str(self.begin) + "-" + str(self.end)
  # }
# }



]b4_declare_symbol_enum[




# /**
#  * Communication interface between the scanner and the Bison-generated
#  * parser <tt>]b4_parser_class[</tt>.
#  */
class Lexer():
]b4_token_enums[
  # /** Deprecated, use ]b4_symbol(eof, id)[ instead.  */
  EOF = ]b4_symbol(eof, id)[
]b4_pull_if([b4_locations_if([[
  # /**
  #  * Method to retrieve the beginning position of the last scanned token.
  #  * @@return the position at which the last scanned token starts.
  #  */
  @abstractmethod
  def getStartPos(): pass 

  # /**
  #  * Method to retrieve the ending position of the last scanned token.
  #  * @@return the first position beyond the last scanned token.
  #  */
  @abstractmethod
  def getEndPos(): pass]])[

  # /**
  #  * Method to retrieve the semantic value of the last scanned token.
  #  * @@return the semantic value of the last scanned token.
  #  */
  @abstractmethod
  def getLVal(): pass

  # /**
  #  * Entry point for the scanner.  Returns the token identifier corresponding
  #  * to the next token and prepares to return the semantic value
  #  * ]b4_locations_if([and beginning/ending positions ])[of the token.
  #  * @@return the token identifier corresponding to the next token.
  #  */
  @abstractmethod
  def yylex(): pass]b4_maybe_throws([b4_lex_throws])[;
]])[
  # /**
  #  * Emit an error]b4_locations_if([ referring to the given location])[in a user-defined way.
  #  *
  #  *]b4_locations_if([[ @@param loc The location of the element to which the
  #  *                error message is related.]])[
  #  * @@param msg The string for the error message.
  #  */
  def yyerror(]b4_locations_if([loc, ])[msg): pass

]b4_parse_error_bmatch(
           [custom], [[
  # /**
  #  * Build and emit a "syntax error" message in a user-defined way.
  #  *
  #  * @@param ctx  The context of the error.
  #  */
  def reportSyntaxError(ctx): pass
]])[
  # }

YYLAST_ = ]b4_last[
YYEMPTY_ = -2
YYFINAL_ = ]b4_final_state_number[
YYNTOKENS_ = ]b4_tokens_number[



def yylloc(rhs, n):
  if (0 < n):
    return ]b4_location_type[(rhs.locationAt(n-1).begin, rhs.locationAt(0).end)
  else:
    return ]b4_location_type[(rhs.locationAt(0).end)
]])[



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

]b4_push_if([
# /**
#  * Returned by a Bison action in order to request a new token.
#  */
YYPUSH_MORE = 4
])[

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
]b4_push_if([[  
YYGETTOKEN = 9# /* Signify that a new token is expected when doing push-parsing.  */
]])[



]b4_parser_class_declaration[():
# {
]b4_identification[
][
]b4_parse_error_bmatch(
           [detailed\|verbose], [[
  # /**
  #  * True if verbose error messages are enabled.
  #  */
  yyErrorVerbose = True

  # /**
  #  * Whether verbose error messages are enabled.
  #  */
  def getErrorVerbose():
    return yyErrorVerbose;

  # /**
  #  * Set the verbosity of error messages.
  #  * @@param verbose True to request verbose error messages.
  #  */
  def setErrorVerbose(verbose):
    yyErrorVerbose = verbose
    return
]])[




]b4_lexer_if([[
  class YYLexer(Lexer):
]b4_percent_code_get([[lexer]])[
  # }

]])[
  # /**
  #  * The object doing lexical analysis for us.
  #  */
  # yylexer = None

]b4_parse_param_vars[

]b4_lexer_if([[
  # /**
  #  * Instantiates the Bison-generated parser.
  #  */
  ]b4_parser_class[(]b4_parse_param_decl([b4_lex_param_decl])[)]b4_maybe_throws([b4_init_throws])[
  {
]b4_percent_code_get([[init]])[]b4_lac_if([[
    this.yylacStack = new ArrayList<Integer>();
    this.yylacEstablished = False;]])[
    this.yylexer = new YYLexer(]b4_lex_param_call[);
]b4_parse_param_cons[
  }
]])[

  # /**
  #  * Instantiates the Bison-generated parser.
  #  * @@param yylexer The scanner that will supply tokens to the parser.
  #  */
  ]b4_lexer_if([[protected]], [[]])def __init__[(]b4_parse_param_decl([[self, yylexer]])[):]b4_maybe_throws([b4_init_throws])[
  # {
]b4_percent_code_get([[init]])[]b4_lac_if([[
    self.yylacStack = []
    self.yylacEstablished = False]])[
    self.yylexer = yylexer
    return
]b4_parse_param_cons[
  # }

]b4_parse_trace_if([[
  yyDebugStream = sys.stderr

  # /**
  #  * The <tt>PrintStream</tt> on which the debugging output is printed.
  #  */
  def getDebugStream(self):
    return self.yyDebugStream

  # /**
  #  * Set the <tt>PrintStream</tt> on which the debug output is printed.
  #  * @@param s The stream that is used for debugging output.
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
  #  * @@param level The verbosity level for debugging output.
  #  */
  def setDebugLevel(self, level):
    self.yydebug = level
    return
]])[

  yynerrs = 0;

  # /**
  #  * The number of syntax errors so far.
  #  */
  def getNumberOfErrors(self):
    return self.yynerrs

  # /**
  #  * Print an error message via the lexer.
  #  *]b4_locations_if([[ Use a <code>None</code> location.]])[
  #  * @@param msg The error message.
  #  */
  def yyerror(self, *args):
    if(len(args) == 1):
      loc = None
      msg = args[0]
    else:
      loc = args[0]
      msg = args[1]
      if(isinstance(loc, ]b4_position_type[)):
        loc = ]b4_location_type[ (loc)
      else:
        assert(isinstance(loc, ]b4_location_type[))
    self.yylexer.yyerror(loc, msg)
    return
  
]b4_locations_if([[
  # /**
  #  * Print an error message via the lexer.
  #  * @@param loc The location associated with the message.
  #  * @@param msg The error message.
  #  */
  # def yyerror(]b4_location_type[ loc, String msg) {
  #     yylexer.yyerror(loc, msg);
  # }

  # /**
  #  * Print an error message via the lexer.
  #  * @@param pos The position associated with the message.
  #  * @@param msg The error message.
  #  */
  # public final void yyerror(]b4_position_type[ pos, String msg) {
  #     yylexer.yyerror(new ]b4_location_type[ (pos), msg);
  # }]])[
]b4_parse_trace_if([[
  def yycdebugNnl(self, s):
    if (0 < self.yydebug):
      print(s, file = self.yyDebugStream)
  

  def yycdebug(self, s):
    if (0 < self.yydebug):
      print(s, file = self.yyDebugStream)
  ]])[

  class YYStack():
    # private int[] stateStack = new int[16];]b4_locations_if([[
    stateStack = []
    # private ]b4_location_type[[] locStack = new ]b4_location_type[[16];]])[
    locStack = []
    # private ]b4_yystype[[] valueStack = new ]b4_yystype[[16];
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
      #   stateStack = newStateStack;]b4_locations_if([[
      #   ]b4_location_type[[] newLocStack = new ]b4_location_type[[size * 2];
      #   System.arraycopy(locStack, 0, newLocStack, 0, height);
      #   locStack = newLocStack;]])

      #   b4_yystype[[] newValueStack = new ]b4_yystype[[size * 2];
      #   System.arraycopy(valueStack, 0, newValueStack, 0, height);
      #   valueStack = newValueStack;

      #   size *= 2;
      # }

      # stateStack[height] = state;]b4_locations_if([[
      # locStack[height] = loc;]])[
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
      #   java.util.Arrays.fill(valueStack, height - num + 1, height + 1, None);]b4_locations_if([[
      #   java.util.Arrays.fill(locStack, height - num + 1, height + 1, None);]])[
      # }
      self.height -= num
    

    def stateAt(self, i):
      return self.stateStack[self.height - i]
    
]b4_locations_if([[

    def locationAt(self, i):
      return self.locStack[self.height - i]
    
]])[
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

]b4_push_if([b4_define_state])[
  # /**
  #  * Whether error recovery is being done.  In this state, the parser
  #  * reads token until it reaches a known state, and then restarts normal
  #  * operation.
  #  */
  def recovering (self):
  
    return self.yyerrstatus_ == 0
  

  # /** Compute post-reduction state.
  #  * @@param yystate   the current state
  #  * @@param yysym     the nonterminal to push on the stack
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
    ]b4_parse_trace_if([[

    self.yyReducePrint(yyn, yystack)]])[

    # switch (yyn)
      # {
    ]b4_user_actions[
        # default: break;
    ]b4_parse_trace_if([[

    self.yySymbolPrint("-> $$ =", SymbolKind.get(self.yyr1_[yyn]), yyval]b4_locations_if([, yyloc])[);]])[

    yystack.pop(yylen);
    yylen = 0;
    # /* Shift the result of the reduction.  */
    yystate = self.yyLRGotoState(yystack.stateAt(0), self.yyr1_[yyn]);
    yystack.push(yystate, yyval]b4_locations_if([, yyloc])[);
    return self.YYNEWSTATE;
  

]b4_parse_trace_if([[
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
                   + yykind.getName() + " ("]b4_locations_if([
                   + yylocation + ": "])[
                   + s_yyvalue + ")")
      
  ]])[

]b4_push_if([],[[
  # /**
  #  * Parse input from the scanner that was specified at object construction
  #  * time.  Return whether the end of the input was reached successfully.
  #  *
  #  * @@return <tt>True</tt> if the parsing succeeds.  Note that this does not
  #  *          imply that there were no syntax errors.
  #  */
  def parse()]b4_maybe_throws([b4_list2([b4_lex_throws], [b4_throws])])[]])[
]b4_push_if([
  # /**
  #  * Push Parse input from external lexer
  #  *
  #  * @@param yylextoken current token
  #  * @@param yylexval current lval]b4_locations_if([[
  #  * @@param yylexloc current position]])[
  #  *
  #  * @@return <tt>YYACCEPT, YYABORT, YYPUSH_MORE</tt>
  #  */
  def push_parse(self, yylextoken, yylexval[]b4_locations_if([, yylexloc]))])[:
  ]b4_locations_if([[
    # /* @@$.  */
    yyloc = None
    if(yylexloc != None and isinstance(yylexloc, Position)):
      yylexloc = Location(yylexloc)
]])[
]b4_push_if([],[[
]b4_define_state[
]b4_lac_if([[
    # // Discard the LAC context in case there still is one left from a
    # // previous invocation.
    yylacDiscard("init");]])[
]b4_parse_trace_if([[
    yycdebug ("Starting parse");]])[
    yyerrstatus_ = 0;
    yynerrs = 0;

    /* Initialize the stack.  */
    yystack.push (yystate, yylval]b4_locations_if([, yylloc])[);
]m4_ifdef([b4_initial_action], [
b4_dollar_pushdef([yylval], [], [], [yylloc])dnl
    b4_user_initial_action
b4_dollar_popdef[]dnl
])[
]])[
]b4_push_if([[
    if (not self.push_parse_initialized):
      # {
        self.push_parse_initialize ();
]m4_ifdef([b4_initial_action], [
b4_dollar_pushdef([yylval], [], [], [yylloc])dnl
    b4_user_initial_action
b4_dollar_popdef[]dnl
])[]b4_parse_trace_if([[
        self.yycdebug ("Starting parse");]])[
        self.yyerrstatus_ = 0;
    else:
        label = self.YYGETTOKEN;

    push_token_consumed = True
]])[
    while (True):
      # switch (label)
      # {
        # /* New state.  Unlike in the C/C++ skeletons, the state is already
        #    pushed when we come here.  */
      if(label == self.YYNEWSTATE):]b4_parse_trace_if([[
        self.yycdebug ("Entering state " + self.yystate);
        if (0 < self.yydebug):
          self.yystack.print (self.yyDebugStream);]])[

        # /* Accept?  */
        if (self.yystate == self.YYFINAL_):
          ]b4_push_if([
          label = self.YYACCEPT
          continue],
                      [return True;])[

        # /* Take a decision.  First try without lookahead.  */
        yyn = self.yypact_[self.yystate]
        if (self.yyPactValueIsDefault (yyn)):
          # {
          label = self.YYDEFAULT
          continue
          # }
]b4_push_if([        
  # /* Fall Through */

      if(label == self.YYGETTOKEN):])[
        # /* Read a lookahead token.  */
        if (self.yychar == YYEMPTY_):
          # {
]b4_push_if([[
            if (not push_token_consumed):
              return self.YYPUSH_MORE]b4_parse_trace_if([[
            self.yycdebug ("Reading a token");]])[
            self.yychar = yylextoken
            self.yylval = yylexval]b4_locations_if([
            self.yylloc = yylexloc])[
            push_token_consumed = False]], [b4_parse_trace_if([[
            self.yycdebug ("Reading a token");]])[
            self.yychar = yylexer.yylex ();
            self.yylval = yylexer.getLVal();]b4_locations_if([[
            self.yylloc = new ]b4_location_type[(yylexer.getStartPos(),
                                          yylexer.getEndPos());]])[
]])[
          # }

        # /* Convert token to internal form.  */
        self.yytoken = self.yytranslate_ (self.yychar)]b4_parse_trace_if([[
        self.yySymbolPrint("Next token is", self.yytoken,
                      self.yylval]b4_locations_if([, self.yylloc])[);]])[

        if (self.yytoken == ]b4_symbol(error, kind)[):
          # {
            # // The scanner already issued an error message, process directly
            # // to error recovery.  But do not keep the error token as
            # // lookahead, it is too special and may lead us to an endless
            # // loop in error recovery. */
            self.yychar = Lexer.]b4_symbol(undef, id)[;
            self.yytoken = ]b4_symbol(undef, kind)[;]b4_locations_if([[
            self.yyerrloc = yylloc;]])[
            label = self.YYERRLAB1;
          # }
        else:
          # {
            # /* If the proper action on seeing token YYTOKEN is to reduce or to
            #    detect an error, take that action.  */
            yyn += self.yytoken.getCode();
            if (yyn < 0 or YYLAST_ < yyn or self.yycheck_[yyn] != self.yytoken.getCode()) ]b4_lac_if([[:
              if (not self.yylacEstablish(self.yystack, self.yytoken)) :
                label = self.YYERRLAB
              else]])[:
                label = self.YYDEFAULT
              continue
            # }

            # /* <= 0 means reduce or error.  */
            yyn = self.yytable_[yyn]
            if(yyn <= 0):
              # {
                if (self.yyTableValueIsError(yyn)) :
                  label = self.YYERRLAB;
                ]b4_lac_if([[elif (not self.yylacEstablish(self.yystack, self.yytoken)) :
                  label = self.YYERRLAB;
                ]])[else:
                  yyn = -yyn;
                  label = self.YYREDUCE;
                # }
              # }

            else:
              # {
                # /* Shift the lookahead token.  */]b4_parse_trace_if([[
                self.yySymbolPrint("Shifting", self.yytoken,
                              self.yylval]b4_locations_if([, self.yylloc])[);
]])[
                # /* Discard the token being shifted.  */
                self.yychar = YYEMPTY_;

                # /* Count tokens shifted since error; after three, turn off error
                #    status.  */
                if (self.yyerrstatus_ > 0):
                  self.yyerrstatus_ -= 1

                self.yystate = yyn;
                self.yystack.push(self.yystate, self.yylval]b4_locations_if([, self.yylloc])[);]b4_lac_if([[
                self.yylacDiscard("shift");]])[
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
            self.yyreportSyntaxError(self.Context(self, self.yystack, self.yytoken]b4_locations_if([[, self.yylloc]])[));
          # }
]b4_locations_if([[
        yyerrloc = yylloc;]])[
        if (yyerrstatus_ == 3):
          # {
            # /* If just tried and failed to reuse lookahead token after an
            #    error, discard it.  */

            if (yychar <= Lexer.]b4_symbol(eof, id)[):
              # {
                # /* Return failure if at end of input.  */
                if (yychar == Lexer.]b4_symbol(eof, id)[):
                  ]b4_push_if([label = self.YYABORT; continue;], [return False;])[
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
      if(label == self.YYERROR):]b4_locations_if([[
        yyerrloc = self.yystack.locationAt (yylen - 1);]])[
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
                yyn += ]b4_symbol(error, kind)[.getCode();
                if (0 <= yyn and yyn <= YYLAST_
                    and self.yycheck_[yyn] == ]b4_symbol(error, kind)[.getCode()):
                  # {
                    yyn = self.yytable_[yyn];
                    if (0 < yyn):
                      break;
                  # }
              # }

            # /* Pop the current state because it cannot handle the
            #  * error token.  */
            if (self.yystack.height == 0):
              ]b4_push_if([label = self.YYABORT; break;],[return False;])[

]b4_locations_if([[
            yyerrloc = self.yystack.locationAt (0);]])[
            self.yystack.pop ();
            yystate = self.yystack.stateAt(0);]b4_parse_trace_if([[
            if (0 < self.yydebug):
              self.yystack.print (self.yyDebugStream);]])[
          # }

        if (label == self.YYABORT):
          # /* Leave the switch.  */
          continue;

]b4_locations_if([[
        # /* Muck with the stack to setup for yylloc.  */
        self.yystack.push (0, None, yylloc);
        self.yystack.push (0, None, yyerrloc);
        yyloc = yylloc (self.yystack, 2);
        self.yystack.pop (2);]])[

        # /* Shift the error token.  */]b4_lac_if([[
        self.yylacDiscard("error recovery");]])[]b4_parse_trace_if([[
        self.yySymbolPrint("Shifting", SymbolKind.get(self.yystos_[yyn]),
                      self.yylval]b4_locations_if([, yyloc])[);]])[

        self.yystate = yyn;
        self.yystack.push (yyn, self.yylval]b4_locations_if([, yyloc])[);
        label = self.YYNEWSTATE;
        continue;

        # /* Accept.  */
      if(label == self.YYACCEPT):
        ]b4_push_if([self.push_parse_initialized = False; return self.YYACCEPT;],
                    [return True;])[

        # /* Abort.  */
      if(label == self.YYABORT):
        ]b4_push_if([self.push_parse_initialized = False; return self.YYABORT;],
                    [return False;])[
      # }
# }
]b4_push_if([[
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
    self.yystack = self.YYStack()]b4_lac_if([[
    self.yylacStack = []
    self.yylacEstablished = False;]])[
    self.label = self.YYNEWSTATE

    # /* Error handling.  */
    self.yynerrs = 0]b4_locations_if([[
    # /* The location where the error started.  */
    self.yyerrloc = None
    self.yylloc = ]b4_location_type[ (None, None)]])[

    # /* Semantic value of the lookahead.  */
    self.yylval = None;

    self.yystack.push (self.yystate, self.yylval]b4_locations_if([, self.yylloc])[)

    self.push_parse_initialized = True

  # }
]b4_locations_if([[
  # /**
  #  * Push parse given input from an external lexer.
  #  *
  #  * @@param yylextoken current token
  #  * @@param yylexval current lval
  #  * @@param yyylexpos current position
  #  *
  #  * @@return <tt>YYACCEPT, YYABORT, YYPUSH_MORE</tt>
  #  */
  # def push_parse(int yylextoken, ]b4_yystype[ yylexval, ]b4_position_type[ yylexpos)]b4_maybe_throws([b4_list2([b4_lex_throws], [b4_throws])])[ :
  #     return push_parse(yylextoken, yylexval, new ]b4_location_type[(yylexpos));
  # }
]])])[

]b4_both_if([[
  # /**
  #  * Parse input from the scanner that was specified at object construction
  #  * time.  Return whether the end of the input was reached successfully.
  #  * This version of parse() is defined only when api.push-push=both.
  #  *
  #  * @@return <tt>True</tt> if the parsing succeeds.  Note that this does not
  #  *          imply that there were no syntax errors.
  #  */
  def parse()]b4_maybe_throws([b4_list2([b4_lex_throws], [b4_throws])])[ :
      if (yylexer == None)
          throw new NullPointerException("Null Lexer");
      int status;
      do {
          int token = yylexer.yylex();
          ]b4_yystype[ lval = yylexer.getLVal();]b4_locations_if([[
          ]b4_location_type[ yyloc = new ]b4_location_type[(yylexer.getStartPos(), yylexer.getEndPos());
          status = push_parse(token, lval, yyloc);]], [[
          status = push_parse(token, lval);]])[
      } while (status == YYPUSH_MORE);
      return status == YYACCEPT;
  # }
]])[

  # /**
  #  * Information needed to get the list of expected tokens and to forge
  #  * a syntax error diagnostic.
  #  */
  class Context():
    def __init__(self, parser, stack, token]b4_locations_if([[, loc]])[):
      self.yyparser = parser
      self.yystack = stack
      self.yytoken = token]b4_locations_if([[
      self.yylocation = loc]])[
      self.yylacStack = []
      self.yylacEstablished = False
    # }

    # private ]b4_parser_class[ yyparser;
    # private YYStack yystack;


    # /**
    #  * The symbol kind of the lookahead token.
    #  */
    def getToken(self):
      return self.yytoken;
    # }

    # private SymbolKind yytoken;]b4_locations_if([[

    # /**
    #  * The location of the lookahead.
    #  */
    def getLocation(self):
      return self.yylocation;
    # }

    # private ]b4_location_type[ yylocation;]])[
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
      yycount = yyoffset;]b4_lac_if([b4_parse_trace_if([[
      # // Execute LAC once. We don't care if it is successful, we
      # // only do it for the sake of debugging output.
      if (not self.yyparser.yylacEstablished):
        self.yyparser.yylacCheck(self.yystack, self.yytoken)
]])[
      for yyx in range(YYNTOKENS_):
        # {
        yysym = SymbolKind.get(yyx);
        if (yysym != ]b4_symbol(error, kind)[
            and yysym != ]b4_symbol(undef, kind)[
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
        ]], [[
      yyn = yypact_[this.yystack.stateAt(0)];
      if (not yyPactValueIsDefault(yyn)):
        # {
          # /* Start YYX at -YYN if negative to avoid negative
          #    indexes in YYCHECK.  In other words, skip the first
          #    -YYN actions for this state because they are default
          #    actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST_ - yyn + 1;
          int yyxend = yychecklim < NTOKENS ? yychecklim : NTOKENS;
          for (int yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck_[yyx + yyn] == yyx && yyx != ]b4_symbol(error, kind)[.getCode()
                && !yyTableValueIsError(yytable_[yyx + yyn])):
              # {
                if (yyarg == None):
                  yycount += 1
                elif (yycount == yyargn):
                  return 0#; // FIXME: this is incorrect.
                else:
                  yyarg[yycount] = SymbolKind.get(yyx)
                  yycount += 1
              # }
        ]])[
      if (yyarg != None and yycount == yyoffset and yyoffset < yyargn):
        yyarg[yycount] = None
      return yycount - yyoffset
    # }
  # }

]b4_lac_if([[
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
      ]b4_parser_class[.yycdebugNnl("LAC: checking lookahead " + yytoken.getName() + ":")
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
        yyrule = ]b4_parser_class[.yypact_[topState];
        check = ]b4_parser_class[.yyPactValueIsDefault(yyrule)
        if (not check):
          yyrule += yytoken.getCode()
          check = yyrule < 0 or YYLAST_ < yyrule or yycheck_[yyrule] != yytoken.getCode()
        if (check):
          # {
            # // Use the default action.
            yyrule = yydefact_[+topState];
            if (yyrule == 0) :
              ]b4_parser_class[.yycdebug(" Err");
              return False;
            # }
          # }
        else:
          # {
            # // Use the action from yytable.
            yyrule = yytable_[yyrule];
            if (]b4_parser_class[.yyTableValueIsError(yyrule)) :
              ]b4_parser_class[.yycdebug(" Err");
              return False;
            # }
            if (0 < yyrule) :
              ]b4_parser_class[.yycdebug(" S" + yyrule);
              return True;
            # }
            yyrule = -yyrule;
          # }
        # // By now we know we have to simulate a reduce.
        ]b4_parser_class[.yycdebugNnl(" R" + (yyrule - 1));
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
        state = ]b4_parser_class[.yyLRGotoState(topState, yyr1_[yyrule]);
        ]b4_parser_class[.yycdebugNnl(" G" + state);
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
]])[

]b4_parse_error_bmatch(
[detailed\|verbose], [[
  def yysyntaxErrorArguments(self,  yyctx,  yyarg,  yyargn) :
    # /* There are many possibilities here to consider:
    #    - If this state is a consistent state with a default action,
    #      then the only way this function was invoked is if the
    #      default action is an error action.  In that case, don't
    #      check for expected tokens because there are none.
    #    - The only way there can be no lookahead present (in tok) is
    #      if this state is a consistent state with a default action.
    #      Thus, detecting the absence of a lookahead is sufficient to
    #      determine that there is no unexpected or expected token to
    #      report.  In that case, just report a simple "syntax error".
    #    - Don't assume there isn't a lookahead just because this
    #      state is a consistent state with a default action.  There
    #      might have been a previous inconsistent state, consistent
    #      state with a non-default action, or user semantic action
    #      that manipulated yychar.  (However, yychar is currently out
    #      of scope during semantic actions.)
    #    - Of course, the expected token list depends on states to
    #      have correct lookahead information, and it depends on the
    #      parser not to perform extra reductions after fetching a
    #      lookahead from the scanner and before detecting a syntax
    #      error.  Thus, state merging (from LALR or IELR) and default
    #      reductions corrupt the expected token list.  However, the
    #      list is correct for canonical LR with one exception: it
    #      will still contain any token that will not be accepted due
    #      to an error action in a later state.
    # */
    yycount = 0;
    if (yyctx.getToken() != None):
      # {
      if (yyarg != None):
        yyarg[yycount] = yyctx.getToken();
      yycount += 1;
      yycount += yyctx.getExpectedTokens(yyarg, 1, yyargn);
      # }
    return yycount;
  # }
]])[

  # /**
  #  * Build and emit a "syntax error" message in a user-defined way.
  #  *
  #  * @@param ctx  The context of the error.
  #  */
  def  yyreportSyntaxError(self,  yyctx) :]b4_parse_error_bmatch(
[custom], [[
      self.yylexer.reportSyntaxError(yyctx);]],
[detailed\|verbose], [[
      if (yyErrorVerbose) :
          argmax = 5
          yyarg = [None] * argmax
          yycount = yysyntaxErrorArguments(yyctx, yyarg, argmax);
          yystr = [None] * yycount
          for yyi in range(yycount):
              yystr[yyi] = yyarg[yyi].getName()
          # }
          String yyformat;
          switch (yycount) {
              default:
              case 0: yyformat = ]b4_trans(["syntax error"])[; break;
              case 1: yyformat = ]b4_trans(["syntax error, unexpected {0}"])[; break;
              case 2: yyformat = ]b4_trans(["syntax error, unexpected {0}, expecting {1}"])[; break;
              case 3: yyformat = ]b4_trans(["syntax error, unexpected {0}, expecting {1} or {2}"])[; break;
              case 4: yyformat = ]b4_trans(["syntax error, unexpected {0}, expecting {1} or {2} or {3}"])[; break;
              case 5: yyformat = ]b4_trans(["syntax error, unexpected {0}, expecting {1} or {2} or {3} or {4}"])[; break;
          }
          yyerror(]b4_locations_if([[yyctx.yylocation, ]])[new MessageFormat(yyformat).format(yystr));
      } else {
          yyerror(]b4_locations_if([[yyctx.yylocation, ]])[]b4_trans(["syntax error"])[);
      }]],
[simple], [[
      yyerror(]b4_locations_if([[yyctx.yylocation, ]])[]b4_trans(["syntax error"])[);]])[
  # }

  # /**
  #  * Whether the given <code>yypact_</code> value indicates a defaulted state.
  #  * @@param yyvalue   the value to check
  #  */
  def  yyPactValueIsDefault(self, yyvalue) :
    return yyvalue == self.yypact_ninf_;
  # }

  # /**
  #  * Whether the given <code>yytable_</code>
  #  * value indicates a syntax error.
  #  * @@param yyvalue the value to check
  #  */
  def  yyTableValueIsError(self,  yyvalue):
    return yyvalue == self.yytable_ninf_;
  # }

  yypact_ninf_ = ]b4_pact_ninf[;
  yytable_ninf_ = ]b4_table_ninf[;

]b4_parser_tables_define[

]b4_parse_trace_if([[
  ]b4_integral_parser_table_define([rline], [b4_rline],
  [[YYRLINE[YYN] -- Source line where rule number YYN was defined.]])[


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
                    ]b4_rhs_data(yynrhs, yyi + 1)b4_locations_if([,
                    b4_rhs_location(yynrhs, yyi + 1)])[);
  ]])[

  # /* YYTRANSLATE_(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
  #    as returned by yylex, with out-of-bounds checking.  */
  def yytranslate_(self, t):
]b4_api_token_raw_if(dnl
[[  
    return SymbolKind.get(t);
  
]],
[[  
    # // Last valid token kind.
    code_max = ]b4_code_max[;
    if (t <= 0):
      return ]b4_symbol(eof, kind)[;
    elif (t <= code_max):
      return SymbolKind.get(yytranslate_table_[t]);
    else:
      return ]b4_symbol(undef, kind)[;
  # }
  ]b4_integral_parser_table_define([translate_table], [b4_translate])[
]])[



]b4_percent_code_get[
# }
]b4_percent_code_get([[epilogue]])[]dnl
b4_epilogue[]dnl
b4_output_end
