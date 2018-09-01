
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AUTHOR BODY BOLD DOCUMENT DOLLAR DOTS DOUBLEQUOTESEND DOUBLEQUOTESSTART ENDDOCUMENT HREF ITALICS ITEM_ST LATEX LCURLY NEWLINE NEWLINEMATHEND NEWLINEMATHSTART OL_EN OL_ST PAR RCURLY SECTION SUBSECTION TEXT TITLE UL_EN UL_ST UNDERLINE URL USEPACKAGE USEPACKAGEPARAMdocument : DOCUMENT document\n\t\t\t\t| TITLE document\n\t\t\t\t| AUTHOR document\n\t\t\t\t| BODY document\n\t\t\t\t| section document\n\t\t\t\t| ENDDOCUMENT\n\t\t\t\tsection : SECTION LCURLY sentence RCURLY section\n\t\t\t   | section subsection\n\t\t\t   | subsection\n\t\t\t   | sentence\n\t\t\t\tsubsection : SUBSECTION LCURLY sentence RCURLY subsection\n\t\t\t\t  | subsection subsectioncon\n\t\t\t\t  | subsectioncon\n\t\t\t\t  subsectioncon : subsectioncon sentence\n\t\t\t\t\t | subsectioncon ul\n\t\t\t\t\t | subsectioncon ol\n\t\t\t\t\t | sentence\n\t\t\t\t\t | ol\n\t\t\t\t\t | ulol : OL_ST list OL_ENul : UL_ST list UL_ENlistitem : ITEM_ST TEXTlist : list listitemlist : listitemsentence : UNDERLINE LCURLY sentence RCURLY sentence\n\t\t\t   | BOLD LCURLY sentence RCURLY sentence\n\t\t\t   | ITALICS LCURLY sentence RCURLY sentence\n\t\t\t   | sentence TEXT\n\t\t\t   | TEXT sentence\n\t\t\t   | TEXT\n\t\t\t   '
    
