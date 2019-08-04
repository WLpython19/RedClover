#this code is to prepare bed file for checking SNPs
import glob
def write_lists_to_file(lists, filename):
    OutFile = open(filename,"w")
    OutFile.writelines("\n".join(lists))
    OutFile.close() 
    return filename
    
def prepare_bed_file(SNP_location_file):
    bed_collection=[]
    bed_file_name=SNP_location_file[:-4]+"_bed.txt"
    for line in open(SNP_location_file):
        line=line.strip("\r")
        line=line.strip("\n")
        line_ele=line.split("\t")
        key_info=line_ele[0].split("_")
        chrom='_'.join(key_info[:-2])
        start=int(key_info[-2])-300
        end=int(key_info[-2])+300
        name='_'.join(key_info)
        if start<0:
            bed_collection.append(chrom+"\t"+"0"+"\t"+str(end)+"\t"+name)
        if end<0:
            bed_collection.append(chrom+"\t"+str(start)+"\t"+"0"+"\t"+name)
        if start>0 and end>0:
            bed_collection.append(chrom+"\t"+str(start)+"\t"+str(end)+"\t"+name)        
#   header="chrom"+"\t"+"chromStart"+"\t"+"chromEnd"+"\t"+"name"
#   bed_collection.insert(0, header)
    write_lists_to_file(bed_collection, bed_file_name)
    return "finished this one:",SNP_location_file
