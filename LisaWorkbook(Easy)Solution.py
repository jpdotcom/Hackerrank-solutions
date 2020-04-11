import math
def page_to_question(k,page_start,total_questions):
    pages=[]
    total_pages=None
    if total_questions%k==0:
        total_pages=total_questions/k
    else:
        total_pages=math.floor(total_questions/k)+1
    while total_pages!=0:
        pages.append(page_start)
        page_start+=1
        total_pages-=1
    return pages
def workbook(k, arr):
    special_questions=0
    page_start=1
    for i in range(0,len(arr)):
        b=page_to_question(k,page_start,arr[i])
        for j in range(0,len(b)):
            if arr[i]%k==0:
                if ((j+1)*k)>=b[j] and  j*k+1<=b[j]:
                    special_questions+=1
            else:
                if j==len(b)-1:
                    if (((j+1)*k)-(k-(arr[i]%k)))>=b[j] and  j*k+1<=b[j]:
                        
                        
                        special_questions+=1
                elif ((j+1)*k)>=b[j] and j*k+1<=b[j]:
                    special_questions+=1
        page_start=b[len(b)-1]+1
    return special_questions
arr=[3,8,15,11,14,1,9,2,24,31]
k=5
print(workbook(k,arr))


                        
                


        

