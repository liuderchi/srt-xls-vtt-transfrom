# srt-xls-vtt-transfrom

## What are these scripts doing?

  - Transform SRT subtitles to XLS file storing different languages
  - After your own translation, transform XLS file to VTT subtitles

## Environment

  - Python: v3.4 or higher
  - Python Package: xlrd (v0.9.4), xlwt (v1.0.0)
      - use ```pip install xlrd && pip install xlwt``` to install

## Run the code

  - transform SRT file to XLS file
      - ```python srt2xls.py ./path/to/my.srt ./path/to/xls```
      - would generate file ```my.xls```
  - transform translated XLS file to VTT file
      - ```python xls2srt.py ./path/to/my.xls ./path/to/vtt```
      - would generate file ```my.vtt```

## License

[MIT License](http://opensource.org/licenses/MIT)
