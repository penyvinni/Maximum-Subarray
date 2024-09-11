import timeit  # φόρτωση της βιβλιοθήκης timeit για να μπορώ να πάρω δεδομένα χρόνου εκτέλεσης κάθε συνάρτησης
import random  # φόρτωση της βιβλιοθήκης random για να μπορώ να παράγω λίστες με τυχαίους αριθμούς κάθε φορά με συγκεκριμένο εύρος
import matplotlib.pyplot as plt


def array(n, m,seed):  # η συνάρτηση array για την παραγωγή των τυχαίων λιστών
    if seed:
        random.seed(seed)
    return [random.randint(-m, m) for _ in range(n)]  # επιστρέφει λίστα με τυχαία νούμερα σε ένα συγκεκριμένο εύρος που δίνω εγώ στη main



def Third(n):  # η συνάρτηση που υπολογίζει τον ζητούμενο αλγόριθμο για Ο (n^3) πολυπλοκότητα η οποία χρησιμοποιεί 3 for loops
    a_list = array(n, 100, 10)  #η μεταβλητή a_list στην οποία καλώ την συνάρτηση array ώστε να αποθηκεύσω σε αυτή τις λίστες μου
    print(f"\nThe random list for the Third function is: {a_list} \n")
    largest_sum = a_list[0]  #η μεταβλητή largest_sum στην οποία αποθηκεύω το πρώτο στοιχείο της λίστας
    start_3 = end_3 = 0  # οι μεταβλητές start και stop για να πάρω την αρχή και το τέλος της max υποακολουθίας
    for i in range (0, len(a_list)):
      for j in range(i, len(a_list)):
         sum = 0 # η μεταβλητή που παοθηκεύω το προσωινό άθροισμα των στοιχείων
         for z in range(i, j+1):
             sum+= a_list[z]  # προσθέτω κάθε στοιχείο με την προσπέλαση της λίστας
         if largest_sum < sum : 
             largest_sum = sum  # αν το max άθροισμα έιναι μικρότερο του προσωρινού sum, τότε αυτό θα γίνει το max
             start_3 = i  # η θέση της λίστας που ξεκινάει η max υποακολουθία
             end_3 = j    # η θέση της λίστας που τελειώνει η max υποακολουθία
    result_3 = a_list[start_3 : end_3 + 1]  # το κομμάτι της λίστας που είναι η max υποακολουθία
    print(f"Largest sum for the Third algorith is: {largest_sum}\n")
    print(f"Start position is: {start_3}  and Stop position is: {end_3} for the Thrid algorithm in the contiguous subarray: \n {result_3} \n")



def Second(n):   # η συνάρτηση που υπολογίζει τον ζητούμενο αλγόριθμο για Ο (n^2) πολυπλοκότητα η οποία χρησιμοποιεί 2 for loops
    a_list = array(n, 100, 10)
    print(f"\n The random list for the Second function is: {a_list}\n")
    prefix = [0] * (len(a_list)+1)  #η μεταβλητή prefix τύπου list που αποθηκεύεται η λίστα με τα prefix αθροίσματα από τη θέση 0 έως το τέλος της λίστας
    for i in range(0, len(a_list)):
        prefix[i] = a_list[i] + prefix[i-1]  # κάθε στοιχείο του prefix γίνεται άμα προσθέτω το προηγούμενο prefix στοιχείο με το επόμενο στοιχέιο της λίστας
    print(f"The prefix list is: {prefix}\n")
    largest_sum = prefix[-1]
    start_2 = end_2 = 0
    for j in range(0,len(a_list)):
        for z in range(j, len(a_list)):
            sum = prefix[z] - prefix[j-1]  # το άθοισμα θα είναι από τη θέση j - 1 (διότι οι θέσεις στη λίστα ξεκινάνε από το 0) έως την z
            if sum > largest_sum:
                largest_sum = sum
                start_2 = j
                end_2 = z
    result_2 = a_list[start_2 : end_2 + 1]
    print(f"Largest sum for the Second algorith is: {largest_sum}\n")
    print(f"Start position is: {start_2} and Stop position is: {end_2} for the Second algorithm in the contiguous subarray: \n {result_2} \n")


