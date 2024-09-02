import pandas,datetime,smtplib

email="sachinkoli8477@gmail.com"
password="rmto bqro jtzj wosb"

content=pandas.read_csv("./birthdays.csv")
x=content.to_dict(orient="records")

now=datetime.datetime.now()
day=now.day
month=now.month

for n in range(0,len(x)):
    info=x[n]
    if info["month"] == month and info["day"] == day:
        name=info["name"]
        with open("./letter_templates/letter_3.txt",mode='r') as data:
            content1=data.read()
            content1=content1.replace("[NAME]",name)
            content1=content1.replace("Angela","Sachin Koli")
        
        with smtplib.SMTP("smtp.gmail.com",587) as conn:
            conn.starttls()
            conn.login(user=email,password=password)
            conn.sendmail(from_addr=email,to_addrs="sachinkoli6396@yahoo.com",msg=f"Subject:Happy Birthday\n\n{content1}")