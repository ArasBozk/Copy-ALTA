import subprocess

with open('/home/bozkurt/output.txt') as f:
    for line2 in f:
        line = line2.strip()
        location = line.split('/')[1].strip()
        location2 = line.split('/')[2].strip()
        task_id = line.split('/')[3].strip()
        beam_num = line.split('/')[4].strip()

        WSRTA = "WSRTA"+str(task_id)+"_B"+str(beam_num)+"_avg.MS"
        WSRTA_tar = "WSRTA"+str(task_id)+"_B"+str(beam_num)+"_avg.MS.tgz"
        cd = "/"+str(location)+"/"+str(location2)+"/"+str(task_id)+"/"
        alta = "/altaZone/ingest/apertif_main/visibilities_continuum/"+str(task_id)+"/WSRTA"+str(task_id)+"_B"+str(beam_num)+"_avg.MS.tgz"
        alta_path = "/altaZone/ingest/apertif_main/visibilities_continuum/"+str(task_id)
        del_path = str(cd)+str(WSRTA)

        subprocess.run(["ln","-s",line,WSRTA],cwd=cd)
        subprocess.run(["tar","--owner=apertif","--group=apertif","-chvzf",WSRTA_tar,WSRTA],cwd=cd)
        subprocess.run(["tar","-tzvf",WSRTA_tar],cwd=cd)
        subprocess.run(["tar","-xvzf",WSRTA_tar],cwd=cd)
        subprocess.run(["ils"],cwd=cd)
        subprocess.run(["imkdir",alta_path])

        if(int(beam_num) < 10):
            subprocess.run(["iput","-KPR","alta-icat-Resc",WSRTA_tar,alta],cwd=cd)
        elif(int(beam_num) > 9 and int(beam_num) < 20):
            subprocess.run(["iput","-KPR","alta-res1-Resc",WSRTA_tar,alta],cwd=cd)
        elif(int(beam_num) > 19 and int(beam_num) < 30):
            subprocess.run(["iput","-KPR","alta-res2-Resc",WSRTA_tar,alta],cwd=cd)
        elif(int(beam_num) > 29 and int(beam_num) < 40):
            subprocess.run(["iput","-KPR","alta-res3-Resc",WSRTA_tar,alta],cwd=cd)

        subprocess.run(["ils","-AL",alta_path],cwd=cd)
        subprocess.run(["rm","-r",del_path])
        subprocess.run(["rm",WSRTA_tar],cwd=cd)

f.close()
