#!usr/bin/python
# -*- coding: utf-8 -*-import string

EXP_OUTER_SUM = 'EXP_OUTER_SUM'
EXP_INFLATION = 'EXP_INFLATION'
EXP_REPETITION = 'EXP_REPETITION'

expcodes = {
	EXP_OUTER_SUM  : 'exp-ous',
	EXP_INFLATION  : 'exp-inf',
	EXP_REPETITION : 'exp-rep'
}

OFFSET_BLOCK = 'OFFSET_BLOCK'
OFFSET_PIXEL = 'OFFSET_PIXEL'
OFFSET_NONE  = 'OFFSET_NONE'

ofscodes = {
	OFFSET_BLOCK : 'ofs-blc',
	OFFSET_PIXEL : 'ofs-pxl',
	OFFSET_NONE  : 'ofs-non'
}

OFM_PAR = 'OFMODE_PARALLEL'
OFM_ORT = 'OFMODE_ORTHOGONAL'

ofmmodes = {
	OFM_PAR : 'ofm-par',
	OFM_ORT : 'ofm-ort'
}