# script which translates characters from file "input.txt" to file "output.txt"
# "output.txt" content is cleared before each script run

print "\n  Macro creator by Miron"
print "  8===========D~ \n"

srcFile = 'input.txt'
dstFile = 'output.txt'

# translation dictionary
dict = {
	'a' : '258:97:1966081:a|',
	'b' : '258:98:3145729:b|',
	'c' : '258:99:3014657:c|',
	'd' : '258:100:2097153:d|',
	'e' : '258:101:1179649:e|',
	'f' : '258:102:2162689:f|',
	'g' : '258:103:2228225:g|',
	'h' : '258:104:2293761:h|',
	'i' : '258:105:1507329:i|',
	'j' : '258:106:2359297:j|',
	'k' : '258:107:2424833:k|',
	'l' : '258:108:2490369:l|',
	'm' : '258:109:3276801:m|',
	'n' : '258:110:3211265:n|',
	'o' : '258:111:1572865:o|',
	'p' : '258:112:1638401:p|',
	'q' : '258:113:1048577:q|',
	'r' : '258:114:1245185:r|',
	's' : '258:115:2031617:s|',
	't' : '258:116:1310721:t|',
	'u' : '258:117:1441793:u|',
	'v' : '258:118:3080193:v|',
	'w' : '258:119:1114113:w|',
	'x' : '258:120:2949121:x|',
	'y' : '258:121:1376257:y|',
	'z' : '258:122:2883585:z|',
	'1' : '258:49:131073:1|',
	'2' : '258:50:196609:2|',
	'3' : '258:51:262145:3|',
	'4' : '258:52:327681:4|',
	'5' : '258:53:393217:5|',
	'6' : '258:54:458753:6|',
	'7' : '258:55:524289:7|',
	'8' : '258:56:589825:8|',
	'9' : '258:57:655361:9|',
	'0' : '258:48:720897:0|',
	'-' : '258:45:786433:-|',
	':' : '258:58:2555905:COLON|',
	' ' : '258:32:3735553:SPACE|',
	'|' : '258:124:2818049:PIPE|',
	'"' : '258:34:2621441:"|',
	'_' : '258:95:786433:_|',
	'\n': '258:13:1835009:RETURN|0:0:0:SLEEPEQUAL1200|\n'
};

# open source file for reading
fileReadHandler = open(srcFile, "r")

# clear destination file
open(dstFile, 'w').close()
# open destination file for writing
fileWriteHandler = open (dstFile, "w")

# read line by line
for line in iter(fileReadHandler):
    print '\nTranslating line: ', line, 'line length: ', len(line)

    # check if line is a comment
    if '#' in line:
        print '\n-=> [INFO]: line is a comment! It will not be translated \n'
        continue

    # check if line is a macro name - it must contains ::
    if '::' in line:
        print '\n-=> [INFO]: line is a macro name! It will not be translated \n'
        # remove '::' & 'newline' and add "=" at the end
        line = line.replace('::', '')
        line = line.replace('\n', '')
        line += '='
        # write translation to output file
        fileWriteHandler.write(line)
        continue

    # do the translation - char by char
    for index, char in enumerate(line):
        if char not in dict:
            print '\n-=> [ERROR]: cannot translate:', char, '- could not find it in dictionary, please update dictionary!\n'
            exit(1)
        if (char == "\n"):
	    print '[', index, ']:\t', '\\n => ', dict[char]
        else:
	    print '[', index, ']:\t', char, ' => ', dict[char]

        # write translation to output file
        fileWriteHandler.write(dict[char])

# close file handlers
fileReadHandler.close()
fileWriteHandler.close()

#text_file.write("Purchase Amount: %s" % TotalAmount)
