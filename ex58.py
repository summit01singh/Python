def grade_you_get(xs):
    if(xs < 40):
        grade =  'F3'
        return grade
    elif(xs >= 40 and xs <= 45):
        grade = 'F2'
        return grade
    elif(xs >= 45 and xs <= 50):
        grade = 'F1 Supp'
        return grade
    elif(xs >= 50 and xs <= 60):
        grade = 'Third'
        return grade
    elif(xs >= 60 and xs <= 70):
        grade = 'Second'
        return grade
    elif(xs >= 70 and xs <= 75):
        grade = 'Upper Second'
        return grade
    elif(xs >= 75 and xs <= 100):
        grade = 'First'
        return grade
    else:
        grade = "you are genius Man"
        return grade
for i in (83,75,74.9,70,69.9,65,60,59.9,55,50,49.9,45,44.9,40,39.9,2,0,102):
    xs1 = i
    print (('You got', xs1) + ('and Your grade is', grade_you_get(xs1)))
