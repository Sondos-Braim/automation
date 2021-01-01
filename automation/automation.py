import re
with open('./assets/potential-contacts.txt') as file:
    content= file.readlines()
    content=''.join(content)
    phone_numbers=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', content)
    emails=re.findall(r'[\w\.-]+@[\w\.-]+',  content)

formated_nums=[]
for i in phone_numbers:
    i='%s-%s-%s' % tuple(re.findall(r'\d{4}$|\d{3}|\d{2}', i))
    formated_nums.append(i)

formated_nums = list(dict.fromkeys(formated_nums))
formated_nums.sort()
emails = list(dict.fromkeys(emails))
emails.sort()
with open('./assets/phone_numbers.txt','w') as num_file:
    num_file.write(','.join(formated_nums))
with open('./assets/emails.txt','w') as num_file:
    num_file.write(','.join(emails))

if __name__ == "__main__":   
    pass  
   
