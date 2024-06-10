
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLOGICAL_OP_ORleftLOGICAL_OP_ANDrightLOGICAL_OP_NOTleftLESS_OPLESS_EQUAL_OPGREATER_OPGREATER_EQUAL_OPEQUAL_OPDIFFERENT_OPleftPLUS_OPMINUS_OPleftMUL_OPDIV_OPnonassocLPARENRPARENASSIGNMENT_OP BREAK COMMENT CONDITIONAL1 CONDITIONAL2 DIFFERENT_OP DIV_OP END_LINE EQUAL_OP FALSE FUNCTION_DECLARATION GREATER_EQUAL_OP GREATER_OP LESS_EQUAL_OP LESS_OP LOGICAL_OP_AND LOGICAL_OP_NOT LOGICAL_OP_OR LOOP1 LOOP2 LPAREN MINUS_OP MUL_OP NULL NUMBER_FLOAT NUMBER_INTEGER PLUS_OP RETURN RPAREN SEPARATION STRUCTURE_BODY TEXT_CHAR TEXT_STRING TRUE TYPE_BOOLEAN TYPE_CHAR TYPE_FLOAT TYPE_INTEGER TYPE_STRING VARIABLEprogram : statement_liststatement_list : statement_list statement\n                      | statementstatement : expression END_LINE\n                 | assignment END_LINE\n                 | declaration END_LINE\n                 | conditional END_LINE\n                 | loop END_LINE\n                 | return_statement END_LINE\n                 | break_statement END_LINE\n                 | comment\n                 expression : binary_expression\n                  | unitary_expression\n                  | primary_expressionbinary_expression : primary_expression PLUS_OP primary_expression\n                         | primary_expression MINUS_OP primary_expression\n                         | primary_expression MUL_OP primary_expression\n                         | primary_expression DIV_OP primary_expression\n                         | primary_expression LESS_OP primary_expression\n                         | primary_expression GREATER_OP primary_expression\n                         | primary_expression LESS_EQUAL_OP primary_expression\n                         | primary_expression GREATER_EQUAL_OP primary_expression\n                         | primary_expression EQUAL_OP primary_expression\n                         | primary_expression DIFFERENT_OP primary_expressionunitary_expression : MINUS_OP primary_expression\n                          | LOGICAL_OP_NOT primary_expressionprimary_expression : LPAREN expression RPAREN\n                          | termterm : NUMBER_INTEGER\n            | NUMBER_FLOAT\n            | VARIABLE\n            | TRUE\n            | FALSE\n            | NULL\n            | TEXT_STRING\n            | TEXT_CHARassignment : VARIABLE ASSIGNMENT_OP expressiondeclaration : TYPE_BOOLEAN VARIABLE \n                   | TYPE_STRING VARIABLE\n                   | TYPE_CHAR VARIABLE\n                   | TYPE_INTEGER VARIABLE\n                   | TYPE_FLOAT VARIABLE\n                   | TYPE_BOOLEAN assignment\n                   | TYPE_STRING assignment\n                   | TYPE_CHAR assignment\n                   | TYPE_INTEGER assignment\n                   | TYPE_FLOAT assignmentconditional : CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list \n                   | CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_listloop : LOOP1 LPAREN expression RPAREN STRUCTURE_BODY statement_list \n            | LOOP2 LPAREN assignment SEPARATION expression SEPARATION assignment RPAREN STRUCTURE_BODY statement_listreturn_statement : RETURN expression\n                        | RETURNbreak_statement : BREAKcomment : COMMENT'
    
