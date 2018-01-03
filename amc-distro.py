from lxml import html
import requests

# the frequency of AMC 12 answers from 2002 - 2017

countA12 = 0
countB12 = 0
countC12 = 0
countD12 = 0
countE12 = 0

for i in range(2002, 2018):
    pageA = requests.get("https://artofproblemsolving.com/wiki/index.php?title=" + str(i) + "_AMC_12A_Answer_Key")
    pageB = requests.get("https://artofproblemsolving.com/wiki/index.php?title=" + str(i) + "_AMC_12B_Answer_Key")
    treeA = html.fromstring(pageA.content)
    treeB = html.fromstring(pageB.content)
    results = treeA.xpath('//li/text()') + treeB.xpath('//li/text()') # arrays
    for item in results:
        if item.strip().split()[0] == 'A':
            countA12 += 1
        elif item.strip().split()[0] == 'B':
            countB12 += 1
        elif item.strip().split()[0] == 'C':
            countC12 += 1
        elif item.strip().split()[0] == 'D':
            countD12 += 1
        elif item.strip().split()[0] == 'E': # precautionary
            countE12 += 1

freq12 = {"A": countA12, "B": countB12, "C": countC12, "D": countD12, "E": countE12}
total12 = countA12 + countB12 + countC12 + countD12 + countE12

# the frequency of AMC 10 answers from 2002 - 2017

countA10 = 0
countB10 = 0
countC10 = 0
countD10 = 0
countE10 = 0

for i in range(2002, 2018):
    treeA10 = html.fromstring(requests.get("https://artofproblemsolving.com/wiki/index.php?title=" + str(i) + "_AMC_10A_Answer_Key").content)
    treeB10 = html.fromstring(requests.get("https://artofproblemsolving.com/wiki/index.php?title=" + str(i) + "_AMC_10B_Answer_Key").content)
    results10 = treeA10.xpath('//li/text()') + treeB10.xpath('//li/text()')
    for item in results10:
        if item.strip().split()[0] == 'A':
            countA10 += 1
        elif item.strip().split()[0] == 'B':
            countB10 += 1
        elif item.strip().split()[0] == 'C':
            countC10 += 1
        elif item.strip().split()[0] == 'D':
            countD10 += 1
        elif item.strip().split()[0] == 'E':
            countE10 += 1

freq10 = {"A": countA10, "B": countB10, "C": countC10, "D": countD10, "E": countE10}
total10 = countA10 + countB10 + countC10 + countD10 + countE10

# writes the frequencies to a text file

result = open('result.txt', 'w')
result.write('*** AMC 12 ***')
for key in freq12:
    result.write("\n" + key + ":" + str(freq12[key]) + "\t" + str(round(100 * freq12[key]/total12, 2)) + "%" + "\n")
result.write('\n*** AMC 10 ***')
for key in freq10:
    result.write("\n" + key + ":" + str(freq10[key]) + "\t" + str(round(100 * freq10[key]/total10, 2)) + "%" + "\n")
result.write('\n*** Combined ***')
for key in freq12:
    result.write("\n" + key + ":" + str(freq12[key] + freq10[key]) + "\t" + str(round(100 * (freq12[key] + freq10[key])/(total12 + total10), 2)) + "%" + "\n")
result.close()