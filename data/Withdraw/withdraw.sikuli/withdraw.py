#coding=utf-8
#sys.path.append(r"E:\data\SikuliLib")
sys.path.append(r"E:\Github\qihooPaySikuliAuto\setting\\")
sys.path.append(r"E:\Github\qihooPaySikuliAuto\lib\\")
from setInfo import qihooSetting
from constant import qihooConstant
from qihooCommLib import qihooCommLib


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
'''  
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
'''
	
def main():
	#增加配置信息
	qihooSetting.init(Settings,Debug)
	
	#生成公共类库对象
	commlib=qihooCommLib()
	
	#用于生成screen的相关数据信息
	screen=Screen()
	rec=screen.getBounds()
	region=Region(rec)
	
	#截图用于报告输出
	flag=commlib.screenShots(screen,region,"shouYe.png",r"E:\Github\qihooPaySikuliAuto\data\Withdraw\result\begin.png")
	if(flag==1):
		print "find Failed!"
	withdraw()
	wait(5)
	commlib.screenShots(screen,region,"shouYe.png",r"E:\Github\qihooPaySikuliAuto\data\Withdraw\result\end.png");
	
    #报告文件写入
	commlib.writefile(qihooConstant.TAG+qihooConstant.WITHDRAW_RESULT)
	
#program begin

if __name__=='__main__':
	main()



