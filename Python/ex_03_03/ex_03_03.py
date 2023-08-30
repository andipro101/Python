score = input("Enter Score: ")
float_score = float(score)
if float_score > 1.0 :
    print('error') 
if float_score >= 0.9 :
    print ('A')
    exit()
if float_score >= 0.8 :
    print ('B')
    exit()
if float_score >= 0.7 :
    print ('C')
    exit()
if float_score >= 0.6 :
    print ('D')
    exit()
if float_score < 0.6 :
    print ('F')
