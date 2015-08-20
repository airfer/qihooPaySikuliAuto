
#coding=utf-8
#sys.path.append(r"E:\data\SikuliLib")
sys.path.append(r"E:\Github\qihooPaySikuliAuto\setting\\")
sys.path.append(r"E:\Github\qihooPaySikuliAuto\lib\\")
from setInfo import qihooSetting
from constant import qihooConstant
from qihooCommLib import qihooCommLib

def pay():
    click("chongZhi.png")
    click("jinE.png")
    wait(3)

    for i in range(2):
        click("money.png")

    click("chongZhi2.png")
    wait(3)
    '''点击相关的测试图标'''
    click("chongZhi2.png")
    wait(5)
    click("chongZhi3.png")
    wait(2)
    type("jiaoYanMa.png","1234")
    click("queRenChongZhi.png")
    wait(10)    
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
	filename=r"E:\Github\qihooPaySikuliAuto\data\Recharge\result\Result_Info_Report.txt"
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
	flag=commlib.screenShots(screen,region,"shouYe.png",r"E:\Github\qihooPaySikuliAuto\data\Recharge\result\begin.png")
	if(flag==1):
		print "find Failed!"
	pay()
	wait(5)
	commlib.screenShots(screen,region,"shouYe.png",r"E:\Github\qihooPaySikuliAuto\data\Recharge\result\end.png");
	
    #报告文件写入
	commlib.writefile(qihooConstant.TAG+qihooConstant.RECHARGE_RESULT)
	
#program begin

if __name__=='__main__':
	main()



