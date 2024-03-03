# Works nicely with Vicuna 13b

## Extractive Prompts - uses few shot techniques to offer guidance.
<pre>
Extract following relations from the query in context of equity public and private offerings.
Format output as a JSON.


product: one or more values like ipo, convertibles, dribble-out, overnight marketed, follow-on etc. use #NA# if not present in query
minimum_size: minimum size in millions along as a range. use 0 if not present in query
maximum_size: maximum size in millions along as a range. use #NA if not present in query
start_date, end_date: a range of dates in format greater. use #NA# if not present in query
region: one of North America, Asia, Japan, Europe, Rest of the World based on closest mapping to country. use #NA# if not present in query
sector: one value like Technology, Healthcare, Consumer Products, Industrials, Transportation etc. use #NA# if not present in query 
text: everything else in the query not matching above relations

query: valuations for ipo deals between 500million and 1billion for LATAM during 2023
</pre>
