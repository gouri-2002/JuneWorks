#loan amount int rate tenure rate

loan_amount=100000
interset_rate_in_years=9
number_of_years=2
interset_rate=9/12/100
num_of_months=24

print(interset_rate)
emi=loan_amount*interset_rate*(1+interset_rate)**num_of_months/((1+interset_rate)**num_of_months-1)
print(f"emi={emi}")

#total_interset_payable
#total_payable_amount

total_payable_amount=emi*num_of_months
print(f"monthly_emi={emi}")
print(f"total payable amount={total_payable_amount}")

total_interset_payable=total_payable_amount-loan_amount
print(f"total interset payable={total_interset_payable}")










