# Maximum-Subarray
The maximum subarray problem is a problem in which a sequence of values (negative, positive or zero) is given a sequence of values (negative, positive or zero) and the continuous sequence of values in the sequence that gives the largest possible sum is to be found. 
In this paper, the algorithmic investigation of the problem is requested. In addition, the implementation of algorithms for solving the problem with different computational complexity, recording and presenting the execution times is requested.

# Η θεωρητική πολυπλοκότητα των αλγορίθμων

**	First Algorithm (Kadane’s) : Υπολογίζει τη max υποακολουθία χρησιμοποιώντας μόνο 1 for loop, δηλαδή με O (n) πολυπλοκότητα. Στην ουσία από μία λίστα παίρνουμε μόνο τα θετικά στοιχεία και όπου υπάρχει αρνητικός αριθμός το μετατρέπει σε 0 κι έτσι βγαίνει το μεγαλύτερο άθροισμα στην max υποακολουθία.

**	Second Algorithm (Prefix) : Υπολογίζει τη max υποακολουθία χρησιμοποιώντας 2 for loops, δηλαδή με O (n2) πολυπλοκότητα. Στην ουσία από μία λίστα δημιουργείται μία άλλη ξεχωριστή με όνομα prefix με τα αθροίσματα των στοιχείων της (το προηγούμενο του prefix με το επόμενο της λίστας) και από αυτά βρίσκει την max υποακολουθία. 

**	Third Algorithm (Kadane’s) : Υπολογίζει τη max υποακολουθία χρησιμοποιώντας 3 for loops, δηλαδή με O (n3) πολυπλοκότητα. Στην ουσία από μία λίστα υπολογίζει όλα τα αθροίσματα όλων των στοιχείων και το μεγαλύτερο που θα βρει θα είναι το max sum στην max υποακολουθία.


# Οι χρόνοι εκτέλεσης των αλγορίθμων

Οι μετρήσεις χρόνων εκτέλεσης των αλγορίθμων με εισόδους : 100, 500, 1000, 2000 (για λόγους ευκολίας χρησιμοποιήθηκαν μικρότεροι αριθμοί) εμφανίζονται στον παρακάτω πίνακα:

n	      100	      500	      1000	    2000
O (n)	  0,00155	  0,00348	  0,00491	  0,00713
O (n2)	0,00377	  0,02526	  0,09720	  0,37322
O (n3)	0,01008	  1,05861	  8,33476	  135,31060


# Γραφική σύγκριση μέσω διαγραμμάτων των αποτελεσμάτων που παράγουν οι αλγόριθμοι

Για τη δημιουργία του παρακάτω διαγράμματος με τους χρόνους εκτέλεσης κάθε αλγορίθμου χρησιμοποιήθηκε η βιβλιοθήκη matplotlib της python. Παρατηρούμε ότι ο αλγόριθμος με πολυπλοκότητα Ο (n3) καθυστερεί αρκετά σε σχέση με τους άλλους δύο, για αυτό και δεν είναι καθόλου αποδοτικός εν αντιθέσει με τον αλγόριθμο του Ο (n) ο οποίος τρέχει σε ελάχιστα δευτερόλεπτα.

![Uploading image.png…]()![Figure_1](https://github.com/user-attachments/assets/2ad1f4d9-00c4-472d-834d-59bc6bae204a)
