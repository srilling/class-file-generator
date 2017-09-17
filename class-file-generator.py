import sys


def generate_header_file(class_name):
	filename = class_name + '.h'
	
	file = open(filename, 'w')
	
	code = ''
	include_guard = class_name.upper() + '_H'
	code += '#ifndef ' + include_guard + '\n'	#ifndef CLASS_NAME_H
	code += '#define ' + include_guard + '\n'	#define CLASS_NAME_H
	code += '\n\n'
	
	code += 'class ' + class_name + '{' + '\n\n'
	
	code += '\t//------------CONSTRUCTORS & DESTRUCTOR-----------------\n'
	code += '\tpublic:\n'
	code += '\t\t' + class_name + '(void);\n' 
	code += '\t\t~' + class_name + '(void);\n\n'
	
	code += '\t//------------MEMBER VARIABLES--------------------------\n'
	code += '\tprivate:\n'
	
	code += '\t//------------MEMBER FUNCTIONS--------------------------\n'
	code += '\tpublic:\n'
	
	code += '};\n\n'
	
	
	code += '#endif //' + include_guard	+ '\n'		#endif //CLASS_NAME_H
	
	
	file.write(code)
	file.close()
	

def generate_source_file(class_name):
	filename = class_name + '.cpp'
	
	file = open(filename, 'w')
	
	code = ''
	code += '#include \"' + class_name + '.h\"\n\n\n'
	
	code += class_name + '::' + class_name + '(void){\n'	#CLASS::CLASS(void){
	code += '}\n\n'
	
	code += class_name + '::~' + class_name + '(void){\n'	#CLASS::CLASS(void){
	code += '}\n\n'
	
	file.write(code)
	file.close()
	


print '* * * class file generator mk 0 * * *'

class_name = ''

if len(sys.argv) == 2:
	class_name = sys.argv[1]
	
else:
	print 'usage: python class-file-generator.py <class name>'
	exit(666)
	
generate_header_file(class_name)
generate_source_file(class_name)
	