def First(n):   # η συνάρτηση που υπολογίζει τον ζητούμενο αλγόριθμο για Ο (n) πολυπλοκότητα η οποία χρησιμοποιεί 1 for loops
    a_list = array(n, 100, 10)
    print(f"\n The random list for the First function is: {a_list}\n")
    largest_sum = a_list[0]
    sum = 0
    start_1 = end_1 = 0
    t = 0  #είναι το μονοπάτι του i ατο παρακάτω for όπου i και t θα βοηθήσουν να βρεθούν η αρχή και το τέλος της max υποακολουθίας
    for i in range(0, len(a_list)):
        sum = sum + a_list[i]
        if sum < a_list[i] :
            sum = a_list[i]
        if largest_sum < sum :
            largest_sum = sum
            start_1 = t  
            end_1 = i
        if sum < 0 : 
            sum = 0   # αν το άθροισμα είναι αρνητικόα αριθμός τότε κάνει reset το sum (το μηδενίζει) και προσπελαύνει το t
            t = i + 1
    result_1 = a_list[start_1 : end_1 + 1]
    print(f"Largest sum for the First algorith is: {largest_sum}\n")
    print(f"Start position is: {start_1} and Stop position is: {end_1} for the First algorithm in the contiguous subarray: \n {result_1} \n")



if __name__ == "__main__":
    functions = [Third, Second, First]  # στη μεταβλητή functions καλώ και τις 3 συναρτήσεις παραπάνω
    n = [100,500,1000,2000]   # στη μεταβλητή n αρίζονται τα δεδομένα εισόδου (ακέραιοι αριθμοί) που δόθηκαν στην εργασία 
    #χρησιμοποίησα μικρότερους αριθμούς για μια πιο γρήγορη εκτέλεση του κώδικα
    timed = dict()   # ενα dictionary για να αποθηκευονται ολες οι τιμες των χρονων για το διαγραμμα
    n1 = list()  # μια λίστα για να αποθηκεύονται οι τιμές για τους χρόνους της First
    n2 = list()  # μια λίστα για να αποθηκεύονται οι τιμές για τους χρόνους της Second
    n3 = list()  # μια λίστα για να αποθηκεύονται οι τιμές για τους χρόνους της Thrid
    for f in functions:
        print(f"The following algorithm is: {f.__name__}")
        for number in n:
            print(f"For {number} integers we have:\n")
            start_time = timeit.default_timer()  # η μεταβλητή start_time κρατάει την ώρα που αρχίζει να τρέχει κάθε ένας αλγόριθμος
            f(number)
            duration = timeit.default_timer() - start_time  # η μεταβλητή duration κρατάει την συνολική ώρα που χρειάστηκε για να εκτελεστεί πλήρως κάθε αλγόριθμος
            print(f"For n = {number}: {duration} seconds")
            timed[(f.__name__,number)]=duration  # παίρνει τις τιμές των χρόνων
            print("--"*70)
            print("\n")

  # για τη δημιουργια του διαγράμματος
    for function_name, m in timed:
        if function_name == 'Third':
            n3.append(timed[function_name,m])
        elif function_name == 'Second':
            n2.append(timed[function_name,m])
        elif function_name == 'First':
            n1.append(timed[function_name,m])

  #ετικέτες πάνω στο διάγραμμα
    plt.plot(n, n1, label="n1")
    plt.plot(n, n2, label="n2")
    plt.plot(n, n3, label="n3")
    plt.xscale("log")  # για να δείχνει τους άξονες σε λογαριθμητική κλίμακα
    plt.yscale("log")
    plt.legend()
    plt.show()