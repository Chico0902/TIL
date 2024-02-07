def solution(today, terms, privacies):
    today = today
    year,month,day = today.split('.')
    year = int(year)
    month = int(month)
    day = int(day)
    D_terms = dict()
    answer = []
    c_year = 0
    for i in range(len(terms)):
        yak, yuhyo = terms[i].split()
        D_terms[yak] = int(yuhyo)
        # print(D_terms)
    for i in range(len(privacies)):
        p_date, p_yak = privacies[i].split()
        # print(p_yak,'pyak')
        p_year, p_month, p_day = p_date.split('.')
        p_year = int(p_year)
        p_month = int(p_month)
        p_day = int(p_day)
        if p_yak in D_terms:
            # print(D_terms[p_yak],i)
            if D_terms[p_yak] < 12:
                # print(month,D_terms[p_yak],i)
                if month > D_terms[p_yak]:
                    c_year = year
                    c_month = month - D_terms[p_yak]
                else:
                    c_year = year - 1
                    c_month = 12 - (D_terms[p_yak] - month)
                # print(c_month,i)
                # print(c_year,'cyear1')
                # print(p_year,'pyear1')    
                if  c_year > p_year:
                    answer.append(i+1)
                if c_year == p_year:
                    # print(c_month,'cmt')
                    # print(p_month,'pmt')
                    if c_month > p_month:
                        # print('chk')
                        answer.append(i+1)
                if c_year == p_year:
                    if c_month == p_month:
                        if day >= p_day:
                            answer.append(i+1)
            else:
                mok = D_terms[p_yak]//12
                namuji = D_terms[p_yak]%12
                # print('ck',i)
                # print(month,'mt')
                # print(namuji,'namu')
                # print(mok,'mok')
                # print(year,'year')
                if month > namuji:
                    c_year = year - mok
                    c_month = month - namuji
                else:
                    c_year = year - mok
                    c_month = 12 - (namuji - month)
                    if namuji >= month:
                        c_year -= 1
                # print(c_month,'cmt')
                # print(c_year,'cyear')
                # print(p_year,'pyear')
                # print(p_month,'pmont')
                if  c_year > p_year:
                    answer.append(i+1)
                if c_year == p_year:
                    if c_month > p_month:
                        answer.append(i+1)
                if c_year == p_year:
                    if c_month == p_month:
                        if day >= p_day:
                            answer.append(i+1)
                            
                            


    # print(answer)
    return answer

solution( "2016.02.15", ["A 100"], ["2000.06.16 A", "2008.02.15 A"])