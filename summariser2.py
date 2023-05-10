import openai
import os


openai.api_key = "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"
doc_a = ["doc1.txt","doc2.txt","doc3.txt"]

def create_summary_all(doc_a):
    file_list = []
    print("Enter the limit of words for summary")
    number_of_words = input()
    print("Enter 1 for summary in points")
    print("Enter 2 for summary in paragraph")
    sum_val = int(input())
    
    for i in doc_a:
        file1 = open(i,"r")
        doc = str(file1.readlines())
        doc = doc[1:-1]
        if(sum_val == 1):
        
            prompt = "Please write a summary of " + str(doc) + " under " + str(number_of_words) + " words in points"
            
            model = "text-davinci-002"
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=2048
            )
            print("---------------------------------------------------------------------")
            fs = i+"_summary"
            with open(fs, "w") as f:
                f.write(response.choices[0].text)
                # print(response.choices[0].text, file=f)
            print("---------------------------------------------------------------------")
            
            
        
        elif(sum_val == 2):
        
            prompt = "Please write a summary of " + str(doc) + " under " + str(number_of_words) + " words in paragraph"
            
            model = "text-davinci-002"
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=2048
            )
            if(len(response.choices[0].text)==0):
                print("Reset the filters")
            print("---------------------------------------------------------------------")
            fs = i+"_summary"
            with open(fs, "w") as f:
                f.write(response.choices[0].text)
                # print(response.choices[0].text, file=f)
            
            print("---------------------------------------------------------------------")
        
        file_list.append(fs)
    f = open("bigfile.txt", "w")
    k=0
    for j in file_list:
        with open(j, 'r') as fn:
            
                f.write("Summary for: {0}".format(doc_a[k]))
                k=k+1
                f.write(fn.read())
                f.write("\n")
            
create_summary_all(doc_a)