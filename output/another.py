filename = 'C:/Users/Uhini Mukherjee/Desktop/goim/output/twitter_combined_WC_maxdegree_15_50_1487723611282_1682961489163.log'

fp = open(filename,'r')
outputFileName=filename[:45]+"output_graph/"+filename[45:-3]
data = []
write = open(outputFileName+"txt", 'a')
write.write("\n")
line = fp.readline()
while len(line) > 0:
    line = line.split("[")[1][:-2]
    # print(line)
    write.write(line+"\n")
    line = fp.readline()

write.close()