_lr_action_items = {'BODY':([0,2,3,7,8,9,13,15,16,18,19,20,22,23,30,31,35,36,37,39,40,47,49,58,59,60,61,62,63,],[16,-10,-30,16,16,16,-13,-9,16,-18,-19,16,-28,-29,-10,-8,-16,-15,-14,-17,-12,-21,-20,-27,-7,-11,-25,-26,-8,]),'ITALICS':([0,2,3,7,8,9,13,15,16,18,19,20,21,22,23,24,30,31,34,35,36,37,38,39,40,42,47,49,53,54,55,56,57,58,59,60,61,62,63,],[1,-10,1,1,1,1,1,1,1,-18,-19,1,1,-28,-29,1,-10,1,1,-16,-15,-14,1,-17,1,1,-21,-20,1,1,1,1,1,-27,1,1,-25,-26,1,]),'BOLD':([0,2,3,7,8,9,13,15,16,18,19,20,21,22,23,24,30,31,34,35,36,37,38,39,40,42,47,49,53,54,55,56,57,58,59,60,61,62,63,],[17,-10,17,17,17,17,17,17,17,-18,-19,17,17,-28,-29,17,-10,17,17,-16,-15,-14,17,-17,17,17,-21,-20,17,17,17,17,17,-27,17,17,-25,-26,17,]),'AUTHOR':([0,2,3,7,8,9,13,15,16,18,19,20,22,23,30,31,35,36,37,39,40,47,49,58,59,60,61,62,63,],[7,-10,-30,7,7,7,-13,-9,7,-18,-19,7,-28,-29,-10,-8,-16,-15,-14,-17,-12,-21,-20,-27,-7,-11,-25,-26,-8,]),'TEXT':([0,2,3,7,8,9,13,15,16,18,19,20,21,22,23,24,25,30,31,34,35,36,37,38,39,40,42,44,45,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,],[3,22,3,3,3,3,3,3,3,-18,-19,3,3,-28,22,3,46,22,3,3,-16,-15,22,3,22,3,3,22,22,-21,-20,22,22,22,3,3,3,3,3,22,3,3,22,22,3,]),'SECTION':([0,2,3,7,8,9,13,15,16,18,19,20,22,23,30,31,35,36,37,39,40,47,49,54,58,59,60,61,62,63,],[4,-10,-30,4,4,4,-13,-9,4,-18,-19,4,-28,-29,-10,-8,-16,-15,-14,-17,-12,-21,-20,4,-27,-7,-11,-25,-26,-8,]),'TITLE':([0,2,3,7,8,9,13,15,16,18,19,20,22,23,30,31,35,36,37,39,40,47,49,58,59,60,61,62,63,],[9,-10,-30,9,9,9,-13,-9,9,-18,-19,9,-28,-29,-10,-8,-16,-15,-14,-17,-12,-21,-20,-27,-7,-11,-25,-26,-8,]),'RCURLY':([3,22,23,44,45,50,51,52,58,61,62,],[-30,-28,-29,53,54,55,56,57,-27,-25,-26,]),'UL_EN':([26,27,46,48,],[47,-24,-22,-23,]),'LCURLY':([1,4,10,14,17,],[21,24,34,38,42,]),'UL_ST':([0,2,3,7,8,9,13,15,16,18,19,20,22,23,30,31,35,36,37,39,40,47,49,54,55,58,59,60,61,62,63,],[5,-10,-30,5,5,5,5,5,5,-18,-19,5,-28,-29,-10,5,-16,-15,-14,-17,5,-21,-20,5,5,-27,5,5,-25,-26,5,]),'SUBSECTION':([0,2,3,7,8,9,13,15,16,18,19,20,22,23,30,31,35,36,37,39,40,47,49,54,55,58,59,60,61,62,63,],[10,-10,-30,10,10,10,-13,-9,10,-18,-19,10,-28,-29,-10,-8,-16,-15,-14,-17,-12,-21,-20,10,10,-27,10,-11,-25,-26,-8,]),'ITEM_ST':([5,6,26,27,28,46,48,],[25,25,25,-24,25,-22,-23,]),'ENDDOCUMENT':([0,2,3,7,8,9,13,15,16,18,19,20,22,23,30,31,35,36,37,39,40,47,49,58,59,60,61,62,63,],[11,-10,-30,11,11,11,-13,-9,11,-18,-19,11,-28,-29,-10,-8,-16,-15,-14,-17,-12,-21,-20,-27,-7,-11,-25,-26,-8,]),'OL_EN':([27,28,46,48,],[-24,49,-22,-23,]),'OL_ST':([0,2,3,7,8,9,13,15,16,18,19,20,22,23,30,31,35,36,37,39,40,47,49,54,55,58,59,60,61,62,63,],[6,-10,-30,6,6,6,6,6,6,-18,-19,6,-28,-29,-10,6,-16,-15,-14,-17,6,-21,-20,6,6,-27,6,6,-25,-26,6,]),'DOCUMENT':([0,2,3,7,8,9,13,15,16,18,19,20,22,23,30,31,35,36,37,39,40,47,49,58,59,60,61,62,63,],[20,-10,-30,20,20,20,-13,-9,20,-18,-19,20,-28,-29,-10,-8,-16,-15,-14,-17,-12,-21,-20,-27,-7,-11,-25,-26,-8,]),'UNDERLINE':([0,2,3,7,8,9,13,15,16,18,19,20,21,22,23,24,30,31,34,35,36,37,38,39,40,42,47,49,53,54,55,56,57,58,59,60,61,62,63,],[14,-10,14,14,14,14,14,14,14,-18,-19,14,14,-28,-29,14,-10,14,14,-16,-15,-14,14,-17,14,14,-21,-20,14,14,14,14,14,-27,14,14,-25,-26,14,]),'$end':([11,12,29,32,33,41,43,],[-6,0,-3,-5,-2,-4,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ol':([0,7,8,9,13,15,16,20,31,40,54,55,59,60,63,],[18,18,18,18,35,18,18,18,18,35,18,18,18,18,18,]),'sentence':([0,3,7,8,9,13,15,16,20,21,24,31,34,38,40,42,53,54,55,56,57,59,60,63,],[2,23,2,30,2,37,39,2,2,44,45,39,50,51,37,52,58,2,39,61,62,39,39,39,]),'section':([0,7,8,9,16,20,54,],[8,8,8,8,8,8,59,]),'list':([5,6,],[26,28,]),'ul':([0,7,8,9,13,15,16,20,31,40,54,55,59,60,63,],[19,19,19,19,36,19,19,19,19,36,19,19,19,19,19,]),'subsection':([0,7,8,9,16,20,54,55,59,],[15,15,31,15,15,15,15,60,63,]),'document':([0,7,8,9,16,20,],[12,29,32,33,41,43,]),'subsectioncon':([0,7,8,9,15,16,20,31,54,55,59,60,63,],[13,13,13,13,40,13,13,40,13,13,13,40,40,]),'listitem':([5,6,26,28,],[27,27,48,48,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> document","S'",1,None,None,None),
  ('document -> DOCUMENT document','document',2,'p_document','latex-parser.py',70),
  ('document -> TITLE document','document',2,'p_document','latex-parser.py',71),
  ('document -> AUTHOR document','document',2,'p_document','latex-parser.py',72),
  ('document -> BODY document','document',2,'p_document','latex-parser.py',73),
  ('document -> section document','document',2,'p_document','latex-parser.py',74),
  ('document -> ENDDOCUMENT','document',1,'p_document','latex-parser.py',75),
  ('section -> SECTION LCURLY sentence RCURLY section','section',5,'p_section','latex-parser.py',100),
  ('section -> section subsection','section',2,'p_section','latex-parser.py',101),
  ('section -> subsection','section',1,'p_section','latex-parser.py',102),
  ('section -> sentence','section',1,'p_section','latex-parser.py',103),
  ('subsection -> SUBSECTION LCURLY sentence RCURLY subsection','subsection',5,'p_subsection','latex-parser.py',115),
  ('subsection -> subsection subsectioncon','subsection',2,'p_subsection','latex-parser.py',116),
  ('subsection -> subsectioncon','subsection',1,'p_subsection','latex-parser.py',117),
  ('subsectioncon -> subsectioncon sentence','subsectioncon',2,'p_subsectioncon','latex-parser.py',129),
  ('subsectioncon -> subsectioncon ul','subsectioncon',2,'p_subsectioncon','latex-parser.py',130),
  ('subsectioncon -> subsectioncon ol','subsectioncon',2,'p_subsectioncon','latex-parser.py',131),
  ('subsectioncon -> sentence','subsectioncon',1,'p_subsectioncon','latex-parser.py',132),
  ('subsectioncon -> ol','subsectioncon',1,'p_subsectioncon','latex-parser.py',133),
  ('subsectioncon -> ul','subsectioncon',1,'p_subsectioncon','latex-parser.py',134),
  ('ol -> OL_ST list OL_EN','ol',3,'p_ol','latex-parser.py',166),
  ('ul -> UL_ST list UL_EN','ul',3,'p_ul','latex-parser.py',173),
  ('listitem -> ITEM_ST TEXT','listitem',2,'p_listitem','latex-parser.py',180),
  ('list -> list listitem','list',2,'p_list_multi','latex-parser.py',185),
  ('list -> listitem','list',1,'p_list_unary','latex-parser.py',190),
  ('sentence -> UNDERLINE LCURLY sentence RCURLY sentence','sentence',5,'p_sentence','latex-parser.py',194),
  ('sentence -> BOLD LCURLY sentence RCURLY sentence','sentence',5,'p_sentence','latex-parser.py',195),
  ('sentence -> ITALICS LCURLY sentence RCURLY sentence','sentence',5,'p_sentence','latex-parser.py',196),
  ('sentence -> sentence TEXT','sentence',2,'p_sentence','latex-parser.py',197),
  ('sentence -> TEXT sentence','sentence',2,'p_sentence','latex-parser.py',198),
  ('sentence -> TEXT','sentence',1,'p_sentence','latex-parser.py',199),
]
