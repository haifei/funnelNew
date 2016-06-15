# funnelNew
漏斗模型——pyspark

提交命令：  pyspark   start.py   -d 20150717 --py-files funnelNew.zip  


读取hdfs数据依据规则，进行漏斗模型分析


 漏斗模型： 描述的是用户浏览行为的相互关联的先后顺序
  比如：用户先访问A再通过A中的连接跳转到B,再从B访问C =========>   简化：  A--->B---->c
          这里定义的分析的漏斗模型就是 从A到B再到C,  产生的PV,UV...指标
   
