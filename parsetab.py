
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DOTS ITEM_ST NEWLINE OL_EN OL_ST TEXT UL_EN UL_STdoc : doc ul\n\t\t   | doc ol\n\t\t   | ol\n\t\t   | ulol : OL_ST list OL_ENul : UL_ST list UL_ENlistitem : ITEM_ST TEXTlist : list listitemlist : listitem'
    
_lr_action_items = {'OL_ST':([0,1,3,4,9,10,14,15,],[2,-3,2,-4,-2,-1,-5,-6,]),'TEXT':([6,],[12,]),'ITEM_ST':([2,5,7,8,11,12,13,],[6,6,6,-9,6,-7,-8,]),'UL_EN':([8,11,12,13,],[-9,15,-7,-8,]),'UL_ST':([0,1,3,4,9,10,14,15,],[5,-3,5,-4,-2,-1,-5,-6,]),'OL_EN':([7,8,12,13,],[14,-9,-7,-8,]),'$end':([1,3,4,9,10,14,15,],[-3,0,-4,-2,-1,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'doc':([0,],[3,]),'ol':([0,3,],[1,9,]),'list':([2,5,],[7,11,]),'listitem':([2,5,7,11,],[8,8,13,13,]),'ul':([0,3,],[4,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> doc","S'",1,None,None,None),
  ('doc -> doc ul','doc',2,'p_doc','latex-parser.py',32),
  ('doc -> doc ol','doc',2,'p_doc','latex-parser.py',33),
  ('doc -> ol','doc',1,'p_doc','latex-parser.py',34),
  ('doc -> ul','doc',1,'p_doc','latex-parser.py',35),
  ('ol -> OL_ST list OL_EN','ol',3,'p_ol','latex-parser.py',42),
  ('ul -> UL_ST list UL_EN','ul',3,'p_ul','latex-parser.py',48),
  ('listitem -> ITEM_ST TEXT','listitem',2,'p_listitem','latex-parser.py',54),
  ('list -> list listitem','list',2,'p_list_multi','latex-parser.py',58),
  ('list -> listitem','list',1,'p_list_unary','latex-parser.py',62),
]
