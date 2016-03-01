def read_grammar(file_name):


  #each production is a key value pair
  fp = open(file_name,'r')

  grammar_productions_list =[]

  #reading eachLine in the file
  for eachLine in fp:
    grammar_productions_list.append(eachLine.strip())

  return grammar_productions_list

def read_grammar_asDict(filename):

  grammar_list = read_grammar(filename)   
  grammar={}
  for eachElement in grammar_list:
    eachElement = eachElement.replace(" ","")
    production = eachElement.split("->")
    if grammar.has_key(production[0]):
        grammar[production[0]].append(production[1])
    else:
        grammar[production[0]] = [production[1]]

  return grammar

if __name__ == '__main__':

  user_input = raw_input('Enter the file name: \n')
  output =read_grammar(user_input)
  print output

