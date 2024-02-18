# -*- coding: utf-8 -*-
"""flashtext1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aFrnVw9WAdTuFwGkuQfIFoq4ZyI2eLGl
"""

!pip install flashtext textrank

from flashtext import KeywordProcessor

# Initialize a KeywordProcessor with a list of keywords
keyword_processor = KeywordProcessor(case_sensitive=False)

questions = """Find memos for IPOs exceeding $500 million in the airline industry announced in the past year.
Show me documents for offerings related to electric vehicles in the transportation sector from companies in Europe.
Are there any memos for offerings led by [Investment Bank Name] involving companies headquartered in Asia?
I'm looking for documents for offerings completed between 2018 and 2020 where Specific Person Name was involved as an advisor.
Show me memos for companies offering freight transportation services with an offering size between $100 million and $200 million.
Find memos for offerings in the shipping industry exceeding $1 billion from companies in North America announced after 2022.
Show me documents for IPOs led by Investment Bank Name involving companies with  "logistics" in their name and a size exceeding $200 million.
Are there any memos for offerings completed between 2019 and 2021 where [Specific Lawyer Name] was involved in the legal team and the offering size was below $50 million?
I'm looking for documents for companies offering autonomous transportation technology with an offering size between $500 million and $1 billion.
Show me memos for offerings in the rail sector from companies headquartered in developing countries with an upcoming offering date.
Find memos for IPOs exceeding $1 billion in the airline industry announced in the past year by companies with "cargo" in their name.
Show me documents for offerings related to electric vehicles in the transportation sector from companies in Europe led by [Investment Bank Name].
Are there any memos for offerings involving companies with "public transportation" in their name and a size exceeding $300 million?
I'm looking for documents for offerings completed between 2017 and 2019 where [Specific Person Name] was involved as an advisor and the offering was in the freight and logistics sector.
Show me memos for companies offering autonomous shipping technology with an offering size between $200 million and $500 million and headquartered in North America.
Find memos for offerings in the airline industry exceeding $750 million from companies in Europe announced after 2021.
Show me documents for IPOs led by [Investment Bank Name] involving companies with "logistics" in their name and a size exceeding $150 million.
Are there any memos for offerings completed between 2018 and 2020 where [Specific Lawyer Name] was involved in the legal team and the offering involved public transportation infrastructure?
I'm looking for documents for companies offering freight transportation services with an offering size between $75 million and $150 million and announced in the past 6 months.
Show me memos for offerings in the rail sector from companies headquartered in developing countries with a completed offering date between 2022 and 2023.
Find memos for offerings exceeding $1 billion in the airline industry announced in the past 2 years by companies with "cargo" in their name and headquartered in North America.
Show me documents for offerings related to electric vehicles in the transportation sector from companies in Europe led by [Investment Bank Name] and completed in the past year.
Are there any memos for offerings involving companies with "public transportation" in their name, a size exceeding $250 million, and announced in the past 3 months?
I'm looking for documents for offerings completed between 2016 and 2018 where [Specific Person Name] was involved as an advisor and the offering was in the shipping industry.
Show me memos for companies offering autonomous transportation technology with an offering size between $100 million and $200 million and led by [Investment Bank Name].
Find memos for offerings in the airline industry exceeding $500 million from companies in Asia announced after 2020.
Show me documents for IPOs led by [Investment Bank Name] involving companies with "logistics" in their name and a size exceeding $100 million.
Are there any memos for offerings completed between 2017 and 2019 where [Specific Lawyer Name] was involved in the legal team and the offering involved freight transportation services?
I'm looking for documents for companies offering electric airplanes with an offering size between $300 million and $500 million and announced in the past year.
Show me memos for offerings in the rail sector from companies headquartered in Europe with an upcoming offering date.
Find memos for offerings exceeding $1 billion in the airline industry announced in the past 3 years by companies with "cargo" in their name and led by [Investment Bank Name].
Show me documents for offerings related to electric vehicles in the transportation sector from companies in North America announced in the past 6 months.
Are there any memos for offerings involving companies with "public transportation" in their name, a size exceeding $200 million, and completed in the past year?
I'm looking for documents for companies offering electric vehicles in the transportation sector with an offering size exceeding $1 billion and announced in the past 2 years.
Show me memos for offerings in the rail sector from companies with a market capitalization exceeding $5 billion and an upcoming offering date.
Find memos for offerings exceeding $800 million in the airline industry announced in the past year by companies with "cargo" in their name and a greenshoe option exceeding 10%.
Show me documents for offerings related to autonomous shipping technology from companies in Europe announced in the past 3 months.
Are there any memos for offerings involving companies with "public transportation" in their name, a size exceeding $150 million, and completed in the past 6 months?
I'm looking for documents for offerings completed between 2014 and 2016 where [Specific Person Name] was involved as an advisor and the offering involved companies with "freight" in their name.
Show me memos for companies offering autonomous transportation technology with an offering size between $75 million and $100 million and led by [Investment Bank Name].
Find memos for offerings in the airline industry exceeding $600 million from companies in North America announced before 2022.
Show me documents for block trades led by [Investment Bank Name] involving companies with "logistics" in their name and a size exceeding $300 million.
Are there any memos for offerings completed between 2015 and 2017 where [Specific Lawyer Name] was involved in the legal team and the offering involved companies with "rail" in their name?
I'm looking for documents for companies offering electric airplanes with an offering size between $200 million and $300 million and announced in the past year.
Show me memos for offerings in the rail sector from companies with a market capitalization below $2 billion and a completed offering date between 2021 and 2022.
Find memos for offerings exceeding $500 million in the airline industry announced in the past year by companies with "cargo" in their name and a lock-up period exceeding 1 year.
Show me documents for offerings related to electric vehicles in the transportation sector from companies in developing countries announced in the past 6 months and led by [Investment Bank Name].
Are there any memos for offerings involving companies with "public transportation" in their name, a size exceeding $100 million, and completed in the past year with a regulation status of Reg A+?
I'm looking for documents for offerings completed between 2013 and 2015 where [Specific Person Name] was involved as an advisor and the offering involved companies with "shipping" in their name.
Show me memos for companies offering autonomous transportation technology with an offering size exceeding $500 million and headquartered outside of North America.
Find memos for offerings in the airline industry exceeding $400 million from companies in Europe announced after 2020 and involving a greenshoe option.
Show me documents for offerings related to electric vehicles in the transportation sector from companies with a market capitalization exceeding $10 billion and announced in the past year.
Are there any memos for offerings involving companies with "public transportation" in their name, a size exceeding $50 million, and completed in the past 6 months with a listing on the NASDAQ exchange?
I'm looking for documents for offerings completed between 2012 and 2014 where [Specific Person Name] was involved as an advisor and the offering involved companies with "logistics" in their name and a size exceeding $100 million.
Show me memos for companies offering autonomous transportation technology with an offering size exceeding $250 million and involving a co-manager from [Specific Investment Bank Name].
Find memos for offerings in the shipping industry exceeding $300 million from companies in North America announced before 2021 and involving a greenshoe option.
Show me documents for convertible offerings led by [Investment Bank Name] involving companies with "logistics" in their name and a size exceeding $200 million.
Are there any memos for offerings completed between 2011 and 2013 where [Specific Lawyer Name] was involved in the legal team and the offering involved companies with "freight" in their name and a size below $50 million?
I'm looking for documents for companies offering electric airplanes with an offering size exceeding $100 million and announced in the past year and involving an underwriter syndicate.
Show me memos for offerings in the rail sector from companies with a market capitalization between $2 billion and $5 billion and an upcoming offering date.
Find memos for offerings exceeding $200 million in the airline industry announced in the past year by companies with "cargo" in their name and a lock-up period exceeding 6 months.
Show me documents for offerings related to electric vehicles in the transportation sector from companies in Europe announced in the past 3 months with a size exceeding $750 million.
Are there any memos for offerings involving companies with "public transportation" in their name, a size exceeding $25 million, and completed in the past year with a listing on the NYSE exchange?
I'm looking for documents for offerings completed between 2010 and 2012 where [Specific Person Name] was involved as an advisor and the offering involved companies with "shipping" in their name and a regulation status of Reg S.
Show me memos for companies offering autonomous transportation technology with an offering size between $250 million and $500 million and led by an investment bank outside the top 10.
Find memos for offerings in the airline industry exceeding $100 million from companies in Asia announced after 2019 and involving a co-manager from [Specific Investment Bank Name].
Show me documents for offerings related to electric vehicles in the transportation sector from companies with a market capitalization below $5 billion and announced in the past year.
Are there any memos for offerings involving companies with "public transportation" in their name, a size exceeding $10 million, and completed in the past 6 months with a greenshoe option exceeding 5%?
I'm looking for documents for offerings completed between 2009 and 2011 where [Specific Person Name] was involved as an advisor and the offering involved companies with "logistics" in their name and a size below $50 million.
Show me memos for companies offering autonomous transportation technology with an offering size exceeding $100 million and involving a lead underwriter with a specialization in technology IPOs.
Find memos for offerings in the shipping industry exceeding $50 million from companies in developing countries announced before 2020 and involving a co-manager from [Specific Investment Bank Name].
Show me documents for offerings related to electric vehicles in the transportation sector from companies headquartered outside of North America and announced in the past 6 months with a size exceeding $500 million.
Are there any memos for offerings involving companies with "public transportation" in their name and completed in the past year with a size exceeding $5 million and a lock-up period exceeding 3 months?
I'm looking for documents for offerings completed between 2008 and 2010 where [Specific Person Name] was involved as an advisor and the offering involved companies with "freight" in their name and a listing on a regional exchange.
Show me memos for companies offering autonomous transportation technology with an offering size below $100 million and involving a legal team with expertise in intellectual property law.
Find memos for offerings exceeding $50 million in the airline industry announced in the past year by companies with "cargo" in their name and a greenshoe option exceeding 3%.
Show me documents for offerings related to electric vehicles in the transportation sector from companies in Europe announced in the past 3 months with a market capitalization exceeding $20 billion.
Are there any memos for offerings involving companies with "public transportation" in their name and completed in the past year with a size exceeding $1 million and a regulation status of Regulation D?
I'm looking for documents for offerings completed between 2007 and 2009 where [Specific Person Name] was involved as an advisor and the offering involved companies with "shipping" in their name and a co-manager from [Specific Investment Bank Name].
Show me memos for companies offering autonomous transportation technology with an offering size exceeding $50 million and involving a lead underwriter with a strong track record in the transportation sector.
Find memos for offerings in the airline industry exceeding $25 million from companies in North America announced after 2018 and involving a greenshoe option and a lock-up period exceeding 1 year.
Show me documents for offerings related to electric vehicles in the transportation sector from companies with a market capitalization below $1 billion and announced in the past year with a size exceeding $250 million.
Are there any memos for offerings involving companies with "public transportation" in their name and completed in the past 6 months with a size exceeding $500,000
...and involving an underwriter syndicate with at least 3 member banks.
I'm looking for documents for offerings completed between 2006 and 2008 where [Specific Person Name] was involved as an advisor and the offering involved companies with "logistics" in their name and a regulation status of Rule 144A.
Show me memos for companies offering autonomous transportation technology with an offering size exceeding $25 million and involving a lead underwriter with experience in complex financial structuring.
Find memos for offerings exceeding $10 million in the shipping industry from companies in Europe announced before 2019 and involving a co-manager from [Specific Investment Bank Name] and a lock-up period exceeding 6 months.
Show me documents for offerings related to electric vehicles in the transportation sector from companies headquartered outside of North America and announced in the past year with a size exceeding $100 million and a listing on a major stock exchange.
Are there any memos for offerings involving companies with "public transportation" in their name and completed in the past year with a size exceeding $250,000 and a greenshoe option exceeding 1%?
I'm looking for documents for offerings completed between 2005 and 2007 where [Specific Person Name] was involved as an advisor and the offering involved companies with "freight" in their name and a size exceeding $25 million.
Show me memos for companies offering autonomous transportation technology with an offering size below $50 million and involving a legal team with experience in international regulatory compliance.
Find memos for offerings exceeding $5 million in the airline industry announced in the past year by companies with "cargo" in their name and a lock-up period exceeding 3 months and a greenshoe option exceeding 2%.
Show me documents for offerings related to electric vehicles in the transportation sector from companies in Europe announced in the past 3 months with a market capitalization exceeding $10 billion and a size exceeding $500 million.
Are there any memos for offerings involving companies with "public transportation" in their name and completed in the past 6 months with a size exceeding $100,000 and a regulation status of Regulation SX?
I'm looking for documents for offerings completed between 2004 and 2006 where [Specific Person Name] was involved as an advisor and the offering involved companies with "shipping" in their name and a co-manager from [Specific Investment Bank Name] and a listing on a regional exchange."""\
.split('\n')

