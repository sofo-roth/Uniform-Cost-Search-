#Ξεκινάω το προγραμμα χτίζοντας την δομη του γραφήματος με τον καθε
#κομβο και την καθε διαδρομη που θα ακολουθησει, μαζι με τα αντιστοιχα κόστη

dendro = {
    'I': [('A', 5), ('B', 9), ('D', 5)],
    'A': [('G1', 8), ('B', 2)],
    'B': [('A', 2), ('C', 1)],
    'C': [('I', 6), ('G2', 7), ('F', 6)],
    'D': [('I', 5), ('C', 3), ('E', 4)],
    'E': [('G3', 2)],
    'F': [('D', 5), ('G3', 8)]
}


#Δημιουργώ μια μέθοδο στην οποία θα επιστρέφω το συνολικό κόστος της διαδρομής

def route_cost(diadromi):

    #Αρχικοποιώ το συνολικο κόστος πριν το for με 0

    total_cost = 0

    #Δημιουργω μια For για να περάσει απο τον καθε κόμβο της
    #διαδρομής και να επαυξάνεται το συνολικό κόστος.

    for (kombos, cost) in diadromi:
        total_cost += cost
    return total_cost



#Αρχικοποιώ την μεθοδο της ομοιόμορφης αναζήτησης δίνοντας ως παραμέτρους το διαγραμμα
#,την αρχή της διαδρομής και το τέλος της διαδρομής

def uniform_cost_search(dendro, arxi, telos):

    #visited ειναι ο πίνακας που θα αποθηκεύει τους κόμβους που έχει επισκεφτεί
    visited = []

    #queue ειναι ο πίνακας των κόμβων της διαδρομής που θα εκτελέσει.
    #Την αρχικοποιώ με τον πρώτο κόμβο ΠΡΙΝ το WHILE, καθώς και με το μηδενικο κόστος,
    #καθως δεν έχει ξεκινήσει ακόμα το "ταξίδι".
    queue = [[(arxi, 0)]]

    #Δημιουργώ μία WHILE οπου για κάθε κόμβο που θα επισκέφτεται, με τερματική συνθήκη
    #να μην έχουν μείνει άλλοι κόμβοι να επισκεφτεί, να τις ταξινομεί με βάση το κόστος
    #σε αυξουσα σειρά. Έπειτα παίρνει τον πρώτο κόμβο ο οποίος θα ναι αυτος με το ελάχιστο
    #κόστος και τον τοποθετεί στην βέλτιστη διαδρομή
    while queue:
        queue.sort()
        diadromi = queue.pop(0)
        kombos = diadromi[-1][0]

        #Με την IF τσεκάρω αν τον κόμβο στον οποίο βρισκόμαστε τωρα τον έχουμε ήδη
        #επισκεφτεί. Αν ΟΧΙ τότε τον προσθέτω στον πίνακα visited.
        if kombos in visited:
            continue
        visited.append(kombos)

        #Με την IF τσεκάρω αν ο κόμβος στον οποίο βρισκόμαστε τώρα είναι ο τελικός προορισμός
        #που έχουμε δώσει. Αν ΝΑΙ τότε επιστρέφω την διαδρομή, καθώς το "ταξίδι" έχει ολοκληρωθεί
        #και εμφανίζω όλους του κόμβους που έχει επισκεφτεί
        #Αν ΟΧΙ τότε τσεκάρω τους γειτονικούς κόμβους, παιρνω την διαδρομη που εχω εκτελεσει
        #μεχρι το εκάστοτε σημείο, προσθέτω στο τελος αυτηνής τον καινούργιο κόμβο και έπειτα
        #ενημερώνω την queue με την καινουργια διαδρομή
        if kombos == telos:
                for v_kombos, v_cost in diadromi:
                    print("Επισκέφτηκε τον", v_kombos, "κόμβο με κόστος:", v_cost)
                return diadromi
        else:
            geitonikoi_komboi = dendro.get(kombos, [])
            for (kombos2, cost) in geitonikoi_komboi:
                nea_diadromi = diadromi.copy()
                nea_diadromi.append((kombos2, cost))
                queue.append(nea_diadromi)

#Εμφανίζω όλα τα αποτελέσμα του αλγόριθμου με βάση τα ζητούμενα της εκφώνησης
#Για τον υπολογισμό του συνολικού κόστους χρησιμοποιώ την route_cost που δημιούργησα παραπάνω
#Το μοναδικό input που δίνει ο χρήστης ειναι το τέλος που επιθυμεί ο αλγόριθμος να βρεί την εκάστοτε διαδρομή
#επιλέγει ένα από τα τρία (G1 , G2 , G3), με έλεγχο δεδομένων εισόδου


pick = input('Επέλεξε τέλος διαδρομής (G1-G2-G3): ')
picks = ['G1', 'G2', 'G3']
while pick not in picks:
    print("Λανθασμένη επιλογή ξαναπροσπάθησε...")
    pick = input('Επέλεξε τέλος διαδρομής (G1-G2-G3): ')

apotelesma = uniform_cost_search(dendro, 'I', pick)
sunoliko_kostos = route_cost(apotelesma)
print("Το μονοπάτι που ακολουθήθηκε από τον αρχικό κόμβο μέχρι τον τελικό είναι:", apotelesma)
print("To συνολικό κόστος της διαδρομής ειναι:", sunoliko_kostos)














