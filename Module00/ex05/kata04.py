# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

print("module_"+str(kata[0]).zfill(2)+", ex_"+str(kata[1]).zfill(2)+" : ", end="")
format_float = "{:.2f}".format(kata[2])
print(str(format_float)+", ",end='')
scientific_notation="{:.2e}".format(kata[3])
print(str(scientific_notation)+", ",end='')
scientific_notation="{:.2e}".format(kata[4])
print(scientific_notation)