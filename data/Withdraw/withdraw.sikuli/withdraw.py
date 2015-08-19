import shutil
#coding=utf-8
#sys.path.append(r"E:\data\SikuliLib")
#from screenShot import screenShot

def withdraw():
	click("tiXian.png")
	wait(5)
	'''
	* 输入密码，密码为147258
	* 密码的输入也可以转换为for循环输入
	'''
	click("miMa1.png")
	click("miMa4.png")
	click("miMa7.png")
	click("miMa2.png")
	click("miMa5.png")
	click("miMa8.png")
	
	wait(2)
	# 提现也同样提11元，当然并非一定要如此
	click("jinE.png")
	wait(2)
	
	for num in range(2):
		click("miMa1.png")
	wait(2)
	click("xiaYiBu.png")
	#确定发生了点击，但是第一次点击导致键盘退回
	wait(1)
	click("xiaYiBu.png")
	wait(3)
	'''点击相关的测试图标'''
	click("wanCheng.png")
  
def screenShots(imag,desPath):
	screen=Screen()
	rec=screen.getBounds()
	region=Region(rec)
	try:
		math=region.find(imag)
		filename=screen.capture(math)
		#print filename 
		cpFile(filename,desPath)
		return 0
	except FindFailed:
		print "Do not find the target picture!"
		return 1


def cpFile(srcPath,destPath):
	shutil.copyfile(srcPath,destPath)
	
def writefile(info):
	filename=r"E:\Github\qihooPaySikuliAuto\data\Withdraw\result\Result_Info_Report.txt"
	file=open(filename,'w+')
	file.write(info)
	file.close()

	
def main():
	flag=screenShots("shouYe.png",r"E:\Github\qihooPaySikuliAuto\data\Withdraw\result\begin.png")
	if(flag==1):
		print "find Failed!"
	withdraw()
	wait(5)
	screenShots("shouYe.png",r"E:\Github\qihooPaySikuliAuto\data\Withdraw\result\end.png");
	tag="""
	------------------------------------------------------------------------
	* The testting framwork was develped based on sikuli.Now it is used for 
	* qihoo360 pay auto testting.The information of author can be found as 
	* following.
	* @author Airong's home wangyukun
	* @email wangyukkun-xy@360.cn
	------------------------------------------------------------------------
	"""
	info="""
	1、The amount of recharge is 11 yuan
	2、The begin.png in the result folder is the init state of the app
	3、The end.png in the result folder is the final state of the app

    result check:
		if difference of cash balance betweent the two picture is 11yuan,the 
		result indicates success,or fail!
	"""
	writefile(tag+info)
#program begin

if __name__=='__main__':
	main()



