#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("plate_no")


if plate_no == "GJ 27 K 9927":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#fcc603;" >Output</h1>')
    print('''<pre>
    Registration Name : RAHUL BHAVSAR 
    License No : 12345688668
    Make / Model : SUZUKI / ERTIGA
    Registration Date : 1/06/2011
    Registering Authority : GUJARAT , INDIA
    Vehicle Class : MCWG
    Fuel Type : DIESEL
    Engine No : IVK3N1734538
    Chassis No : DJSKSJSJSJJS
    Insurance Upto : 6/12/2025
    Fitness Upto : 4/7/2030
    </pre>''')
    print("</body>")

elif plate_no == "HR 26 BR 9044":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : ABRAHAM NAICKER
    License No : 098363357292
    Make / Model : HYUNDAI / VERNA
    Registration Date : 1/12/2012
    Registering Authority : MUMBAI, INDIA
    Vehicle Class : MCWG
    Fuel Type : PETROL
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_no == "KL 12 HZ 0148":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : MEET KOTHATI
    License No : 735382526878
    Make / Model : MAHINDRA / TUV200
    Registration Date : 1/12/2014
    Registering Authority : MANDSAUR, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")