'''
* 本文件主要用于一些常用的函数，将其作为方法进行管理，调用的时候使用类方法
* @author: wangyukun
* @email : wangyukun-xy@360.cn airfer@126.com
'''
import shutil

class qihooCommLib:
	def screenShots(self,screen,region,imag,desPath):
		'''
		try:
			math=region.find(imag)
			filename=screen.capture(math)
			#print filename 
			cpFile(filename,desPath)
			return 0
		except FindFailed:
			print "Do not find the target picture!"
			return 1
		'''	
		#由于暂不支持外模块调用screen、region等对象
		math=region.find(imag)
		filename=screen.capture(math)
		#print filename 
		self.cpFile(filename,desPath)
		return 0

	def cpFile(self,srcPath,destPath):
		shutil.copyfile(srcPath,destPath)
	
	def writefile(self,info,path):
		filename=path+r"Result_Info_Report.txt"
		file=open(filename,'w+')
		file.write(info)
		file.close()
		