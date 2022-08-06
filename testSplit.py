
def NewLine(line):
   partes = line.split("'")
   return 'exec sp_ArchiveSQL_Signed ' + "'" + (partes[1]) + "'" + ' , @OpType'



print(NewLine("exec sp_ArchiveSQL 'Entity', @OpType, @sql output"))

