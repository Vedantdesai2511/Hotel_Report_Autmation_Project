# import codecs

file = open('final_output.html','r')
a = file.read()

# file = codecs.open("final_output.html", "r", "utf-8")
# a = file.read()

f = open('final_output.html','w')

message = """<style>
th {
  font-size: 20px;
}

td {
  font-size: 30px;
}
</style>

""" + a

# print(f.read())

f.write(message)
f.close()
