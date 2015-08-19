import shutil
#coding=utf-8
#sys.path.append(r"E:\data\SikuliLib")
#from screenShot import screenShot

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

	
def main():
	flag=screenShots("shouYe.png",r"E:\Github\qihooPaySikuliAuto\data\Recharge\result\begin.png")
	if(flag==1):
		print "find Failed!"
	pay()
	wait(5)
	screenShots("shouYe.png",r"E:\Github\qihooPaySikuliAuto\data\Recharge\result\end.png");
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



