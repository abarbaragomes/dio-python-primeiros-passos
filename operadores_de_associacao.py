frutas = ['limao', 'uva']
print('laranja' in frutas)

frutas = ['limao', 'uva', 'laranja']
print('laranja' in frutas)

frutas = ['limao', 'uva', 'laranja']
print('UVA' in frutas) # Resulta em False por ser CASE SENSITIVE

frutas = ['limao', 'uva', 'laranja']
print('limao' not in frutas)

curso = 'Curso de Python'
print('Python' in curso)

curso = 'Curso de Python'
print('python' in curso) # Novamente resulta em False por ser CASE SENSITIVE