_lr_action_items = {'VARIABLE':([0,2,3,11,16,17,18,19,20,22,25,27,28,29,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,70,71,93,94,95,97,98,99,102,104,105,106,],[15,15,-3,-11,57,59,61,63,65,69,69,-55,69,69,-2,-4,-5,-6,-7,-8,-9,-10,69,69,69,69,69,69,69,69,69,69,69,69,69,90,69,15,15,15,15,90,15,15,15,15,]),'TYPE_BOOLEAN':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[16,16,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,16,16,16,16,16,16,16,16,]),'TYPE_STRING':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[17,17,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,17,17,17,17,17,17,17,17,]),'TYPE_CHAR':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[18,18,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,18,18,18,18,18,18,18,18,]),'TYPE_INTEGER':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[19,19,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,19,19,19,19,19,19,19,19,]),'TYPE_FLOAT':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[20,20,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,20,20,20,20,20,20,20,20,]),'CONDITIONAL1':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[21,21,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,21,21,21,21,21,21,21,21,]),'LOOP1':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[23,23,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,23,23,23,23,23,23,23,23,]),'LOOP2':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[24,24,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,24,24,24,24,24,24,24,24,]),'RETURN':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[25,25,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,25,25,25,25,25,25,25,25,]),'BREAK':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[26,26,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,26,26,26,26,26,26,26,26,]),'COMMENT':([0,2,3,11,27,38,39,40,41,42,43,44,45,94,95,97,98,102,104,105,106,],[27,27,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,27,27,27,27,27,27,27,27,]),'MINUS_OP':([0,2,3,11,14,15,22,25,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,56,67,69,70,87,93,94,95,97,98,102,104,105,106,],[28,28,-3,-11,47,-31,28,28,-55,-28,-29,-30,-32,-33,-34,-35,-36,-2,-4,-5,-6,-7,-8,-9,-10,28,28,-31,28,-27,28,28,28,28,28,28,28,28,28,]),'LOGICAL_OP_NOT':([0,2,3,11,22,25,27,38,39,40,41,42,43,44,45,56,67,70,93,94,95,97,98,102,104,105,106,],[29,29,-3,-11,29,29,-55,-2,-4,-5,-6,-7,-8,-9,-10,29,29,29,29,29,29,29,29,29,29,29,29,]),'LPAREN':([0,2,3,11,21,22,23,24,25,27,28,29,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[22,22,-3,-11,67,22,70,71,22,-55,22,22,-2,-4,-5,-6,-7,-8,-9,-10,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'NUMBER_INTEGER':([0,2,3,11,22,25,27,28,29,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[31,31,-3,-11,31,31,-55,31,31,-2,-4,-5,-6,-7,-8,-9,-10,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'NUMBER_FLOAT':([0,2,3,11,22,25,27,28,29,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[32,32,-3,-11,32,32,-55,32,32,-2,-4,-5,-6,-7,-8,-9,-10,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'TRUE':([0,2,3,11,22,25,27,28,29,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[33,33,-3,-11,33,33,-55,33,33,-2,-4,-5,-6,-7,-8,-9,-10,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'FALSE':([0,2,3,11,22,25,27,28,29,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[34,34,-3,-11,34,34,-55,34,34,-2,-4,-5,-6,-7,-8,-9,-10,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'NULL':([0,2,3,11,22,25,27,28,29,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[35,35,-3,-11,35,35,-55,35,35,-2,-4,-5,-6,-7,-8,-9,-10,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'TEXT_STRING':([0,2,3,11,22,25,27,28,29,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[36,36,-3,-11,36,36,-55,36,36,-2,-4,-5,-6,-7,-8,-9,-10,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'TEXT_CHAR':([0,2,3,11,22,25,27,28,29,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[37,37,-3,-11,37,37,-55,37,37,-2,-4,-5,-6,-7,-8,-9,-10,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'$end':([1,2,3,11,27,38,39,40,41,42,43,44,45,],[0,-1,-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,]),'CONDITIONAL2':([3,11,27,38,39,40,41,42,43,44,45,97,],[-3,-11,-55,-2,-4,-5,-6,-7,-8,-9,-10,100,]),'END_LINE':([3,4,5,6,7,8,9,10,11,12,13,14,15,25,26,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,57,58,59,60,61,62,63,64,65,66,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,97,98,104,106,],[-3,39,40,41,42,43,44,45,-11,-12,-13,-14,-31,-53,-54,-55,-28,-29,-30,-32,-33,-34,-35,-36,-2,-4,-5,-6,-7,-8,-9,-10,-38,-43,-39,-44,-40,-45,-41,-46,-42,-47,-31,-52,-25,-26,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-37,-27,-48,-50,-49,-51,]),'RPAREN':([12,13,14,30,31,32,33,34,35,36,37,68,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,101,],[-12,-13,-14,-28,-29,-30,-32,-33,-34,-35,-36,87,-31,-25,-26,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-37,91,-27,92,103,]),'SEPARATION':([12,13,14,30,31,32,33,34,35,36,37,69,73,74,75,76,77,78,79,80,81,82,83,84,85,87,89,96,],[-12,-13,-14,-28,-29,-30,-32,-33,-34,-35,-36,-31,-25,-26,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-37,-27,93,99,]),'PLUS_OP':([14,15,30,31,32,33,34,35,36,37,69,87,],[46,-31,-28,-29,-30,-32,-33,-34,-35,-36,-31,-27,]),'MUL_OP':([14,15,30,31,32,33,34,35,36,37,69,87,],[48,-31,-28,-29,-30,-32,-33,-34,-35,-36,-31,-27,]),'DIV_OP':([14,15,30,31,32,33,34,35,36,37,69,87,],[49,-31,-28,-29,-30,-32,-33,-34,-35,-36,-31,-27,]),'LESS_OP':([14,15,30,31,32,33,34,35,36,37,69,87,],[50,-31,-28,-29,-30,-32,-33,-34,-35,-36,-31,-27,]),'GREATER_OP':([14,15,30,31,32,33,34,35,36,37,69,87,],[51,-31,-28,-29,-30,-32,-33,-34,-35,-36,-31,-27,]),'LESS_EQUAL_OP':([14,15,30,31,32,33,34,35,36,37,69,87,],[52,-31,-28,-29,-30,-32,-33,-34,-35,-36,-31,-27,]),'GREATER_EQUAL_OP':([14,15,30,31,32,33,34,35,36,37,69,87,],[53,-31,-28,-29,-30,-32,-33,-34,-35,-36,-31,-27,]),'EQUAL_OP':([14,15,30,31,32,33,34,35,36,37,69,87,],[54,-31,-28,-29,-30,-32,-33,-34,-35,-36,-31,-27,]),'DIFFERENT_OP':([14,15,30,31,32,33,34,35,36,37,69,87,],[55,-31,-28,-29,-30,-32,-33,-34,-35,-36,-31,-27,]),'ASSIGNMENT_OP':([15,57,59,61,63,65,90,],[56,56,56,56,56,56,56,]),'STRUCTURE_BODY':([91,92,100,103,],[94,95,102,105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,94,95,102,105,],[2,97,98,104,106,]),'statement':([0,2,94,95,97,98,102,104,105,106,],[3,38,3,3,38,38,3,38,3,38,]),'expression':([0,2,22,25,56,67,70,93,94,95,97,98,102,104,105,106,],[4,4,68,72,85,86,88,96,4,4,4,4,4,4,4,4,]),'assignment':([0,2,16,17,18,19,20,71,94,95,97,98,99,102,104,105,106,],[5,5,58,60,62,64,66,89,5,5,5,5,101,5,5,5,5,]),'declaration':([0,2,94,95,97,98,102,104,105,106,],[6,6,6,6,6,6,6,6,6,6,]),'conditional':([0,2,94,95,97,98,102,104,105,106,],[7,7,7,7,7,7,7,7,7,7,]),'loop':([0,2,94,95,97,98,102,104,105,106,],[8,8,8,8,8,8,8,8,8,8,]),'return_statement':([0,2,94,95,97,98,102,104,105,106,],[9,9,9,9,9,9,9,9,9,9,]),'break_statement':([0,2,94,95,97,98,102,104,105,106,],[10,10,10,10,10,10,10,10,10,10,]),'comment':([0,2,94,95,97,98,102,104,105,106,],[11,11,11,11,11,11,11,11,11,11,]),'binary_expression':([0,2,22,25,56,67,70,93,94,95,97,98,102,104,105,106,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'unitary_expression':([0,2,22,25,56,67,70,93,94,95,97,98,102,104,105,106,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'primary_expression':([0,2,22,25,28,29,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[14,14,14,14,73,74,75,76,77,78,79,80,81,82,83,84,14,14,14,14,14,14,14,14,14,14,14,14,]),'term':([0,2,22,25,28,29,46,47,48,49,50,51,52,53,54,55,56,67,70,93,94,95,97,98,102,104,105,106,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',20),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',24),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',25),
  ('statement -> expression END_LINE','statement',2,'p_statement','parser.py',32),
  ('statement -> assignment END_LINE','statement',2,'p_statement','parser.py',33),
  ('statement -> declaration END_LINE','statement',2,'p_statement','parser.py',34),
  ('statement -> conditional END_LINE','statement',2,'p_statement','parser.py',35),
  ('statement -> loop END_LINE','statement',2,'p_statement','parser.py',36),
  ('statement -> return_statement END_LINE','statement',2,'p_statement','parser.py',37),
  ('statement -> break_statement END_LINE','statement',2,'p_statement','parser.py',38),
  ('statement -> comment','statement',1,'p_statement','parser.py',39),
  ('expression -> binary_expression','expression',1,'p_expression','parser.py',44),
  ('expression -> unitary_expression','expression',1,'p_expression','parser.py',45),
  ('expression -> primary_expression','expression',1,'p_expression','parser.py',46),
  ('binary_expression -> primary_expression PLUS_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',50),
  ('binary_expression -> primary_expression MINUS_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',51),
  ('binary_expression -> primary_expression MUL_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',52),
  ('binary_expression -> primary_expression DIV_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',53),
  ('binary_expression -> primary_expression LESS_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',54),
  ('binary_expression -> primary_expression GREATER_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',55),
  ('binary_expression -> primary_expression LESS_EQUAL_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',56),
  ('binary_expression -> primary_expression GREATER_EQUAL_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',57),
  ('binary_expression -> primary_expression EQUAL_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',58),
  ('binary_expression -> primary_expression DIFFERENT_OP primary_expression','binary_expression',3,'p_binary_expression','parser.py',59),
  ('unitary_expression -> MINUS_OP primary_expression','unitary_expression',2,'p_unitary_expression','parser.py',85),
  ('unitary_expression -> LOGICAL_OP_NOT primary_expression','unitary_expression',2,'p_unitary_expression','parser.py',86),
  ('primary_expression -> LPAREN expression RPAREN','primary_expression',3,'p_primary_expression','parser.py',94),
  ('primary_expression -> term','primary_expression',1,'p_primary_expression','parser.py',95),
  ('term -> NUMBER_INTEGER','term',1,'p_term','parser.py',102),
  ('term -> NUMBER_FLOAT','term',1,'p_term','parser.py',103),
  ('term -> VARIABLE','term',1,'p_term','parser.py',104),
  ('term -> TRUE','term',1,'p_term','parser.py',105),
  ('term -> FALSE','term',1,'p_term','parser.py',106),
  ('term -> NULL','term',1,'p_term','parser.py',107),
  ('term -> TEXT_STRING','term',1,'p_term','parser.py',108),
  ('term -> TEXT_CHAR','term',1,'p_term','parser.py',109),
  ('assignment -> VARIABLE ASSIGNMENT_OP expression','assignment',3,'p_assignment','parser.py',124),
  ('declaration -> TYPE_BOOLEAN VARIABLE','declaration',2,'p_declaration','parser.py',129),
  ('declaration -> TYPE_STRING VARIABLE','declaration',2,'p_declaration','parser.py',130),
  ('declaration -> TYPE_CHAR VARIABLE','declaration',2,'p_declaration','parser.py',131),
  ('declaration -> TYPE_INTEGER VARIABLE','declaration',2,'p_declaration','parser.py',132),
  ('declaration -> TYPE_FLOAT VARIABLE','declaration',2,'p_declaration','parser.py',133),
  ('declaration -> TYPE_BOOLEAN assignment','declaration',2,'p_declaration','parser.py',134),
  ('declaration -> TYPE_STRING assignment','declaration',2,'p_declaration','parser.py',135),
  ('declaration -> TYPE_CHAR assignment','declaration',2,'p_declaration','parser.py',136),
  ('declaration -> TYPE_INTEGER assignment','declaration',2,'p_declaration','parser.py',137),
  ('declaration -> TYPE_FLOAT assignment','declaration',2,'p_declaration','parser.py',138),
  ('conditional -> CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list','conditional',6,'p_conditional','parser.py',147),
  ('conditional -> CONDITIONAL1 LPAREN expression RPAREN STRUCTURE_BODY statement_list CONDITIONAL2 STRUCTURE_BODY statement_list','conditional',9,'p_conditional','parser.py',148),
  ('loop -> LOOP1 LPAREN expression RPAREN STRUCTURE_BODY statement_list','loop',6,'p_loop','parser.py',164),
  ('loop -> LOOP2 LPAREN assignment SEPARATION expression SEPARATION assignment RPAREN STRUCTURE_BODY statement_list','loop',10,'p_loop','parser.py',165),
  ('return_statement -> RETURN expression','return_statement',2,'p_return_statement','parser.py',182),
  ('return_statement -> RETURN','return_statement',1,'p_return_statement','parser.py',183),
  ('break_statement -> BREAK','break_statement',1,'p_break_statement','parser.py',190),
  ('comment -> COMMENT','comment',1,'p_comment','parser.py',194),
]
