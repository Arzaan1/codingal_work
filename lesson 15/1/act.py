print("welcome to the XYZ bank... \n \n \n\ ")

total_c = 0

total = 0 

notes_t_100 = 0; notes_t_50 = 0; notes_t_10=0; notes_t_1 =0

rem=0

while True:
    name =str(input("What's your name: "))
    amt = int(input(f"{name} How much do you want to withdraw"))

    total += amt
    remaining = amt 

    total_c +=1

    co1, co2, co3, co4, co5=0

    curr=1

    print(f"dispensing amount: {amt}to the customer: {name}\n\n")

    while(remaining>0):
        if curr==1:
         co1 = remaining//100
         if co1>0:
          print(f"100 bucs x {co1} notes are given")
         remaining = remaining%100
         curr+=1
        elif curr==2:
         co2 = remaining//100
         if co2>0:
          print(f"50 bucs x {co1} notes are given")
         remaining = remaining%100
         curr+=1
        if curr==3:
         co3 = remaining//100
         if co3>0:
          print(f"20 bucs x {co1} notes are given")
         remaining = remaining%100
         curr+=1
        if curr==4:
         co4 = remaining//100
         if co4>0:
          print(f"10 bucs x {co1} notes are given")
         remaining = remaining%100
         curr+=1
        if curr==5:
         co5 = remaining//100
         if co5>0:
          print(f"1 bucs x {co1} notes are given")
         remaining = remaining%100
         curr+=1



       
        
        
