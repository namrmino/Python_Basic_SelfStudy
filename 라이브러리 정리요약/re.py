import re
"""
? 0,1ë²ˆ
* more 0
+ more 1
^spam  with start
spam$ with end
. except \n
?! ^((?![A-Z]).)*$  eg) no-caps-here,$ymb0ls a4e f!ne

{n} n
{n,} more n
{,m} less m
{n,m} more n less m
{n,m}? / *? / +? minimum 

(com|org|edu|net) com OR org OR edu OR net

[abc] with a, b, c
[^abc] not a, b, c

\. .
\d 0~9
\D not 0~9
\w ë‹¨ì–´
\W not ë‹¨ì–´
\s ë¹ˆì¹¸
\S not ë¹ˆì¹¸
"""
# | ? * {,}

# | OR
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
mo.group(1)

# ? *
batRegex = re.compile(r'Bat(wo)?man') # 0 OR 1
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

batRegex = re.compile(r'Bat(wo)*man') # more than 0
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()

batRegex = re.compile(r'Bat(wo)+man') # more than 1
mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None

# {,}
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group() # HaHaHa

nongreedyHaRegex = re.compile(r'(Ha){3,5}')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group() # HaHaHaHaHa

# 
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')

#
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 prtrodge')

"""
[abc] with a, b, c
[^abc] not a, b, c
"""
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoBoCop eats baby food. BABY FOOD.')

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

wholeStringIsNum = re.compile(r'\d+$')
wholeStringIsNum.search('12345xyz67890').group() # 67890
wholeStringIsNum.search('12   34567890').group() # 34567890

# .
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

nameRegex = re.compile(r'First Name: (.*) Last name: (.*)')
mo = nameRegex.search('First Name: Al Last name: Sweigart')
mo.group(0)
mo.group(1)
mo.group(2)

nongreedyRegex = re.compile(r'<.*>')
nongreedyRegex.search('<To serve man> for dinner.>').group()

# .*
noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold The law.').group()

noNewlineRegex = re.compile('.*', re.DOTALL)
noNewlineRegex.search('Serve the public trust,\npRotect the innocent.\nUphold the law.').group()

# re.I
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
robocop.search('ROBOCOP protects the innocent.').group()
robocop.search('Al, why does your programming book talk about robocop so much?').group()

# sub
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

#
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew\
                    Agent Bob was a double agent.')

#
phoneRegex = re.compile('''(
        (\d{3}|\(\d{3}\))              # area code
        (\s|-|\.)?                     # separator
        \d{3}                          # first 3 digits
        (\s|-|\.)?                     # separator
        \d{4}                          # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
        )''', re.VERBOSE)
# re.IGNORECASE = re.I
somRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
somRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)