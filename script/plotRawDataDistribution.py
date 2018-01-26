import matplotlib.pyplot as plt
import gzip
import sys
import time
import re
import argparse

def get_args():
    """
    Function for getting the commandline arguments
    """
    
    if len( sys.argv) ==1: sys.argv.append('--help')
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-r',"--reads-file", help="barcode reads file/fwd read/first read/read one (must be gzipped fastq format)",metavar='<file>',required=True)
    parser.add_argument('-b',"--barcode-file", help="ID file with barcodes and positions",metavar='<file>',required=True)
    parser.add_argument('-i',"--img-file", help="image file name (pdf)",required=True,metavar='<file>')
    parser.add_argument('-s',"--stop-after", help="stop after this many reads",required=False,metavar='<int>',default=0,type=int)
    parser.add_argument('-p',"--plot-every", help="print plot to pdf after this many reads",required=False,metavar='<int>',default=100000,type=int)
    parser.add_argument('-v',"--verbose", help="print more stuff to stderr",required=False,default=False,action="store_true")

    
    _args = parser.parse_args()    
    if _args.verbose: sys.stderr.write( 'LOGMSG: Arguments from commandline now in memory.\n' )
    
    return _args

def thousandString(string):
    """
    takes a number and returns it formatted as a string with a white space every third number
    """
    if type(string) == type(None): return 'NA'
    if type(string) != str: string = str(int(round(float(string),0)))
    outstring = ''
    for i in range(len(string)):
        outstring += string[-(i+1)]
        if (i+1)%3 == 0: outstring += '.'
    if outstring[-1] == '.':outstring=outstring[:-1]
    return outstring[::-1]

def plot( data, args, counter ):
    plot_x = []
    plot_y = []
    plot_c = []
    plot_x_0 = []
    plot_y_0 = []
    plot_c_0 = []
    for x_,ys in data.iteritems():
        for y_, c_ in ys.iteritems():
            if c_ != 0:
                plot_x.append(x_)
                plot_y.append(y_)
                plot_c.append(c_)
            else:
                plot_x_0.append(x_)
                plot_y_0.append(y_)
                plot_c_0.append(c_)

    junk = plt.title(str(round(counter/4000000.0,1))+'Mreads')
    junk = plt.scatter(plot_x, plot_y, c=plot_c, cmap='PuRd')#, cmap='PuBu_r')
    ax = plt.gca()
    ax.set_ylim(ax.get_ylim()[::-1])            
    junk = plt.colorbar()
    junk = plt.savefig(args.img_file, format='pdf')
    junk = plt.close()

def main():
    
    args = get_args()
    
    bcs_file = open(args.barcode_file)
    bcs = {line.split()[0]:(int(line.split()[1]),int(line.split()[2])) for line in bcs_file}
    reads_file = gzip.open(args.reads_file)
    data = { x:{} for x in range(35) }
    for x in range(35): data[x] = { y:0 for y in range(35) }
    
    counter = 0
    bc_perfect = 0
    start_time = time.time()
    for line in reads_file:
        if re.match('[AGTCN]+',line.rstrip()):
            try:
                x,y = bcs[line[:18]]
                data[x][y] += 1
                bc_perfect += 1
            except KeyError: pass
        counter += 1
        if ((args.stop_after and counter/4 == args.stop_after) or counter%(4*args.plot_every) == 0) and counter != 0:
            sys.stderr.write('#Progress: '+thousandString(counter/4)+' reads, '+str(round(100*float(bc_perfect)/(counter/4),2))+'% perfect barcodes, '+str(round((counter/4.0)/(time.time()-start_time),2))+' reads/second on average.\n')
            plot(data,args,counter)
        if args.stop_after and counter/4 == args.stop_after: break

if __name__ == '__main__': main()
