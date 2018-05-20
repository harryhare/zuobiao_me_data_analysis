import csv
import codecs
import matplotlib.pyplot as plt

Debug=0
DebugLine=10
start_year = 1940
end_year = 2000

def init():
	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus'] = False

def plot_num(x_index):
	file=open('2014data.csv','r',encoding='UTF-8')
	reader=csv.reader(file)
	m={}
	line_num=0
	xtitle="x"
	ytitle="填写问卷的人数，按出生时间的统计"
	for line in reader:
		if(line_num==0):
			line_num+=1
			xtitle=line[x_index]
			continue
		try:
			born_year=line[x_index]
			born_year=int(born_year)
		except Exception:
			continue
		if born_year not in m.keys():
			m[born_year]=0
		m[born_year]+=1
		line_num+=1
		if(Debug and line_num>DebugLine):
			print(m)
			break
	during_year=end_year-start_year
	c=[0]*during_year
	for y in range(start_year,end_year):
		if(y in m.keys()):
			c[y-start_year]=m[y]
	plt.bar(range(start_year, end_year), c, 0.5)
	plt.xlabel(xtitle)
	plt.ylabel("人数")
	plt.title(ytitle)
	#plt.axis([-1,11,0,7])
	plt.savefig("people_num",dpi=600)#plt.savefig()将输出图形存储为文件，默认为png格式，可以通过dpi修改输出质量
	if(Debug):
		plt.show()

def plot(x_index,y_index):
	plt.figure(figsize=(7, 5))#图片属性设置，图片大小
	rect=[0.1,0.15,0.7,0.7]
	subplt=plt.axes(rect)#此处设置柱状通在图片中的位置
	file=open('2014data.csv','r',encoding='UTF-8')
	#file=codecs.open('E:\\git\\my\\zuobiao_analysis\\2014data.csv','rb','utf-8')
	reader=csv.reader(file)
	m={}
	line_num=0
	ans_map={"强烈同意":0,"同意":1,"反对":2,"强烈反对":3}
	ans_map_r={0:"强烈同意",1:"同意",2:"反对",3:"强烈反对",4:"其他"}
	color_map_r={0:'#ff0000',1:'#eeee00',2:'#00eeee',3:'#0000ff',4:'#000000'}
	xtitle="x"
	ytitle="y"
	for line in reader:
		if(line_num==0):
			line_num+=1
			xtitle=line[x_index]
			ytitle=line[y_index]
			continue
		#print(line[3],line[54])
		try:
			born_year=line[x_index]
			born_year=int(born_year)
		except Exception:
			#print(line[54])
			continue
		ans=line[y_index]
		if(born_year not in m.keys()):
			m[born_year]=[0]*4
		if(ans not in ans_map.keys()):
			print("error:"+ans)
			continue
		m[born_year][ans_map[ans]]+=1
		line_num+=1
		if(Debug and line_num>DebugLine):
			#print(m)
			break
	start_year=1940
	end_year=2000
	during_year=end_year-start_year
	c=[1]*during_year
	plt.bar(range(start_year, end_year), c, 0.5, color=color_map_r[0],label=ans_map_r[0])
	for ans in range(4):
		for y in range(start_year,end_year):
			if y not in m.keys():
				continue
			if(sum(m[y])==0):
				continue
			c[y-start_year]-=m[y][ans]*1.0/sum(m[y])
		plt.bar(range(start_year,end_year),c,0.5,color=color_map_r[ans+1],label=ans_map_r[ans+1])
	plt.xlabel(xtitle)
	plt.ylabel("百分比")
	plt.title(ytitle)
	plt.legend( bbox_to_anchor=(1,0.7))
	#plt.axis([-1,11,0,7])
	plt.savefig('pic'+str(y_index),dpi=600)#plt.savefig()将输出图形存储为文件，默认为png格式，可以通过dpi修改输出质量
	if(Debug):
		plt.show()


def test():
	plt.plot([2,3,4,5,1,6])
	plt.ylabel("Grade")
	plt.ylabel("number")
	plt.axis([-1,11,0,7])
	plt.savefig('test',dpi=600)#plt.savefig()将输出图形存储为文件，默认为png格式，可以通过dpi修改输出质量
	plt.show()


if __name__=="__main__":
	# for i in range(3,53):
	# 	plot(54,i)
	init()
	plot_num(54)