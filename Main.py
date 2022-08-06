
def NewLine(linea):
   partes = linea.split("'")
   return '                exec sp_ArchiveSQL_Signed ' + "'" + (partes[1]) + "'" + ' , @OpType\n'


f = open('C:/SANTI/triggers.txt')

f1 = open('C:/SANTI/output.txt', 'w')

for line in f.readlines():

     doIHaveToCopyTheLine = True
     if 'ALTER TABLE' in line or 'sp_executesql' in line:
          doIHaveToCopyTheLine=False
     if 'sp_ArchiveSQL' in line:
        line = NewLine(line)
     if doIHaveToCopyTheLine:
        f1.write(line)

f1.close()
f.close()

