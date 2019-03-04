import pandas as pd
import numpy as np


# total_loan=2640000
# repayment_duration = 360
# rate_per_year = 0.0539
def equal_principal(total_loan, repayment_duration, rate_per_year):
    repayment_per_month = float(total_loan / repayment_duration)
    # print(repayment_per_month)
    first_interest = float(rate_per_year / 12 * total_loan)
    # print(first_interest)
    firstmonth_payment = repayment_per_month+first_interest
    # print(firstmonth_payment)
    x = np.empty([repayment_duration, 4], dtype=float)
    for i in range(repayment_duration):
        if i == 0:
            x[i][0]=total_loan
            x[i][1]=firstmonth_payment
            x[i][2]=first_interest
            x[i][3]=repayment_per_month
            leaving_loan = total_loan - repayment_per_month
        if i>0:
            interest_per_month = float(rate_per_year / 12 * leaving_loan)
            actual_payment_month = repayment_per_month + interest_per_month
            x[i][0] = leaving_loan
            x[i][1] = actual_payment_month
            x[i][2] = interest_per_month
            x[i][3] = repayment_per_month
            leaving_loan = leaving_loan - repayment_per_month
    # print(x)
    # month = list(range(1,361))
    # print(month)
    df = pd.DataFrame(x, index=list(range(1,repayment_duration+1)), columns=["本金","贷款还本息和","贷款还息","贷款还本"])
    # print(df)
    df.to_excel("贷款%s元%s期等额本金.xlsx"%(total_loan,repayment_duration))

def equal_total(total_loan, repayment_duration, rate_per_year):
    total_repayment = float(total_loan*rate_per_year/12*(1+rate_per_year/12)**repayment_duration/((1+rate_per_year/12)**repayment_duration-1))
    x =np.empty([repayment_duration,4],dtype=float)
    for i in range(repayment_duration):
        if i == 0:
            interest_per_month = float(total_loan*rate_per_year/12)
            actual_payment_month = total_repayment-interest_per_month
            x[i][0] = total_loan
            x[i][1] = total_repayment
            x[i][2] = interest_per_month
            x[i][3] = actual_payment_month
            leaving_loan = total_loan-actual_payment_month
        if i>0:
            interest_per_month = float(leaving_loan * rate_per_year / 12)
            actual_payment_month = total_repayment - interest_per_month
            x[i][0] = leaving_loan
            x[i][1] = total_repayment
            x[i][2] = interest_per_month
            x[i][3] = actual_payment_month
            leaving_loan = leaving_loan - actual_payment_month
    df = pd.DataFrame(x,index=list(range(1,repayment_duration+1)),columns=["本金","贷款还本息和","贷款还息","贷款还本"])
    # print(df)
    df.to_excel("贷款%s元%s期等额本息.xlsx"%(total_loan,repayment_duration))

def main():
    mode = input("等额本金请输入0，等额本息请输入1：")
    total_loan = int(input("请输入贷款本金数目（元）："))
    repayment_duration = int(input("按揭年数（请输入月数，如20年请输入240）："))
    rate_per_year = float(input("请输入贷款年利率（请输入小数，如4.9%请输入0.049）："))
    if mode == '0':
        equal_principal(total_loan,repayment_duration,rate_per_year)
    if mode == '1':
        equal_total(total_loan,repayment_duration,rate_per_year)


if __name__ == '__main__':
    main()
    # equal_principal(total_loan,repayment_duration,rate_per_year)
    # equal_total(total_loan,repayment_duration,rate_per_year)

