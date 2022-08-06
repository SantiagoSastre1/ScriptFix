linea = "exec sp_ArchiveSQL 'BatchProcess', @OpType, @sql output"

pos = linea.find("'")
linea = linea[pos:]


print(linea)

pos = linea.find("',")+1

print(pos)

linea = linea[:pos]

print(linea)

print("exec sp_ArchiveSQL_Signed "+(linea)+" , @OpType")
