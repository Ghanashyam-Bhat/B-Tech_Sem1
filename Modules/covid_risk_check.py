def covid():
    print("THIS TEST WILL HELP YOU DIFFERENTIATE BETWEEN COVID AND OTHER DISEASES BASED ON YOUR SYMPTOMS")
    AGE=int(input('How old are you? '))
    q1=input('Do you have a fever? ').upper()
    if q1=='YES':
        q2=input('Are you experiencing shortess of breath?').upper()
        if q2=='YES':
                    print('YOU MAY HAVE COVID 19')
                    l=['fatigue', 'weakness', 'cough', 'loss of taste', 'exhaustion']
                    print('Other symptoms include:')
                    for i in l:
                              print(i)
                    if AGE<=30:
                        print('Fatality risk: Low')
                        print('Isolate yourself and call the covid helpline number')
                    elif 30<AGE<=50:
                        print('Fatality risk: Moderate')
                        print('Isolate yourself and call the covid helpline number')
                    else:
                        print('Fatality risk: High')
                        print('RUSH TO THE NEAREST COVID-19 TREATMENT CENTRE IMMEDIATELY')

        else:
                    print('YOU MAY HAVE THE FLU')
                    l=['fatigue', 'weakness', 'cough', 'exhaustion']
                    print('Other symptoms include:')
                    for i in l:
                              print(i)
    else:
        q3=input('Do you have itchy eyes?').upper()
        if q3=="YES":
            print('YOU MAY HAVE ALLERGIES')
            l=['Running nose', 'Sneezing']
            for i in l:
                print(i)
        else:
            print('You may have the common cold')
            l=['Running nose', 'Sneezing','Mild chest discomfort']
            for i in l:
                print(i)






