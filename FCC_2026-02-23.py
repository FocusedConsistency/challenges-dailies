def can_donate(donor, recipient):
    donor_abo = donor[:-1]
    donor_rh = donor[-1]
    recipient_abo = recipient[:-1]
    recipient_rh = recipient[-1]
    abo_rule = False
    rh_rule = False
    
    if donor_abo in recipient_abo or donor_abo == "O":
        abo_rule = True
    
    if donor_rh == "-" or (donor_rh == "+" and recipient_rh == "+"):
        rh_rule = True

    return abo_rule and rh_rule

can_donate("O+", "A-")
# False
can_donate("B-", "AB+")
# True
can_donate("B-", "A+")
# False
can_donate("O-", "O+")
# True
can_donate("O+", "O-")
# False
