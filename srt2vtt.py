'''srt2vtt.py
Created date: 2015-12-22
Author: derek liu
Description: transform a .srt subtitle to a .vtt file with en-subtitle in comment
reference https://w3c.github.io/webvtt/#introduction-comments

run the code:
    $ python srt2vtt.py ./in/mySubtitle.srt ./out/vttFolder/
    # output file name is same as input file name
'''

import sys
import os

if __name__ == "__main__":
    if len(sys.argv) is not 3:
        print( 'wrong argv: %d' % len(sys.argv))
        sys.exit(0)
    '''$ python srt2vtt.py ./in/mySubtitle.srt ./out/vttFolder/'''
    # parse arg
    in_file_path, out_folder_path = sys.argv[1:3]
    in_file_name = os.path.basename(in_file_path)
    #out_folder_path = sys.argv[2]
    out_file_name = os.path.splitext(in_file_name)[0] + '.vtt' # remove '.srt'

    with open(in_file_path) as in_file:

        # srt open, read, group frames
        frames = in_file.read().split('\n\n')

        # parse frames
        for rowid in range(len(frames)):
            # split frame into three parts: [frameid, timestamp, en]
            frames[rowid] = frames[rowid].split('\n', 2)
            # NOTE frames[rowid][2] may contain nothing (slient frame)

        # discard invalid frame (e.g. silence frame with no line)
        frames = [frame for frame in frames if len(frame) == 3]

        # update frame index
        for index in range(len(frames)):
            frames[index][0] = index + 1

        #open vtt and redirect stdout
        out_file = open(os.path.join(out_folder_path, out_file_name), "w")
        # must UTF-8

        oldstdout = sys.stdout # save original stdout
        sys.stdout = out_file # stdout redirect
        # vtt write
        print( 'WEBVTT\n' ) # vtt file header
        for frame in frames:
            print( frame[0] ) # frame id
            print( frame[1].replace(',', '.') ) # format timestamp
            print("") # for chinese line
            print( "\nNOTE\n" + frame[2] + '\n') # en subtitle
            sys.stdout.flush()

        # close vtt file
        out_file.close() # print() require close() to flush
        sys.stdout = oldstdout; # restore stdout

    print('done: %s' % (out_folder_path + '/' + out_file_name) )
