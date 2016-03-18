print "\n  Macro creator by Miron"
print "  8===========D~ \n"

#sourceFile = 'MobaXterm.bin'
sourceFile = 'dupa.txt'

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
	' ' : '258:32:3735553:SPACE|',
	'\n': '258:13:1835009:RETURN|'
};

# read source file
f = open(sourceFile)

for line in iter(f):
    print 'Translating line: ', line, len(line)
    for index, char in enumerate(line):
        print '[', index, ']:\t', char, ' => ', dict[char]

# close file handler
f.close()
