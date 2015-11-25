'''xls2vtt.py
Created date: 20151104
Author: derek liu
Description: transform a pre-defined .xls subtitle to a .vtt file

xls format:
    <frame, timing, en-lines, zh-lines, notes>
run the code:
    $ python xls2vtt.py ./in/mySheet.xls ./out/vttFolder/
    # output file name is same as input file name
'''

import sys
import os
import xlrd

frameCol = 0
timingCol = 1
enCol = 2
zhCol = 3
notesCol = 4

if __name__ == "__main__":
    if len(sys.argv) is not 3:
        print( 'wrong argv: %d' % len(sys.argv))
        sys.exit(0)
    '''$ python xls2vtt.py ./in/mySheet.xls ./out/vttFolder/'''
    inFilePath = sys.argv[1]
    inFileName = os.path.split(inFilePath)[1]
    outFolder = sys.argv[2]
    outFileName = os.path.splitext(inFileName)[0] + '.vtt'

    workbook = xlrd.open_workbook( inFilePath )
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(r, col)
                for col in range(sheet.ncols)]
                    for r in range(sheet.nrows)]

    outFileObj = open( outFolder + '/' + outFileName, "w",  encoding='UTF-8')
    oldstdout = sys.stdout
    sys.stdout = outFileObj

    print( 'WEBVTT\n' )
    for row in range(sheet.nrows)[1:]:
        print(  data[row][ frameCol ]  )
        print( data[row][ timingCol ].replace(',', '.') )
        print( data[row][ zhCol ] + '\n')
        '''TODO: if notes not empty, write to webvtt'''
        sys.stdout.flush() 

    outFileObj.close()
    sys.stdout = oldstdout;
    print('done: %s' % (outFolder + '/' + outFileName) )
