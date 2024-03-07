import math

class LoanCalculator:
    @staticmethod
    def calculate_monthly_payment(loan_amount, loan_term, interest_rate):
        monthly_interest_rate = interest_rate / 12
        term_length_in_months = loan_term * 12
        monthly_payment = loan_amount * (monthly_interest_rate * pow(1 + monthly_interest_rate, term_length_in_months)) / (pow(1 + monthly_interest_rate, term_length_in_months) - 1)
        return monthly_payment

    @staticmethod
    def calculate_total_interest(loan_amount, loan_term, interest_rate):
        monthly_interest_rate = interest_rate / 12
        term_length_in_months = loan_term * 12
        total_interest = loan_amount * term_length_in_months * monthly_interest_rate
        return total_interest

    @staticmethod
    def calculate_total_payment(loan_amount, loan_term, interest_rate):
        monthly_interest_rate = interest_rate / 12
        term_length_in_months = loan_term * 12
        total_payment = loan_amount * pow(1 + monthly_interest_rate, term_length_in_months)
        return total_payment
