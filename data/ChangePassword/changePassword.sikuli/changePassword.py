#coding=utf-8
sys.path.append(r"E:\Github\qihooPaySikuliAuto\setting\\")
sys.path.append(r"E:\Github\qihooPaySikuliAuto\lib\\")
from setInfo import qihooSetting
from constant import qihooConstant
from qihooCommLib import qihooCommLib

def inputPassword(type):
	'''
	* 使用type来判断是需要输入原密码还是修改后的密码
	* 当type为0的时候则输入原密码，当type为1的时候则
	* 输入新密码
	'''
	if type==True:
		click("miMa1.png")
		click("miMa4.png")
		click("miMa7.png")
		click("miMa2.png")
		click("miMa5.png")
		click("miMa8.png")
		
	elif type==False:
		click("miMa1.png")
		click("miMa4.png")
		click("miMa7.png")
		click("miMa3.png")
		click("miMa6.png")
		click("miMa9.png")

def changePassword(type,screen,region,commlib):
	click("sanDian.png")
	click("miMaGuanli.png")
	click("xiuGaiZhiFuMiMa.png")
	
	'''
	* 原密码为147258，将其改为147369，
	* 在改过以后，为了后续的测试，再将其改回来
	* 密码的输入也可以转换为for循环输入
	'''
	
	#验证旧的手机密码
	inputPassword(type)
	wait(1)
	
	#设置新的手机密码
	inputPassword(not type)
	wait(2)
	inputPassword(not type)
	wait(2)
	click("xiaYiBu.png")
	wait(5)
	
	resultPic=""
	if type==True:
		resultPic=r"result1.png"
	elif type==False:
		resultPic=r"result2.png"
	commlib.screenShots(screen,region,"miMaGuanLiYe.png",qihooConstant.CHANGE_PASSWORD_RESULT_PATH+resultPic)
	wait(1)
	click("fanHui.png")
	

	
def main():
	#增加配置信息
	#qihooSetting.init(Settings,Debug)
	
	#生成公共类库对象
	commlib=qihooCommLib()
	
	#用于生成screen的相关数据信息
	screen=Screen()
	rec=screen.getBounds()
	region=Region(rec)
	
	#截图用于报告输出
	changePassword(True,Screen,Region,commlib)
    #报告文件写入
	commlib.writefile(qihooConstant.TAG+qihooConstant.CHANGE_PASSWORD_RESULT,qihooConstant.CHANGE_PASSWORD_RESULT_PATH)
	
#program begin

if __name__=='__main__':
	main()
