# coding =utf-8

import os

jscode = '<script src="http://127.0.0.1:8000/vconsole.min.js"></script> <script scr="http://127.0.0.1:8000/jquery.js"></script> <script> var vConsole = new VConsole(); </script>'


def selectAllfiles(path):

    file_list = os.listdir(path)

    for file in file_list:

		cur_path = os.path.join(path, file)

		if os.path.isdir(cur_path):
			selectAllfiles(cur_path)
		else:
			if cur_path[cur_path.rfind(".")+1:]=='html':
				print(cur_path)
				str = jscode
				keyword='</style>'
				file = open(cur_path,'r')
				content = file.read()
				post = content.find(keyword)
				if post != -1:
					content = content[:post+len(keyword)]+str+content[post+len(keyword):]
					file = open(cur_path,'w')
					file.write(content)
				file.close()

selectAllfiles('data')


