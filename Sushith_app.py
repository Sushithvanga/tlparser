
from datetime import datetime
import math
import numpy as np
import pandas as pd
import streamlit as st

def tlparser(words):
  amt = 1
  count = 0
  sum = 0
  while words:
    if "am" not in words or "pm" not in words :
      count += 1
    else:
      letter = words.split(': ')
      s = letter[-1].split('- ')  
      var1 = s[-1].strip()
      e = var1.split(" ")

      in_status = s[0].strip()
      in_status = in_status.split(":")
      x = in_status[0] + ":" + in_status[1][:2] + " " + in_status[1][2:].upper()
      out_status = e[0].strip()
      out_status = out_status.split(":")
      y = out_status[0] + ":" + out_status[1][:2] + " " + out_status[1][2:].upper()

      in_ = datetime.strptime(x,"%I:%M %p")
      int_time = datetime.strftime(in_, "%H:%M")
      int_time = datetime.strptime(int_time,"%H:%M")
      ou_ = datetime.strptime(y,"%I:%M %p")
      out_time = datetime.strftime(ou_, "%H:%M")
      out_time = datetime.strptime(out_time,"%H:%M")
      sum += (out_time - int_time).total_seconds()/60/60
    words = docx_file.readline()
    amt += 1

  st.write(f" Total of {abs(sum)} has been spent by the author on this file")
  st.write(f" {count} lines did not have any timing")

if __name__ ==  "__main__" :

  st.title("Streamlit web app")
  html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">Time Log Parser App </h2>
    </div>
    """
  st.markdown(html_temp,unsafe_allow_html=True)
  docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])
  if st.button("Enter"):
    if docx_file is not None:
        file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
        st.write(file_details)
        # Check File Type
        if docx_file.type == "text/plain":
          line = str(docx_file.read(),"utf-8")
          tlparser(line)

