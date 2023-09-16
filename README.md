# Pokeit to H2N converter for Poker Players

A very simple and tiny CLI to convert files from Pokeit format, to H2N format.

Simple Usage
- Place the executable in the same folder as the files you want to convert and double-click it.

Moderate Usage
- Place the executable in the same folder as the hand history files you want to convert, and run it in terminal to see the progress.

Advanced Usage
- Open the executable in terminal and use -f flag to pass the individual filenames which you want to process. Or you can use -d flag to pass the directory you want to process

Running as a cron/scheduled task
- Put the executable in PATH and run the following command in cron
```
format_converter_cli.exe -d <path/to/pppoker_hh/folder> -o <path/to/output/folder>
```