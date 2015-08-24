#coding=utf-8
sys.path.append(r"E:\Github\qihooPaySikuliAuto\setting\\")
sys.path.append(r"E:\Github\qihooPaySikuliAuto\lib\\")
from setInfo import qihooSetting
from constant import qihooConstant
from qihooCommLib import qihooCommLib

def myBankcard():
	click("sanDian.png")
	click("woDeYinHangKa.png")
	wait(2)
	click("zhaoShangYinHang.png")
	wait(2)
	click("queRenJieBang.png")
	
def main():
	#增加配置信息
	#qihooSetting.init(Settings,Debug)
	
	#生成公共类库对象
	commlib=qihooCommLib()
	
	#用于生成screen的相关数据信息
	screen=Screen()
	rec=screen.getBounds()
	region=Region(rec)
	
	myBankcard()
    #报告文件写入
	commlib.writefile(qihooConstant.TAG+qihooConstant.MY_BANKCARD_RESULT,qihooConstant.MY_BANKCARD_RESULT_PATH)
	
#program begin

if __name__=='__main__':
	main()