len(questions)

keyword_dict = {
    "<ipo|product>": "ipo,ipos,initial public offering",
    "<convertibles|product>": "convert,converts,convertible,convertibles",
    "<spac|product>": "spac,spacs",
    "<offering|product>": "offering,offerings",
    "<equity|product>": "equity,equity offering,equity offerings",
    "<electric vehicles|industry>": "ev,evs,electric vehicle,electric vehicles",
    "<airlines|industry>":"airline,airlines,airline industry",
    "<freight|industry>":"freight,freight carriers,freight transportation",
    "<shipping|industry>":"shipping,shipping industry",
    "<autonomus transportation|indstry":"self driving,autonomous vehicles,automatic driving,driverless vehicles,driverless cars,autonomus transportation",
    "<railroad|indstry>":"railways,railroad,rails industry,railway industry,railroad industry",
    "<transportation|sector>":"transpo,transportation sector,transportation",
    "<north america|region>":"na,north america,america,american",
    "<latin america|region>":"latam,latin,latin america,latin american",
    "<africa|region>":"africa,african",
    "<europe|region>":"europe,eu,european",
    "<asia|region>":"asia,asian",
    "<announced|event>":"announced",
    "<completed|event>":"completed",
    "<greater than|operator>":"exceeds,exceeding,over,larger than,more than",
    "<less than|operator>":"less than,under,smaller than,lesser than,below",
    "<between|operator>":"between,betn",
    "<after|dateop>":"after,later than,since",
    "<before|dateop>":"before,earlier than,prior to",
    "<past|dateop>":"past",
    "<Q1|date>":"first quarter,q1 of",
    "<Q2|date>":"second quarter,q2 of",
    "<Q3|date>":"third quarter,q3 of",
    "<Q4|date>":"fourth quarter,q3 of",
    "<ytd|date>":"year to date,year-to-date",
    "<qtd|date>":"quarter to date,quarter-to-date",
    "<mtd|date>":"month to date,month-to-date",
    "<offering size|attribute>":"offering size,size,sized,sizes",
    "<greenshoe|attribute>":"greenshoe,green shoe",
    "<led by|role>":"led by,managed by,co-managed by,comanaged,manager,co-manager,comanager,bookrunner,book runner,active bookrunner,passive bookrunner",
    "<underwriter|role>":"underwriter,underwriting",
    "<legal team|unknown>":"legal team",
    "<headquarters|unknown>":"headquartered,headquarters in,headquartered at"
}

for i,(k,v) in enumerate(keyword_dict.items()):
  keyword_dict[k] = keyword_dict[k].split(',')

# {'clean_name': ['list of unclean names']}
keyword_processor.add_keywords_from_dict(keyword_dict)
print(len(keyword_processor))

keyword_processor.extract_keywords(questions[1], span_info=True)

keyword_processor.replace_keywords(questions[1])

for idx, q in enumerate(questions):
  print(idx+1, q)
  print(idx+1, keyword_processor.extract_keywords(q, span_info=False))
  print()

