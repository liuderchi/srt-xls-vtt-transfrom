'''srt2xls.py
Created date: 20151104
Author: derek liu
Description: transform a .srt subtitle to a .xls file

xls format:
    <frame, timing, en-lines, zh-lines, notes>
run the code:
    $ python srt2xls.py ./in/mySubtitle.srt ./out/xlsFolder/
    # output file name is same as input file name
'''

import sys
import os
import xlwt

frameCol = 0
timingCol = 1
enCol = 2
zhCol = 3
notesCol = 4


if __name__ == "__main__":
    if len(sys.argv) is not 3:
        print( 'wrong argv: %d' % len(sys.argv))
        sys.exit(0)
    '''$ python srt2xls.py ./in/mySubtitle.srt ./out/xlsFolder/'''
    inFilePath = sys.argv[1]
    inFileName = os.path.split(inFilePath)[1]
    outFolder = sys.argv[2]
    outFileName = os.path.splitext(inFileName)[0] + '.xls'

    fileObj = open( inFilePath )
    data = fileObj.read()
    data = data.split('\n\n')
    for rowid in range(len(data)):
        data[rowid] = data[rowid].split('\n', 2)
        if len( data[rowid] ) < 3:
            data.pop()

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("Sheet1")
    colNames = ['frame ', 'timing', 'en-lines ', 'zh-lines', 'notes' ]
    for colid in range(len(colNames)):
        worksheet.write( 0 , colid, colNames[colid])
    for rowid in range(len(data)):
        for colid in range(len(data[0])):
            worksheet.write( rowid + 1, colid, data[rowid][colid])
            # row id starts from secon,

    worksheet.col(1).width = 256 * max([len(frame[1]) for frame in data])
    worksheet.col(2).width = 128 * max([len(frame[2]) for frame in data])
    worksheet.col(3).width = worksheet.col(2).width

    workbook.save( outFolder + '/' + outFileName )
    print('done: %s' % (outFolder + '/' + outFileName) )
