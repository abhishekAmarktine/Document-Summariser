import openai
import os


openai.api_key = "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"
doc_a = ["doc1.txt"]

#   file1 = open(i,"r")
#   doc = str(file1.readlines())
#   doc = doc[1:-1]
#   prompt = "what is the category of this" + str(doc) + " in single word"
#   model = "text-davinci-002"
#   response = openai.Completion.create(
#     engine=model,
#     prompt=prompt,
#     max_tokens=2048
#   )
#   print("The category of doc is :")

def create_summary(file_name):
  
  file1 = open(file_name,"r")
  doc = str(file1.readlines())
  doc = doc[1:-1]
  while(True):
    
    print("1 for filter")
    print("0 for no filter")    
    val = int(input())
        
    if(val == 1):
      print("Enter the limit of words for summary")
      number_of_words = input()
      print("Enter 1 for summary in points")
      print("Enter 2 for summary in paragraph")
      sum_val = int(input())
      if(sum_val == 1):
        
        prompt = "Please write a summary of " + str(doc) + " under " + str(number_of_words) + " words in points"
        
        model = "text-davinci-002"
        response = openai.Completion.create(
          engine=model,
          prompt=prompt,
          max_tokens=2048
        )
        print("---------------------------------------------------------------------")
        fs = file_name+"_summary"
        with open(fs, "w") as f:
          print(response.choices[0].text, file=f)
        break
        print("---------------------------------------------------------------------")
        
      elif(sum_val == 2):
        
        prompt = "Please write a summary of " + str(doc) + " under " + str(number_of_words) + " words in paragraph"
        print(prompt)
        model = "text-davinci-002"
        response = openai.Completion.create(
          engine=model,
          prompt=prompt,
          max_tokens=2048
        )
        if(len(response.choices[0].text)==0):
          print("Reset the filters")
        print("---------------------------------------------------------------------")
        fs = file_name+"_summary"
        with open(fs, "w") as f:
          print(response.choices[0].text, file=f)
        break
        print("---------------------------------------------------------------------")
    elif(val == 0):
      prompt = "Please write a summary of " + str(doc)
      model = "text-davinci-002"
      response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2048
      )
      if(len(response.choices[0].text)==0):
        print("Reset the filters")
      print("---------------------------------------------------------------------")
      fs = file_name+"_summary"
      with open(fs, "w") as f:
        print(response.choices[0].text, file=f)
      # print(response.choices[0].text)
      print("---------------------------------------------------------------------")
      break


for i in doc_a:
  create_summary(i)
# print("1 for summary of summary of all docs")
# print("No summary of summary needed")
# new_val = int(input())
# if(new_val == 1):
#   new_doc=""
#   for i in doc_a:
#     file_name = i+"_summary"
#     file1 = open(file_name,"r")
#     doc = str(file1.readlines())
#     doc = doc[1:-1]
#     new_doc = new_doc+doc
#   fs = "final_summary.txt"
#   with open(fs, "w") as f:
#       print(new_doc, file=f)
#   create_summary(fs)

# elif(new_val == 0):
#   print("Thanks")

  