#!/usr/bin/env python

# Copyright 2015.
#   Michael A. DeJesus, Chaitra Ambadipudi, and  Thomas R. Ioerger.
#
#
#    This file is part of TRANSIT.
#
#    TRANSIT is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#
#    TRANSIT is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with TRANSIT.  If not, see <http://www.gnu.org/licenses/>.


import glob,os,sys,time,math
import sys, re, shutil
import platform
import gzip

if len(sys.argv)==1:
 import wx, wx.lib.filebrowsebutton
 class MyForm(wx.Frame):
 
    def __init__(self,vars):
        self.vars = vars
        initialize_globals(self.vars)

        wx.Frame.__init__(self, None, wx.ID_ANY, "Tn-Seq PreProcessor") # v%s" % vars.version)
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        #panel.SetFont(wx.Font(14,wx.DECORATIVE,wx.NORMAL,wx.NORMAL,False,u'times'))
        # panel.SetFont(wx.Font(14,wx.DECORATIVE,wx.NORMAL,wx.NORMAL,False,u'fixed'))
        #panel.SetFont(wx.Font(14,wx.DECORATIVE,wx.NORMAL,wx.BOLD,False,u'courier'))

        sizer = wx.BoxSizer(wx.VERTICAL)

        self.list_ctrl = None    
        self.InitMenu()
        self.InitFiles(panel,sizer)

        buttonrow = wx.BoxSizer(wx.HORIZONTAL)

        btn = wx.Button(panel, label="Start")
        btn.Bind(wx.EVT_BUTTON, self.map_reads)
        buttonrow.Add(btn,0,0,0,10)

        btn = wx.Button(panel, label="Quit")
        btn.Bind(wx.EVT_BUTTON, self.OnQuit)
        buttonrow.Add(btn,0,0,0,10)
        sizer.Add(buttonrow,0,0,0)

        self.InitList(panel,sizer)

        panel.SetSizer(sizer)
        # self.SetSize((1305, 700))
        self.SetSize((900, 700))
        #self.SetTitle('Simple menu')
        self.Centre()
        #self.Show(True)

        self.pid = None

    '''
    def initialize_globals(self):
      vars = self.vars
      vars.fq1,vars.fq2,vars.ref,vars.bwa,vars.base,vars.maxreads = "","","","","temp",-1
      read_config(vars)
    '''

    def InitFiles(self,panel,sizer):
        vars = self.vars
        sizer0 = wx.BoxSizer(wx.HORIZONTAL)
        label0 = wx.StaticText(panel, label='BWA executable:',size=(340,-1))
        sizer0.Add(label0,0,0,0)
        print os.path.dirname(vars.bwa)
        #self.picker0 = wx.FilePickerCtrl(panel, wx.ID_ANY,message="path to BWA",size=(400,30))#,path=os.path.abspath(vars.bwa))
        #self.picker0.SetDirName('/pacific/home/cambadipudi/chaitra/tpp/')
        self.picker0 = wx.lib.filebrowsebutton.FileBrowseButton(panel, id = wx.ID_ANY, size=(400,30), dialogTitle='Path to BWA', fileMode=wx.OPEN, fileMask='bwa*', startDirectory=os.path.dirname(vars.bwa), initialValue=vars.bwa, labelText='')
        sizer0.Add(self.picker0, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(sizer0,0,wx.EXPAND,0)

        sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        label3 = wx.StaticText(panel, label='Choose a reference genome (FASTA):',size=(340,-1))
        sizer3.Add(label3,0,0,0)
        #self.picker3 = wx.FilePickerCtrl(panel, wx.ID_ANY,message="Please select the reference genome", wildcard='*.fna;*.fasta;*.fa', size=(400,30),path=vars.ref)
        self.picker3 = wx.lib.filebrowsebutton.FileBrowseButton(panel, id=wx.ID_ANY, dialogTitle='Please select the reference genome', fileMode=wx.OPEN, fileMask='*.fna;*.fasta;*.fa', size=(400,30), startDirectory=os.path.dirname(vars.ref), initialValue=vars.ref, labelText='')
        sizer3.Add(self.picker3, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(sizer3,0,wx.EXPAND,0)
       
        
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        label1 = wx.StaticText(panel, label='Choose the Fastq file for read 1:',size=(340,-1))
        sizer1.Add(label1,0,0,0)
        # self.picker1 = wx.FilePickerCtrl(panel, wx.ID_ANY,message="Please select the .fastq file for read 1", wildcard='*.fastq;*.fq;*.reads;*.fasta;*.fa', size=(400,30),path=vars.fq1)
        self.picker1 = wx.lib.filebrowsebutton.FileBrowseButton(panel, id=wx.ID_ANY, dialogTitle='Please select the .fastq file for read 1', fileMode=wx.OPEN, fileMask='*.fastq;*.fq;*.reads;*.fasta;*.fa;*.fastq.gz', size=(400,30), startDirectory=os.path.dirname(vars.fq1), initialValue=vars.fq1, labelText='',changeCallback=self.OnChanged2)
        #self.picker1.OnChanged = self.OnChanged(self.picker1.GetValue(), self.base)
        #self.Bind(wx.EVT_TEXT, self.OnChanged, id=self.picker1.GetId())
        #self.picker1.Bind(wx.EVT_TEXT, self.OnChanged)
        sizer1.Add(self.picker1, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(sizer1,0,wx.EXPAND,0)
       
        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        label2 = wx.StaticText(panel, label='Choose the Fastq file for read 2:',size=(340,-1))
        sizer2.Add(label2,0,0,0)
        #self.picker2 = wx.FilePickerCtrl(panel, wx.ID_ANY,message="Please select the .fastq file for read 2", wildcard='*.fastq;*.fq;*.reads;*.fasta;*.fa', size=(400,30),path=vars.fq2)
        self.picker2 = wx.lib.filebrowsebutton.FileBrowseButton(panel, id=wx.ID_ANY, dialogTitle='Please select the .fastq file for read 2', fileMode=wx.OPEN, fileMask='*.fastq;*.fq;*.reads;*.fasta;*.fa;*.fastq.gz', size=(400,30), startDirectory=os.path.dirname(vars.fq2), initialValue=vars.fq2, labelText='', changeCallback=self.OnChanged2)
        sizer2.Add(self.picker2, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(sizer2,0,wx.EXPAND,0)

        sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        label4 = wx.StaticText(panel, label='Prefix to use for output filenames:',size=(350,-1))
        sizer4.Add(label4,0,0,0)
        self.base = wx.TextCtrl(panel,value=vars.base,size=(400,30))
        sizer4.Add(self.base, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(sizer4,0,wx.ALL,0)

        sizer7 = wx.BoxSizer(wx.HORIZONTAL)
        label7 = wx.StaticText(panel, label='Transposon used:',size=(350,-1))
        sizer7.Add(label7,0,0,0)
        self.transposon = wx.ComboBox(panel,choices=['Himar1','Tn5'],size=(400,30))
        self.transposon.SetStringSelection(vars.transposon)
        sizer7.Add(self.transposon, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(sizer7,0,wx.ALL,0)    

        sizer5 = wx.BoxSizer(wx.HORIZONTAL)
        label5 = wx.StaticText(panel, label='Max reads (leave blank to use all):',size=(350,-1))
        sizer5.Add(label5,0,0,0)
        self.maxreads = wx.TextCtrl(panel,size=(400,30))
        sizer5.Add(self.maxreads, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(sizer5,0,wx.ALL,0)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)
        label6 = wx.StaticText(panel, label='Mismatches allowed in Tn prefix:',size=(350,-1))
        sizer6.Add(label6,0,0,0)
        self.mismatches = wx.TextCtrl(panel,value=str(vars.mm1),size=(400,30))
        sizer6.Add(self.mismatches, proportion=1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(sizer6,0,wx.ALL,0)    

        #self.picker1.OnChanged = self.OnChanged(self.picker1.GetValue())


    def OnChanged(self, str_path):
        print "changed"
        value = os.path.basename(str_path).split('.')[0]
        if '_R1' in value or '_R2':
            value = value.split('_')[0]
        self.base.SetValue(value)

    def OnChanged2(self, event):
        value2 = os.path.basename(self.picker2.GetValue()).split('.')[0]
        value1 = os.path.basename(self.picker1.GetValue()).split('.')[0]
        value = os.path.commonprefix([value1, value2])
        self.base.SetValue(value)
        self.base.Refresh()

    def InitList(self,panel,sizer):
        self.list_ctrl = wx.ListCtrl(panel, size=(500,500), style=wx.LC_HRULES|wx.LC_VRULES|wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, 'Dataset (*.tn_stats)',width=300)
        self.list_ctrl.InsertColumn(1, 'total reads',wx.LIST_FORMAT_RIGHT,width=125)
        self.list_ctrl.InsertColumn(2, 'TGTTA prefix', wx.LIST_FORMAT_RIGHT,width=125)
        self.list_ctrl.InsertColumn(3, 'R1_mapped', wx.LIST_FORMAT_RIGHT,width=90)
        self.list_ctrl.InsertColumn(4, 'R2_mapped', wx.LIST_FORMAT_RIGHT,width=90)
        self.list_ctrl.InsertColumn(5, 'mapped\nreads', wx.LIST_FORMAT_RIGHT,width=90)
        self.list_ctrl.InsertColumn(6, 'template\ncount', wx.LIST_FORMAT_RIGHT,width=90)
        self.list_ctrl.InsertColumn(7, 'TAs hit', wx.LIST_FORMAT_RIGHT,width=90)
        self.list_ctrl.InsertColumn(8, 'insertion\ndensity',wx.LIST_FORMAT_RIGHT,width=90)
        self.list_ctrl.InsertColumn(9, 'NZmean', wx.LIST_FORMAT_RIGHT,width=90)
        self.list_ctrl.InsertColumn(10, 'maxcount', wx.LIST_FORMAT_RIGHT,width=90)
        self.list_ctrl.InsertColumn(11, 'primer', wx.LIST_FORMAT_RIGHT,width=90)
        self.list_ctrl.InsertColumn(12, 'vector',wx.LIST_FORMAT_RIGHT,width=90)
        #self.list_ctrl.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL))
        #btn = wx.Button(panel, label="Add Line")
        #btn.Bind(wx.EVT_BUTTON, self.add_line)
 
        sizer.Add(self.list_ctrl, 0, wx.ALL|wx.EXPAND, 10)
        #sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

    def InitMenu(self):    
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        #dataset_menuitem = fileMenu.Append(wx.ID_ANY, 'Add New Dataset', 'Analyze New Dataset')
        #self.Bind(wx.EVT_MENU, self.addNewDataset, dataset_menuitem)

        quit_menuitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        self.Bind(wx.EVT_MENU, self.OnQuit, quit_menuitem)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

    def addNewDataset(self, event):
      dlg = wx.FileDialog(
          self, message="Choose a file",
          defaultDir=".",
          defaultFile="",
          wildcard="*.wig",
          style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
          )
      if dlg.ShowModal() == wx.ID_OK:
          paths = dlg.GetPaths()
          for path in paths:
            print "analyzing dataset:",path
            analyze_dataset(path)
      dlg.Destroy()
      self.update_dataset_list()

    def update_dataset_list(self):
      if self.list_ctrl==None: return
      self.list_ctrl.DeleteAllItems()
      self.index = 0
      datasets = []
      for fname in glob.glob("*.tn_stats"):
        filedate = os.path.getmtime(fname)
        datasets.append((filedate,fname))
      datasets.sort(reverse=True)
      for (filedate,fname) in datasets:
        stats = self.read_stats_file(fname)
        
        vals = [stats.get("total_reads","?"),stats.get("TGTTA_reads","?"),stats.get("reads1_mapped", "?"),stats.get("reads2_mapped","?"),stats.get("mapped_reads","?"),stats.get("template_count","?"), stats.get("TAs_hit","?"), stats.get("density", "?"), stats.get("NZ_mean", "?"), stats.get("max_count", "?"), stats.get("primer_matches:","?"),stats.get("vector_matches:","?")]

        #dataset = "[%s] %s" % (time.strftime("%m/%d/%y",time.localtime(os.path.getmtime(fname))),fname[:fname.rfind('.')])
        dsname = "[%s] %s" % (time.strftime("%m/%d/%y",time.localtime(filedate)),fname[:fname.rfind('.')])
        self.add_data(dsname, vals)

    def read_stats_file(self,fname):
      stats = {}
      for line in open(fname):
        w = line.rstrip().split()
        val = ""
        if len(w)>2: val = w[2]
        stats[w[1]] = val
      return stats

    def add_data(self, dataset,vals):
        self.list_ctrl.InsertStringItem(self.index, dataset)
        for i in range(1, len(vals)+1):
            self.list_ctrl.SetStringItem(self.index, i, vals[i-1])
        self.index += 1

    def OnQuit(self, e):
        print "Quitting TPP.  Good bye."
        self.vars.action = "quit"
        self.Close()
        return 0

    def map_reads(self,event):
      # add bwa path, prefix
      # bwapath = self.picker0.GetPath()
      bwapath = self.picker0.GetValue()
      #fq1,fq2,ref,base,maxreads = self.picker1.GetPath(),self.picker2.GetPath(),self.picker3.GetPath(),self.base.GetValue(),self.maxreads.GetValue()
      fq1, fq2, ref, base, maxreads = self.picker1.GetValue(), self.picker2.GetValue(), self.picker3.GetValue(), self.base.GetValue(), self.maxreads.GetValue()

      mm1 = self.mismatches.GetValue()
      try: mm1 = int(mm1)
      except Exception: mm1 = 1

      self.vars.transposon = self.transposon.GetStringSelection()

      self.vars.bwa = bwapath
      self.vars.fq1 = fq1
      self.vars.fq2 = fq2
      self.vars.ref = ref
      self.vars.base = base  
      self.vars.mm1 = mm1
      if maxreads == '': self.vars.maxreads = -1
      else: self.vars.maxreads = int(maxreads)

      self.vars.action = "start"
      self.Close()
      return 0

# http://www.blog.pythonlibrary.org/2013/09/04/wxpython-how-to-update-a-progress-bar-from-a-thread/\

def analyze_dataset(wigfile):
  data = []
  TAs,ins,reads = 0,0,0
  for line in open(wigfile):
    if line[0]=='#': continue
    if line[:3]=='var': continue # variableStep
    w = line.rstrip().split()
    TAs += 1
    cnt = int(w[1])
    if cnt>1: ins += 1
    reads += cnt
    data.append((cnt,w[0]))

  output = open(wigfile+".stats","w")
  output.write("total TAs: %d, insertions: %d (%0.1f%%), total reads: %d\n" % (TAs,ins,100*(ins/float(TAs)),reads))
  output.write("mean read count per non-zero site: %0.1f\n" % (reads/float(ins)))
  output.write("5 highest counts:\n")
  data.sort(reverse=True)
  for cnt,coord in data[:5]:
    output.write("coord=%s, count=%s\n" % (coord,cnt))
  output.close()

#############################################################################

def fastq2reads(infile,outfile,maxreads):
  output = open(outfile,"w")
  cnt,tot = 0,0
  for line in open(infile):
    if cnt==0 and line[0]=='@':
        tot += 1
        if tot%1000000==0: message("%s reads processed" % tot)
    if maxreads > -1:
        if tot > maxreads:
            break
    if cnt==0: 
      h = line[1:] # strip off '@'
      #h = h.replace(' ','_')
      output.write(">%s" % h)
    if cnt==1: output.write(line)
    cnt = (cnt+1)%4
  output.close()

# the headers for each pair must be identical up to /1 and /2 at the ends
# if the variable character with the read number occurs in the middle, move it to the end

def fix_paired_headers_for_bwa(reads1,reads2):
  a = open(reads1)
  b = open(reads2)
  temp1 = "temp."+reads1
  temp2 = "temp."+reads2
  c = open(temp1,"w")
  d = open(temp2,"w")
  tot = 0
  try:
   while True:
    e = a.readline().rstrip()
    f = b.readline().rstrip()
    if len(e)<=2 or len(f)<=2: break
    if e[0]=='>':
      tot += 1
      if tot%1000000==0: message("%s reads processed" % tot)
      # find first position where there is a difference
      i,n = 0,len(e)
      if len(f)!=n: raise Exception('unexpected format of headers in .fastq files')
      while i<n and e[i]==f[i]: i += 1
      if i==n: raise Exception('unexpected format of headers in .fastq files')
      e = e.replace(' ','_')
      f = f.replace(' ','_')
      e = e.replace('/','_') # this was neceesary for bwa 0.7.10 but not 0.7.12
      f = f.replace('/','_')
      #if i<n-1:
      if e[i+1:]!=f[i+1:]: raise Exception('unexpected format of headers in .fastq files')
      e,f = e[:-1],f[:-1] # strip EOL
      # needed for bwa 0.7.12? which apparently trims off last 2 chars to make ids identical
      # "/[1|2]" are automatically trimmed, but not /3
      e = e[:i]+e[i+1:]
      f = f[:i]+f[i+1:]
    c.write(e+"\n")
    d.write(f+"\n")      
  except Exception as ex:
    a.close(); b.close(); c.close(); d.close()
    error(ex.args[0])
  a.close(); b.close(); c.close(); d.close()
  
  if(os.path.exists(reads1)): os.remove(reads1)
  if(os.path.exists(reads2)): os.remove(reads2)
  os.rename(temp1, reads1)
  os.rename(temp2, reads2)
  
  '''
  if platform.platform == 'win32':
	  os.system("move %s %s" % (temp1,reads1))
	  os.system("move %s %s" % (temp2,reads2))
  else:
	  os.system("mv %s %s"%(temp1, reads1))
	  os.system("mv %s %s" % (temp2, reads2))
  '''

def mmfind(G,n,H,m,max): # lengths; assume n>m
  for i in range(0,n-m):
    cnt = 0
    for k in range(m):
      if G[i+k]!=H[k]: cnt += 1
      if cnt>max: break
    if cnt<=max: return i
  return -1

def extract_staggered(infile,outfile,vars):
  Himar1 = "ACTTATCAGCCAACCTGTTA"
  Tn5 = "TAAGAGACAG"
  if vars.transposon=='Tn5': Tn = Tn5
  elif vars.transposon=='Himar1': Tn = Himar1
  lenTn = len(Tn)
  ADAPTER2 = "TACCACGACCA"
  lenADAP = len(ADAPTER2)

  #P,Q = 5,10 # 1-based inclusive positions to look for start of Tn prefix
  P,Q = 0,15

  vars.tot_tgtta = 0
  vars.truncated_reads = 0
  output = open(outfile,"w")
  tot = 0
  for line in open(infile):
    line = line.rstrip()
    if line[0]=='>': header = line; continue
    tot += 1
    if tot%1000000==0: message("%s reads processed" % tot)
    readlen = len(line)
    a = mmfind(line,readlen,Tn,lenTn,vars.mm1) # allow some mismatches
    b = mmfind(line,readlen,ADAPTER2,lenADAP,vars.mm1) # look for end of short frags
    if a>=P and a<=Q:
      gstart,gend = a+lenTn,readlen
      if b!=-1: gend = b; vars.truncated_reads += 1
      if gend-gstart<20: continue # too short
      output.write(header+"\n")
      output.write(line[gstart:gend]+"\n")
      vars.tot_tgtta += 1
  output.close()

def message(s):
  print "[tn_preprocess]",s
  sys.stdout.flush()

def get_id(line):
  a,b = line.find(":")+1,line.rfind("#")
  if b==-1: b = line.rfind("_")
  return line[a:b]

# select the reads from infile that have headers occuring in goodreads

def select_reads(goodreads,infile,outfile):
  hash = {}
  for line in open(goodreads):
    if line[0]=='>': 
      #id = line[line.find(":")+1:line.rfind("#")]
      id = get_id(line)
      hash[id] = 1

  output = open(outfile,"w")
  for line in open(infile):
    if line[0]=='>':
      header = line
      id = get_id(line)
    else:
      if hash.has_key(id):
        output.write(header)
        output.write(line)
  output.close()

def replace_ids(infile1,infile2,outfile):
  f = open(infile1)
  g = open(infile2)
  h = open(outfile,"w")

  while True:
    a = f.readline()
    b = g.readline()
    if len(a)<2: break
    if a[0]=='>': header = a
    else: 
      h.write(header)
      h.write(b)
  f.close()
  g.close()
  h.close()

# indexes i and j are 1-based and inclusive (could be -1)

def select_cycles(infile,i,j,outfile):
  output = open(outfile,"w")
  for line in open(infile):
    if line[0]=='>': header = line
    else:
      output.write(header)
      output.write(line[i-1:j]+"\n")
  output.close()

def read_genome(filename):
  s = ""
  for line in open(filename):
    if line[0]=='>': continue # skip fasta header
    else: s += line[:-1]
  return s

# convert to bistring (8 bits; bit 0 is low-order bit)
#
# Bit Description
# 0 0x1 template having multiple segments in sequencing
# 1 0x2 each segment properly aligned according to the aligner
# 2 0x4 segment unmapped
# 3 0x8 next segment in the template unmapped
# 4 0x10 SEQ being reverse complemented
# 5 0x20 SEQ of the next segment in the template being reversed
# 6 0x40 the first segment in the template
# 7 0x80 the last segment in the template
#
# code[6]=1 means read1
# code[4]=1 means reverse strand

def samcode(num): return bin(int(num))[2:].zfill(8)[::-1]

def template_counts(ref,sam,bcfile,vars):
  genome = read_genome(ref)
  barcodes = {}

  
  fil1 = open(bcfile)
  fil2 = open(sam)

  idx=1
  for line in fil1:
    if idx==1: break
    idx+=1

  idx=1
  for line in fil2:
    if idx==2: break
    idx+=1
  
  '''
  for line in open(bcfile):
    line = line.rstrip()
    if line[0]=='>': id = line[1:]
    else: barcodes[id] = line
  '''
  hits = {}
  vars.tot_tgtta,vars.mapped = 0,0
  vars.r1 = vars.r2 = 0

  #for line in open(sam):
  bcline=''
  for line in fil2:
    try:
      bcline = fil1.next().rstrip()
      if bcline[0] !='>': bc = bcline
    except StopIteration:
      pass
    if line[0]=='@': continue
    else:
      w = line.split('\t')
      code = samcode(w[1])
      if 'S' in w[5]: continue #elimate softclipped reads
      if code[6]=="1": # previously checked for for reads1's via w[1]<128 
        vars.tot_tgtta += 1 
        if code[2]=="0": vars.r1 += 1
      if code[7]=="1" and code[2]=="0": vars.r2 += 1
      # include "improperly mapped reads, which might just be short frags
      #if w[1]=="99" or w[1]=="83" or w[1]=="97" or w[1]=="81": 
      if code[6]=="1" and code[2]=="0" and code[3]=="0": # both reads mapped (proper or not)
        vars.mapped += 1
        readlen = len(w[9])
        pos,size = int(w[3]),int(w[8]) # note: size could be negative
        strand,delta = 'F',-2
        if code[4]=="1": strand,delta = 'R',readlen

        pos += delta
        #bc = barcodes[w[0]]
        if pos not in hits: hits[pos] = []
        hits[pos].append((strand,size,bc))

  sites = []
  for i in range(len(genome)-1):
    if genome[i:i+2]=="TA":
      pos = i+1
      h = hits.get(pos,[])
      f = filter(lambda x: x[0]=='F',h)
      r = filter(lambda x: x[0]=='R',h)
      h.sort()
      unique = {}
      for (strand,size,bc) in h:
        #print strand,bc,size
        s = "%s-%s-%s" % (strand,bc,size)
        unique[s] = 1
      u = unique.keys()
      uf = filter(lambda x: x[0]=='F',u)
      ur = filter(lambda x: x[0]=='R',u)
      data = [pos,len(f),len(uf),len(r),len(ur),len(f)+len(r),len(uf)+len(ur)]
      sites.append(data)

  return sites # (coord, Fwd_Rd_Ct, Fwd_Templ_Ct, Rev_Rd_Ct, Rev_Templ_Ct, Tot_Rd_Ct, Tot_Templ_Ct)

# pretend that all reads count as unique templates

def read_counts(ref,sam,vars):
  genome = read_genome(ref)
  hits = {}
  vars.tot_tgtta,vars.mapped = 0,0
  vars.r1 = vars.r2 = 0
  for line in open(sam):
    if line[0]=='@': continue
    else:
      w = line.split('\t')
      code,icode = samcode(w[1]),int(w[1])
      vars.tot_tgtta += 1 
      if icode==0 or icode==16: 
        vars.r1 += 1
        vars.mapped += 1
        readlen = len(w[9])
        pos = int(w[3])
        strand,delta = 'F',-2
        if code[4]=="1": strand,delta = 'R',readlen
        pos += delta
        if pos not in hits: hits[pos] = []
        hits[pos].append(strand)

  sites = []
  for i in range(len(genome)-1):
    if genome[i:i+2]=="TA" or vars.transposon=='Tn5':
      pos = i+1
      h = hits.get(pos,[])
      lenf,lenr = h.count('F'),h.count('R')
      data = [pos,lenf,lenf,lenr,lenr,lenf+lenr,lenf+lenr]
      sites.append(data)

  return sites # (coord, Fwd_Rd_Ct, Fwd_Templ_Ct, Rev_Rd_Ct, Rev_Templ_Ct, Tot_Rd_Ct, Tot_Templ_Ct)

def driver(vars):
  vars.reads1 = vars.base+".reads1"
  vars.reads2 = vars.base+".reads2"
  vars.tgtta1 = vars.base+".tgtta1"
  vars.tgtta2 = vars.base+".tgtta2"
  vars.barcodes1 = vars.base+".barcodes1"
  vars.barcodes2 = vars.base+".barcodes2"
  vars.genomic2 = vars.base+".genomic2"
  vars.sai1 = vars.base+".sai1"
  vars.sai2 = vars.base+".sai2"
  vars.sam = vars.base+".sam"
  vars.tc = vars.base+".counts"
  vars.wig = vars.base+".wig"
  vars.stats = vars.base+".tn_stats"

  extract_reads(vars)

  run_bwa(vars)

  generate_output(vars)

  message("Done.")

def uncompress(filename):
   outfil = open(filename[0:-3], "w+")
   for line in gzip.open(filename):
      outfil.write(line)
   return filename[0:-3]

def extract_reads(vars):
    message("extracting reads...")
    
    flag = ['','']
    for idx, name in enumerate([vars.fq1, vars.fq2]):
        if idx==1 and vars.single_end==True: continue
        fil = open(name)
        for line in fil:
            if line[0] == '>':
                flag[idx] = 'FASTA'
                break
            flag[idx] = 'FASTQ'
            break
        fil.close() 

    if vars.fq1.endswith('.gz'):
       vars.fq1 = uncompress(vars.fq1)
        
    if vars.fq2.endswith('.gz'):
       vars.fq2 = uncompress(vars.fq2)

    if(flag[0] == 'FASTQ'):
        message("fastq2reads: %s -> %s" % (vars.fq1,vars.reads1))
        fastq2reads(vars.fq1,vars.reads1,vars.maxreads)
    else:
        shutil.copyfile(vars.fq1, vars.reads1)

    if vars.single_end==True:
      message("assuming single-ended reads")
      message("creating %s" % vars.tgtta1)
      extract_staggered(vars.reads1,vars.tgtta1,vars)
      return 

    if(flag[1] == 'FASTQ'):  
        message("fastq2reads: %s -> %s" % (vars.fq2,vars.reads2))
        fastq2reads(vars.fq2,vars.reads2,vars.maxreads)
    else:
        shutil.copyfile(vars.fq2, vars.reads2)

    message("fixing headers of paired reads for bwa...")
    fix_paired_headers_for_bwa(vars.reads1,vars.reads2)

    message("extracting barcodes and genomic parts of reads...")

    message("creating %s" % vars.tgtta1)
    extract_staggered(vars.reads1,vars.tgtta1,vars)

    message("creating %s" % vars.tgtta2)
    select_reads(vars.tgtta1,vars.reads2,vars.tgtta2)
    #message("creating %s" % vars.barcodes2)
    #select_cycles(vars.tgtta2,22,30,vars.barcodes2)
    #message("creating %s" % vars.genomic2)
    #select_cycles(vars.tgtta2,43,-1,vars.genomic2)

    # instead of using select_cycles, do these both in one shot by looking for constant seqs
    message("creating %s" % vars.barcodes2)
    message("creating %s" % vars.genomic2)
    extract_barcodes(vars.tgtta2,vars.barcodes2,vars.genomic2)

    message("creating %s" % vars.barcodes1)
    replace_ids(vars.tgtta1,vars.barcodes2,vars.barcodes1)

#  pattern for read 2...
#    TAGTGGATGATGGCCGGTGGATTTGTG GTAATTACCA TGGTCGTGGTAT CCCAGCGCGACTTCTTCGGCGCACACACC TAACAGGTTGGCTGATAAGTCCCCG?AGAT AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGT
#    -----const1---------------- --barcode- ---const2--- ------genomic---------------- ------const3--------------------------------------------------------------
#    const suffix might appear if fragment is shorter than read length; if so, truncate
#    if genomic part is too short, just output at least 20bp of const so as not to mess up BWA
#    could the start of these be shifted slightly?

def extract_barcodes(fn_tgtta2,fn_barcodes2,fn_genomic2):
  const1 = "GATGGCCGGTGGATTTGTG"
  const2 = "TGGTCGTGGTAT"
  const3 = "TAACAGGTTGGCTGATAAG"
  nconst1,nconst2,nconst3 = len(const1),len(const2),len(const3)
  fl_barcodes2 = open(fn_barcodes2,"w")
  fl_genomic2 = open(fn_genomic2,"w")
  tot,DEBUG = 0,0
  for line in open(fn_tgtta2):
    line = line.rstrip()
    if line[0]=='>': header = line
    else:
      tot += 1
      if tot%1000000==0: message("%s reads processed" % tot)
      #a  = line.find(const1)
      #b  = line.find(const2)
      #c  = line.find(const3)
      a  = mmfind(line,len(line),const1,nconst1,vars.mm1)
      b  = mmfind(line,len(line),const2,nconst2,vars.mm1)
      c  = mmfind(line,len(line),const3,nconst3,vars.mm1)
      bstart,bend = a+nconst1,b
      gstart,gend = b+nconst2,len(line)
      if c!=-1 and c-gstart>20: gend = c
      if a==-1 or bend<bstart+5 or bend>bstart+15:
        # you can't just reject these, beacuse they are paired with R1
        # but setting the genomic part to the first 20 cycles should prevent it from mapping
        bstart,bend = 0,10
        gstart,gend = 0,20
        barcode,genomic = "XXXXXXXXXX","XXXXXXXXXX"
      else: barcode,genomic = line[bstart:bend],line[gstart:gend]
      if DEBUG==1:
        fl_barcodes2.write(header+"\n")
        fl_barcodes2.write(line+"\n")
        #fl_barcodes2.write((" "*bstart)+line[bstart:bend]+"\n")
        fl_barcodes2.write((" "*bstart)+barcode+"\n")
        fl_genomic2.write(header+"\n")
        fl_genomic2.write(line+"\n")
        #fl_genomic2.write((" "*gstart)+line[gstart:gend]+"\n")
        fl_genomic2.write((" "*gstart)+genomic+"\n")
      else:
        fl_barcodes2.write(header+"\n")
        #fl_barcodes2.write(line[bstart:bend]+"\n")
        fl_barcodes2.write(barcode+"\n")
        fl_genomic2.write(header+"\n")
        #fl_genomic2.write(line[gstart:gend]+"\n")
        fl_genomic2.write(genomic+"\n")
  fl_barcodes2.close()
  fl_genomic2.close()
  if DEBUG==1: sys.exit(0)

def run_bwa(vars):
    message("mapping reads using BWA...(this takes a couple of minutes)")

    if not os.path.exists(vars.ref+".amb"):
      cmd = vars.bwa+" index "+vars.ref
      message(cmd)
      os.system(cmd)

    cmd = "%s aln %s %s > %s" % (vars.bwa,vars.ref,vars.tgtta1,vars.sai1)
    message(cmd)
    os.system(cmd)

    if vars.single_end==True:
      cmd = "%s samse %s %s %s > %s" % (vars.bwa,vars.ref,vars.sai1,vars.tgtta1,vars.sam)
      message(cmd)
      os.system(cmd)

    else:
      cmd = "%s aln %s %s > %s" % (vars.bwa,vars.ref,vars.genomic2,vars.sai2)
      message(cmd)
      os.system(cmd)

      cmd = "%s sampe %s %s %s %s %s > %s" % (vars.bwa,vars.ref,vars.sai1,vars.sai2,vars.tgtta1,vars.genomic2,vars.sam)
      message(cmd)
      os.system(cmd)


def stats(vals):
  sum,ss = 0,0
  for x in vals: sum += x; ss += x*x
  N = float(len(vals))
  mean = sum/N
  var = ss/N-mean*mean
  stdev = math.sqrt(var)
  return mean,stdev

def corr(X,Y):
  muX,sdX = stats(X)
  muY,sdY = stats(Y)
  cX = [x-muX for x in X]
  cY = [y-muY for y in Y]
  s = sum([x*y for (x,y) in zip(cX,cY)])
  return s/(float(len(X))*sdX*sdY)

def get_read_length(filename):
   fil = open(filename)
   i = 0
   for line in fil:
      if i == 1: 
         print "reads1 line: " + line
         return len(line.strip())
      i+=1

def get_genomic_portion(filename):
   fil = open(filename)
   i = 0
   tot_len = 0.0
   n = 1
   for line in fil:
      if i%2 == 1:
         tot_len += len(line.strip())
         n += 1
      i+=1
   return tot_len/n


def generate_output(vars):
  message("tabulating template counts and statistics...")
  if vars.single_end==True: counts = read_counts(vars.ref,vars.sam,vars) # return read counts copied as template counts
  else: counts = template_counts(vars.ref,vars.sam,vars.barcodes1,vars)
  tcfile = open(vars.tc,"w")
  tcfile.write('\t'.join("coord Fwd_Rd_Ct Fwd_Templ_Ct Rev_Rd_Ct Rev_Templ_Ct Tot_Rd_Ct Tot_Templ_Ct".split())+"\n")
  for data in counts: tcfile.write('\t'.join([str(x) for x in data])+"\n")
  tcfile.close()

  message("writing %s" % vars.wig)
  output = open(vars.wig,"w")

  read1 = os.path.basename(vars.fq1)
  read2 = os.path.basename(vars.fq2)
  fi = re.split(r'\.', os.path.basename(vars.ref))[0]
  output.write("# Generated by tpp from " + read1 + " and " + read2 + "\n")
  output.write("variableStep chrom="+ fi + "\n")
  for data in counts: output.write("%s %s\n" % (data[0],data[-1]))
  output.close()

  primer = "CTAGAGGGCCCAATTCGCCCTATAGTGAGT"
  vector = "CTAGACCGTCCAGTCTGGCAGGCCGGAAAC"

  tot_reads,nprimer,nvector = 0,0,0
  prefixes = {}
  for line in open(vars.reads1):
    if line[0]=='>': tot_reads += 1; continue
    if primer in line: nprimer += 1
    if vector in line: nvector += 1
    #prefix = line[:30]
    #if prefix not in prefixes: prefixes[prefix] = 0
    #prefixes[prefix] += 1
  #temp = prefixes.items()
  #temp.sort(key=lambda x: x[1],reverse=True)

  rcounts = [x[5] for x in counts]
  tcounts = [x[6] for x in counts]
  rc,tc = sum(rcounts),sum(tcounts)
  ratio = rc/float(tc)
  ta_sites = len(rcounts)
  tas_hit = len(filter(lambda x: x>0,rcounts))
  density = tas_hit/float(ta_sites)
  counts.sort(key=lambda x: x[-1])
  max_tc = counts[-1][6]
  max_coord = counts[-1][0]
  NZmean = tc/float(tas_hit)
  FR_corr = corr([x[1] for x in counts],[x[3] for x in counts])
  BC_corr = corr([x for x in rcounts if x!=0],[x for x in tcounts if x!=0])

  read_length = get_read_length(vars.base + ".reads1")
  mean_r1_genomic = get_genomic_portion(vars.base + ".tgtta1")
  if vars.single_end==False: mean_r2_genomic = get_genomic_portion(vars.base + ".genomic2")

  output = open(vars.stats,"w")
  version = "1.0"
  #output.write("# title: Tn-Seq Pre-Processor, version %s\n" % vars.version)
  output.write("# title: Tn-Seq Pre-Processor\n")
  output.write("# date: %s\n" % time.strftime("%m/%d/%Y %H:%M:%S"))
  output.write("# command: python ")
  output.write(' '.join(sys.argv)+"\n")
  output.write('# transposon type: %s\n' % vars.transposon)
  output.write('# read1: %s\n' % vars.fq1)
  output.write('# read2: %s\n' % vars.fq2)
  output.write('# ref_genome: %s\n' % vars.ref)
  output.write("# total_reads %s (read pairs)\n" % tot_reads)
  #output.write("# truncated_reads %s (fragments shorter than the read length; ADAP2 appears in read1)\n" % vars.truncated_reads)
  output.write("# TGTTA_reads %s (reads with valid Tn prefix, and insert size>20bp)\n" % vars.tot_tgtta)
  output.write("# reads1_mapped %s\n" % vars.r1)
  output.write("# reads2_mapped %s\n" % vars.r2)
  output.write("# mapped_reads %s (both R1 and R2 map into genome)\n" % vars.mapped)
  output.write("# read_count %s (TA sites only)\n" % rc)
  output.write("# template_count %s\n" % tc)
  output.write("# template_ratio %0.2f (reads per template)\n" % ratio)
  output.write("# TA_sites %s\n" % ta_sites)
  output.write("# TAs_hit %s\n" % tas_hit)
  output.write("# density %0.3f\n" % density)
  output.write("# max_count %s (among templates)\n" % max_tc)
  output.write("# max_site %s (coordinate)\n" % max_coord)
  output.write("# NZ_mean %0.1f (among templates)\n" % NZmean)
  output.write("# FR_corr %0.3f (Fwd templates vs. Rev templates)\n" % FR_corr)
  output.write("# BC_corr %0.3f (reads vs. templates, summed over both strands)\n" % BC_corr)
  output.write("# primer_matches: %s reads contain %s\n" % (nprimer,primer))
  output.write("# vector_matches: %s reads contain %s\n" % (nvector,vector))
  output.write("# read_length: %s bp\n" % read_length)
  output.write("# mean_R1_genomic_length: %0.1f bp\n" % mean_r1_genomic)
  if vars.single_end==False: output.write("# mean_R2_genomic_length: %0.1f bp\n" % mean_r2_genomic)

  #output.write("# most_abundant_prefix: %s reads start with %s\n" % (temp[0][1],temp[0][0]))
  # since these are reads (within Tn prefix stripped off), I expect ~1/4 to match Tn prefix
  vals = [vars.fq1,vars.fq2,tot_reads,vars.tot_tgtta,vars.r1,vars.r2,vars.mapped,rc,tc,ratio,ta_sites,tas_hit,max_tc,density,max_coord,NZmean,FR_corr,BC_corr,nprimer,nvector]
  output.write('\t'.join([str(x) for x in vals])+"\n")
  output.close()

  message("writing %s" % vars.stats)
  #os.system("grep '#' %s" % vars.stats)
  infile = open(vars.stats)
  for line in infile:
      if '#' in line:
          print line.rstrip()
  infile.close()
  
#############################################################################

def error(s):
  print "error:",s
  sys.exit(0)

def verify_inputs(vars):
  if not os.path.exists(vars.fq1): error("file not found: "+vars.fq1)
  vars.single_end = False
  if vars.fq2=="": vars.single_end = True   
  elif not os.path.exists(vars.fq2): error("file not found: "+vars.fq2)
  if not os.path.exists(vars.ref): error("file not found: "+vars.ref)
  if vars.base == '': error("prefix cannot be empty")
  if vars.fq1 == vars.fq2: error('fastq files cannot be identical')

def initialize_globals(vars):
      vars.fq1,vars.fq2,vars.ref,vars.bwa,vars.base,vars.maxreads = "","","","","temp",-1
      vars.mm1 = 1 # mismatches allowed in Tn prefix
      vars.transposon = 'Himar1'
      read_config(vars)

def read_config(vars):
  if not os.path.exists("tpp.cfg"): return
  for line in open("tpp.cfg"):
    w = line.split()
    if len(w)>=2 and w[0]=='reads1': vars.fq1 = w[1]
    if len(w)>=2 and w[0]=='reads2': vars.fq2 = w[1]
    if len(w)>=2 and w[0]=='ref': vars.ref = w[1]
    if len(w)>=2 and w[0]=='bwa': vars.bwa = w[1]
    if len(w)>=2 and w[0]=='prefix': vars.base = w[1]
    if len(w)>=2 and w[0]=='mismatches1': vars.mm1 = int(w[1])
    if len(w)>=2 and w[0]=='transposon': vars.transposon = w[1]

def save_config(vars):
  f = open("tpp.cfg","w")
  f.write("reads1 %s\n" % vars.fq1)
  f.write("reads2 %s\n" % vars.fq2)
  f.write("ref %s\n" % vars.ref)
  f.write("bwa %s\n" % vars.bwa)
  f.write("prefix %s\n" % vars.base)
  f.write("mismatches1 %s\n" % vars.mm1) 
  f.write("transposon %s\n" % vars.transposon) 
  f.close()

def show_help():
  print 'usage: python PATH/src/tpp.pyc -bwa PATH_TO_EXECUTABLE -ref REF_SEQ -reads1 PATH_TO_FASTQ_OR_FASTA_FILE -reads2 PATH_TO_FASTQ_OR_FASTA_FILE -prefix OUTPUT_BASE_FILENAME [-maxreads N] [-mismatches N] [-tn5]'
    
class Globals:
  pass


def main():
    # if -nowin is command-line arg, skip the GUI and set filenames in vars
    
    vars = Globals()
    #vars.version = "$Revision: 1.5 $".split()[1]
    
    if(len(sys.argv) <= 1):
        app = wx.App(False)
        form = MyForm(vars)
        form.update_dataset_list()

        form.Show()
        app.MainLoop()

        # vars.action not defined, quit...

        if vars.action=="start":
            verify_inputs(vars)
            if vars.fq2=="": msg = 'running pre-processing on %s' % (vars.fq1)
            else: msg = 'running pre-processing on %s and %s' % (vars.fq1,vars.fq2)
            message(msg)
            message("transposon type: %s" % vars.transposon)
            save_config(vars)
            driver(vars)

    else:
        flag = False
        initialize_globals(vars)
        for i in range(0, len(sys.argv)):
            if sys.argv[i] == '-help':
                show_help()
                sys.exit()
            if sys.argv[i] == '-tn5': 
                vars.transposon = 'Tn5'
            if sys.argv[i] == '-reads1': 
                vars.fq1 = sys.argv[i+1]
            elif sys.argv[i] == '-reads2':
                flag = True
                vars.fq2 = sys.argv[i+1]
            elif sys.argv[i] == '-bwa':
                vars.bwa = sys.argv[i+1]
            elif sys.argv[i] == '-ref':
                vars.ref = sys.argv[i+1]
            elif sys.argv[i] == '-maxreads':
                vars.maxreads = int(sys.argv[i+1])
            elif sys.argv[i] == '-prefix':
                vars.base = sys.argv[i+1]
            elif sys.argv[i] == '-mismatches':
                vars.mm1 = int(sys.argv[i+1])
        if flag==False: vars.fq2 = ""
        if vars.fq2=="": msg = 'running pre-processing on %s' % (vars.fq1)
        else: msg = 'running pre-processing on %s and %s' % (vars.fq1,vars.fq2)
        message(msg)
        message("transposon type: %s" % vars.transposon)
        verify_inputs(vars)
        save_config(vars)
        driver(vars)

if __name__ == "__main__":
    main()


