# Copy-ALTA
Copy Apertif averaged continuum data to ALTA

Use find command to find related documents in Alta server. It will write the related paths in a txt file called output.txt

```
find -L /data*/apertif/200102*/1* -type d -name *_avg.MS > output.txt
```

Run Python command to transfer related datas to ALTA:

```
python3 alta.py 
```
