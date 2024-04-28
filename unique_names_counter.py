import csv
class unique_names_counter:
    nicknames = {}
    wasLoaded = False
    
    def load_nicknames(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                name = line[0]
                unique_names_counter.nicknames[name] = line[1:]
    
    def isNickname(name1, name2):
        if not unique_names_counter.wasLoaded:
            unique_names_counter.load_nicknames("names.csv")
            unique_names_counter.wasLoaded = True
        name1Nicknames = unique_names_counter.nicknames.get(name1)
        if name1Nicknames!=None and name2 in name1Nicknames:
            return True
        name2Nicknames = unique_names_counter.nicknames.get(name2)
        if name2Nicknames!=None and name1 in name2Nicknames:
            return True
        return False
    
    @staticmethod
    def is_typo_or_identical(str1, str2):
        if str1 == str2:
            return True
        
        if len(str1) != len(str2):
            return False
        
        typo_count = 0
        for c1, c2 in zip(str1, str2):
            if c1 != c2:
                typo_count += 1
                if typo_count > 1:
                    return False
        
        return typo_count == 1
    
    def isSameWithMiddleName(name1, name2):
        return name1 in name2 or name2 in name1
    
    def isSameSeperatedNames(first1, last1, first2, last2):
        if (unique_names_counter.isSameWithMiddleName(first1, first2) or unique_names_counter.is_typo_or_identical(first1, first2) or unique_names_counter.isNickname(first1, first2))  and unique_names_counter.is_typo_or_identical(last1, last2):
            return 1
        return 0

    def isSameFullNames(fullname1, fullname2):
        return (all(name in fullname2 or any(unique_names_counter.is_typo_or_identical(name, subname2) or unique_names_counter.isNickname(name, subname2) for subname2 in fullname2.split()) for name in fullname1.split())) or (all(name in fullname1 or any(unique_names_counter.is_typo_or_identical(name, subname1) or unique_names_counter.isNickname(name, subname1) for subname1 in fullname1.split()) for name in fullname2.split()))
    
    @staticmethod
    def countUniqueNames(billFirstName, billLastName,shipFirstName,shipLastName,cardFullName):
        billFirstName = " ".join(sorted(billFirstName.lower().split()))
        billLastName = " ".join(sorted(billLastName.lower().split()))
        shipFirstName = " ".join(sorted(shipFirstName.lower().split()))
        shipLastName = " ".join(sorted(shipLastName.lower().split()))
        billFullName = " ".join(sorted([billFirstName, billLastName]))
        shipFullName = " ".join(sorted([shipFirstName, shipLastName]))
        cardFullName = " ".join(sorted(cardFullName.lower().split()))
        billEqualsShip = unique_names_counter.isSameSeperatedNames(billFirstName,billLastName,shipFirstName,shipLastName)
        billEqualsCard = unique_names_counter.isSameFullNames(billFullName, cardFullName)
        shipEqualsCard = unique_names_counter.isSameFullNames(shipFullName, cardFullName)
        counter = billEqualsShip + billEqualsCard + shipEqualsCard
        if counter > 1:
            return 1
        elif counter == 1:
            return 2
        return 3